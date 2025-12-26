# Case Técnico – Pipeline de Dados e Data App (Simulação de Plataforma Analítica)

https://huggingface.co/spaces/raigarcia/dadosfera

## 1. Contexto
Este projeto foi desenvolvido como parte de um case técnico na área de dados, com o objetivo de demonstrar domínio do ciclo completo de dados, incluindo ingestão, exploração, transformação, consumo e disponibilização por meio de um Data App.

Devido à indisponibilidade de acesso à plataforma Dadosfera no momento do desenvolvimento, todo o fluxo foi simulado localmente, respeitando os conceitos, arquitetura e responsabilidades descritas no documento oficial do case. A solução foi estruturada de forma a ser facilmente portável para um ambiente corporativo real.

---

## 2. Fonte de Dados
Foi utilizado o dataset público AMAZON-Products-2023, disponibilizado no Hugging Face, contendo metadados reais de produtos de e-commerce.

https://huggingface.co/datasets/milistu/AMAZON-Products-2023/tree/main

Os dados estavam particionados em múltiplos arquivos no formato Apache Arrow (IPC Stream), os quais foram baixados, carregados e concatenados localmente.

Principais campos da base:
- parent_asin: identificador único do produto
- title: título do produto
- description: descrição textual
- main_category: categoria principal
- price: preço informado
- average_rating: avaliação média dos usuários

---

## 3. Arquitetura de Dados
O projeto segue uma arquitetura em camadas, simulando práticas adotadas em plataformas corporativas de dados como a Dadosfera.

Camadas utilizadas:
- Raw: dados brutos, sem tratamento
- Silver: dados tratados e padronizados
- Gold: dados prontos para consumo analítico e aplicações de IA

Essa separação garante organização, governança, rastreabilidade e clareza de responsabilidades ao longo do pipeline.

---

## 4. Etapas do Projeto

### 4.1 Ingestão de Dados (Raw)
Nesta etapa foram realizadas as seguintes atividades:
- Leitura de múltiplos arquivos Apache Arrow
- Concatenação das partições
- Amostragem controlada com mais de 100 mil registros
- Exportação para CSV (products_raw.csv)
- Armazenamento na camada Raw

---

### 4.2 Exploração e Catálogo de Dados
Foram realizadas análises exploratórias iniciais com o objetivo de compreender a estrutura e a qualidade da base:
- Identificação de tipos de dados
- Análise de valores ausentes
- Avaliação de distribuições
- Documentação dos campos via Markdown, simulando um catálogo de dados

Essa abordagem substitui o uso direto do catálogo da plataforma, mantendo o mesmo propósito conceitual.

---

### 4.3 Transformações e Qualidade (Silver)
Na camada Silver, os dados foram tratados e padronizados, incluindo:
- Seleção das colunas relevantes para o caso de uso
- Remoção de registros duplicados
- Tratamento de valores ausentes
- Conversão e padronização de tipos de dados
- Padronização de textos e categorias

O resultado foi salvo como products_cleaned.csv, representando uma base consistente e confiável.

---

### 4.4 Consumo Analítico e Preparação para IA (Gold)
A partir da base Silver, foram realizadas análises orientadas ao negócio, incluindo:
- Identificação das categorias com maior volume de produtos
- Análise de preços médios
- Avaliação de produtos com melhores ratings
- Criação de um campo textual consolidado (título + descrição)

Esse campo prepara a base para aplicações de IA e NLP, como busca semântica, classificação automática e recomendação de produtos.

O dataset final foi salvo como products_analytics.csv, compondo a camada Gold.

---

## 5. Item 9 – Data App (Streamlit)
Conforme solicitado no case técnico, foi desenvolvido um Data App utilizando Streamlit, simulando a camada de Data Apps da arquitetura proposta.

O aplicativo demonstra como os dados podem ser disponibilizados para usuários finais e áreas de negócio de forma interativa.

Funcionalidades implementadas:
- Leitura dos dados da camada Raw
- Visualização tabular interativa
- Filtros por categoria
- Exploração básica dos dados
- Similaridade entre produtos baseada em texto, utilizando TF-IDF e similaridade por cosseno

Essa funcionalidade exemplifica o uso de IA aplicada a dados textuais.

---

## 6. Execução do Data App

Pré-requisitos:
- Python 3.9 ou superior
- Ambiente virtual (opcional)

Instalação das dependências:
pip install -r streamlit_app/requirements.txt

Execução do aplicativo:
streamlit run streamlit_app/app.py

Observação: o Data App foi executado localmente devido à ausência de credenciais da plataforma Dadosfera, mantendo aderência conceitual total à arquitetura proposta no case.

---

## 7. Possíveis Evoluções
- Integração com data lake ou banco analítico
- Automatização do pipeline de ingestão
- Implementação de embeddings e busca semântica avançada
- Dashboards analíticos
- Deploy do Data App em ambiente cloud

---

## 8. Considerações Finais
Mesmo sem acesso direto à plataforma Dadosfera, o projeto demonstra domínio do fluxo completo de dados, desde a ingestão até o consumo por meio de um Data App interativo.

A solução foi construída com foco em organização, clareza arquitetural, boas práticas de engenharia de dados e preparo para aplicações de inteligência artificial, atendendo integralmente aos objetivos do case técnico.

---

## 9. Roteiro de Apresentação do Case (5–7 minutos)

Abertura:
Este projeto demonstra um pipeline completo de dados, desde a ingestão até o consumo, simulando uma plataforma analítica corporativa.

Fonte de dados:
Foi utilizado um dataset público de produtos da Amazon, representando um cenário real de dados em escala.

Arquitetura:
A solução foi organizada em camadas Raw, Silver e Gold, garantindo separação de responsabilidades e governança.

Transformações:
Na camada Silver, os dados foram limpos, padronizados e preparados para consumo analítico.

Consumo e IA:
Na camada Gold, foram realizadas análises orientadas ao negócio e preparada a base para aplicações de IA. Além disso, foi desenvolvido um Data App em Streamlit para exploração interativa e similaridade entre produtos.

Fechamento:
Mesmo sem acesso direto à plataforma, o projeto demonstra domínio técnico, capacidade de abstração e aderência aos conceitos propostos no case, sendo facilmente adaptável a um ambiente corporativo real.
