# Checklist de requisitos e auditoria do material existente

## 1. Requisitos do PDF (slide 27, SOA e Web Services) × implementação

| Requisito | Peso | Onde está | Como comprovar |
| --- | --- | --- | --- |
| Estruturação do domínio | 3,0 | Camadas `domain/`, `services/`, `repositories/`, `routers/`, `schemas.py`, `errors.py`; entidade `Previsao` com regra `e_perigosa`; índice de calor NOAA em `domain/calor.py`; preditor atrás de interface (`ml/preditor.py`) | README (estrutura), código, testes de domínio |
| Conexão com banco de dados | 3,0 | `database.py` (engine, sessão por requisição), `PrevisaoRepository`, SQLAlchemy 2.0, URL por variável de ambiente | Roteiro 3, 16, 17 |
| Migrações | 1,5 | Alembic: `migrations/versions/0001` (tabela) e `0002` (índice) | Roteiro 1, 2, 19 |
| Documentação automática | 1,5 | OpenAPI/Swagger do FastAPI, com exemplos, descrições e respostas de erro | Roteiro 5 |
| Testes automatizados | 1,0 | `tests/` (14 testes, executados: 14 passed) | `docs/evidencias/18_pytest.png` |
| Chamadas de APIs REST (objetivo) | n/d | `POST/GET /previsoes`, consumido pela API em C# | Roteiro 6 a 15 |
| Repositório GitHub | entregável | Este repositório | Link no Teams |
| README com execução, descrição e integrantes | entregável | `README.md` (preencher integrantes e links) | Revisão |
| Documentação dos endpoints | entregável | `/docs`, `/redoc` | Roteiro 5 |
| Evidências | entregável | `docs/evidencias/` | Roteiro inteiro |

## 2. Auditoria do que o colega deixou pronto

**Aproveitado sem mudar:** Ficha, Persona, ODS, tabela de contratos, níveis do índice de calor, exemplos de requisição e resposta de `POST /previsoes`, modelo do `prompts.md`.

**Correto e alinhado ao PDF:** o README segue a sugestão de ficha do slide 20; registra dados simulados vs. públicos; a arquitetura coloca o serviço de previsão em Python/FastAPI (o PDF permite qualquer linguagem).

**Completado por mim:** descrição desta parte, estrutura do projeto, passos de execução, tabela de entregáveis com a rubrica de SOA, nova entrada no `prompts.md`, destaque do serviço de previsão no diagrama Mermaid (o modelo destacava `API`).

**Pontos que a equipe precisa decidir ou revisar:**

1. **Campos de entrada do modelo.** O README diz que o responsável de ML define os campos finais. Usei os quatro do exemplo. Se o notebook usar outros, mude `FEATURES`, `schemas.py` e o README.
2. **Modelo treinado ainda não existe aqui.** Há uma heurística (baseline) rotulada como tal em `versaoModelo`. Não a apresente como modelo de ML.
3. **Resposta `201`.** O README só mostra o corpo da resposta, não o status. Usei `201 Created`. Avise quem faz a API em C# para aceitar 2xx.
4. **Campos extras.** O `POST` responde exatamente os cinco campos do contrato. Os `GET` devolvem mais campos (entrada e `criadoEm`); a API em C# deve ignorar o que não usar.
5. **Mesmo dia com várias previsões.** Cada `POST` cria um registro novo; `GET /previsoes/data/{data}` devolve o mais recente. Se preferirem uma previsão única por dia, é uma mudança pequena (migração nova + `409` ou atualização).
6. **Professor da disciplina:** o PDF não traz o nome. Não inventei nenhum.
7. **Links:** falta só o link das outras partes e os responsáveis na tabela de repositórios.
8. **Combinado da GS:** cada integrante deve saber explicar cada linha. Leia o código antes de entregar.
