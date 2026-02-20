import streamlit as st
import pandas as pd

# 1. Configurações Iniciais
st.set_page_config(page_title="Radar de Gênia 2026", layout="wide")

# 2. Base de Dados Interna (Fiel à sua planilha)
@st.cache_data
def carregar_dados():
    data = {
        "Nome da Legislação": [
            "ABNT NBR ISO 31000, de 2018",
            "Ajuste SINIEF n. 02, de 2009",
            "Resolução CONAMA n. 204, de 1996",
            "Resolução Tjmg 880, de 2018",
            "Resolução TJPA n. 14, de 2016 – Código de Ética do TJPA",
            "Resolução TSE n. 23.709, de 2022",
            "Resolução RDC ANVISA n. 430, de 2020"
        ],
        "Monitoramento": ["Ativo", "Ativo", "Ativo", "Ativo", "Ativo", "Ativo", "Ativo"],
        "Status": ["Estável", "Estável", "⚠️ ANALISAR", "⚠️ ANALISAR", "Estável", "⚠️ ANALISAR", "Estável"],
        "Data Atualização": ["05/01/2026", "05/01/2026", "10/02/2026", "13/01/2026", "13/01/2026", "20/02/2026", "20/02/2026"],
        "Artigo / Lei Invasora": [
            "", 
            "", 
            "Alterado pelo Art. 5º da Lei 14.123/2025", 
            "Nova redação no Art. 12 (Procedimentos)", 
            "", 
            "Impacto da LGPD no Art. 45", 
            ""
        ]
    }
    return pd.DataFrame(data)

df = carregar_dados()

# 3. Cabeçalho
st.title("🛡️ Radar Legislativo & Normativo")
st.subheader("Painel de Controle - Elaine (Edição Executiva 2026)")

# Métricas de Impacto
c1, c2, c3 = st.columns(3)
c1.metric("Itens Monitorados", "2.607")
c2.metric("Motor de Busca", "Fragmento Ativo")
# Conta quantos precisam analisar na base de teste
pendentes = len(df[df['Status'] == '⚠️ ANALISAR'])
c3.metric("Alertas Críticos", pendentes, delta="Atenção", delta_color="inverse")

st.markdown("---")

# 4. SISTEMA DE ABAS (O que você achou fantástico!)
tab1, tab2 = st.tabs(["📊 Base de Consulta", "🔔 Detalhamento de Atualizações"])

with tab1:
    st.write("### 🔎 Pesquisar Norma")
    busca = st.text_input("Digite o número (ex: 880), órgão (ex: TJPA) ou nome:")

    if busca:
        # A lógica do "880" que deu certo!
        mask = df['Nome da Legislação'].str.contains(busca, case=False, na=False)
        resultado = df[mask]
        
        if not resultado.empty:
            st.success(f"✅ Encontrado: {len(resultado)} item(ns)")
            
            # Destaque visual
            def style_analisar(val):
                return 'background-color: #fff3cd; font-weight: bold' if 'ANALISAR' in str(val) else ''
            
            st.dataframe(resultado[['Nome da Legislação', 'Status', 'Data Atualização']].style.applymap(style_analisar, subset=['Status']), use_container_width=True)
        else:
            st.error(f"❌ Nenhum resultado para '{busca}'.")
    else:
        st.write("Aguardando busca... Veja os primeiros itens da base:")
        st.dataframe(df[['Nome da Legislação', 'Status', 'Data Atualização']].head(10), use_container_width=True)

with tab2:
    st.write("### ⚠️ Relatório de Alterações Detectadas")
    st.info("O sistema identifica a norma original e qual alteração (Artigo ou Lei) causou a mudança de status.")
    
    # Filtra apenas o que é 'ANALISAR'
    df_alertas = df[df['Status'] == '⚠️ ANALISAR']
    
    if not df_alertas.empty:
        # Tabela focada no detalhamento técnico
        st.table(df_alertas[['Nome da Legislação', 'Artigo / Lei Invasora', 'Data Atualização']])
    else:
        st.success("Tudo em ordem! Nenhuma pendência de análise no momento.")

# 5. Barra Lateral
st.sidebar.markdown("### ⚙️ Próximos Passos")
st.sidebar.info("Aprovação da Gerência: ⏳ Pendente")
st.sidebar.write("A sincronização automática será habilitada após o OK da gestão.")
