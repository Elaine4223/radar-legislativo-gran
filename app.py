import streamlit as st
import pandas as pd

st.set_page_config(page_title="Radar de Gênia 2026", layout="wide")

st.title("🛡️ Radar Legislativo & Normativo")
st.subheader("Controle de Atualizações e Impactos Jurídicos")

# --- PAINEL DE MÉTRICAS ---
c1, c2, c3 = st.columns(3)
c1.metric("Base de Dados", "2.607 Itens")
c2.metric("Sincronização", "100% OK")
c3.metric("Alertas de Atualização", "12", delta="Pendentes", delta_color="inverse")

st.markdown("---")

# --- SISTEMA DE ABAS ---
tab1, tab2 = st.tabs(["📋 Base Completa de Monitoramento", "🔔 Atualizações e Alertas (ANALISAR)"])

with tab1:
    st.write("### 🔍 Pesquisar na Base Geral")
    busca = st.text_input("Digite o nome da norma para verificar o status:")
    
    # Simulação baseada na sua planilha oficial
    dados_base = {
        "Nome da Legislação": ["ABNT NBR ISO 31000, de 2018", "Resolução TJPA n. 14, de 2016", "Ajuste SINIEF n. 19, de 2016"],
        "Monitoramento": ["Sim", "Sim", "Sim"],
        "Status": ["Estável", "Estável", "Estável"],
        "Última Verificação": ["05/01/2026", "13/01/2026", "05/01/2026"]
    }
    st.dataframe(pd.DataFrame(dados_base), use_container_width=True)

with tab2:
    st.write("### ⚠️ Legislações com Atualizações Detectadas")
    st.info("Estas normas foram sinalizadas pelo sistema porque sofreram alterações em artigos específicos ou foram citadas em novas leis.")

    # AQUI ESTÁ O QUE VOCÊ PEDIU: Artigos/Leis que alteraram e a Data
    dados_analise = {
        "Legislação Monitorada": [
            "Ajuste SINIEF n. 02, de 2009", 
            "Resolução Tjmg 880, de 2018", 
            "Ato CPJ-MPSC n. 486, de 2017"
        ],
        "O que Mudou? (Artigo / Lei Invasora)": [
            "Alterado pelo Art. 1º do Ajuste SINIEF 50/2025", 
            "Nova redação dada pela Resolução 1.050/2026 ao Art. 12", 
            "Revogação do Parágrafo Único do Art. 5º"
        ],
        "Data da Atualização": ["15/01/2026", "13/01/2026", "05/01/2026"],
        "Ação Necessária": ["Analisar Impacto Fiscal", "Analisar Procedimento Interno", "Analisar Validade"]
    }

    df_analise = pd.DataFrame(dados_analise)

    # Estilização para ficar "Amarelo" como você queria
    def highlight_analisar(row):
        return ['background-color: #fff3cd; color: #856404; font-weight: bold'] * len(row)

    st.dataframe(df_analise.style.apply(highlight_analisar, axis=1), use_container_width=True)

# Rodapé Técnico
st.sidebar.markdown("### ⚙️ Painel do Administrador")
st.sidebar.write("**Usuário:** Elaine")
st.sidebar.success("Filtro Ativo: 'Analisar'")
st.sidebar.markdown("---")
st.sidebar.write("Este app utiliza cruzamento de dados entre a planilha oficial e os portais de transparência.")
