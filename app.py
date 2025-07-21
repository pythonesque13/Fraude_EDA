import streamlit as st
import pandas as pd
import plotly_express as px
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Analyse Exploratoire - Fraude Bancaire",
    page_icon=":bar_chart:",
    layout="centered",
)

@st.cache_data
def load_data():
    df = pd.read_csv("data/creditcard.csv")
    return df

data= load_data()

st.title("Analyse Exploratoire des Données de Fraude Bancaire")
st.markdown("""Ce tableau de bord présente une analyse exploratoire d'un jeu de données de transactions par carte de crédit.
L'objectif est de comprendre la structure des données, d'identifier les caractéristiques des transactions frauduleuses et de visualiser les relations clés avant toute modélisation.
""")

st.header("1. Aperçu du jeu de données")
if st.checkbox("Afficher un aprecu des donnees brutes"):
    st.dataframe(data.head(10))

st.write(f"Le jeu de donnees contient **{data.shape[0]}** transactions et **{data.shape[1]}** colonnes.")

st.header("2. Le desequilibre critique des classes")
class_counts = data['Class'].value_counts()
class_df=pd.DataFrame({
    'Classe': ['Normales (0)', 'Fraudes (1)'],
    'Nombre de transactions': class_counts.values
})

st.write('Distribution des transactions :')
st.dataframe(class_df)

fig_pie=px.pie(class_df, 
               values='Nombre de transactions', 
               names='Classe',
               title='Proportions des Transactions Normales vs. Fraudes',
               color='Classe',
                color_discrete_map={
                    'Normales (0)': 'royalblue',
                    'Fraudes (1)': 'crimson'
                })

st.plotly_chart(fig_pie, use_container_width=True)
st.warning(f"""**Observation Clé :** Le jeu de données est extrêmement déséquilibré. 
Seulement **{class_counts[1]} transactions ({class_counts[1]/data.shape[0]:.4%})** sont des fraudes.
Ceci est un point crucial pour la future modélisation.""")

st.header("3. Analyse de Montants et du Temps")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Distribution des Montants(Amount)")
    fig_amount=px.histogram(data, 
                            x='Amount', 
                            nbins=100,
                            title='Distribution des Montants des transactions',
                            labels={'Amount': 'Montant (€)'})
    
    fig_amount.update_layout(showlegend=False)
    st.plotly_chart(fig_amount,use_container_width= True)
    st.info("La plupart des transactions ont un montant relativement faible, avec quelques transactions de montants élevés. Cela peut indiquer des transactions normales et des fraudes potentielles.")

with col2:
    st.subheader("Distribution des Transactions dans le (Time)")
    data['Hour']=data['Time'].apply(lambda x: (x/3600) % 24)
    fig_time=px.histogram(data,
                           x='Hour',
                           nbins=24,
                           title='Distribution des Transactions sur 24h',
                           labels={'Hour': 'Heure de la journee'})
    fig_time.update_layout(showlegend=False)
    st.plotly_chart(fig_time, use_container_width=True)

    st.info("La plupart des transactions ont lieu pendant la journée, avec une légère augmentation en soirée. Les fraudes peuvent survenir à tout moment, mais il est intéressant de noter les pics d'activité.")


st.header("4. Exploration des variables et de leur relation avec la fraude")

v_features=[f'V{i}' for i in range(1, 29)]
selected_feature = st.selectbox(
    "Choisissez une variable V pour l'analyse",
     options= v_features,
     index=16
)

st.subheader(f"Distribution de {selected_feature} pour les transactions normales et frauduleuses")
fig_v = px.histogram(
    data, 
    x=selected_feature, 
    color='Class',
    color_discrete_map={0: 'royalblue', 1: 'crimson'},
    marginal="box",
    barmode='overlay',
    opacity=0.7,
    title=f"Distribution de {selected_feature} par classe"
)
st.plotly_chart(fig_v, use_container_width=True)

st.markdown("""
**Comment lire ce graphique ?**
- La distribution en **bleu** représente les transactions normales (Classe 0).
- La distribution en **rouge** représente les transactions frauduleuses (Classe 1).
- **Hypothèse :** Si les deux distributions sont très différentes, la variable est probablement un bon prédicteur de la fraude. Essayez avec `V17`, `V14`, `V10` (corrélations négatives) ou `V11`, `V4` (corrélations positives).
""")