import mysql.connector
import random

laplateformeServer = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sqlroot"
)

dbCursor = laplateformeServer.cursor()
dbCursor.execute("CREATE DATABASE zoo")
dbCursor.close()


zoo = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sqlroot",
    database = "zoo"
)

dbCursor = zoo.cursor()
dbCursor.execute("CREATE TABLE animal (\
                                      id int NOT NULL AUTO_INCREMENT,\
                                      nom varchar(255),\
                                      race varchar(255),\
                                      id_cage int,\
                                      birthdate datetime,\
                                      origin_country varchar(255),\
                                      PRIMARY KEY (id)\
                                      );")

dbCursor.execute("CREATE TABLE cage (\
                                    id int NOT NULL AUTO_INCREMENT,\
                                    n_animals int,\
                                    superficie int,\
                                    PRIMARY KEY (id)\
                                    );")





def InputCommand(message:str, nCommand:int):
    try:
        command = int(input(message))
        if isinstance(command, int):
            return command

    except KeyboardInterrupt:
        exit("\nExit program")

    except:
        print(f"Input must be an integer between 1 and {nCommand}")
        InputCommand()





class CRUD:
    def __init__(self, cursor, table):
        self.__cursor = cursor

        self.__currentTable = table
        self.__tableDesc = cursor.description
        self.__tableColumns = self.__tableDesc.column_names



    '''Public methods'''

    #To me, there isn't any C operations to do on a table
    '''def C_Operations(self, op:str):
        return None'''
    


    def R_Operations(self, columnToRead:str="*"):
        self.__cursor.execute(f"SELECT {columnToRead} FROM {self.__currentTable}")
        for data in self.__cursor:
            print(data)
    


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
    
    def GetTableColumns(self):
        return self.__tableColumns





def Main():
    command = InputCommand("Choose a command (1- Add, 2- Delete, 3- Update, 4- Display, 5- Area): ")

    if command == 4:
        dbCursor.execute(f"SELECT * FROM animal")
        dbCursor.execute(f"SELECT * FROM cage")
        return
    
    if command == 5:
        dbCursor.execute(f"SELECT * FROM cage")
        area = 0

        for data in dbCursor:
            area += data[2]

        print(f"Total area of all cages: {area}m2")
        return


    table = InputCommand("Animal or cage table ? (1- animal, 2- cage): ")

    if table == 1:
        dbCursor.execute(f"SELECT * FROM animal")
        opOnTable = CRUD(zoo.cursor(), dbCursor)
        
    elif table == 2:
        dbCursor.execute(f"SELECT * FROM cage")
        opOnTable = CRUD(zoo.cursor(), dbCursor)


    if command == 1:
        column = input(f"Which column (you can use index) ? {opOnTable.GetTableColumns()}: ")
        newValue = input("Input the new value")
        opOnTable.U_Operations("INSERT", newValue, column)
        opOnTable.R_Operations()

    elif command == 2:
        column = input(f"Which column (you can use index) ? {opOnTable.GetTableColumns()}: ")
        deleteValue = input("Input the new value")
        opOnTable.D_Operations(column, deleteValue)

    elif command == 3:
        column = input(f"Which column (you can use index) ? {opOnTable.GetTableColumns()}: ")
        newValue = input("Input the new value")
        opOnTable.U_Operations("UPDATE", newValue, column)
        opOnTable.R_Operations()











if __name__ == "__main__":
    while True:
        Main()