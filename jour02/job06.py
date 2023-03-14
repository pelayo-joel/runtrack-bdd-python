import mysql.connector

laplateformeDB = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sqlroot",
    database = "laplateforme"
)

dbCursor = laplateformeDB.cursor()
dbCursor.execute("SELECT capacite FROM salles")



def Main():
    laplateformeSuperficie = 0

    for data in dbCursor:
        laplateformeSuperficie += data[0]

    print(f"La capacite de toutes les salles de La Plateforme est de: {laplateformeSuperficie}")





if __name__ == "__main__":
    Main()