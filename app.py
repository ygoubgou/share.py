import streamlit as st
from formulaire import get_forms
import model_helper as models
import numpy as np
from dataclasses import asdict
from pathlib import Path

# Configuration de la page
st.set_page_config(
    page_title="Estimation du bien-être après veuvage",
    page_icon="💼",
    layout="wide"
)

# === SIDEBAR ===
with st.sidebar:
    st.image("graphiques/logo.png", width=250)
    st.markdown("""
        ## Paramètres
        Renseignez les informations dans le formulaire
        puis sélectionnez les modèles pour l'estimation.
    """)

# === TITRE PRINCIPAL ===
st.markdown("""
    <h1 style='text-align: center; color: #0B5345;'>
        🧠 Estimation du bien-être après veuvage
    </h1>
    <h4 style='text-align: center; color: #1F618D;'>
        Projet M2 IDEE · Discrimination sur le marché du travail
    </h4>
""", unsafe_allow_html=True)

st.info("Professeur référent : CHRISTOPHE DANIEL")

with st.expander("ℹ️ À propos de l'application", expanded=True):
    st.markdown("""
    Cette application estime le **score de bien-être subjectif** d’un individu de plus de 50 ans **avant et après un veuvage**.

    ### Mode d'emploi :
    - Renseignez les caractéristiques de l’individu à gauche.
    - Sélectionnez deux modèles (avant et après).
    - Comparez les résultats et visualisez les impacts.
    """)

# === FORMULAIRE UTILISATEUR ===
user_input = get_forms()
mlinput = np.array([*asdict(user_input.convert_to_mlinput()).values()]).reshape(1, -1)

# === PRÉDICTIONS ===
st.markdown("## 🔮 Estimations du score de bien-être")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Avant traitement")
    model_name_av = st.selectbox("Choisissez un modèle (avant)", ["--", "Gradient Boosting", "KNN"], key="avant")
    prediction_av = None
    if model_name_av != "--":
        model = models.get_boosting_model_av() if model_name_av == "Gradient Boosting" else models.get_knn_model_av()
        prediction_av = model.predict(mlinput)[0]
        st.metric("Score prédit AVANT", f"{prediction_av:.0f} points")

with col2:
    st.subheader("Après traitement")
    model_name_ap = st.selectbox("Choisissez un modèle (après)", ["--", "Gradient Boosting", "KNN"], key="apres")
    prediction_ap = None
    if model_name_ap != "--":
        model = models.get_boosting_model_ap() if model_name_ap == "Gradient Boosting" else models.get_knn_model_ap()
        prediction_ap = model.predict(mlinput)[0]
        st.metric("Score prédit APRÈS", f"{prediction_ap:.0f} points")

# === COMPARAISON ===
if prediction_av is not None and prediction_ap is not None:
    diff = prediction_ap - prediction_av
    st.markdown("### ⚖️ Comparaison des scores")
    delta_color = "normal" if diff == 0 else "inverse" if diff < 0 else "off"
    st.metric("Différence (Après - Avant)", f"{diff:+.0f} points", delta_color=delta_color)

# === GRAPHIQUES INTERACTIFS ===
st.markdown("## 📊 Visualisation interactive")
vis1, vis2 = st.columns(2)

with vis1:
    if st.button("Afficher les appariements", use_container_width=True):
        html_path = Path("graphiques/appariement.html")
        if html_path.exists():
            st.components.v1.html(html_path.read_text(encoding='utf-8'), height=600)
        else:
            st.error("Fichier 'appariement.html' non trouvé")

with vis2:
    if st.button("Afficher la corrélation", use_container_width=True):
        html_path = Path("graphiques/correlation_interactive.html")
        if html_path.exists():
            st.components.v1.html(html_path.read_text(encoding='utf-8'), height=600)
        else:
            st.error("Fichier 'correlation_interactive.html' non trouvé")

# === FOOTER ===
st.markdown("""
    ---
    <div style='text-align: center;'>
        <small>Développé dans le cadre du projet M2 IDEE · 2025</small>
    </div>
""", unsafe_allow_html=True)
