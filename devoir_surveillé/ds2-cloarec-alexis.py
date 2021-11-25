# Première implémentation pour les piles
def creer_pile():
    '''Renvoie une pile vide'''
    return []

def est_vide(pile):
    '''Renvoie un booléen, True si la pile est vide et False sinon'''
    return p == []

def empiler(pile, element):
    '''Empile element au sommet de pile'''
    pile.append(element)
    
def depiler(pile):
    '''Renvoie et enlève la valeur du sommet de pile'''
    assert not est_vide(pile), "Pile vide"
    return pile.pop()

# Deuxième implémentation pour les piles
class Pile:

    '''classe Pile création d’une instance Pile avec une liste'''
    
    def __init__(self):
        '''Initialise une pile vide'''
        self.liste = []
        
    def est_vide(self):
        '''Renvoie un booléen, True si la pile est vide et False sinon'''
        return len(self.liste) == 0

    def empiler(self, element):
        '''Empile element au sommet de pile'''
        self.liste.append(element)

    def depiler(self):
        '''Renvoie et enlève la valeur du sommet de pile'''
        return self.liste.pop()

    def __repr__(self):
        return repr(self.liste)

def sommet(pile):
    
    ''' Renvoie la valeur au sommet de la pile mais sans la supprimer de la pile '''
    if est_vide(pile) == True :
        msg = f'IndexError: pile vide'
        return msg
    else :
        return pile[-1]
    

def mettre_disques(pile, n):
    '''met des disques de taille n à 1 sur la pile'''

def creation_tours(n):
    ''' renvoie une liste de 3 piles,
    la première correspond à la pile des n disques,
    les autres étant vides.'''

