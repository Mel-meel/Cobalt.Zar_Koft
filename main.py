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

    def acces_site(self) -> "Vérifie si l'url est accessible" :
        """
        :name: acces_site
        :params: url string
        :return: booléen
        :desc: blabla
        """
    
        res = False
        if requests.get(self.url, headers = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'}).status_code == 200 :
            res = True
        return res
    
    def page_html(self) -> "" :
        """
        
        """
        # HTML de la page
        html = requests.get(self.url, headers = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'}).content
        


def lecture_liste_calibres(fichier) -> "Ouvre simplement un fichier" :
    """
    :name: lecture_liste_calibres
    :params: fichier string
    :return: liste
    :desc: Ouvre le fichier, renvoie son contenu sous forme de liste, un élément par ligne
    """
    
    with open(fichier) as f :
        lignes = [ligne.rstrip() for ligne in f]
    return lignes



def format_valeur_caracteristiques(chaine) -> "Nettoie la chaine" :
    """
    :name: format_nom_caracteristiques
    :params: chaine string
    :return: string
    :desc: Nettoie la chaine en paramètre. retire les paranthèses, remplce les espaces par des underscores pour un meilleur traitement.
    """
    
    chaine = chaine.replace("\xa0", " ")
    
    return chaine


def scrap_page_calibre(url) -> "Scrape les informations du calibre" :
    calibre = {}
    
    """
    :name: scrap_page_calibre
    :params: url string
    :return: dict
    :desc: Coeur du programme. C'est ici que se déroule le scrapage (la scrapation?) de la page html.
    """
    
    # HTML de la page
    html = requests.get(url, headers = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'}).content
    
    # Prépare la tambouille
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    
    # Capte la description du calibre en anglais (sera traduite ensuite par le logiciel mais pas dans la base de données)
    # La description est conservée telle qu'elle est, le logiciel comprendra un petit interpréteur HTML pour l'afficher
    description = soup.select_one("p").getText()
    
    # Rempli le dictionnaire de retour avec deux éléments de base : l'url et la descritpion
    calibre["url"] = url
    calibre["description"] = description
    
    # On souhaite récupérer la description et les informations techniques concernant le calibre
    # Les infos techniques sont dans 'table class="infobox"'
    # Pour la description, c'est moins simple, on verra plus tard si j'ai le temps, de toute façon, c'est même pas prévu dans la base de données
    table_infobox = soup.select("table[class='infobox'] tbody tr")
    
    # Parcours (le parcourationnage?) les informations techniques
    for ligne in table_infobox :
        th = ligne.findChild("th")
        if th != None :
            if type(th.get("class")) == list :
                # Le nom du calibre se trouve dans la ligne de classe "infobox-above"
                if "infobox-above" in th.get("class") :
                    clef = "name"
                    valeur = th.getText()
                    calibre[clef] = valeur
                # Toutes les autres infos sont dans des lignes de classe "infobox-label"
                elif "infobox-label" in th.get("class") :
                    clef = format_nom_caracteristiques(th.getText())
                    valeur = format_valeur_caracteristiques(ligne.findChild("td").getText())
                    # Si il s'agit d'une données numérique, on ne garde que sa valeur en mm, pas en pouces
                    if clef in ["bullet_diameter", "neck_diameter", "shoulder_diameter", "base_diameter", "rim_diameter", "rim_thickness", "case_length", "overall_length"] :
                        valeur = trouve_mm(valeur)
                    # Pareil pour les données concernant la pression mais cette faois on conserve (de haricot) les données en MPa
                    elif clef in ["maximum_pressure_saami", "maximum_pressure_cip"] :
                        valeur = trouve_mpa(valeur)
                    calibre[clef] = valeur
    
    return calibre



# Liste des calibres et de leurs pages wikipédia

if __name__ == "__main__" :
    
    acces = Acces("https://www.gold.fr/cours-or-prix-de-l-or/")
    
    if acces.acces_site() :
        print("Le site est accessible")
        
        print(acces.page_html)
