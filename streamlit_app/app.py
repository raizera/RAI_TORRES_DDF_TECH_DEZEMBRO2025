import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Product Explorer", layout="wide")

st.title("🛒 Product Explorer – E-commerce Analytics")

@st.cache_data
def load_data():
    return pd.read_csv("../data/raw/products_raw.csv")

df = load_data()

st.sidebar.header("Filtros")

category_col = "category" if "category" in df.columns else None

if category_col:
    categories = st.sidebar.multiselect(
        "Categoria",
        df[category_col].dropna().unique()
    )
    if categories:
        df = df[df[category_col].isin(categories)]

st.subheader("Visão Geral")
st.write(f"Total de produtos: {len(df):,}")
st.dataframe(df.head(20))

# -------------------------------
# Similaridade de Produtos
# -------------------------------
st.subheader("🔍 Similaridade entre Produtos")

text_col = "title" if "title" in df.columns else df.columns[0]

selected_product = st.selectbox(
    "Escolha um produto",
    df[text_col].dropna().unique()
)

if st.button("Encontrar similares"):
    corpus = df[text_col].fillna("").tolist()
    tfidf = TfidfVectorizer(stop_words="english", max_features=5000)
    tfidf_matrix = tfidf.fit_transform(corpus)

    idx = df[df[text_col] == selected_product].index[0]
    sim_scores = cosine_similarity(tfidf_matrix[idx], tfidf_matrix)[0]

    df["similarity"] = sim_scores
    top_similar = (
        df.sort_values("similarity", ascending=False)
        .iloc[1:6][[text_col, "similarity"]]
    )

    st.write("Produtos mais similares:")
    st.dataframe(top_similar)
