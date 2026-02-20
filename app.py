import streamlit as st
import pandas as pd
import unicodedata
import os

# Configuração da Página
st.set_page_config(page_title="Radar de Gênia 2026", layout="wide")

# Função para remover acentos e facilitar a busca
def normalizar(texto):
    if not isinstance(texto, str):
        return str(texto)
    return "".join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn').lower()

# Título
st.title("🛡️ Radar Legislativo & Normativo")
st.subheader("Sistema de Monitoramento Integrado - Versão 2026")

# 1. Carregamento Blindado do Arquivo
@st.cache_data
def carregar_planilha():
    nome_arquivo = 'Atualizações Legislações 2026.xlsx - Planilha1.csv'
    if os.path.exists(nome_arquivo):
        df = pd.read_csv(nome_arquivo)
        # Limpa nomes de colunas ocultas
        df.columns = [c.strip() for c in df.columns]
        return df
    else:
        # Se o arquivo não for achado, tentamos o primeiro CSV da pasta
        arquivos = [f for f in os.listdir('.') if f.endswith('.csv')]
        if arquivos:
            return pd.read_csv(arquivos[0])
        return None

df = carregar_planilha()

if df is not None:
    # 2. Métricas Iniciais
    c1, c2, c3 = st.columns(3)
    c1.metric("Base Total", f"{len(df)} itens")
    c2.metric("Status", "Sincronizado")
    
    # Identifica pendências de análise
    col_status = 'VisualPing' if 'VisualPing' in df.columns else df.columns[1]
    pendentes = len(df[df[col_status].astype(str).str.contains('Analisar', case=False, na=False)])
    c3.metric("Alertas de Hoje", pendentes, delta="Pendentes", delta_color="inverse")

    st.markdown("---")

    # 3. Motor de Busca Inteligente
    st.write("### 🔎 Pesquisar Norma")
    busca_usuario = st.text_input("Digite o número, órgão ou nome (Ex: 204, TJPA, SINIEF):")

    if busca_usuario:
        termo = normalizar(busca_usuario)
        
        # Filtra em qualquer parte do nome
        col_nome = 'Nome' if 'Nome' in df.columns else df.columns[0]
        # Aplica a normalização em toda a coluna para busca perfeita
        resultado = df[df[col_nome].apply(normalizar).str.contains(termo, na=False)]
        
        if not resultado.empty:
            st.success(f"✅ Sucesso! Encontramos {len(resultado)} resultado(s).")
            
            # Estilização Profissional
            def colorir(row):
                val = str(row.get(col_status, '')).lower()
                return ['background-color: #fff3cd' if 'analisar' in val else '' for _ in row]

            st.dataframe(resultado.style.apply(colorir, axis=1), use_container_width=True)
        else:
            st.error(f"Nenhum resultado encontrado para '{busca_usuario}'.")
            st.info("💡 Tente apenas o número (ex: 880) ou o órgão (ex: TJMG).")
    else:
        st.write("Visualize os itens da sua base:")
        st.dataframe(df.head(15), use_container_width=True)

    # 4. Aba de Alertas (Diferencial da Gênia)
    with st.expander("🔔 RESUMO EXECUTIVO: Itens para Analisar"):
        df_alerta = df[df[col_status].astype(str).str.contains('Analisar', case=False, na=False)]
        st.dataframe(df_alerta)

else:
    st.error("❌ Atenção: Não conseguimos ler o arquivo CSV. Verifique se ele está no mesmo local que o app.py.")

# Rodapé
st.sidebar.markdown("### ⚙️ Painel Elaine")
st.sidebar.write("Busca Habilitada: Fragmentos e Números")
