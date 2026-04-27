# prompt IA :
Bonjour, je voudrais que tu analyses mon code actuel du fond en comble et de manière structuré, ici j'ai déjà posé les bases notemment sur l'environnement Devsecops et les fichiers Dockerfile.test, Dockerfile, deocker-compose.yml et le pipeline CI/CD , ton rôle est d'écrire le code suivant tout en suivant l'arborescence qui est déjà en place , voici une petite résumer de l'arborescence en question :
project/src/project
- controller/ (pour les routes des endpoints)
- domains/ (où se regroupe les logiques métier et les validations des données d'où son nom le domaine)
- dtos/ (où se situe les dtos pour faciliter les transfert des données)
- repositories/ pour l'interaction avec la base de donnée (mais ici nous n'allons pas utilisé une base de donnée mais une simulation avec list+dict le nom de la variable est "THRESHOLDS")

- à bien noter : quand tu vas écrire du code j'aimerai que tu n'ajoutes pas des fichiers .md et .txt et partout dans le projet je veux que tu ne mets pas des écritures avec des émojis ou des iconnographies , ton rôle est d'écrire le code en suivant les règles que je vais de donner ci dessous , et je veux du code simple , lisible, facile à comprendre et scalable, ici le code est en python avec poetry FastAPI

- une fois le code en place , j'aimerai ensuite que tu mets en place les tests unitaires, intégrations et fonctionnel , ici l'objectif est de couvrir et de dépasser le coverage de 80% , j'ai déjà préparé le terrain pour cela 

- il y a déjà du code d'exemple que tu peux t'inspirer et prendre comme référence pour écrire le nouveau code dans le dossier project , j'aimerai que tu supprimes tout les fichiers en premier pour remplacer avec le vrai projet , le code déjà existant me servait juste de base afin que tu comprennes bien ma structure , il a déjà aussi une base de donnée que tu vas utiliser dans project/database/db_ms6.sql tu vas utiliser la base de donnée pour les données

- maintenant voici le contexte pour le projet :
ce projet est un microservice , ici il doit exposer qu'un seul endpoint POST/validate , c'est une simulation dont des capteurs IoT envoie des données avec leur seuils de réference sur la qualité d'air
exemple :
Voici les capteurs :
Capteur(Co2, temperature, noise, pm25)

chaque capteurs ont leur pripre seuil de référence (ce sont leur règle métier à utiliser dans le code)
exemple :
c02 : (seuil modéré:800, seuil critique:1000, unité:ppm)
temperature : (seuil modéré:35, seuil critique:40, unité:°C)
noise : (seuil modéré:70, seuil critique:85, unité:dB)
pm25 : (seuil modéré:25, seuil critique:50, unité:micro-gramme/m3)
humidity : (seuil modéré:60, seuil critique:80, unité:%)

- dans le code il y a une dictionnaire (list+dict) en python , voici comment va se dérouler les scénario suivant :
voici des exemples d'entrée et sortie
POST/valildate :

Entrée {"sensor": "co2", "value":500.0}

Sortie 
cas1 - valeur normale (< seuil modéré) :
{
  "valid": true,
  "level": "normal",
  "sensor": "co2",
  "value": 500.0,
  "threshold": 800,
  "timestamp": "2026-04-27T09:00:00Z"
}

cas2 - valeur modérée (>= seuil modéré, < seuil critique) :
{
  "valid": true,
  "level": "moderate",
  "sensor": "co2",
  "value": 850.0,
  "threshold": 800,
  "timestamp": "2026-04-27T09:00:00Z"
}

cas3 - valeur critique (>= seuil critique) :
{
  "valid": false,
  "level": "critical",
  "sensor": "co2",
  "value": 1500.0,
  "threshold": 1000,
  "timestamp": "2026-04-27T09:00:00Z"
}

cas4 - capteur inconnu :
{
  "valid": false,
  "level": "unknown",
  "message": "Capteur non répertorié"
}

cas5 
{
  "valid": true,
  "level": "moderate",
  "sensor": "humidity",
  "value": 65.0,
  "threshold": 60,
  "timestamp": "2026-04-27T09:00:00Z"
}


maintenant voici les instructions dont tu vas suivre à la lettre :
- tout d'abord, après avoir analysé le projet supprime tout les fichiers liées avec le projet équation second degré qui est en place , on va le changer je prepète , le projet est dans project/src/project

- après cela crée le fichier sensor.py dans le repositories avec la list dict en utilisant ces données là afin que dans le post/validate je peux saisir les tests dans swagger et avoir des résultats n'utilse pas de base donnée donc supprime le dossier database et aussi les fichiers de connexions avec la base de données et aussi le docker-compose yml 

- ensuite dans domains , ajoute le fichier validator.py où reside tout les logiques métier et les règles métiers de validations des capteurs , n'oublie pas d'ajouter les excepetions , ici code de manière le plus simples possible 

- après configure la route POST/validate dans le controllers

- n'oublie pas d'utiliser des DTO dans dtos pour le data transfert object

- et n'oublie pas de modifier main.py

- ici nous n'aurons pas aussi besoin de config.py

---------------------------------------------
Pour les tests unitaires + intégrations + fonctionnel (avec l'objectif de coverage supérieur à 80% que je vais vérifier sur Dockerfile.test ensuite)
- voici d'abord les 4 tests fonctionnels dont tu dois ajouté afin qu'il soit scané dans sonarcloud
test_normal : valeur < seuil modéré -> level='normal', valid=True
test_moderate ; valeur entre seuil modéré et critique -> level ='moderate', valid=True
test_critical : valeur >= seuil critique -> level='critical', valid = False
test_inconnu : capteur non répertorié -> level='inconnu', valid=False

- ensuite ajoute les tests unitaires et intégrations 
