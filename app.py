import streamlit as st
import pandas as pd

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Radar Gran 2026", page_icon="⚖️", layout="wide")

# CABEÇALHO
st.title("⚖️ Radar Legislativo Gran - Cronograma 2026")
st.info("Monitorando itens marcados como 'Não' ou 'Analisar' no Visualping (Aba 2026).")

# DADOS DA PLANILHA
dados = [
    {"Lei/Edital": "SEFA PA - Fiscal de Receitas", "Visualping": "Não", "Link": "https://www.sefa.pa.gov.br"},
    {"Lei/Edital": "TJ MS - Analista Judiciário", "Visualping": "Analisar", "Link": "https://www.tjms.jus.br"},
    {"Lei/Edital": "CLDF - Regimento Interno", "Visualping": "Analisar", "Link": "https://www.cl.df.gov.br"},
    {"Lei/Edital": "PMDF - Legislação Específica", "Visualping": "Não", "Link": "https://www.pm.df.gov.br"}
]
df = pd.DataFrame(dados)

# EXIBIÇÃO NO NOTEBOOK
for index, row in df.iterrows():
    with st.expander(f"📍 {row['Lei/Edital']}"):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"**Status no Radar:** {row['Visualping']}")
        with col2:
            st.link_button("Abrir Site Oficial", row['Link'])
        
        if st.button("Marcar como Conferido hoje", key=f"btn_{index}"):
            st.success(f"Conferência de {row['Lei/Edital']} registrada!")

# BARRA LATERAL
st.sidebar.image("https://www.grancursosonline.com.br/images/logo-gran.png", width=150)
st.sidebar.write("👤 **Analista:** Elaine")
st.sidebar.write("📅 **Foco:** Cronograma 2026")
