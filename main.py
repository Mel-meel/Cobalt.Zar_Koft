import os
import requests
from bs4 import BeautifulSoup
from lxml import etree
import sqlite3
import time


class Acces :

    # Constructeur de la classe
    def __init__(self, url):      
        self.url = url
        self.soup = ""

    def acces_site(self) -> "Vérifie si l'url est accessible" :
        """
        
        
        """
    
        res = False
        if requests.get(self.url, headers = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'}).status_code == 200 :
            res = True
        return res
    
    
    def cours_or(self) -> "" :
        """
        
        
        """
        # HTML de la page
        html = requests.get(self.url, headers = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'}).content
        #print(html)
        # Prépare la tambouille
        soup = BeautifulSoup(html, "html.parser")
        
        #print(soup.prettify())
        
        table_prix = soup.select("table[class='pricesTable realtime invertable'] tbody tr")
        
        return table_prix

    def format_table_prix(self, table) -> "" :
        """
        
        """
        

# >F>onction principale

if __name__ == "__main__" :
    
    acces = Acces("https://www.gold.fr/cours-or-prix-de-l-or/")
    
    if acces.acces_site() :
        print("Le site est accessible")
        
        cours_once = acces.cours_or()[0]
        
        prin(acces.cours_or(cours_once))
