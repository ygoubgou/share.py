import streamlit as st
from formulaire import get_forms
import model_helper as models
import numpy as np
from dataclasses import asdict
from pathlib import Path

# Configuration de la page
st.set_page_config(
    page_title="Estimation du score de bien-être après veuvage",
    page_icon="💼",
    layout="wide"
)

with st.sidebar:
    st.image("graphiques/logo.png", width=300)  

st.title("PROJET M2 IDEE – Discrimination sur le marché du travail ")
st.warning("Professeur : CHRISTOPHE DANIEL")
with st.container():
    st.markdown("## Bienvenue dans l'application d'estimation du bien-être")

    st.markdown(
        """
        Cette application vous permet d’estimer le **score de bien-être d’un individu** 
        agé de plus de 50 ans **avant et après la survenue du veuvage**, en utilisant des modèles de machine learning.

        ---
        ### 🧭 Mode d'emploi :
        -  **Renseignez** les informations de l’individu via le formulaire à gauche.
        -  **Choisissez** un modèle prédictif *avant traitement* et un autre *après traitement*.
        -  **Comparez automatiquement** les deux scores estimés.
        -  **Visualisez** les résultats avec des graphiques interactifs.

        ---
        🔍 *L’objectif est d’évaluer l'impact du veuvage sur le bien-être subjectif estimé.*
        """
    )




# Récupération des données utilisateur une seule fois
user_input = get_forms()
mlinput = np.array([*asdict(user_input.convert_to_mlinput()).values()]).reshape(1, -1)

# Colonnes pour afficher les prédictions
col1, col2 = st.columns(2)

# Bloc AVANT traitement
with col1:
    st.info("💡 Estimation du score de bien-être AVANT traitement")
    
    MODEL_NAMES = {
        "Gradient Boosting": models.get_boosting_model_av,
        "KNN": models.get_knn_model_av,
    }

    selected_model_name = st.selectbox(
        "🔍 Choisissez un modèle", 
        ["--"] + list(MODEL_NAMES.keys()), 
        key="avant"
    )

    prediction_av = None
    if selected_model_name != "--":
        model = MODEL_NAMES[selected_model_name]()
        prediction_av = model.predict(mlinput)[0]
        st.success(
            f"✅ Modèle **{selected_model_name}** : **{prediction_av:,.0f} points**"
        )

# Bloc APRÈS traitement
with col2:
    st.info("💡 Estimation du score de bien-être APRÈS traitement")
    
    MODEL_NAMES_AP = {
        "Gradient Boosting": models.get_boosting_model_ap,
        "KNN": models.get_knn_model_ap,
    }

    selected_model_name_ap = st.selectbox(
        "🔍 Choisissez un modèle", 
        ["--"] + list(MODEL_NAMES_AP.keys()), 
        key="apres"
    )

    prediction_ap = None
    if selected_model_name_ap != "--":
        model = MODEL_NAMES_AP[selected_model_name_ap]()
        prediction_ap = model.predict(mlinput)[0]
        st.success(
            f"✅ Modèle **{selected_model_name_ap}** : **{prediction_ap:,.0f} points**"
        )

# Comparaison des prédictions
if prediction_av is not None and prediction_ap is not None:
    st.markdown("### 🔍 Comparaison des scores prédits")
    diff = prediction_ap - prediction_av
    st.info(f"📉 Différence (Après - Avant) : **{diff:+.0f} points**")

# Espace pour afficher les graphiques HTML interactifs
st.markdown("## 📈 Explorer les résultats visuellement")

col1, col2 = st.columns(2)

with col1:
    if st.button("🔍 Visualiser les appariements"):
        html_path = Path("graphiques/appariement.html")
        if html_path.exists():
            st.components.v1.html(html_path.read_text(encoding='utf-8'), height=600)
        else:
            st.warning("⚠️ Graphique non trouvé : `graphiques/appariement.html`")

with col2:
    if st.button("📊 Afficher la matrice de corrélation"):
        html_path = Path("graphiques/correlation_interactive.html")
        if html_path.exists():
            st.components.v1.html(html_path.read_text(encoding='utf-8'), height=600)
        else:
            st.warning("⚠️ Graphique non trouvé : `graphiques/correlation_interractive.html`")

# Footer
st.markdown("---")
st.caption("Développé dans le cadre du projet Discrimination et marché du travail · 2025")
