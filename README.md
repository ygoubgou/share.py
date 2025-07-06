# 🧓 Évaluation de la Santé des Personnes Âgées – Application Streamlit

Une application interactive conçue avec **Streamlit** pour prédire et analyser l’état de santé de personnes âgées devenus veufs(ves) à partir de données cliniques, comportementales ou socio-économiques. 

---

## 🎯 Objectifs

- 🩺 Prédire l’état de santé global ou la probabilité de fragilité/dépendance chez les seniors.
- 📈 Comparer les performances de plusieurs modèles de machine learning.
- 🧠 Identifier les facteurs de risque les plus influents à l’aide de méthodes interprétables (SHAP, LIME).
- 👁️ Visualiser les tendances et profils à risque via des graphiques clairs et interactifs.

---

## 🔍 Fonctionnalités clés

### 🔬 Prédiction de l’état de santé
- Formulaire utilisateur pour saisir les données personnelles ou médicales (âge, IMC, pathologies, autonomie, isolement, etc.).
- Prédiction en temps réel avec un modèle ML entraîné.
- Retour visuel sur le niveau de risque ou de fragilité.

### 🧠 Modèles de machine learning
- Entraînement de plusieurs modèles : Random Forest, Logistic Regression, XGBoost, etc.
- Comparaison des métriques : Accuracy, ROC-AUC, F1-score, etc.
- Interprétabilité des résultats (SHAP values, importance des variables).

### 📊 Visualisation des données
- Graphiques interactifs pour explorer la population étudiée.
- Analyse de corrélations, distribution des variables, profils types.
- Cartes ou histogrammes selon les régions, âges, sexes, etc.

---

## 🧰 Technologies utilisées

- **Framework** : [Streamlit](https://streamlit.io/)
- **Machine Learning** : scikit-learn, XGBoost, LightGBM
- **Interprétabilité** : SHAP, LIME
- **Visualisation** : seaborn, Plotly, matplotlib
- **Traitement des données** : pandas, numpy
- **Sérialisation** : joblib / pickle

---

## 🚀 Lancer l’application

```bash
git clone https://github.com/ton-pseudo/senior-health-predictor.git
cd senior-health-predictor
pip install -r requirements.txt
streamlit run app.py
