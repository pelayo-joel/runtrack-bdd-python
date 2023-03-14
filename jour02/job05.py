import mysql.connector

laplateformeDB = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sqlroot",
    database = "laplateforme"
)

dbCursor = laplateformeDB.cursor()
dbCursor.execute("SELECT superficie FROM etage")



def Main():
    laplateformeSuperficie = 0

    for data in dbCursor:
        laplateformeSuperficie += data[0]

    print(f"La superficie de La Plateforme est de {laplateformeSuperficie}m2")





if __name__ == "__main__":
    Main()