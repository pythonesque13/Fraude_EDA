#  Analyse Exploratoire de Données : Détection de Fraude Bancaire

Ce projet consiste en une Analyse Exploratoire de Données (EDA) sur un jeu de données de transactions par carte de crédit. L'objectif est d'identifier des schémas et des caractéristiques propres aux transactions frauduleuses. Les résultats de cette analyse sont présentés via un tableau de bord interactif développé avec Streamlit.

**Lien vers l'application déployée :** [À venir après le déploiement]

---

## Objectifs du Projet

- **Comprendre la structure** des données et la distribution des variables.
- **Identifier le déséquilibre** majeur entre les transactions normales et frauduleuses.
- **Analyser les relations** entre les différentes variables et la classe de fraude.
- **Produire des visualisations claires et interactives** pour communiquer les résultats de l'analyse.
- **Mettre en place un projet de A à Z**, de la création du repo Git au déploiement d'une application web.

---

##  Technologies et Librairies

- **Langage :** Python 3.12+
- **Analyse de données :** Pandas, NumPy
- **Visualisation :** Matplotlib, Seaborn, Plotly Express
- **Application Web :** Streamlit
- **Environnement :** `.env` pour la gestion des dépendances
- **Versionning :** Git & GitHub

---

##  Installation et Lancement en Local

Suivez ces étapes pour lancer le projet sur votre machine.

### 1. Prérequis

- Avoir [Git](https://git-scm.com/) installé.
- Avoir [Python](https://www.python.org/downloads/) (version 3.9 ou supérieure) installé.

### 2. Cloner le Dépôt

Ouvrez un terminal et clonez ce dépôt :
```bash
git clone https://github.com/pythonesque13/Fraude_EDA.git
cd  Fraude_EDA
```

### 3. Télécharger les Données

- Le jeu de données n'est pas inclus dans ce dépôt en raison de sa taille.
- Téléchargez le dataset depuis Kaggle : [Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud).
- Créez un dossier data à la racine du projet.
- Placez le fichier creditcard.csv que vous venez de télécharger à l'intérieur de ce dossier data.

### 4. Créer l'Environnement Virtuel et Installer les Dépendances
- Créer un environnement virtuel
```bash
    python -m venv .env
```

-  Activer l'environnement
   -  Sur Windows :
   ```bash
        .env\Scripts\activate
   ```
   - Sur macOS/Linux :
   ```bash
        source .env/bin/activate
    ```

- Installer les librairies nécessaires
    ```bash
        pip install -r requirements.txt
    ```

### 5. Lancer l'Application Streamlit
Une fois les dépendances installées, lancez l'application :

```bash
    streamlit run app.py
```

L'application devrait s'ouvrir automatiquement dans votre navigateur à l'adresse http://localhost:8501.

--- 


### Principales Découvertes de l'Analyse

- **Déséquilibre Extrême** : Moins de 0.2% des transactions sont frauduleuses. C'est le défi principal pour toute tentative de modélisation future.

- **Cycle Journalier** : L'activité des transactions suit un cycle de 24 heures, avec une baisse notable durant la "nuit".

- **Distributions Révélatrices** : Plusieurs variables anonymisées (notamment V4, V11, V14, V17) montrent des distributions très différentes entre les transactions normales et frauduleuses, ce qui indique qu'elles sont de puissants indicateurs de fraude.