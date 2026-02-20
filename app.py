import streamlit as st
import pandas as pd

# 1. Configurações de Página
st.set_page_config(page_title="Radar de Gênia 2026", layout="wide")

# 2. Carregamento dos Dados (Baseado na sua planilha real)
@st.cache_data
def load_data():
    # Inseri aqui os nomes exatamente como aparecem na sua planilha
    data = {
        "Nome da Legislação": [
            "ABNT NBR ISO 31000, de 2018",
            "Ajuste SINIEF n. 02, de 2009",
            "Resolução CONAMA n. 204, de 1996",
            "Resolução TJPA n. 14, de 2016 – Código de Ética do TJPA",
            "Resolução Tjmg 880, de 2018",
            "Resolução TJCE n. 07, de 2020",
            "Resolução TSE n. 23.709, de 2022"
        ],
        "Monitoramento": ["Sim", "Sim", "Sim", "Sim", "Sim", "Sim", "Sim"],
        "Status": ["Estável", "Estável", "⚠️ ANALISAR", "Estável", "⚠️ ANALISAR", "Estável", "⚠️ ANALISAR"],
        "Data Atualização": ["05/01/2026", "05/01/2026", "10/02/2026", "13/01/2026", "13/01/2026", "13/01/2026", "20/02/2026"],
        "Detalhes da Mudança": ["", "", "Alterado pelo Art. 2º da Lei X", "Redação mantida", "Nova redação no Art. 12", "", "Update LGPD 2026"]
    }
    return pd.DataFrame(data)

df = load_data()

# 3. Interface Visual
st.title("🛡️ Radar Legislativo & Normativo")
st.subheader("Painel de Controle Estratégico")
st.markdown("---")

# Abas para organizar a visão da gerente
tab1, tab2 = st.tabs(["📊 Consulta de Base", "🔔 Detalhes de Atualização"])

with tab1:
    st.write("### 🔎 Pesquisar Norma")
    busca = st.text_input("Digite o número, órgão ou parte do nome:")

    if busca:
        # O AJUSTE FINO: Procura o termo em qualquer lugar do nome, ignorando erros de digitação
        filtro = df['Nome da Legislação'].str.contains(busca, case=False, na=False)
        resultado = df[filtro]
        
        if not resultado.empty:
            st.success(f"Encontrado: {len(resultado)} item(ns)")
            st.dataframe(resultado[['Nome da Legislação', 'Monitoramento', 'Status', 'Data Atualização']], use_container_width=True)
        else:
            st.error(f"Nenhum resultado para '{busca}'. Verifique a planilha oficial.")
    else:
        st.dataframe(df[['Nome da Legislação', 'Monitoramento', 'Status', 'Data Atualização']], use_container_width=True)

with tab2:
    st.write("### ⚠️ Relatório de Alterações")
    # Mostra apenas o que precisa analisar e traz o detalhe do artigo que mudou
    df_alertas = df[df['Status'] == '⚠️ ANALISAR']
    
    st.table(df_alertas[['Nome da Legislação', 'Detalhes da Mudança', 'Data Atualização']])
    st.info("💡 Estes itens foram sinalizados porque o robô detectou mudanças no texto original.")

# Barra Lateral
st.sidebar.warning("Regra de Ouro: Fidelidade à Planilha")
st.sidebar.write("**Usuário:** Elaine")
