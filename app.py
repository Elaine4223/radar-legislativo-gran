import streamlit as st
import pandas as pd

st.set_page_config(page_title="Radar de Gênia 2026", layout="wide")

st.title("🛡️ Radar Legislativo & Normativo")
st.subheader("Inteligência e Monitoramento - Elaine (Edição 2026)")

# --- BASE DE DADOS REAL (Simulando sua planilha) ---
# Aqui listamos alguns exemplos da sua planilha para o teste de busca
dados_completos = [
    {"Nome": "ABNT NBR ISO 31000, de 2018", "Status": "✅ Estável", "Data": "05/01/2026", "Update": ""},
    {"Nome": "Ajuste SINIEF n. 02, de 2009", "Status": "⚠️ ANALISAR", "Data": "15/01/2026", "Update": "Alterado pelo Ajuste 50/2025"},
    {"Nome": "Resolução Tjmg 880, de 2018", "Status": "⚠️ ANALISAR", "Data": "13/01/2026", "Update": "Nova redação Art. 12"},
    {"Nome": "Resolução TJPA n. 14, de 2016", "Status": "✅ Estável", "Data": "13/01/2026", "Update": ""},
    {"Nome": "Resolução TJCE n. 07, de 2020", "Status": "✅ Estável", "Data": "13/01/2026", "Update": ""}
]
df_total = pd.DataFrame(dados_completos)

# --- SISTEMA DE ABAS ---
tab1, tab2 = st.tabs(["📊 Base de Monitoramento", "🔔 Atualizações Recentes"])

with tab1:
    st.write("### 🔍 Pesquisar na Base Geral")
    # O PULO DO GATO: A busca agora filtra a tabela abaixo
    busca = st.text_input("Digite o nome da norma (Ex: TJPA ou 31000):")
    
    if busca:
        # Filtra a tabela ignorando maiúsculas/minúsculas
        resultado = df_total[df_total['Nome'].str.contains(busca, case=False)]
        if not resultado.empty:
            st.success(f"Encontrado: {len(resultado)} item(ns)")
            st.dataframe(resultado, use_container_width=True)
        else:
            st.error("Nenhuma norma encontrada com esse nome na base de teste.")
    else:
        st.dataframe(df_total, use_container_width=True)

with tab2:
    st.write("### ⚠️ Detalhamento de Alterações")
    # Filtra apenas o que é "ANALISAR" para aparecer nesta aba
    df_alertas = df_total[df_total['Status'] == "⚠️ ANALISAR"]
    st.warning("Itens que exigem revisão jurídica imediata:")
    st.table(df_alertas[['Nome', 'Update', 'Data']])

# Rodapé
st.sidebar.info(f"Monitorando {len(df_total)} normas de teste.")
