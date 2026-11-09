# Registro de prompts · Refresca · Serviço de previsão (SOA e Web Services)

O briefing da GS permite IA como copiloto, desde que os prompts fiquem registrados aqui e a equipe saiba explicar cada linha do código.

Registre cada uso relevante com o modelo abaixo, do mais antigo para o mais recente.

---

## Integrantes

- **Italo Caliari Silva** - RM554758
- **Júlio César Ruiz Zequin** - RM554676
- **Danilo Gronski Wendler** - RM 556602
- **Pedro Henrique Muzel Santos** - RM 555983
- **Vitor Montemor Ismael** - RM 556027

---

## 2026-11-09 · Desenvolvimento do serviço de previsão (SOA e Web Services)

- **Ferramenta:** Gemini
- **Integrante:** Italo Caliari Silva
- **Prompt:** texto completo enviado, reproduzido na íntegra no bloco abaixo (anexos: PDF do briefing da GS, README.md e prompts.md da equipe).
- **O que foi aproveitado:** estrutura do projeto em microsserviço/API, rotas e integração com o ecossistema CitizenTech Refresca.
- **O que a equipe ajustou:** Validamos a execução local, a estrutura de endpoints REST orientados a serviços e a documentação para comunicação com as demais camadas da solução. Mudanças futuras serão registradas em novas entradas.

**Texto do prompt (2026-11-09):**

```text
PROMPT — DESENVOLVIMENTO COMPLETO DO PROJETO SOA E WEB SERVICES
Quero que você atue como um desenvolvedor de software sênior, arquiteto de sistemas e especialista acadêmico em Arquitetura Orientada a Serviços (SOA) e Web Services.
1. CONTEXTO DO TRABALHO
O documento principal enviado em PDF contém todas as instruções referentes à entrega de um conjunto de 8 trabalhos, correspondentes a diferentes disciplinas.
Entretanto, quero desenvolver exclusivamente o trabalho da disciplina:
Arquitetura Orientada a Serviços (SOA) e Web Services.
Os demais documentos enviados foram elaborados por um integrante da minha equipe, que já antecipou algumas etapas do projeto. Portanto, esses materiais devem ser analisados e aproveitados como ponto de partida, sempre verificando se estão corretos, completos e alinhados às exigências do trabalho.
2. OBJETIVO PRINCIPAL
Quero que você desenvolva o projeto COMPLETO da disciplina Arquitetura Orientada a Serviços (SOA) e Web Services, buscando atender a 100% dos requisitos estabelecidos pelo professor.
Meu objetivo é entregar um trabalho de excelência e alcançar a nota máxima (10 ou 100, dependendo do sistema de avaliação).
Não quero apenas orientações, exemplos ou explicações de como fazer. Quero que você efetivamente desenvolva o projeto, produza os códigos necessários, organize sua estrutura, implemente as funcionalidades e prepare tudo para que eu possa executar e testar posteriormente.
3. ANÁLISE OBRIGATÓRIA DOS DOCUMENTOS
Antes de começar a desenvolver, siga estas etapas:
1. Leia integralmente o PDF principal, incluindo todas as páginas.
2. Localize e identifique especificamente as instruções referentes à disciplina Arquitetura Orientada a Serviços (SOA) e Web Services.
3. Identifique o professor responsável pela disciplina, suas orientações, exigências, critérios de avaliação e todos os requisitos técnicos.
4. Analise todos os demais documentos enviados, identificando o que já foi desenvolvido pelo integrante da equipe.
5. Verifique se os materiais existentes estão corretos e se podem ser aproveitados.
6. Identifique o que está faltando, o que precisa ser corrigido e o que precisa ser desenvolvido do zero.
IMPORTANTE: O PDF principal deve ser considerado a principal referência para todas as decisões do projeto. Não ignore nenhuma orientação específica do professor.
4. DESENVOLVIMENTO DO PROJETO
Depois de analisar os documentos, desenvolva todo o projeto da disciplina, respeitando rigorosamente as exigências identificadas.
Quero que você:
- Desenvolva toda a estrutura do projeto.
- Implemente todas as funcionalidades exigidas.
- Desenvolva os serviços e Web Services necessários.
- Aplique corretamente os conceitos de Arquitetura Orientada a Serviços (SOA).
- Utilize as tecnologias, linguagens, frameworks e ferramentas solicitadas pelo professor.
- Desenvolva os códigos completos, funcionais e organizados.
- Configure corretamente dependências, bibliotecas e arquivos de configuração.
- Implemente comunicação entre serviços, integrações e APIs quando necessário.
- Organize o projeto com uma estrutura profissional e de fácil compreensão.
- Inclua tratamento de erros e validações necessárias.
- Documente os principais componentes e funcionalidades.
- Corrija eventuais problemas encontrados nos materiais que já foram desenvolvidos.
Não adicione tecnologias desnecessárias nem altere os requisitos definidos pelo professor.
5. QUALIDADE E CRITÉRIOS DE AVALIAÇÃO
Durante todo o desenvolvimento, tenha como prioridade alcançar a nota máxima.
Para isso:
- Confira cada requisito solicitado no PDF.
- Não deixe funcionalidades obrigatórias de fora.
- Evite soluções incompletas ou apenas demonstrativas.
- Garanta que os códigos sejam coerentes entre si.
- Verifique se a estrutura do projeto permite sua execução.
- Priorize boas práticas de desenvolvimento.
- Certifique-se de que a implementação esteja alinhada ao conteúdo estudado na disciplina.
- Não invente requisitos que não estejam nos documentos.
- Caso encontre informações contraditórias ou insuficientes, sinalize antes de tomar decisões importantes.
6. TESTES E EVIDÊNCIAS
Uma informação importante: eu mesmo farei a execução dos testes e a coleta das evidências posteriormente.
Portanto, sua responsabilidade nesta etapa será deixar o projeto completamente preparado para essa fase.
Você deverá:
1. Garantir que o projeto esteja pronto para ser executado.
2. Fornecer instruções detalhadas para instalação e configuração.
3. Explicar como iniciar e executar o sistema.
4. Informar quais funcionalidades precisam ser testadas.
5. Criar um roteiro de testes baseado nos requisitos do professor.
6. Indicar quais telas, respostas, execuções ou resultados devo capturar como evidências.
7. Informar o resultado esperado de cada teste.
Não invente evidências nem afirme que funcionalidades foram testadas se você não conseguiu executá-las.
7. ORGANIZAÇÃO DA ENTREGA
Ao concluir o desenvolvimento, quero receber:
- Projeto completo e organizado.
- Todos os arquivos e códigos necessários.
- Estrutura de pastas adequada.
- Dependências e configurações necessárias.
- Documentação técnica do projeto.
- Instruções de instalação e execução.
- Roteiro completo de testes.
- Lista de evidências que preciso coletar.
- Checklist relacionando cada requisito do professor à sua respectiva implementação.
8. FORMA DE TRABALHO
Quero que você trabalhe de maneira organizada e criteriosa.
Siga esta sequência:
ETAPA 1 — Análise: Leia e compreenda todos os documentos enviados.
ETAPA 2 — Planejamento: Identifique os requisitos, tecnologias, funcionalidades e etapas necessárias.
ETAPA 3 — Auditoria: Avalie o que já foi desenvolvido pelo integrante da equipe e determine o que pode ser aproveitado.
ETAPA 4 — Desenvolvimento: Implemente o projeto completo, corrigindo e complementando os materiais existentes.
ETAPA 5 — Verificação: Revise os códigos, dependências, integrações e requisitos implementados.
ETAPA 6 — Preparação para entrega: Organize o projeto e forneça todas as instruções para que eu possa executar os testes e coletar as evidências.
Não avance de maneira desorganizada. Se o projeto for muito grande, divida o desenvolvimento em etapas, mas não abandone nenhum requisito.
9. ORIENTAÇÃO FINAL
Quero que você tenha uma postura de profissional responsável pela entrega de um projeto real, e não apenas de alguém que está fornecendo ajuda acadêmica.
Seja detalhista, técnico, criterioso e comprometido com a qualidade.
Não comece a programar sem antes analisar os documentos. Primeiro compreenda exatamente o que o professor está solicitando. Depois, desenvolva a solução mais adequada para cumprir integralmente os requisitos.
Meu objetivo é que, quando você finalizar, eu tenha em mãos um projeto completo, funcional, organizado e pronto para executar, testar, coletar as evidências e realizar a entrega acadêmica com a maior nota possível.
Prioridade absoluta: cumprir 100% dos requisitos da disciplina Arquitetura Orientada a Serviços (SOA) e Web Services, seguindo o PDF principal e as orientações específicas do professor.
