import streamlit as st 
import pandas as pd
from datetime import datetime


st.set_page_config(page_title="Matriz de Eisenhower", layout="wide")
st.title("⏱️ Gerenciador de Tarefas - Matriz de Eisenhower")
st.markdown("Organize suas tarefas automaticamente por urgência e importância.")

if "tarefas" not in st.session_state:
    st.session_state.tarefas = pd.DataFrame(columns=["Tarefa", "Prazo", "Urgência", "Importância", "Quadrante"])

st.sidebar.header("➕ Adicionar Tarefa")

tarefa = st.sidebar.text_input("Descrição da tarefa")
prazo = st.sidebar.date_input("Prazo Final")
urgencia = st.sidebar.slider("Urgência (1 = baixa, 5 = alta)", 1, 5, 3)
importancia = st.sidebar.slider("Importância (1 = baixa, 5 = alta)", 1, 5, 3)

if st.sidebar.button("Adicionar"):
    if not tarefa:
        st.sidebar.error("Digite uma descrição para a tarefa")
    else:
        if urgencia >= 3 and importancia >= 3:
            quadrante = "Fazer agora"
        elif urgencia >= 3 and importancia < 3:
            quadrante = "Delegar"
        elif urgencia < 3 and importancia >= 3:
            quadrante = "Planejar"
        elif urgencia < 3 and importancia < 3:
            quadrante = "Eliminar"

    nova_tarefa = pd.DataFrame([{
        "Tarefa":tarefa,
        "Prazo":prazo,
        "Urgência":urgencia,
        "Importância":importancia,
        "Quadrante":quadrante
    }])

    st.session_state.tarefas = pd.concat([st.session_state.tarefas, nova_tarefa], ignore_index=True)
    st.sidebar.success("Terefa adcionada com sucesso")

if st.session_state.tarefas.empty:
    st.info("Adcione sua tarefa antes de começar!")
else:
    st.subheader("📆 Tarefas Registradas")
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    fazer_agora = st.session_state.tarefas.query("Quadrante == 'Fazer agora'")
    delegar = st.session_state.tarefas.query("Quadrante == 'Delegar'")
    planejar = st.session_state.tarefas.query("Quadrante == 'Planejar'")
    eliminar = st.session_state.tarefas.query("Quadrante == 'Eliminar'")

    def bloco_colorido(titulo, df, cor):
        if df.empty:
            tabela_html = "<p><i>Nenhuma tarefa.</i></p>"
        else:
            tabela_html = df.to_html(index=False).replace(
                "<table", f"<table style='width:100%; border-collapse: collapse;'"
            )

        st.markdown(
            f"""
            <div style="
                background-color:{cor};
                padding:20px;
                border-radius:15px;
                margin-bottom:20px;
            ">
                <h3 style="margin-top:0; color:black;">{titulo}</h3>
                {tabela_html}
            </div>
            """,
            unsafe_allow_html=True
        )



    with col1:
        bloco_colorido("Fazer agora", fazer_agora, "#ffb3b3")  
        
    with col2:
        bloco_colorido("Delegar", delegar, "#ffe8a3")  
        
    with col3:
        bloco_colorido("Planejar", planejar, "#bff5bf")  
        
    with col4:
        bloco_colorido("Eliminar", eliminar, "#e6e6e6")  
        

if not st.session_state.tarefas.empty:
    st.download_button(
        label="Baixar tarefa em CSV",
        data=st.session_state.tarefas.to_csv(index=False).encode("utf-8"),
        file_name="matriz_eisenhower.csv",
        mime="text/csv"
    )
