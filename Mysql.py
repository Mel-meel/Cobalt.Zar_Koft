from mysql import connector

class Mysql :

    # Constructeur de la classe
    def __init__(self, configs) :
        try :
            with connector.connect(
                host = configs[0],
                user = configs[1],
                password = configs[2]
            ) as connexion :
                self.connexion = connexion
        except connector.Error as e :
            print(e)
