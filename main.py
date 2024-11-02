import os
import requests
from bs4 import BeautifulSoup
from lxml import etree
import time
from Mysql import Mysql
import configparser


class Acces :

    # Constructeur de la classe
    def __init__(self, url) :
        self.url = url
        self.soup = ""

    def acces_site(self) -> "Vérifie si l'url est accessible" :
        """
        
        
        """
    
        res = False
        if requests.get(self.url, headers = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'}).status_code == 200 :
            res = True
        return res
    
    
    def cours_or(self):
        """Récupère les informations détaillées du cours de l'or."""
        # Requête pour récupérer le contenu HTML de la page
        html = requests.get(self.url, headers={'User-agent': 'Mozilla/5.0 ...'}).content
        soup = BeautifulSoup(html, "html.parser")
        
        # Trouver les lignes dans la table des prix
        table_prix = soup.select("table[class='pricesTable realtime invertable'] tbody tr")
        
        # Stocker les informations extraites
        prix_details = []
    
        for row in table_prix:
            data = {}
    
            # Nom de l'actif (e.g., "Once d'Or")
            data['name'] = row.select_one(".name").get_text(strip=True)
    
            # Prix actuel en dollars et euros
            data['current_price_dol'] = row.select_one(".price .value-currency.dol").get_text(strip=True)
            data['current_price_eur'] = row.select_one(".price .value-currency.eur").get_text(strip=True)
    
            # Les autres valeurs de prix
            prices = row.select(".price")
            if len(prices) > 1:
                data['opening_price_dol'] = prices[1].select_one(".value-currency.dol").get_text(strip=True)
                data['opening_price_eur'] = prices[1].select_one(".value-currency.eur").get_text(strip=True)
            if len(prices) > 2:
                data['highest_price_dol'] = prices[2].select_one(".value-currency.dol").get_text(strip=True)
                data['highest_price_eur'] = prices[2].select_one(".value-currency.eur").get_text(strip=True)
            if len(prices) > 3:
                data['lowest_price_dol'] = prices[3].select_one(".value-currency.dol").get_text(strip=True)
                data['lowest_price_eur'] = prices[3].select_one(".value-currency.eur").get_text(strip=True)
    
            # Variation en pourcentage
            variation_dol = row.select_one(".var .value-currency.dol .variation")
            if variation_dol:
                data['variation_dol'] = variation_dol.get_text(strip=True)
    
            variation_eur = row.select_one(".var .value-currency.eur .variation")
            if variation_eur:
                data['variation_eur'] = variation_eur.get_text(strip=True)
    
            prix_details.append(data)
        
        return prix_details

    def format_table_prix(self, table) -> "" :
        """
        
        """
        

# >F>onction principale

if __name__ == "__main__" :

    container_conf = configparser.ConfigParser()
    container_conf.read('example.cfg')
    
    
    acces = Acces("https://www.gold.fr/cours-or-prix-de-l-or/")
    
    if acces.acces_site() :
        print("Le site est accessible")
        
        cours = acces.cours_or()
        
        cours_once = cours[0]
        
        cours_lingot = cours[1]
        
        print(cours_once)
        print(cours_lingot)
        
        mysql = Mysql(["localhost", "root", "root", "cobalt_zar_koft_test"])
        
        for data in cours:
            try:
                mysql.insert_gold_price(data)
            except Exception as e:
                print(f"Erreur lors de l'insertion des données pour {data['name']}: {e}")
            
        # Fermer la connexion
        mysql.close_connection()