import streamlit as st
from objets import UserInput

def get_forms() -> UserInput:
    with st.sidebar:
        st.header("🧍 Informations personnelles")
        female = st.selectbox("Sexe", ["--", "Homme", "Femme"])
        female = 1 if female == "Femme" else 0

        age = st.number_input("Âge", min_value=50.0, max_value=100.0)
        age_2 = age ** 2

        iv009_mod = str(st.selectbox("Lieu de résidence", [
            "--",
            "1. A big city",
            "2. The suburbs or outskirts of a big city",
            "3. A large town",
            "4. A small town",
            "5. A rural area or village"
        ]))

        eduyears_mod = st.number_input("Années d'éducation", min_value=0.0, max_value=30.0)
        eduyears_mod_2 = eduyears_mod ** 2

        hhsize = st.number_input("Taille du ménage", min_value=1, max_value=10)
        hhsize_2 = hhsize ** 2

        ch001_ = st.number_input("Nombre d'enfants dans le ménage", min_value=0, max_value=10)
        ch001_2 = ch001_ ** 2

        sp002_mod = int(st.selectbox("Recevez-vous une aide régulière ?", [0, 1]))

        st.header("🩺 Santé et bien-être")
        sphus = str(st.selectbox(
            "État de santé",
            ["--", "1. Poor", "2. Fair", "3. Good", "4. Very good", "5. Excellent"]
        ))

        chronic_mod = st.number_input("Nombre de maladies chroniques", min_value=0, max_value=15)
        eurod = st.slider("Score Euro-D (niveau de dépression)", min_value=0.0, max_value=12.0)

        hc002_mod = st.number_input("Consultations médicales annuelles", min_value=0.0, max_value=100.0)
        hc002_mod_2 = hc002_mod ** 2

        hc012_ = st.selectbox("Limité dans les activités quotidiennes ?", [0, 1, 2, 3, 4])
        maxgrip = st.number_input("Force de préhension maximale (kg)", min_value=0, max_value=100)

        bmi = st.number_input("IMC (Indice de Masse Corporelle)", min_value=10.0, max_value=50.0)
        bmi_2 = bmi ** 2

        mobilityind = st.selectbox("Indice de mobilité", [0, 1, 2, 3, 4])
        smoking = int(st.radio("Fumeur ?", ["Non", "Oui"]) == "Oui")

        st.header("💰 Situation professionnelle et financière")
        ep005_ = str(st.selectbox("Statut professionnel", [
            "--",
            "1. retired",
            "3. unemployed",
            "4. permanently sick or disabled",
            "5. homemaker",
            "97. other"
        ]))

        thinc_m = st.number_input("Revenu net annuel (€)", min_value=0.0, max_value=1_000_000.0)
        thinc_m_2 = thinc_m ** 2

        changement_statut = int(st.selectbox("A-t-il/elle perdu son conjoint ?", [0, 1]))

        return UserInput(
            female, age, age_2,
            iv009_mod,
            eduyears_mod, eduyears_mod_2,
            hhsize, hhsize_2,
            ch001_, ch001_2,
            sphus,
            chronic_mod,
            bmi, bmi_2,
            thinc_m, thinc_m_2,
            hc002_mod, hc002_mod_2,
            hc012_, mobilityind, maxgrip, smoking,
            ep005_,
            eurod,
            sp002_mod,
            changement_statut,
          
        )
