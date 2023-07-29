import mysql.connector

class Mysql :

    # Constructeur de la classe
    def __init__(self, configs) :
        self.url = url
        self.soup = ""
        mydb = mysql.connector.connect(
            host=configs[0],
            user=configs[1],
            password=configs[2]
        )
