import pandas as pd
import sqlite3


df = pd.read_csv('objets-trouves-restitution.csv')

conn = sqlite3.connect('bdd.db')

df.to_sql('objet_trouve', conn, if_exists='append', index=False)

conn.close()
