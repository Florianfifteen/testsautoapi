# services-api

## Groupe de projet
- Florian Hochart
- Gwendal Garrenaux
- Benoit Defebvre
- Antoine Cornuel

## Requis

- Python3
- Pip3

Puis, exécutez cette commande :

```
pip3 install -r requirements.txt
```

## Création de la base de données

Créer la base de données MongoDB:
```
use personnes
```

Pour vérifier la base de données actuellement sélectionnée, utilisez la commande :

```
db
```

Pour vérifier la liste de bases de données, utilisez la commande:

```
show dbs
```

Ici, votre base de données créée « personnes » ne figure pas dans la liste, insérez-y au moins un document pour afficher la base de données.Ensuite supprimez tous les documents

Retournez sur la liste des DB :

```
show dbs
```

Votre base de données est désormais active.

## Utiliser l'interface
Il suffit de se rendre dans le dossier racine de l'API et exécutez cette commande :
```
python3 personne.py
```
L'API se lance, rendez-vous sur l'adresse web donnée par la console python. Deux formulaires seront disponibles : Ajouter ou Supprimer une personne.

Pour observer les personnes disponibles, ajoutez "/personne" à l'url de base.
```
127.0.0.1/personne
```

