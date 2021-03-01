# geo_api
Test API with Django and Django Rest frameworks

Bonjour l'équipe,

Voici quelques explications sur mon rendu pour l'API de test avec Django

Le script qui importe les données est à la racine du projet (test_app) et se nomme 'populate.py'
Les modèles ainsi que leurs attributs sont traduits en anglais.
J'ai pris les tâches du document point par point, le seul point qui est toujours flou pour moi étant celui sur les interfaces à ajouter
(J'ai juste ajouté une route '/api' qui retourne la page de la liste des villes avec possibilité de recherche)
Je n'ai pas appelé mon endpoint de recherche de ville (/api/cities/ en GET) pour la vue de recherche car la requète de toutes les villes étant super longue j'ai voulu gérer la pagination en amont.
Je n'ai pas fait le bonus.

J'ai joint le requirements.txt pour installer l'environnement pour tester en local si souhaité.
Je n'ai écrit ni doc ni tests pour l'API.

Guillaume
