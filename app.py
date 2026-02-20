import streamlit as st
import pandas as pd

# 1. Configurações
st.set_page_config(page_title="Radar de Gênia 2026", layout="wide")

# 2. Dados da sua Planilha (Amostra Real da sua Cópia)
@st.cache_data
def load_data():
    data = {
        "Nome": [
            "ABNT NBR ISO 31000, de 2018",
            "Ajuste SINIEF n. 02, de 2009",
            "Resolução Tjmg 880, de 2018",
            "Resolução TJPA n. 14, de 2016",
            "Resolução TJCE n. 07, de 2020",
            "Resolução TSE n. 23.709, de 2022"
        ],
        "VisualPing": ["Não", "Analisar", "Analisar", "Não", "Não", "Analisar"],
        "Atualização": ["", "Art. 1º alterado", "Nova redação Art. 12", "", "", "Update LGPD"],
        "Data": ["2026-01-05", "2026-01-15", "2026-01-13", "2026-01-13", "2026-01-13", "2026-02-20"]
    }
    return pd.DataFrame(data)

df = load_data()

# 3. Interface
st.title("🛡️ Radar Legislativo & Normativo")
st.markdown("---")

tab1, tab2 = st.tabs(["📊 Base Completa", "🔔 Alertas (Analisar)"])

with tab1:
    st.write("### 🔍 Pesquisa Rápida")
    # O segredo está aqui: busca flexível
    busca = st.text_input("Digite qualquer parte do nome da lei:")
    
    if busca:
        # Ele procura o termo dentro do nome, ignorando se é maiúsculo ou minúsculo
        resultado = df[df['Nome'].str.contains(busca, case=False, na=False)]
        
        if not resultado.empty:
            st.success(f"Encontrado(s) {len(resultado)} item(ns):")
            st.dataframe(resultado, use_container_width=True)
        else:
            st.error(f"Nenhum resultado para '{busca}'. Tente um termo mais curto (ex: apenas o número ou o órgão).")
    else:
        st.dataframe(df, use_container_width=True)

with tab2:
    st.write("### ⚠️ Itens para Análise")
    df_alertas = df[df['VisualPing'] == 'Analisar']
    st.dataframe(df_alertas.style.applymap(lambda x: 'background-color: #fff3cd', subset=['VisualPing']), use_container_width=True)

st.sidebar.info("Dica: Digite apenas o número da lei para uma busca mais rápida.")
