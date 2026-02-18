import streamlit as st
import pandas as pd

1. CONFIGURAÇÃO PARA NOTEBOOK (TELA LARGA)
st.set_page_config(page_title="Radar Gran 2026", page_icon="⚖️", layout="wide")

2. CABEÇALHO PROFISSIONAL
st.title("⚖️ Radar Legislativo Gran - Cronograma 2026")
st.info("Monitorando itens marcados como 'Não' ou 'Analisar' no Visualping (Aba 2026).")

Estilo de fundo para o Analista
st.markdown("<style>.stApp { background-color: #f5f5f5; }</style>", unsafe_allow_html=True)

3. DADOS DA SUA PLANILHA (FILTRO: NÃO / ANALISAR)
dados = [
{"Lei/Edital": "SEFA PA - Fiscal de Receitas", "Visualping": "Não", "Link": ""},
{"Lei/Edital": "TJ MS - Analista Judiciário", "Visualping": "Analisar", "Link": "[link suspeito removido]"},
{"Lei/Edital": "CLDF - Regimento Interno", "Visualping": "Analisar", "Link": ""},
{"Lei/Edital": "PMDF - Legislação Específica", "Visualping": "Não", "Link": ""}
]
df = pd.DataFrame(dados)

4. EXIBIÇÃO ORGANIZADA PARA NOTEBOOK
for index, row in df.iterrows():
with st.expander(f"📍 {row['Lei/Edital']}"):
col1, col2 = st.columns([3, 1])
with col1:
st.write(f"Status no Radar: {row['Visualping']}")
with col2:
st.link_button("Abrir Site Oficial", row['Link'])

5. BARRA LATERAL COM IDENTIDADE GRAN
st.sidebar.image("", width=150)
st.sidebar.write("👤 Analista: Elaine")
st.sidebar.write("📅 Foco: Cronograma 2026")
