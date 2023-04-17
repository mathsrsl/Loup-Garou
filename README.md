# Loup-Garou

## Organisation des dossiers et fichiers
> Le dossier `assets` sert pour stocker les fichiers de type image, font, vidéo, son, etc...

> Le dossier `utils` sert pour ranger les fichiers python pour les fonctions génériques du jeu/interface (par exemple button.py, server.py, etc..)

> Le dossier `display` permettera de stocker tous les écrans/fenêtre de jeu

<blockquote>

Les fichiers nommés `__init__.py` servent à importer toutes les fonctions/classes contenus dans le dossier.

Exemple avec le dossier `utils` :

<blockquote>

Importation dans le fichier __init__.py :
```python
from .home import *
from .button import *
from .settings import *
```

Importer les fonctions/classes dans n'importe quel fichier:
```python 
import utils
```

Utiliser les fonctions/classes :
```python
elt = utils.button.Button()
utils.button.draw(elt)

utils.settings.main(screen)
```
'
</blockquote>
'
</blockquote>

## Organisation des fenêtres (dossier display)

* `main.py` sert à jouer l'annimation de départ et redirige vers `home.py`
* 

## Utilsation des classes
<blockquote>

## La classe `Button`
description
<blockquote>

## Créer un buouton

<blockquote>

Exemple

```python
```
</blockquote>

<blockquote>

## Utiliser les méthodes

<blockquote>

##Méthode de couleur

<blockquote>

Exemple:
```python
```
</blockquote>
</blockquote>
</blockquote>
</blockquote>
</blockquote>