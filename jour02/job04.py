import mysql.connector

laplateformeDB = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sqlroot",
    database = "laplateforme"
)

dbCursor = laplateformeDB.cursor()
dbCursor.execute("SELECT nom, capacite FROM salles")



def Main():
    laplateformeRoom = []

    for data in dbCursor:
        laplateformeRoom.append(data)

    print(laplateformeRoom)





if __name__ == "__main__":
    Main()