import mysql.connector

class DataBase:
    def connect(self):
        connection = mysql.connector.connect(host="localhost", user="root", password="@umesh2005", database="project3")
        # connection = mysql.connector.connect(host="localhost", user="pythonuser", password="Python@1234", database="project3")

        return connection

    