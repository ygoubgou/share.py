import streamlit as st
from formulaire import get_forms
import model_helper as models
import numpy as np
from dataclasses import asdict
from pathlib import Path

# Configuration de la page
st.set_page_config(
    page_title="Estimation du score de bien-être après veuvage",
    page_icon="💡",
    layout="wide"
)

st.title("PROJET M2 – Discrimination sur le marché du travail 💼")
st.markdown("## Estimation du score de bien-être à l’aide de modèles prédictifs")

# Choix du modèle
MODEL_NAMES = {
    "Gradient Boosting": models.get_boosting_model,
    "KNN": models.get_knn_model,
}

selected_model_name = st.selectbox("🔍 Choisissez un modèle de prédiction", ["--"] + list(MODEL_NAMES.keys()))
user_input = get_forms()

if selected_model_name != "--":
    model = MODEL_NAMES[selected_model_name]()
    mlinput = np.array([*asdict(user_input.convert_to_mlinput()).values()]).reshape(1, -1)
    prediction = model.predict(mlinput)

    st.success(
        f"✅ Le modèle **{selected_model_name}** prédit un score de bien-être de **{prediction[0]:,.0f} points**."
    )

    # Interprétation textuelle enrichie
    st.markdown("---")
st.subheader("Remarques")

st.markdown(
    """
    <div style='font-size:16px; line-height:1.6'>
    Le modèle de <b>voisins les plus proches</b> semble relativement <span style="color:red"><b>insensible à la variable de veuvage</b></span>.
    <br><br>
    En revanche, il est influencé par :
    <ul>
        <li>👵 <b>L'âge</b></li>
        <li>👶 <b>Le nombre d'enfants</b></li>
        <li>💪 <b>La force de préhension</b></li>
        <li>⚖️ <b>L'indice de masse corporelle (IMC)</b></li>
    </ul>
    Cela suggère que <b>d'autres facteurs personnels ou biologiques</b> sont plus déterminants dans le score de bien-être.
    </div>
    """,
    unsafe_allow_html=True
)

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
