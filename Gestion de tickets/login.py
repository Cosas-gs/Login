import streamlit as st
import requests
from PIL import Image

def main():
    # Configuración de la página
    logo = Image.open("Global.png")
    st.set_page_config(page_title="Inicio de sesión", page_icon=logo)

    # Estilo oscuro
    dark_theme = """
        <style>
        .reportview-container {
            background: #1a1a1a;
            color: white;
        }
        </style>
    """
    st.markdown(dark_theme, unsafe_allow_html=True)

    # Título
    st.title("Inicio de sesión")
    image_path = "C:/Users/gener/OneDrive/Escritorio/Gestion de tickets/Global.jpg"  # Ruta de la imagen

    # Icono en el centro
    st.markdown(
        """
        <div style="display: flex; justify-content: center; align-items: center; margin-top: 2rem;">
            <img src='{}' width='400'>
        </div>
        """.format(image_path),
        unsafe_allow_html=True
    )

    # Formulario de inicio de sesión
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    login_button = st.button("Iniciar sesión")

    # Lógica de inicio de sesión
    if login_button:
        if username == "admin" and password == "password":
            st.success("Inicio de sesión exitoso")
        else:
            st.error("Credenciales incorrectas")

if __name__ == "__main__":
    main()