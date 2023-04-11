import sqlite3 

con = sqlite3.connect("bdd.db")
curseur = con.cursor()

"""
https://sql.sh/
"""

curseur.execute("""
                CREATE TABLE IF NOT EXISTS objet_trouve (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date DATETIME NOT NULL,
                    nature_objet TEXT NOT NULL,
                    type_objet TEXT NOT NULL,
                    id_gare TEXT NOT NULL,
                    FOREIGN KEY (id_gare) REFERENCES gare(id)
)
""")
con.commit()

curseur.execute("""
                CREATE TABLE IF NOT EXISTS gare (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom_gare TEXT NOT NULL
                    
)
""")
con.commit()


con.close()
