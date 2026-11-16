# BrutForceOnPDF

Outil de brute force de fichiers PDF en Python.

## Dépendances

* **pikepdf** : Gestion des fichiers PDF utilisée pour itérer les mots de passe.



* **tqdm**  : présent pour l'affichage / temps de la boucle en fonction de votre dictionnaire

Note : Peut nécessiter --break-system-packages si votre environnement virtuel n'est pas créé.

  ```bash
  pip install pikepdf tqdm 
```

Performances

Lors des tests : 14 millions de mots de passe itérés en une quinzaine de minutes à partir du rockyou 150 Mo (version 2026) sur un PDF test.


Possibilités pour améliorer la vitesse

    Passer du Python au C : Par nature, le C est un langage plus proche du langage machine et bien plus rapide que le Python.

    Dictionnaire adapté / personnalisé : L'utilisation d'un dictionnaire utilisant des informations propres à la personne permet une recherche plus affinée et efficace.

    Supprimer la partie graphique qui ralentit le reste.

Credits 

Pdf de Test : MrPhilippe Livolsi 
