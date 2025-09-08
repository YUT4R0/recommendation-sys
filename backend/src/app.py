import random
import streamlit as st
from .services.recommendation_service import RecomendationService
from .db.users import users


class App:
    def __init__(self):
        pass

    def run(self):
        st.title("Sistema de recomendação colaborativo de musica")

        username = st.text_input("Digite o nome do usuário: ")

        if st.button("Recomendar música"):
            if username in users:
                recommendation_system = RecomendationService()
                recommendations = recommendation_system.recommend(username, users)

                for rec in recommendations:
                    st.write(f"{rec[0]} - Pontuação: {rec[1]}")
            else:
                st.write("Usuario nao encontrado")
