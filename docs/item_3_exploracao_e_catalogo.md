# Item 3 – Exploração e Catálogo de Dados

## 3.1 Visão Geral da Base
A base de dados utilizada contém metadados de produtos de e-commerce, incluindo informações como identificador do produto, título, descrição, categoria, preço e avaliações. Os dados foram obtidos a partir de um dataset público e processados localmente antes da ingestão na plataforma.

## 3.2 Estrutura dos Dados
Após a ingestão, foi realizada uma análise exploratória inicial para compreensão da estrutura da base. O dataset apresenta colunas textuais e numéricas, possibilitando tanto análises descritivas quanto aplicações de inteligência artificial, como busca semântica e classificação.

Principais campos:
- `parent_asin`: identificador único do produto
- `title`: título do produto
- `description`: descrição textual
- `main_category`: categoria principal
- `price`: preço do produto
- `average_rating`: avaliação média dos usuários

## 3.3 Qualidade dos Dados
Foram identificados alguns desafios comuns em bases reais de e-commerce, como:
- valores ausentes em campos de descrição e preço
- variação no tamanho e qualidade dos textos
- necessidade de padronização de categorias

Esses pontos foram considerados para as etapas posteriores de tratamento e enriquecimento dos dados.

## 3.4 Catálogo de Dados
Os dados foram catalogados na plataforma, permitindo:
- visualização do schema
- documentação dos campos
- reutilização da base por outros usuários
- governança e rastreabilidade dos dados
