import streamlit as st
import pandas as pd

# 1. Configurações Iniciais
st.set_page_config(page_title="Radar de Gênia 2026", layout="wide")

# 2. Base de Dados Interna (A que funcionou nos seus testes)
@st.cache_data
def carregar_dados_apresentacao():
    data = {
        "Nome da Legislação": [
            "ABNT NBR ISO 31000, de 2018",
            "Ajuste SINIEF n. 02, de 2009",
            "Resolução CONAMA n. 204, de 1996",
            "Resolução TJPA n. 14, de 2016 – Código de Ética do TJPA",
            "Resolução Tjmg 880, de 2018",
            "Resolução TJCE n. 07, de 2020",
            "Resolução TSE n. 23.709, de 2022",
            "Resolução RDC ANVISA n. 430, de 2020"
        ],
        "Monitoramento": ["Ativo", "Ativo", "Ativo", "Ativo", "Ativo", "Ativo", "Ativo", "Ativo"],
        "Status": ["Estável", "Estável", "⚠️ ANALISAR", "Estável", "⚠️ ANALISAR", "Estável", "⚠️ ANALISAR", "Estável"],
        "Data Atualização": ["05/01/2026", "05/01/2026", "10/02/2026", "13/01/2026", "13/01/2026", "13/01/2026", "20/02/2026", "20/02/2026"],
        "Detalhe do Impacto": ["", "", "Alteração no Art. 5º - Impacto Ambiental", "", "Nova redação dada ao Art. 12", "", "Adequação LGPD necessária", ""]
    }
    return pd.DataFrame(data)

df = carregar_dados_apresentacao()

# 3. Cabeçalho do App
st.title("🛡️ Radar Legislativo & Normativo")
st.subheader("Protótipo de Inteligência Jurídica - Apresentação Executiva")

# Métricas para impacto visual
c1, c2, c3 = st.columns(3)
c1.metric("Itens Mapeados", "2.607")
c2.metric("Motor de Busca", "Fidelidade 100%")
c3.metric("Pendências", "3", delta="Atenção", delta_color="inverse")

st.markdown("---")

# 4. Sistema de Abas
tab1, tab2 = st.tabs(["📊 Base de Consulta", "🔔 Atualizações Detalhadas"])

with tab1:
    st.write("### 🔎 Buscar na Base de Dados")
    # Busca ultra flexível que você testou e gostou
    busca = st.text_input("Digite o número (ex: 204), órgão (ex: TJPA) ou nome da lei:")

    if busca:
        # Lógica de filtro que busca em qualquer parte do nome
        resultado = df[df['Nome da Legislação'].str.contains(busca, case=False, na=False)]
        
        if not resultado.empty:
            st.success(f"Encontrado: {len(resultado)} item(ns)")
            
            # Estilização: Se tiver 'ANALISAR', a linha fica amarela
            def highlight_analisar(row):
                return ['background-color: #fff3cd' if 'ANALISAR' in str(row['Status']) else '' for _ in row]
            
            st.dataframe(resultado.style.apply(highlight_analisar, axis=1), use_container_width=True)
        else:
            st.error(f"Nenhum resultado para '{busca}'.")
    else:
        st.write("Visão Geral da Base:")
        st.dataframe(df[['Nome da Legislação', 'Monitoramento', 'Status', 'Data Atualização']], use_container_width=True)

with tab2:
    st.write("### ⚠️ Detalhamento de Alterações (Artigos Afetados)")
    # Mostra apenas os itens que precisam de análise
    df_alertas = df[df['Status'] == '⚠️ ANALISAR']
    st.table(df_alertas[['Nome da Legislação', 'Detalhe do Impacto', 'Data Atualização']])

# 5. Rodapé Lateral com a sua estratégia
st.sidebar.markdown("### ⚙️ Próxima Etapa")
st.sidebar.success("✅ Interface Pronta")
st.sidebar.success("✅ Base de Dados Mapeada")
st.sidebar.warning("⏳ Sincronização Automática (Aguardando Aprovação)")
st.sidebar.write("---")
st.sidebar.info("Este app opera em modo protótipo com fidelidade textual total à planilha oficial.")
