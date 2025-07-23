class Symbol:
    '''Class symbol with 2 attributes une couleur qui doit être un string
    et une icone qui represente les 4 couleurs d'un paquet de cartes'''
    def __init__(self,color:str,icon):
    
        self.color = color
        self.icon = icon

class Card(Symbol):
    '''Class card qui hérite de symbol qui rajoute une valeur value (A,2,3,....)
 et une icone qui represente les 4 couleurs d'un paquet de cartes'''
    def __init__(self,color:str,icon,value:str):
        super().__init__(color,icon)
        self.value = value

    def __str__(self):
        return self.value+self.icon


