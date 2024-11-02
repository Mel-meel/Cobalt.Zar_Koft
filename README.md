# Cobalt.Zar_Koft

**زر كوفت**

## Description

**Cobalt.Zar_Koft** is a scraping script that collects gold price data from an online source and stores it in a MySQL database. This project enables users to track price evolution and perform historical analyses on gold prices thanks to structured data storage.

## Features

- **Data Scraping**: Automatically extracts gold price data (current price, opening price, high, low, variations) from a website.
- **Database Storage**: Inserts extracted data into a MySQL database for historical tracking.
- **Error Handling and Resilience**: Robustness against connection and scraping errors, with handling for incorrect data entries to ensure clean storage.

## Requirements

- **Python 3.8+**
- **MySQL Server**
- The following Python modules:
  - `requests`
  - `BeautifulSoup` (via `bs4`)
  - `mysql-connector-python`
  - `configparser`

## Installation

1. Clone the project:

   ```bash
   git clone https://github.com/Mel-meel/Cobalt.Zar_Koft
   cd Cobalt.Zar_Koft
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure the MySQL database. Create a dedicated database (e.g., `cobalt_zar_koft_test`) and set up access in the `example.cfg` configuration file.

## Configuration

Create an `example.cfg` file with your MySQL database credentials:

```ini
[mysql]
host = localhost
user = root
password = root
database = cobalt_zar_koft_test
```

## Usage

To run the script and start scraping gold price data, use the following command:

```bash
python main.py
```

The script:
1. Checks the website’s accessibility.
2. Scrapes gold price data in a structured table format.
3. Inserts each data entry into the MySQL database.

### Example Output

```plaintext
The site is accessible
Gold Ounce - 2737.27 $ - 2526.50 €
Data inserted successfully.
...
```

## Project Structure

- `main.py`: Script entry point, managing the scraping and insertion loop.
- `Acces`: Class for accessing the website and extracting data.
- `Mysql`: Class for MySQL connection and data insertion.
- `config.cfg`: Configuration file for database credentials.

## Contributing

Contributions are welcome! To propose an improvement:

1. Fork the project.
2. Create a branch for your feature (`git checkout -b new-feature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push your branch (`git push origin new-feature`).
5. Open a Pull Request.

## Author

- **Mel_meel**

## License

This project is licensed under GPL v3.0 - see the [LICENSE](LICENSE) file for details.

---

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

## Installation

1. Clonez le projet :

   ```bash
   git clone https://github.com/Mel-meel/Cobalt.Zar_Koft
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
- `config.cfg` : Fichier de configuration pour les identifiants de la base de données.

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