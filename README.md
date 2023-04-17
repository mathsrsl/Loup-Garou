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
* `home.py` page d'accueil du jeu
* `settings.py` page pour paramétrer le jeu | accessible depuis l'accueil
* `stat.py` page d'affichage des statistiques du joueur
* 

## Utilsation des classes
<blockquote>

## La classe `Button`
La classe `Button` sert à créer des bouton personnalisable, à les afficher et à contrôler s'ils sont cliqués pour intéragir avec le jeu.
<blockquote>

## Créer un buouton

On utilisera la commande suivante pour créer un bouton :

```python
button_confirmer = utils.button.Button(..., ..., ...)
```
<blockquote>

**Les paramètres obligatoires à renseigner :**

- :`text`: le contenue du bouton | type(str)
- :`pos`: la position (x, y) du bouton sur la page en px| type(tuple)
- :`width`: la largeur du bouton en px  | type(int)
</blockquote>
<blockquote>

**Les paramètres optionnels à renseigner :**

- :`height`: La hauteur du bouton en px, par défaut à 70px (taille conseillé) | type(int)
- :`elevation`: La hauteur entre le bouton et son ombre en px, par défaut à 5px | type(int)
- :`clickable`: Définit si le bouton est cliquable ou non, s'il ne l'ai pas, il sera grisé, par défaut sur True | type(bool)
- :`idColor`: Personnaliser les couleurs du bouton avec des couleurs prè-existantes (0: noir/blanc; 1: bleu; 2: violet), par défaut à 1 | type(int)
- :`fontSize`: La taille de la police en px, par défaut à 25 | type(int)
- :`borderRaduis`: Le degrés d'arrondi du bouton en degés, par défaut sur 20 | type(int)
- :`pawDisplaying`: Afficher ou non un logo de patte de loup dans le coin inférieur droit du bouton, par défaut sur True | type(bool) 
- :`colorText`: La couleur du texte en hexadécimal au format '#XXXXXX', par défaut sur blanc (#FFFFFF) | type(str)
</blockquote>


Exemple :

```python
#créer un bouton basic (les paramètres obligatoires):
button_confirmer = utils.button.Button('confirmer', (200, 300), 250)

#créer un bouton personnalisé (les paramètres optionnels):
button_confirmer = utils.button.Button('confirmer',(200, 100), 300, height=40, clickable=False, elevation=7, idColor=2, fontSize=20, borderRadius=15, pawDisplaying=False, colorText='#F3A8AF')

#afficher le bouton:
button_confirmer.draw(screen)
```

Étant donné qu'il y a beaucoup de paramètres optionnels, il est conseillé d'écrire le nom du paramètre avant sa valeur (Exemple : `height=40` au lieu de `40`). Cela permettra de s'y retrouver plus facilement. De plus, cela est nécessaire si les paramètres ne sont pas indiqués dans l'ordre souhaité par la classe.
</blockquote>

## Utiliser les méthodes

Les méthodes serviront pour modifier les propriétés et/ou apparence d'un bouton pour le bon déroulement du jeu.
<blockquote>

**Vérifier si le bouton est cliqué**

[description]

Exemple:
```python
#code
```
</blockquote>
<blockquote>

**Changer le texte**

Cette méthode, nommée `set_text`, permet de modifier la couleur du texte à la demande. Cela fonctionne uniquement avec les couleurs en hexadécimal `'#FFFFFF'`, ou en rensignant le nom de la couleur en anglais `'white'`. La méthode `rgb()` n'est pas prise en charge.

Exemple :
```python
button_confirmer.set_text('envoyé')
```
</blockquote>
<blockquote>

**Changer la couleur du texte**

[description]

Exemple:
```python
#code
```
</blockquote>
<blockquote>

**Modifier la possibilité de cliquer sur le bouton**

[description]

Exemple:
```python
#code
```
</blockquote>
</blockquote>
</blockquote>