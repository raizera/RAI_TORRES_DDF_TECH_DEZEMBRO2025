# Item 1 – Base de Dados

## 1.1 Contexto do Negócio

O cliente deste projeto é uma **grande empresa de e-commerce** que busca construir uma Plataforma de Dados capaz de:

- Centralizar informações de produtos e vendas
- Explorar dados estruturados e desestruturados
- Utilizar Inteligência Artificial para melhorar a experiência de compra
- Acelerar a geração de insights para as áreas de negócio

Nesse contexto, dados relacionados ao **catálogo de produtos** são críticos, pois impactam diretamente:
- Busca e recomendação
- Conversão de vendas
- Experiência do usuário
- Estratégias de precificação e marketing

---

## 1.2 Dataset Selecionado

### 📦 Product Search Corpus (Hugging Face)

O dataset escolhido para este case foi o **Product Search Corpus**, disponibilizado publicamente no Hugging Face, e explicitamente sugerido na descrição do case técnico.

**Principais características:**
- Domínio: E-commerce
- Tipo de dados: Estruturados e desestruturados
- Volume: +1 milhão de registros (foi utilizada uma amostra com mais de 150.000 registros)
- Formato: JSON / Parquet
- Fonte: Hugging Face Datasets

---

## 1.3 Estrutura dos Dados

O dataset contém, entre outros, os seguintes atributos relevantes:

| Campo | Descrição |
|------|----------|
| product_id | Identificador único do produto |
| product_title | Título do produto |
| product_description | Descrição detalhada do produto |
| category | Categoria do produto |
| brand | Marca |
| price | Preço do produto |
| created_at | Data de criação do produto |
| rating | Avaliação média |
| sales_volume | Volume de vendas |
| region | Região de comercialização |

> Observação: Alguns atributos (preço, região, vendas) foram gerados de forma sintética para enriquecer as análises e simular um ambiente real de e-commerce.

---

## 1.4 Justificativa da Escolha da Base

A escolha do Product Search Corpus se justifica pelos seguintes fatores:

1. **Aderência ao domínio do negócio**  
   O dataset representa fielmente o catálogo de produtos de um e-commerce, permitindo análises reais de mercado.

2. **Volume de dados significativo**  
   O volume atende ao requisito mínimo do case (mais de 100.000 registros), possibilitando análises escaláveis.

3. **Presença de dados desestruturados**  
   Os campos de texto (título e descrição) são ideais para:
   - Uso de LLMs
   - Extração de features
   - Similaridade entre produtos
   - Análises semânticas

4. **Alinhamento com GenAI**  
   O dataset permite demonstrar, na prática, como a Inteligência Artificial pode transformar texto em dados estruturados de alto valor analítico.

5. **Flexibilidade para análises futuras**  
   A base permite expansão para:
   - Recomendação de produtos
   - Análise de categorias
   - Séries temporais
   - Modelos preditivos

---

## 1.5 Papel da Base no Ciclo de Vida dos Dados

Dentro do Ciclo de Vida dos Dados da Dadosfera, essa base é utilizada para:

- **Integrar**: ingestão dos dados brutos
- **Explorar**: catalogação e entendimento dos dados
- **Processar**: transformação e enriquecimento via GenAI
- **Analisar**: criação de dashboards e análises avançadas
- **Consumir**: uso em Data Apps e modelos de IA

---

## 1.6 Considerações Finais

A base de dados escolhida oferece o equilíbrio ideal entre **complexidade técnica**, **valor de negócio** e **aderência ao case proposto**, permitindo demonstrar de forma prática como a Dadosfera acelera o caminho entre dados brutos e geração de valor por meio de Inteligência Artificial.
