from mysql import connector

class Mysql:
    
    # Constructeur de la classe
    def __init__(self, configs):
        try:
            # Connexion persistante
            self.connexion = connector.connect(
                host=configs[0],
                user=configs[1],
                password=configs[2],
                database=configs[3]
            )
            self.create_table()  # Création de la table si elle n'existe pas
        except connector.Error as e:
            print(f"Erreur de connexion : {e}")
    
    def create_table(self):
        """Vérifie et crée la table si elle n'existe pas."""
        try:
            cursor = self.connexion.cursor()
            # Création de la table pour stocker les prix de l'or
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS gold_prices (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255),
                    current_price_dol DECIMAL(10, 2),
                    current_price_eur DECIMAL(10, 2),
                    opening_price_dol DECIMAL(10, 2),
                    opening_price_eur DECIMAL(10, 2),
                    highest_price_dol DECIMAL(10, 2),
                    highest_price_eur DECIMAL(10, 2),
                    lowest_price_dol DECIMAL(10, 2),
                    lowest_price_eur DECIMAL(10, 2),
                    variation_dol DECIMAL(5, 2),
                    variation_eur DECIMAL(5, 2),
                    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            self.connexion.commit()
            cursor.close()
        except connector.Error as e:
            print(f"Erreur lors de la création de la table : {e}")
    
    def clean_value(self, value):
        """Nettoie la valeur pour enlever les signes $, €, %, et les espaces, et retourne un nombre décimal."""
        # Retirer les symboles et les espaces
        cleaned_value = value.replace('$', '').replace('€', '').replace('%', '').replace(' ', '').replace(',', '.').strip()
        
        # Convertir en float si c'est un nombre, sinon None
        try:
            return float(cleaned_value) if cleaned_value else None
        except ValueError:
            return None

    def insert_gold_price(self, data):
        """Insère une nouvelle ligne dans la table gold_prices."""
        try:
            cursor = self.connexion.cursor()
            # Requête d'insertion avec les données nettoyées
            query = """
                INSERT INTO gold_prices (
                    name, current_price_dol, current_price_eur, 
                    opening_price_dol, opening_price_eur, 
                    highest_price_dol, highest_price_eur, 
                    lowest_price_dol, lowest_price_eur, 
                    variation_dol, variation_eur
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (
                data['name'],
                self.clean_value(data['current_price_dol']),
                self.clean_value(data['current_price_eur']),
                self.clean_value(data.get('opening_price_dol', '0')),
                self.clean_value(data.get('opening_price_eur', '0')),
                self.clean_value(data.get('highest_price_dol', '0')),
                self.clean_value(data.get('highest_price_eur', '0')),
                self.clean_value(data.get('lowest_price_dol', '0')),
                self.clean_value(data.get('lowest_price_eur', '0')),
                self.clean_value(data.get('variation_dol', '0')),
                self.clean_value(data.get('variation_eur', '0'))
            ))
            self.connexion.commit()
            cursor.close()
            print("Données insérées avec succès.")
        except connector.Error as e:
            print(f"Erreur lors de l'insertion des données : {e}")

    def close_connection(self):
        """Ferme la connexion à la base de données."""
        if self.connexion.is_connected():
            self.connexion.close()
            print("Connexion fermée.")
