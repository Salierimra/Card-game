import player_nth

class Board:
    '''Class board qui possede les attributs suivants
    la liste des joueurs
    le compte des tours
    la liste des cartes en jeu en cours
    la liste des cartes deja jouées'''

    def __init__(self,players:list,turn_count:int,active_cards:list,history_cards:list):
        self.players = players
        self.turn_count= turn_count
        self.active_cards = active_cards
        self.history_cards = history_cards
    
    def start_game(self):
        print("Le jeu commence")
        deck = player_nth.Deck([]) #création d'un deck
        deck.fill_deck() #remplit le deck
        deck.shuffle() #melange le deck
        print("Le deck est mélangé")
        deck.distribute(self.players)#distribue le deck parmis la liste des joueurs
        print("Le deck est distribué")
    
    def whowon(self,cartesactives):
        '''Cette fonction prend en paramètre la liste des cartes joués ce round ci :
        'les cartes actives' et va retourner l'index de la carte gagnante'''
        
        #on crée un dictionaire pour ordonner les valeur du plus faible au plus fort selon la valeur de la clef
        dico_des_valeurs_ordonnés = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'R':13,'A':14}
        
        #on supprime l'icone
        my_value_list = [x[:-1] for x in cartesactives]
        
        liste_value = []
        liste_max_value = []
        #parcourt de la liste sans icone et ajout dans une nouvelle liste de la valeur de la carte (ex : roi = 13)
        for e in my_value_list:
            
            liste_value.append(dico_des_valeurs_ordonnés[e])
        max_value = max(liste_value) #on trouve la valeur max de cette liste de valeur

        #on parcours notre liste pour recup l'index des joueurs qui avaient la meilleur carte
        for i,val in enumerate(liste_value):
            if (val == max_value):
                print(i)
                liste_max_value.append(i) #a la fin on veut une liste avec les index des joueurs qui avaient la meilleur carte
        
        if (len(liste_max_value)==1): #si on a que un gagnant
            print ("Le joueur gagnant est le ",str(liste_max_value[0]+1))
            self.players[liste_max_value[0]].nb_points +=1
        
        else: #si on a plusieurs gagnants
            for elts in liste_max_value:
                print ("Les joueurs gagnants sont les joueurs ",str(elts+1))
                
                self.players[elts].nb_points +=1 #on rajoute un point a tous les gagnants
            
        return liste_max_value #on retourne la liste des indices des joueurs gagnants
    

    def cpt_score(self):
        '''Fin du jeu -> on dit qui est gagnant et le score de chacun'''
        liste_score_fin = []
        '''on remplit notre liste de retour avec les points de tous les joueurs'''
        for pl in self.players:
            liste_score_fin.append(pl.nb_points)

        joueur_gagnant = 0
        joueur_gagnant = player_nth.Player.trouve_index(liste_score_fin,max(liste_score_fin)) # on va considerer qu'il n'y a pas d'égalité a la fin mais ca pourrait arriver
        return liste_score_fin,joueur_gagnant #on retourne la liste des scores et l'index du joueur gagnant

    

        

        
        
