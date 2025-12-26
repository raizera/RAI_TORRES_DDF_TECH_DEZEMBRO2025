# Item 0 – Planejamento, Agilidade e Gestão do Projeto

## 0.1 Visão Geral do Projeto

Este projeto tem como objetivo a construção de uma **Plataforma de Dados para um grande e-commerce**, utilizando a plataforma **Dadosfera SaaS**, com foco em:

- Centralização de dados de múltiplas fontes  
- Geração de análises descritivas e prescritivas  
- Uso de Inteligência Artificial e GenAI para extração de valor a partir de dados desestruturados  
- Redução do tempo entre dados e decisão  

O projeto foi estruturado seguindo boas práticas de **gestão de projetos (PMBOK)** e **metodologias ágeis**, considerando entregas incrementais e geração contínua de valor.

---

## 0.2 Metodologia Adotada

A metodologia adotada combina:

- **PMBOK** para planejamento macro, riscos e dependências
- **Agile / Kanban** para execução incremental das atividades
- Entregas orientadas ao **Ciclo de Vida dos Dados da Dadosfera**

O projeto foi dividido em **fases claras**, cada uma associada a ativos entregáveis na plataforma.

---

## 0.3 Fases do Projeto e Entregáveis

### Fase 1 – Concepção e Planejamento
**Objetivo:** Definir escopo, arquitetura inicial e estratégia de dados.

**Atividades:**
- Entendimento do problema de negócio do e-commerce
- Definição do domínio de dados (catálogo de produtos e vendas)
- Escolha da base de dados principal
- Definição da arquitetura lógica do Data Lake
- Planejamento das etapas do projeto

**Entregáveis:**
- Documento de planejamento do projeto
- Fluxograma das etapas
- Definição da base de dados

---

### Fase 2 – Integração e Ingestão de Dados
**Objetivo:** Conectar e carregar os dados brutos na Dadosfera.

**Atividades:**
- Conexão da base de dados escolhida
- Carga de mais de 100.000 registros
- Organização inicial dos dados na Landing Zone

**Entregáveis:**
- Dataset integrado na Dadosfera
- Evidências de ingestão (prints e links)

---

### Fase 3 – Exploração, Catálogo e Governança
**Objetivo:** Garantir organização, rastreabilidade e entendimento dos dados.

**Atividades:**
- Catalogação dos datasets
- Criação do dicionário de dados
- Organização dos dados nas zonas do Data Lake
- Aplicação de boas práticas de governança

**Entregáveis:**
- Ativos catalogados na Dadosfera
- Dicionário de dados documentado

---

### Fase 4 – Qualidade de Dados
**Objetivo:** Identificar e mitigar problemas de qualidade que impactam análises e modelos de IA.

**Atividades:**
- Análise de dados faltantes e inconsistências
- Definição de regras de qualidade
- Geração de relatório de Data Quality utilizando biblioteca especializada

**Entregáveis:**
- Relatório de qualidade dos dados
- Evidências de validação

---

### Fase 5 – Processamento e GenAI
**Objetivo:** Transformar dados desestruturados em dados analíticos de alto valor.

**Atividades:**
- Processamento de textos de títulos e descrições de produtos
- Uso de LLMs para extração de features estruturadas
- Enriquecimento do dataset para análises avançadas

**Entregáveis:**
- Dataset enriquecido com features geradas por IA
- Notebook documentando o processo de GenAI

---

### Fase 6 – Modelagem de Dados
**Objetivo:** Estruturar os dados para análise e tomada de decisão.

**Atividades:**
- Definição do modelo de dados (abordagem Kimball)
- Criação de visões analíticas
- Justificativa da modelagem adotada

**Entregáveis:**
- Modelo dimensional documentado
- Diagrama da modelagem

---

### Fase 7 – Análise e Visualização
**Objetivo:** Gerar valor para o negócio por meio de análises visuais.

**Atividades:**
- Criação de queries SQL
- Desenvolvimento de dashboards analíticos
- Análises de categorias e séries temporais

**Entregáveis:**
- Dashboards na Dadosfera
- Queries SQL salvas e documentadas

---

### Fase 8 – Data Apps
**Objetivo:** Permitir exploração interativa dos dados pelos usuários finais.

**Atividades:**
- Desenvolvimento de Data App com Streamlit
- Exploração de similaridade entre produtos
- Integração com modelos de IA

**Entregáveis:**
- Data App funcional
- Código versionado no GitHub

---

## 0.4 Análise de Riscos

| Risco | Impacto | Mitigação |
|------|--------|-----------|
| Dados incompletos ou inconsistentes | Médio | Aplicação de regras de Data Quality |
| Alto volume de dados | Médio | Uso de amostragem controlada |
| Complexidade de GenAI | Médio | Uso de prompts simples e iterativos |
| Falhas de integração | Baixo | Testes incrementais |

---

## 0.5 Dependências e Pontos Críticos

- A **qualidade dos dados** impacta diretamente os modelos de IA
- A **catalogação correta** é essencial para análises e visualizações
- O **processamento com GenAI** depende da boa ingestão dos dados textuais

---

## 0.6 Considerações Finais

Este planejamento garante uma execução estruturada, incremental e alinhada ao **Ciclo de Vida dos Dados da Dadosfera**, permitindo demonstrar de forma prática como a plataforma acelera a geração de valor a partir dos dados em um cenário real de e-commerce.
