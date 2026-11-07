from tests.conftest import ENTRADA


def test_post_segue_o_contrato_do_readme(client):
    resposta = client.post("/previsoes", json=ENTRADA)
    assert resposta.status_code == 201
    corpo = resposta.json()
    assert set(corpo) == {"id", "data", "probabilidade", "perigoso", "versaoModelo"}
    assert corpo["data"] == "2026-11-20"
    assert corpo["probabilidade"] == 0.82
    assert corpo["perigoso"] is True
    assert corpo["versaoModelo"] == "teste-1.0"


def test_limiar_de_perigo(client, preditor_fixo):
    preditor_fixo.valor = 0.5
    assert client.post("/previsoes", json=ENTRADA).json()["perigoso"] is True
    preditor_fixo.valor = 0.49
    assert client.post("/previsoes", json=ENTRADA).json()["perigoso"] is False


def test_dia_quente_e_perigoso_e_dia_ameno_nao(client_heuristica):
    quente = {**ENTRADA, "temperaturaMaxOntem": 36.0, "umidadeMediaOntem": 60.0}
    ameno = {**ENTRADA, "temperaturaMaxOntem": 22.0, "temperaturaMinOntem": 15.0, "umidadeMediaOntem": 60.0}
    assert client_heuristica.post("/previsoes", json=quente).json()["perigoso"] is True
    assert client_heuristica.post("/previsoes", json=ameno).json()["perigoso"] is False


def test_entradas_invalidas_retornam_422(client):
    invalidos = [
        {**ENTRADA, "umidadeMediaOntem": 150},
        {**ENTRADA, "temperaturaMinOntem": 35.0},  # mínima maior que a máxima
        {**ENTRADA, "data": "20/11/2026"},
        {k: v for k, v in ENTRADA.items() if k != "ventoMedioOntem"},
    ]
    for corpo in invalidos:
        assert client.post("/previsoes", json=corpo).status_code == 422


def test_get_por_id(client):
    criada = client.post("/previsoes", json=ENTRADA).json()
    resposta = client.get(f"/previsoes/{criada['id']}")
    assert resposta.status_code == 200
    corpo = resposta.json()
    assert corpo["temperaturaMaxOntem"] == 31.2
    assert "criadoEm" in corpo


def test_get_por_id_inexistente_retorna_404(client):
    resposta = client.get("/previsoes/9999")
    assert resposta.status_code == 404
    assert resposta.json()["erro"] == "nao_encontrada"


def test_listagem_com_filtro_e_paginacao(client):
    for dia in ("2026-11-18", "2026-11-19", "2026-11-19"):
        client.post("/previsoes", json={**ENTRADA, "data": dia})
    assert len(client.get("/previsoes").json()) == 3
    assert len(client.get("/previsoes", params={"data": "2026-11-19"}).json()) == 2
    assert len(client.get("/previsoes", params={"limite": 1}).json()) == 1
    assert client.get("/previsoes", params={"limite": 0}).status_code == 422


def test_ultima_previsao_da_data(client, preditor_fixo):
    client.post("/previsoes", json=ENTRADA)
    preditor_fixo.valor = 0.1
    segunda = client.post("/previsoes", json=ENTRADA).json()
    resposta = client.get("/previsoes/data/2026-11-20")
    assert resposta.status_code == 200
    assert resposta.json()["id"] == segunda["id"]
    assert client.get("/previsoes/data/2030-01-01").status_code == 404


def test_health(client):
    resposta = client.get("/health")
    assert resposta.status_code == 200
    assert resposta.json() == {"status": "ok", "banco": "ok", "versaoModelo": "teste-1.0"}
