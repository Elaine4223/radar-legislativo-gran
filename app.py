import streamlit as st
import pandas as pd
import os

# 1. Configurações Iniciais
st.set_page_config(page_title="Radar de Gênia 2026", layout="wide")

st.title("🛡️ Radar Legislativo & Normativo")
st.subheader("Consulta Integrada à Planilha Oficial")

# 2. Função para Carregar o Arquivo que você subiu
@st.cache_data
def load_excel_data():
    file_path = 'Atualizações Legislações 2026.xlsx - Planilha1.csv'
    if os.path.exists(file_path):
        # Lendo o CSV com a grafia exata
        df = pd.read_csv(file_path)
        return df
    else:
        st.error("Arquivo não encontrado. Certifique-se de que o CSV está na mesma pasta do app.")
        return pd.DataFrame()

df = load_data = load_excel_data()

# 3. Interface de Busca
if not df.empty:
    st.write(f"📊 Base carregada com sucesso: **{len(df)} normas monitoradas.**")
    
    st.markdown("---")
    st.write("### 🔎 Pesquisar Norma")
    # Campo de busca que aceita qualquer parte do nome
    busca = st.text_input("Digite o número da lei ou nome do órgão (Ex: 204, TJPA, SINIEF):")

    if busca:
        # Lógica de Filtro "Contém": procura o termo em qualquer lugar da coluna 'Nome'
        # Convertemos tudo para texto para evitar erro com números
        filtro = df['Nome'].astype(str).str.contains(busca, case=False, na=False)
        resultado = df[filtro]
        
        if not resultado.empty:
            st.success(f"✅ Encontramos {len(resultado)} item(ns).")
            
            # Estilização: Se na coluna 'VisualPing' estiver 'Analisar', fica amarelo
            def destacar_analise(row):
                return ['background-color: #fff3cd' if row['VisualPing'] == 'Analisar' else '' for _ in row]

            st.dataframe(resultado.style.apply(destacar_analise, axis=1), use_container_width=True)
        else:
            st.error(f"❌ Nenhuma norma encontrada para '{busca}'.")
            st.info("💡 Dica: Verifique se o número está correto ou tente um termo mais curto.")
    else:
        # Se não houver busca, mostra apenas as primeiras 10 para não poluir a tela
        st.write("Aguardando busca... Abaixo, uma prévia da base:")
        st.dataframe(df.head(10), use_container_width=True)

# 4. Aba de Atualizações (O que a gerente quer ver)
st.markdown("---")
with st.expander("🔔 Ver apenas itens para ANALISAR"):
    df_analisar = df[df['VisualPing'] == 'Analisar']
    if not df_analisar.empty:
        st.dataframe(df_analisar, use_container_width=True)
    else:
        st.write("Nenhuma atualização pendente no momento.")

st.sidebar.warning("Regra de Ouro: Fidelidade à Planilha")
st.sidebar.info("Este app lê diretamente o seu arquivo CSV.")
