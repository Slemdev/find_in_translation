import pandas as pd

# Charger le fichier CSV
df = pd.read_csv('objets-trouves-restitution.csv', delimiter=';')

# Renommer les colonnes
df = df.rename(columns=lambda x: x.strip().lower().replace(' ', '_').replace("'",""))

# Enregistrer le fichier CSV avec les nouvelles colonnes uniformisées
df.to_csv('objets-trouves-restitution2.csv', index=True)