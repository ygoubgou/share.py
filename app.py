import streamlit as st
from formulaire import get_forms
import model_helper as models
import numpy as np
from dataclasses import asdict
import polars as pl
import plotly.express as px
from pathlib import Path

# Configuration
st.set_page_config(page_title="Estimation du score de bien être après veuvage", page_icon="💡", layout="wide")
st.header("PROJET M2 IDEE DISCRIMINATION SUR LE MARCHE DU TRAVAIL")


# Choix du modèle
MODEL_NAMES = {
    #"Régression linéaire": models.get_linear_model,
    "Gradient Boosting": models.get_boosting_model,
    "KNN": models.get_knn_model,
}

selected_model_name = st.selectbox(" Choisissez un modèle de prédiction", ["--"] + list(MODEL_NAMES.keys()))
user_input = get_forms()

if selected_model_name != "--":
    model = MODEL_NAMES[selected_model_name]()
    mlinput = np.array([*asdict(user_input.convert_to_mlinput()).values()]).reshape(1, -1)
    prediction = model.predict(mlinput)
    st.success(f"✅ Le modèle **{selected_model_name}** prédit un score de bien être de **{prediction[0]:,.0f} points**.")



st.markdown("Notre modèle de voisin le plus proche est insensible à notre variable qui mésure le veuvage," \
"il l'est plutôt par rapport à l'âge, au nombre d'enfant, à la force de préhension, à l'indice de masse corporelle.")