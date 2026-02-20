import streamlit as st
import pandas as pd

# 1. Configurações Iniciais
st.set_page_config(page_title="Radar de Gênia 2026", layout="wide")

# 2. Conexão Direta com a sua Planilha Google
# Transformamos o link de edição em um link de exportação CSV para o código ler
sheet_id = "1r5yoDM2Hzrh3S3idFEAz6vWtegYQZ3cziTht84IFJBU"
gid = "1568671051"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"

@st.cache_data(ttl=60) # Atualiza os dados a cada 1 minuto se houver mudança na planilha
def carregar_dados_google():
    try:
        df = pd.read_csv(url)
        # Limpeza de nomes de colunas
        df.columns = [c.strip() for c in df.columns]
        return df
    except Exception as e:
        st.error(f"Erro ao conectar com o Google Sheets: {e}")
        return None

df = carregar_dados_google()

# 3. Interface do App
st.title("🛡️ Radar Legislativo & Normativo")
st.subheader("Monitoramento Inteligente (Conexão Google Sheets)")

if df is not None:
    # Métricas no topo
    c1, c2, c3 = st.columns(3)
    c1.metric("Total de Itens", len(df))
    c2.metric("Fonte", "Google Planilha")
    # Tenta encontrar a coluna de status para contar os "Analisar"
    col_status = 'VisualPing' if 'VisualPing' in df.columns else df.columns[1]
    alertas = len(df[df[col_status].astype(str).str.contains('Analisar', case=False, na=False)])
    c3.metric("Alertas Ativos", alertas, delta_color="inverse")

    st.markdown("---")

    # 4. Motor de Busca Flexível
    st.write("### 🔎 Pesquisar na Base")
    busca = st.text_input("Digite o número, órgão ou termo da lei (Ex: 204, TJPA, SINIEF):")

    col_nome = 'Nome' if 'Nome' in df.columns else df.columns[0]

    if busca:
        # Busca inteligente que ignora maiúsculas e minúsculas
        filtro = df[col_nome].astype(str).str.contains(busca, case=False, na=False)
        resultado = df[filtro]
        
        if not resultado.empty:
            st.success(f"✅ Encontramos {len(resultado)} item(ns).")
            
            # Função para colorir a linha se for 'Analisar'
            def highlight_row(row):
                return ['background-color: #fff3cd' if 'analisar' in str(row[col_status]).lower() else '' for _ in row]
            
            st.dataframe(resultado.style.apply(highlight_row, axis=1), use_container_width=True)
        else:
            st.error(f"Nenhum resultado para '{busca}'. Verifique a grafia na planilha.")
    else:
        st.write("Visualize os itens da planilha (Top 20):")
        st.dataframe(df.head(20), use_container_width=True)

    # 5. Aba de Pendências (Foco da Gerente)
    with st.expander("🔔 LISTA DE PRIORIDADES (Status: Analisar)"):
        df_prioridade = df[df[col_status].astype(str).str.contains('Analisar', case=False, na=False)]
        st.dataframe(df_prioridade)

st.sidebar.markdown("### ⚙️ Painel de Controle")
st.sidebar.write("**Status:** Conectado ao Google Drive")
st.sidebar.info("As alterações feitas na planilha aparecem aqui após 1 minuto.")
