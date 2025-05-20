import streamlit as st
import pandas as pd
from datetime import datetime
import os
import sys

# Configuração da página
st.set_page_config(
    page_title="JGR Broker - Acompanhamento de Processos",
    page_icon="🚢",
    layout="wide",
)

# Verificação de login usando secrets
def verificar_login(username, password):
    """Verifica se as credenciais estão corretas"""
    try:
        # Verificar no sistema de secrets do Streamlit
        if "credenciais" in st.secrets:
            if username in st.secrets["credenciais"]:
                if password == st.secrets["credenciais"][username]:
                    return True
        return False
    except Exception as e:
        st.error(f"Erro ao verificar login: {e}")
        # Em desenvolvimento, permitir acesso com credenciais padrão
        if username == "admin" and password == "admin123":
            st.warning("Usando credenciais de desenvolvimento. Configure secrets em produção.")
            return True
        return False

# Inicialização do estado de autenticação
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False
if 'usuario' not in st.session_state:
    st.session_state.usuario = None
if 'perfil' not in st.session_state:
    st.session_state.perfil = None

# Função para determinar o perfil com base no nome de usuário
def determinar_perfil(username):
    """Determina o perfil do usuário com base no nome"""
    if username in ["admin", "gerente"]:
        return "administrador"
    return "cliente"

# Lógica de autenticação
if not st.session_state.autenticado:
    # Layout da página de login
    col1, col2 = st.columns([1, 1])
    
    with col1:
        try:
            st.image("assets/images/jgr_logo.png", width=200)
        except:
            st.write("**JGR BROKER**")
    
    with col2:
        st.subheader("Login do Sistema")
        
        with st.form("formulario_login"):
            username = st.text_input("Usuário")
            password = st.text_input("Senha", type="password")
            login_btn = st.form_submit_button("Entrar", use_container_width=True)
            
            if login_btn:
                if verificar_login(username, password):
                    st.session_state.autenticado = True
                    st.session_state.usuario = username
                    st.session_state.perfil = determinar_perfil(username)
                    st.success(f"Bem-vindo, {username}!")
                    st.rerun()
                else:
                    st.error("Usuário ou senha incorretos")

else:
    # Interface principal após o login
    
    # Cabeçalho com logo e informações do usuário
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col1:
        try:
            st.image("assets/images/jgr_logo.png", width=150)
        except:
            st.write("**JGR BROKER**")
    
    with col2:
        st.title("Sistema de Acompanhamento de Processos")
        st.caption("JGR BROKER - Monitoramento e gestão de processos de importação e exportação")
    
    with col3:
        st.write(f"Olá, **{st.session_state.usuario}**")
        st.caption(f"Perfil: {st.session_state.perfil.capitalize()}")
        
        if st.button("🚪 Sair", use_container_width=True):
            st.session_state.autenticado = False
            st.session_state.usuario = None
            st.session_state.perfil = None
            st.rerun()
    
    # Barra de navegação
    if st.session_state.perfil == "administrador":
        cols = st.columns(7)
        with cols[0]:
            st.button("📋 Painel", use_container_width=True)
        with cols[1]:
            st.button("➕ Novo Processo", use_container_width=True)
        with cols[2]:
            st.button("📦 Arquivados", use_container_width=True)
        with cols[3]:
            st.button("🔗 Compartilhar", use_container_width=True)
        with cols[4]:
            st.button("📊 Importar Planilha", use_container_width=True)
        with cols[5]:
            st.button("⚙️ Configurações", use_container_width=True)
        with cols[6]:
            st.button("👥 Usuários", use_container_width=True)
    else:
        # Menu simplificado para clientes
        st.button("📋 Painel", use_container_width=True)
    
    st.divider()
    
    # Conteúdo principal
    st.header("Painel de Processos")
    
    # Conteúdo de exemplo para demonstração
    st.info("Sistema configurado com autenticação via Streamlit Secrets.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Informações de Acesso")
        st.write(f"**Usuário:** {st.session_state.usuario}")
        st.write(f"**Perfil:** {st.session_state.perfil.capitalize()}")
        st.write(f"**Login realizado em:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    
    with col2:
        st.subheader("Configuração de Secrets")
        st.code("""
# .streamlit/secrets.toml
[credenciais]
admin = "admin123"
gerente = "gerente456"
cliente = "cliente789"
        """)
    
    st.subheader("Como implementar no sistema atual")
    st.write("""
    Para implementar esta funcionalidade no sistema existente:
    
    1. Adicione o arquivo `.streamlit/secrets.toml` com as credenciais
    2. Substitua o sistema de login atual pelo sistema de secrets
    3. Configure os segredos na plataforma Streamlit Cloud quando fizer o deploy
    
    No Streamlit Cloud, você pode configurar os segredos através do painel administrativo
    do seu aplicativo, na seção "Secrets".
    """)
    
    # Rodapé
    st.divider()
    ano_atual = datetime.now().year
    st.caption(f"© {ano_atual} JGR BROKER - Todos os direitos reservados")