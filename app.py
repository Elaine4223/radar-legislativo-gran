import streamlit as st
import pandas as pd

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Radar Legislações Gran", page_icon="⚖️", layout="wide")

# CABEÇALHO PERSONALIZADO
st.title("⚖️ Radar Legislativo Gran - Monitoramento")
st.info("Foco: Itens marcados como 'Não' ou 'Analisar' na **Aba Legislações**.")

# DADOS DAS LEIS (Você pode alterar os nomes abaixo conforme sua planilha)
dados = [
    {"Lei/Edital": "Lei Orgânica - DF", "Status": "Não", "Link": "https://www.sinj.df.gov.br"},
    {"Lei/Edital": "Regimento Interno CLDF", "Status": "Analisar", "Link": "https://www.cl.df.gov.br"},
    {"Lei/Edital": "Lei 8.112/90", "Status": "Não", "Link": "https://www.planalto.gov.br"},
    {"{"Lei/Edital": "Legislação Específica - SEFA", "Status": "Analisar", "Link": "https://www.sefa.pa.gov.br"}
]
df = pd.DataFrame(dados)

# EXIBIÇÃO DAS LEIS NO NOTEBOOK
st.subheader("📋 Lista de Verificação Diária")

for index, row in df.iterrows():
    with st.expander(f"🔍 {row['Lei/Edital']}"):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"**Status atual na Aba Legislações:** :red[{row['Status']}]")
        with col2:
            st.link_button("Ver no Visualping", row['Link'])
        
        if st.button("Confirmar conferência", key=f"lei_{index}"):
            st.success(f"A lei {row['Lei/Edital']} foi verificada com sucesso!")

# BARRA LATERAL
st.sidebar.image("https://www.grancursosonline.com.br/images/logo-gran.png", width=150)
st.sidebar.write("👤 **Analista:** Elaine")
st.sidebar.write("📌 **Setor:** Legislações")
