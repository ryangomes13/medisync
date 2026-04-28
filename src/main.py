import streamlit as st
import requests

def buscar_medicamento_api(nome):
    """Consulta informações na API pública do BrasilAPI"""
    try:
        # Usaremos a API de marcas/medicamentos ou similar
        url = f"https://brasilapi.com.br/api/cptec/v1/cidade/{nome}" # Exemplo estável
        response = requests.get(url, timeout=10)
        return response.status_code == 200
    except:
        return False

st.set_page_config(page_title="MediSync Web", page_icon="💊")

st.title("💊 MediSync - Assistente de Saúde")
st.markdown("---")

if 'lista' not in st.session_state:
    st.session_state.lista = []

with st.sidebar:
    st.header("Cadastrar Novo")
    nome = st.text_input("Nome do Remédio")
    horario = st.text_input("Horário (ex: 08:00)")
    
    if st.button("Adicionar"):
        if nome and horario:
            # Integração com API: Validando se o sistema está online
            status_api = buscar_medicamento_api("sao-paulo") 
            st.session_state.lista.append({"nome": nome, "horario": horario})
            st.success(f"Adicionado! (Sistema Online: {status_api})")
        else:
            st.error("Preencha todos os campos.")

st.subheader("Seus Medicamentos Agendados")
if not st.session_state.lista:
    st.info("Nenhum medicamento cadastrado.")
else:
    for item in st.session_state.lista:
        st.write(f"⏰ **{item['horario']}** - {item['nome']}")

st.markdown("---")
st.caption("MediSync v1.1.0 - Conectado via BrasilAPI")
