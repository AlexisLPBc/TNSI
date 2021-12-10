# Création du canvas c
from types import resolve_bases
from typing_extensions import runtime


c = Canvas(width = 800, height = 600)

# Une fonction pour effacer la scène et redessiner un background
def background(couleur : str = 'black') :
    '''
    Rafraichit la scène avec un fond de la couleur
    'couleur' passée en paramètre et fixée sur `black` par défaut
    Préconditions :
    - couleur (str) : une chaine de caractères définissant une couleur HTML valide
    '''
    c.fill_style = "black"
    c.fill_rect(0, 0, c.width, c.height)
    # Tests
if __name__ == '__main__':
    display(c)
    background()

# Changement d'origine au milieu de la base du canvas

c.translate(800/2, 600)

# réglage de l'épaisseur et de la couleur du trait

c.line_width = 3
c.stroke_style = 'yellow'

# trait du tronc

c.stroke_line(0, 0, 0, -150)

