import streamlit as st

# CSS personalizado para fondo y ventana de login
st.markdown('''
    <style>
    body {
        background: linear-gradient(135deg, purple, black);
    }
    .login-window {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        width: 300px;
        margin: auto;
        margin-top: 100px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    }
    </style>
    ''', unsafe_allow_html=True)

# Ventana de autenticación
st.markdown("<div class='login-window'>", unsafe_allow_html=True)
st.header("Login")
user_id = st.text_input("User ID")
password = st.text_input("Password", type="password")
login_button = st.button("Login")

if login_button:
    st.write(f"Bienvenido {user_id}")
st.markdown("</div>", unsafe_allow_html=True)
