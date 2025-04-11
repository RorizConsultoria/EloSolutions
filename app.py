import streamlit as st
import pandas as pd
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Autenticação com Google Drive via Sheets
def authenticate_google_drive():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)
    return client

# Função para salvar dados no Google Sheets
def save_data_to_google_sheets(data):
    client = authenticate_google_drive()
    # Abre a planilha existente
    sheet = client.open('Cadastro de Clientes').sheet1
    # Adiciona uma nova linha
    sheet.append_row(data)

# Função para mostrar o dashboard
def display_dashboard():
    st.title('Cadastro de Clientes')
    
    with st.form(key='Cadastro'):
        # Campos de entrada
        nome_empresa = st.text_input('Nome da Empresa')
        nome_responsavel = st.text_input('Nome Responsável')
        telefone = st.text_input('Telefone')
        email = st.text_input('Email')
        tipo_base = st.selectbox('Tipo de Base', ['Base A', 'Base B', 'Base C'])
        usuario = st.text_input('Usuário')
        senha = st.text_input('Senha', type='password')
        data_aquisicao = st.date_input('Data de Aquisição', datetime.today())
        data_vencimento = st.date_input('Data de Vencimento', datetime.today())
        status_base = st.selectbox('Status da Base', ['Ativa', 'Expirada'])
        
        submit_button = st.form_submit_button('Cadastrar')

        if submit_button:
            # Dados do formulário
            data = [
                nome_empresa,
                nome_responsavel,
                telefone,
                email,
                tipo_base,
                usuario,
                senha,
                str(data_aquisicao),
                str(data_vencimento),
                status_base
            ]
            
            # Salva os dados no Google Sheets
            save_data_to_google_sheets(data)
            st.success('Cadastro realizado com sucesso!')

# Executa o app
if __name__ == '__main__':
    display_dashboard()
