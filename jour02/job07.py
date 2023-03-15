import mysql.connector
import random

laplateformeServer = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sqlroot"
)

dbCursor = laplateformeServer.cursor()
dbCursor.execute("CREATE DATABASE job07")
dbCursor.close()


job07DB = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sqlroot",
    database = "job07"
)

dbCursor = job07DB.cursor()



def Main():
    dbCursor.execute("CREATE TABLE employes (\
                                            id int NOT NULL AUTO_INCREMENT,\
                                            nom varchar(255),\
                                            prenom varchar(255),\
                                            salaire decimal,\
                                            id_service int,\
                                            PRIMARY KEY (id)\
                                            );")
    

    names = ["Man", "Man", "Bro", "Girl"]
    firstNames = ["Chad", "Rizz", "Gym", "E"]
    
    for i in range(4):
        dbCursor.execute(f"INSERT INTO employes (\
                                                nom,\
                                                prenom,\
                                                salaire,\
                                                id_service,\
                                                )\
                                         VALUES (\
                                                {firstNames[i]},\
                                                {names[i]},\
                                                {random.uniform(2900.00, 3200.00)},\
                                                {random.randint(0, 50)},\
                                                );")


    dbCursor.execute("SELECT * FROM employes WHERE salaire > 3000.00")

    for data in dbCursor:
        print(data)


    dbCursor.execute("CREATE TABLE services (\
                                            id int NOT NULL AUTO_INCREMENT,\
                                            nom varchar(255),\
                                            PRIMARY KEY (id)\
                                            );")
    
    services = ["Wins And Leaves", "RizzMove", "Gym Training", "UwU"]
    
    for i in range(4):
        dbCursor.execute(f"INSERT INTO services (\
                                                nom,\
                                                )\
                                         VALUES (\
                                                {services[i]},\
                                                );")
        

    dbCursor.execute("SELECT * FROM employes, services")

    for data in dbCursor:
        print(data)

    dbCursor.close()



class CRUD:
    def __init__(self, cursor, table):
        self.__cursor = cursor

        self.__currentTable = table
        self.__tableColumns = self.__tableDesc.column_names



    '''Public methods'''

    #To me, there isn't any C operations to do on a table
    '''def C_Operations(self, op:str):
        return None'''
    


    def R_Operations(self, columnToRead:str):
        self.__cursor.execute(f"SELECT {columnToRead} FROM {self.__currentTable}")
    


    def U_Operations(self, op:str, valueUpdate, columnToUpdate, columnComparison=None, columnCompValue=None):
        try:
            if isinstance(str, columnToUpdate) and columnToUpdate.lower() in self.__tableColumns:
                columnUpdate = columnToUpdate.lower()

            elif isinstance(int, columnToUpdate) and 0 <= columnToUpdate <= len(self.__tableColumns):
                columnUpdate = self.__tableColumns[columnToUpdate]
        except:
            exit("Specified column name or index are not in this table")


        if op == "INSERT":
            self.__cursor.execute(f"INSERT INTO {self.__currentTable} (\
                                                                {columnUpdate},\
                                                                )\
                                                        VALUES (\
                                                                {valueUpdate},\
                                                                );")
            
        elif op == "UPDATE":
            try:
                if isinstance(str, columnComparison) and columnComparison.lower() in self.__tableColumns:
                    columnComp = columnComparison.lower()

                elif isinstance(int, columnComparison) and 0 <= columnComparison <= len(self.__tableColumns):
                    columnComp = self.__tableColumns[columnComparison]
            except:
                exit("Column to compare hasn't been given or is not in this table")

            self.__cursor.execute(f"UPDATE {self.__currentTable}\
                                       SET {columnToUpdate} = {valueUpdate}\
                                     WHERE {columnComp} = {columnCompValue}")



    def D_Operations(self, op:str, columnName:str, dataToDELETE:str):
        self.__cursor.execute(f"DELETE FROM {self.__currentTable}\
                                 WHERE {columnName} = {dataToDELETE};")
    

    #Getters/Setters

    def GetTable(self):
        return self.__currentTable





if __name__ == "__main__":
    Main()