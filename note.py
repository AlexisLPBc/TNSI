def demander_entier(message : str) -> int :
    """ ==================================================================================================================
    
        * Description : 
            Je demande à l'utilisateur un nombre correspondant à la question du message et renvoie le résultat au format entier ;
                > Remarque : Ici, pas de gestion de vérification de validité de la saisie utilisateur.
                        
        * Exemple :
            >>> demander_entier("Combien de notes sont à saisir ? ")
            Combien de notes sont à saisir ? 5
            5
                    
        * Préconditions :
            message (str) : question définissant le nombre à saisir ;
                    
        * Postconditions :
            (int) : la valeur saisie convertie en entier.       
        
        ==================================================================================================================
    """
    # Assertions de vérification des préconditions :
    assert type(message) == str  , "Le message doit être une chaine de caractères."
            
    # bloc d'instructions :
    nombre = int(input(message))
    return nombre

def saisir_note() -> float :
    """ ==================================================================================================================
    
        A COMPLETER
        * Description : 
                Je demande à l'utilisateur une note format entier ;
                        
        * Exemple :
            >>> saisir_note()=int(input())
            
                                           
        * Préconditions :
             Il faut que ce soit un entier ;
                     
        * Postconditions :
            (float) : la valeur saisie convertie en float.       
        
        ==================================================================================================================
    """
    
    # Instructions A CODER
try :
    saisie = input(f"Saisir une note comprise entre 0.0 et 20.0 : ")
    saisie.replace(',','.') # prévoir de remplacer le séparateur décimal au cas où ...
    note = float(saisie)
    if note <= 0.0 or note >= 20.0 :
        raise ValueError
    return note
    
except ValueError :
    print(f"La valeur saisie doit être un nombre entier ou décimal suppérieur ou égal à 0.0 et inférieur ou égal à 20.0.")   
        
def minimum(liste:list) -> float :
    """ ==================================================================================================================
    
        A COMPLETER
        
        * Description : 
        Je demande à liste valeurs le minimum qu'elle contient. ;
                        
        * Exemple :
           liste[]=[1,6,20,14] 
           minimum_table(liste)
           1
        * Préconditions :
             il faut que ce soit dans une liste composer d'entier ;
                    
        * Postconditions :
            (float) : la valeur mini de la liste d'entrée.       
        
        ==================================================================================================================
    """
    
    # Instructions A CODER
    minimum=liste[0]
    for i in liste:
        if i<=minimum:
            minimum=i
        return minimum  

def maximum(liste:list) -> float :
    """ ==================================================================================================================
    
        A COMPLETER
        
        * Description : 
            Je demande à liste valeurs le maximum qu'elle contient. ;
                        
        * Exemple :
            >>> liste[]=[1,6,20,14] 
           minimum_table(liste)
           20
                                           
        * Préconditions :
             il faut que ce soit dans une liste composer d'entier ;
        * Postconditions :
            (float) : la valeur maxi de la liste d'entrée.       
        
        ==================================================================================================================
    """
    # Instructions A CODER
    maximum=liste[0]
    for i in liste:
        if i>=minimum:
            maximum=i
    print (maximum)

def moyenne(liste:list) -> float :
    """ ==================================================================================================================
    
        A COMPLETER
        
        * Description : 
        je demande a la liste le nombre de notes qu'elle contient puis je l'ai additionne entre eux puis je divise par le nombre de note;
                        
        * Exemple :
        liste=[1,2,3]
        moyenne(liste)
        2
             
                                         
        * Préconditions :
             Une liste avec des nombres entiers ;
                    
        * Postconditions :
            (float) : la valeur moyenne de la liste d'entrée.       
        
        ==================================================================================================================
    """
    # Instructions A CODER
    s=0
    for n in liste :
        s+=n
    return s/len(liste)
    print(moyenne(liste))