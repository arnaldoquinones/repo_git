import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Página con Fondo Negro", page_icon="🖤")

# Estilo del fondo
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: black;
        color: white;
    }
    .sidebar .sidebar-content {
        background-color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título y contenido
st.title("Bienvenido a mi Página")
st.write("Esta es una página de ejemplo con fondo negro.")

# Agregar un formulario de autenticación simple
user_id = st.text_input("User ID")
password = st.text_input("Password", type='password')
if st.button("Login"):
    if user_id and password:
        st.success("¡Has iniciado sesión exitosamente!")
    else:
        st.error("Por favor, ingresa tu User ID y Password.")
