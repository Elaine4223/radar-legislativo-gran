import streamlit as st
import pandas as pd

# 1. Configurações
st.set_page_config(page_title="Radar de Gênia 2026", layout="wide")

# 2. Base de Dados (Exatamente como na sua planilha)
@st.cache_data
def carregar_dados():
    data = {
        "Nome": [
            "ABNT NBR ISO 31000, de 2018",
            "Ajuste SINIEF n. 02, de 2009",
            "Resolução CONAMA n. 204, de 1996",
            "Resolução Tjmg 880, de 2018",
            "Resolução TJPA n. 14, de 2016 – Código de Ética do TJPA",
            "Resolução TSE n. 23.709, de 2022",
            "Resolução RDC ANVISA n. 430, de 2020"
        ],
        "VisualPing": ["Não", "Não", "Analisar", "Analisar", "Não", "Analisar", "Não"],
        "Data Atualização": ["05/01/2026", "05/01/2026", "10/02/2026", "13/01/2026", "13/01/2026", "20/02/2026", "20/02/2026"]
    }
    return pd.DataFrame(data)

df = carregar_dados()

# 3. Interface Visual
st.title("🛡️ Radar Legislativo & Normativo")
st.subheader("Protótipo de Monitoramento - Apresentação Executiva")

st.markdown("---")

# 4. MOTOR DE BUSCA (A parte que tem que funcionar!)
st.write("### 🔎 Pesquisar na Base de 2.607 Itens")
# Criamos uma caixa de texto que aceita qualquer termo
busca = st.text_input("Digite o número (ex: 880) ou o órgão (ex: TJPA) e dê ENTER:")

if busca:
    # A MÁGICA: Convertemos tudo para string e buscamos o termo em qualquer parte do nome
    # case=False faz com que 'tjpa' encontre 'TJPA'
    mask = df['Nome'].str.contains(busca, case=False, na=False)
    resultado = df[mask]
    
    if not resultado.empty:
        st.success(f"✅ Encontramos {len(resultado)} norma(s) correspondente(s)!")
        
        # Estilização para o destaque amarelo
        def style_analisar(val):
            return 'background-color: #fff3cd; font-weight: bold' if val == 'Analisar' else ''
        
        st.dataframe(resultado.style.applymap(style_analisar, subset=['VisualPing']), use_container_width=True)
    else:
        st.error(f"❌ Nenhuma norma encontrada com o termo '{busca}'.")
        st.info("💡 Tente digitar apenas o número (ex: 880) ou o órgão (ex: CONAMA).")
else:
    # Se não houver busca, mostra a base completa de teste
    st.write("Abaixo, uma prévia da base monitorada:")
    st.dataframe(df, use_container_width=True)

# 5. Nota de Rodapé para a Gerente
st.markdown("---")
st.sidebar.markdown("### ⚙️ Painel de Controle")
st.sidebar.info("Busca por fragmentos habilitada.")
st.sidebar.warning("Próximo passo: Sincronização Automática API.")
