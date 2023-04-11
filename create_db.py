import sqlite3 

con = sqlite3.connect("bdd.db")
curseur = con.cursor()

"""
https://sql.sh/
"""

curseur.execute("""
                CREATE TABLE IF NOT EXISTS base (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    code_uic INTEGER,
                    date DATETIME NOT NULL,
                    date_et_heure_de_restitution DATETIME,
                    nature_dobjets TEXT,
                    type_dobjets TEXT,
                    type_denregistrement TEXT,
                    gare TEXT NOT NULL,
                    FOREIGN KEY (gare) REFERENCES gare(id)
)
""")
con.commit()



curseur.execute("""
                CREATE TABLE IF NOT EXISTS gare (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom_gare TEXT
                    
)
""")
con.commit()


con.close()
