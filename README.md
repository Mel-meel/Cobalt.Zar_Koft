# Cobalt.Zar_Koft

**زر كوفت**

## Description

**Cobalt.Zar_Koft** est un script de scraping qui collecte les données du cours de l’or à partir d’une source en ligne et les stocke dans une base de données MySQL. Le projet permet de suivre l’évolution des prix et d’effectuer des analyses historiques des cours de l’or grâce à un stockage structuré en base de données.

## Fonctionnalités

- **Scraping des Données** : Extraction automatique des données du cours de l'or (prix actuel, ouverture, plus haut, plus bas, variations) à partir d’un site web.
- **Stockage en Base de Données** : Insertion des données extraites dans une base de données MySQL pour un suivi historique.
- **Gestion des Erreurs et Reprises** : Robustesse face aux erreurs de connexion et de scraping, avec une gestion des données incorrectes pour un stockage propre.

## Prérequis

- **Python 3.8+**
- **MySQL Server**
- Les modules Python suivants :
  - `requests`
  - `BeautifulSoup` (via `bs4`)
  - `mysql-connector-python`
  - `configparser`
  - (Optionnel) `tabulate` pour un affichage en tableau dans la console

## Installation

1. Clonez le projet :

   ```bash
   git clone https://github.com/ton-utilisateur/Cobalt.Zar_Koft.git
   cd Cobalt.Zar_Koft
   ```

2. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

3. Configurez la base de données MySQL. Créez une base de données dédiée (par exemple, `cobalt_zar_koft_test`) et configurez les accès dans le fichier de configuration `example.cfg`.

## Configuration

Créez un fichier `example.cfg` avec les informations d’identification de la base de données MySQL :

```ini
[mysql]
host = localhost
user = root
password = root
database = cobalt_zar_koft_test
```

## Utilisation

Pour exécuter le script et commencer à scraper les données du cours de l’or, lancez la commande suivante :

```bash
python main.py
```

Le script :
1. Vérifie l’accessibilité du site.
2. Récupère les données du cours de l’or sous forme de tableau.
3. Insère chaque entrée de données dans la base de données MySQL.

### Exemple de Sortie

```plaintext
Le site est accessible
Once d'Or - 2737.27 $ - 2526.50 €
Données insérées avec succès.
...
```

## Structure du Projet

- `main.py` : Point d’entrée du script, qui gère la boucle de scraping et d’insertion.
- `Acces` : Classe pour accéder au site web et extraire les données.
- `Mysql` : Classe pour gérer la connexion MySQL et l’insertion des données.
- `example.cfg` : Fichier de configuration pour les identifiants de la base de données.

## Contribuer

Les contributions sont les bienvenues ! Pour proposer une amélioration :

1. Forkez le projet.
2. Créez une branche pour votre fonctionnalité (`git checkout -b nouvelle-fonctionnalite`).
3. Committez vos changements (`git commit -m 'Ajout d'une nouvelle fonctionnalité'`).
4. Poussez votre branche (`git push origin nouvelle-fonctionnalite`).
5. Ouvrez une Pull Request.

## Autrice

- **Mel_meel**

## License

Ce projet est sous licence GPL v3.0 - voir le fichier [LICENSE](LICENSE) pour plus de détails.