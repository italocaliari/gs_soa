# Roteiro de testes e evidências · Serviço de previsão

Execute na raiz do projeto, com o ambiente virtual ativo e `pip install -r requirements-dev.txt` feito.
Salve os prints em `docs/evidencias/` com os nomes sugeridos.

| # | O que fazer | Resultado esperado | Evidência (arquivo sugerido) |
| --- | --- | --- | --- |
| 1 | `alembic upgrade head` | Mensagens `Running upgrade -> 0001` e `0001 -> 0002`; arquivo `refresca_previsao.db` criado | `01_migracao_upgrade.png` |
| 2 | `alembic current` e `alembic history` | `0002 (head)` e as duas revisões listadas | `02_migracao_historico.png` |
| 3 | `sqlite3 refresca_previsao.db ".schema previsoes"` | Tabela `previsoes` com as colunas e o índice `ix_previsoes_data` | `03_schema_banco.png` |
| 4 | `uvicorn app.main:app --port 8000` | `Uvicorn running on http://127.0.0.1:8000` | `04_servidor_no_ar.png` |
| 5 | Abrir http://localhost:8000/docs | Swagger com `/previsoes` (POST, GET), `/previsoes/{id}`, `/previsoes/data/{data}`, `/health` | `05_swagger.png` |
| 6 | No Swagger, `POST /previsoes` com o exemplo (ou o `curl` do README) | `201`; corpo com `id`, `data`, `probabilidade`, `perigoso`, `versaoModelo` | `06_post_201.png` |
| 7 | No Swagger (`/docs`), executar `POST /previsoes` com o JSON abaixo | `201`, `perigoso: true` e `versaoModelo: "heuristica-1.0"` enquanto o modelo treinado não estiver configurado | `07_post_dia_quente.png` |
| 8 | `POST /previsoes` com `temperaturaMaxOntem: 22`, `temperaturaMinOntem: 15` | `201` e `perigoso: false` | `08_post_dia_ameno.png` |
| 9 | `POST /previsoes` com `umidadeMediaOntem: 150` | `422` com o campo inválido apontado | `09_post_422.png` |
| 10 | `POST /previsoes` com `temperaturaMinOntem` maior que a máxima | `422` | `10_post_422_min_max.png` |
| 11 | No Swagger (`/docs`), executar `GET /previsoes/{id}` usando o `id` retornado no passo 6 | `200` com os dados de entrada, resultado da previsão e `criadoEm` | `11_get_id.png` |
| 12 | `GET /previsoes/9999` | `404` com `{"erro":"nao_encontrada",...}` | `12_get_404.png` |
| 13 | `GET /previsoes?data=2026-11-20&limite=10` | `200` com lista só do dia filtrado | `13_get_lista.png` |
| 14 | `GET /previsoes/data/2026-11-20` | `200` com a última previsão do dia | `14_get_por_data.png` |
| 15 | `GET /health` | `200` com `{"status":"ok","banco":"ok","versaoModelo":"heuristica-1.0"}` | `15_health.png` |
| 16 | `sqlite3 refresca_previsao.db "select id,data,probabilidade,perigoso,versao_modelo from previsoes;"` | Linhas gravadas pelos passos 6 a 8 | `16_dados_no_banco.png` |
| 17 | Reiniciar o servidor e repetir o passo 11 | A previsão continua lá (persistência) | `17_persistencia.png` |
| 18 | `pytest -v` | Todos os testes `PASSED` (são 14); `0 failed` | `18_pytest.png` |
| 19 | `alembic downgrade base` e depois `alembic upgrade head` | Reverte as duas migrações e reaplica sem erro | `19_migracao_downgrade.png` |
| 20 | (opcional, se o ML entregar o modelo) definir `REFRESCA_MODELO_PATH` e repetir 6 e 15 | `versaoModelo` muda para o valor de `REFRESCA_MODELO_VERSAO` | `20_modelo_treinado.png` |

### JSON exato para a evidência 07

No Swagger, abra `POST /previsoes`, clique em **Try it out** e use este corpo (a data pode ser ajustada para um dia futuro):

```json
{
  "data": "2026-11-10",
  "temperaturaMaxOntem": 36,
  "temperaturaMinOntem": 22,
  "umidadeMediaOntem": 60,
  "ventoMedioOntem": 2
}
```

Clique em **Execute** e capture a tela mostrando o corpo enviado e a resposta `201`, incluindo `perigoso: true`. Salve como `docs/evidencias/07_post_dia_quente.png`.

### Como coletar a evidência 11

Use o `id` devolvido no passo 6. No Swagger, abra `GET /previsoes/{previsao_id}`, clique em **Try it out**, informe esse número no campo `previsao_id` e clique em **Execute**. Capture a resposta `200` com os dados da previsão e o campo `criadoEm`. Salve como `docs/evidencias/11_get_id.png`.

**Importante:** não crie ou edite imagens manualmente para simular respostas. Os prints devem ser capturados da execução real do Swagger na sua máquina.

Observações:

- Se o `pytest` apontar falha, **não ajuste o teste para passar**: leia a mensagem, corrija o código e rode de novo. Me envie a saída se precisar de ajuda.
- Os valores exatos de `probabilidade` nos passos 6 a 8 dependem da heurística; o que se valida é o `perigoso` e o formato.
