import card_nth
import random

class Player:
    '''Classe player ayant les attributs suivants
    Nom du joueur
    Liste des cartes dans sa main
    Liste des cartes jouées
    nombre des points du joueur
    number_of cards startant a 0 comptant le nombre de carte joué
    turn_number comptant le nombre de tour joué'''
    def __init__(self,name:str,cards:list,history:list,nb_points=0,number_of_cards=0,turn_count=0):
        self.name = name
        self.cards = cards
        self.history = history
        self.nb_points = nb_points
        self.number_of_cards = number_of_cards
        self.turn_count = turn_count

    '''Création d'une fonction permettant de retrouver l'indice d'un element en fonction de sa valeur'''
    def trouve_index(liste,valeur):
        if valeur in liste:
            index_v = liste.index(valeur)
        return index_v
    
    def play(self,cartejoue:str):
        '''prend en param la carte jouée apres l'avoir choisie'''
        my_cards = [x.value + x.icon for x in self.cards] #transforme la liste des carte en cartes sous forme 7 de carreau
                
        index_cj = Player.trouve_index(my_cards,cartejoue)#trouve l'index de la carte jouée
        carte_joué = self.cards[index_cj]
        self.history.append(carte_joué) #ajout dans l'historique des cartes
        self.cards.remove(carte_joué) #suppression dans les cartes restantes

        print("tour numero : "+ str(self.turn_count+1)+" le joueur : "+self.name +" a joué la carte "+ carte_joué.value +" "+carte_joué.icon+ " a son " +str(self.turn_count+1)+ " ieme tour")
        self.turn_count +=1
        self.number_of_cards+=1
        
        return carte_joué #retourne la carte jouée :) 


class Deck:
    def __init__(self,cards:list):
        '''Constructeur prenant une liste de cartes en attribut'''
        self.cards = cards

   
    def fill_deck(self):
        '''Remplir le deck avec toutes les combinaisons (52)'''
        symbols = ['♥', '♦', '♣', '♠']
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','R']
        colors = ['rouge','noir']
        cpt = 0
        for v in values:
            for s in symbols:
                
                instan = card_nth.Card(colors[cpt],s,v) #attention il faudra gerer le rouge/noir
                cpt+=1
                self.cards.append(instan) #on ajoute l'instance dans la liste des cartes du deck
        
    def shuffle(self):
        '''Melange le deck'''
        random.shuffle(self.cards)

    def distribute(self,nb_player:list):
        ''' va distribuer les 52 cartes de maniere equivalente'''
        my_list = self.cards
        for i in range(0,len(my_list)):
            '''on parcourt la liste des cartes qui sont des instances de cards'''
            #ici le modulo est utilisé pour cibler le joueur voulu -> ex la 7 ieme cartes est donné au 1er joueur si le nombre de joueur est 3 car 7%3 = 1
            #dans notre exemple le 1er joueur recevra la 7ieme carte
            nb_player[i%(len(nb_player))].cards.append(my_list[i])
                
            
       
    
        
        


        

        
        



