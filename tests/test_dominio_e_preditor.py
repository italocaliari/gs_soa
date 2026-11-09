import pytest

from app.domain.calor import indice_calor_celsius, nivel_do_indice
from app.errors import ModeloIndisponivel
from app.ml.preditor import HeuristicaCalor, ModeloSklearn, Observacao, criar_preditor


def f(c):
    return c * 9 / 5 + 32


def test_indice_de_calor_bate_com_a_tabela_da_noaa():
    assert f(indice_calor_celsius(32.22, 50)) == pytest.approx(95, abs=1.0)  # 90 °F, 50 %
    assert f(indice_calor_celsius(26.67, 40)) == pytest.approx(80, abs=1.0)  # 80 °F, 40 %


def test_niveis_seguem_as_faixas_do_contrato():
    assert nivel_do_indice(26.9) == "normal"
    assert nivel_do_indice(27.0) == "atencao"
    assert nivel_do_indice(31.9) == "atencao"
    assert nivel_do_indice(32.0) == "perigo"


def test_heuristica_cresce_com_a_temperatura():
    h = HeuristicaCalor()
    p = [h.probabilidade(Observacao(t, 15.0, 60.0, 2.0)) for t in (20, 28, 32, 36)]
    assert p == sorted(p)
    assert 0 <= p[0] < 0.1 and p[-1] > 0.9


def test_modelo_inexistente_falha_com_mensagem_clara(tmp_path):
    with pytest.raises(ModeloIndisponivel):
        criar_preditor(str(tmp_path / "nao_existe.joblib"), "1.0")


def test_carrega_modelo_sklearn_treinado(tmp_path):
    joblib = pytest.importorskip("joblib")
    linear_model = pytest.importorskip("sklearn.linear_model")
    X = [[20, 12, 60, 2], [24, 15, 70, 3], [34, 22, 45, 1], [37, 24, 40, 1]]
    y = [0, 0, 1, 1]
    caminho = tmp_path / "modelo.joblib"
    joblib.dump(linear_model.LogisticRegression().fit(X, y), caminho)

    preditor = criar_preditor(str(caminho), "2.0")
    assert isinstance(preditor, ModeloSklearn) and preditor.versao == "2.0"
    assert preditor.probabilidade(Observacao(37, 24, 40, 1)) > preditor.probabilidade(Observacao(20, 12, 60, 2))
