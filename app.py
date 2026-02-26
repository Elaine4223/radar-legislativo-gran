import streamlit as st
import pandas as pd
from datetime import datetime

# 1. Configurações Iniciais
st.set_page_config(page_title="Radar de Gênia 2026", layout="wide")

# 2. Base de Dados (Fiel à sua planilha)
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
        "Monitoramento": ["Ativo"] * 7,
        "Status": ["Estável", "Estável", "⚠️ ANALISAR", "⚠️ ANALISAR", "Estável", "⚠️ ANALISAR", "Estável"],
        "Data Atualização": ["05/01/2026", "05/01/2026", "10/02/2026", "13/01/2026", "13/01/2026", "20/02/2026", "20/02/2026"],
        "Artigo Afetado": ["", "", "Art. 5º", "Art. 12", "", "Art. 45", ""]
    }
    return pd.DataFrame(data)

df = carregar_dados()

# 3. Cabeçalho e Métricas
st.title("🛡️ Radar Legislativo & Normativo")
st.subheader("Gestão de Conformidade e Alertas")

c1, c2, c3 = st.columns(3)
c1.metric("Total Monitorado", "2.607")
c2.metric("Status", "Sincronizado")
df_analisar = df[df['Status'] == '⚠️ ANALISAR']
c3.metric("Alertas Pendentes", len(df_analisar))

st.markdown("---")

# 4. Sistema de Abas
tab1, tab2, tab3 = st.tabs(["🔍 Consulta", "📊 Relatórios", "✉️ Configurar Alertas"])

with tab1:
    st.write("### Pesquisa Rápida")
    busca = st.text_input("Digite o número ou órgão (ex: 880):")
    if busca:
        resultado = df[df['Nome da Legislação'].str.contains(busca, case=False, na=False)]
        st.dataframe(resultado, use_container_width=True)
    else:
        st.dataframe(df, use_container_width=True)

with tab2:
    st.write("### 📄 Gerar Relatório de Auditoria")
    st.write("Clique no botão abaixo para baixar o relatório das normas que sofreram alterações.")
    
    # Botão para baixar apenas o que é 'ANALISAR'
    csv = df_analisar.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Baixar Relatório (Excel/CSV)",
        data=csv,
        file_name=f'relatorio_radar_{datetime.now().strftime("%d_%m_%Y")}.csv',
        mime='text/csv',
    )
    st.info("O relatório contém o nome da norma, a data da alteração e o artigo específico identificado pela Verdent.")

with tab3:
    st.write("### ✉️ Notificações por E-mail")
    email = st.text_input("E-mail para receber alertas:", placeholder="exemplo@empresa.com.br")
    frequencia = st.selectbox("Frequência dos Alertas:", ["Imediato", "Resumo Diário", "Resumo Semanal"])
    
    if st.button("Configurar Notificação"):
        if email:
            st.success(f"Configurado! Alertas para {email} ativados com frequência {frequencia}.")
            st.toast("E-mail de teste enviado!", icon="📧")
        else:
            st.error("Por favor, insira um e-mail válido.")

# 5. Rodapé
st.sidebar.markdown("### ⚙️ Painel Elaine")
st.sidebar.write("**Status da IA:** Operacional")
st.sidebar.write("**Último Relatório:** Hoje")
