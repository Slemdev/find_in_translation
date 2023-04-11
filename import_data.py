import pandas as pd
import sqlite3


df = pd.read_csv('objets-trouves-restitution2.csv',delimiter=';')

conn = sqlite3.connect('bdd.db')

df.to_sql('base', conn, if_exists='append', index=False)

conn.close()
