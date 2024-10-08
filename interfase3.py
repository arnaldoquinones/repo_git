# Importo librerias.
import streamlit as st

# Configuración de la página (este debe estar antes de cualquier otro comando de Streamlit).
st.set_page_config(
    page_title="Fondo Púrpura y Negro",
    page_icon="🌟",
    layout="wide",
)

def main():
    # Estilos CSS para el fondo degradado.
    st.markdown(
        """
        <style>
        body {
            background: linear-gradient(to bottom, #4e008e, #000000);
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Contenido de la página.
    st.title("Página con Fondo Púrpura y Negro")
    st.write("¡Bienvenido! Esta es una página con un fondo degradado en tonos púrpura y negro.")
    st.write("¡Espero que te guste!")
    st.sidebar.title("Navegacion")

    # Creo menu lateral.

pagina = st.sidebar.selectbox("", ["Pagina principal","Visualizacion de datos","Graficos"]) 

    # Agregar un formulario de autenticación simple.
user_id = st.text_input("User ID")
password = st.text_input("Password", type='password')
if st.button("Login"):
        if user_id and password:
            st.success("¡Has iniciado sesión exitosamente!")
        else:
            st.error("Por favor, ingresa tu User ID y Password.")

if __name__ == "__main__":
        main()
# INICIO