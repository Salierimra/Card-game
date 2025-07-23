import game_nth
import player_nth


'''Création d'une fonction permettant de retrouver l'indice d'un element en fonction de sa valeur'''
def trouve_index(liste,valeur):
    print(liste)
    print(valeur)
    if valeur in liste:
        index_v = liste.index(valeur)
    return index_v

''' Création des Joueurs'''
Nom_joueurs = ""
liste_joueur = []
cpt_joueur = 1
while Nom_joueurs != "GO":
    Nom_joueurs = input(f"Veuillez rentrer un nom de joueur {cpt_joueur} , 'GO' pour start le jeu : ")
    Nom_joueurs = Nom_joueurs.upper()
    if Nom_joueurs == "GO":
        break
    else :
        p = player_nth.Player(Nom_joueurs,[],[]) #instantiation des joueurs
        liste_joueur.append(p) #on remplit la liste avec les instantiations des joueurs
        cpt_joueur +=1

'''Création du board + start game'''

board = game_nth.Board(liste_joueur,0,[],[]) #on passe la liste des joueurs en paramètre
board.start_game()
'''Tant que le dernier joueur n'est pas a court de carte on continue '''
while len(liste_joueur[len(liste_joueur)-1].cards) !=0:
    #print(liste_joueur[len(liste_joueur)-1].cards)
    board.active_cards = [] #on reset a chaque tour
    for pp in liste_joueur: #pour tous les joueurs
        print ("Voici les cartes jouables")
        my_card = [x.value + x.icon for x in pp.cards] #création du liste qui reprend toutes les cartes par joueur mais qui les affiche sous la forme 7carreau
        
        '''on recupere la carte que le joueur veut jouer'''
        ok = False #tant que ok est false il y a un problème avec le choix de lacarte donc on continue de redemander
        while not(ok):
            try:

                cj = input("Quelle carte voulez vous jouer sous laforme : valueicon " \
                "value('A','2','3','4','5','6','7','8','9','10','J','Q','R') icon ('♥', '♦', '♣', '♠') ")
                index_valeur = trouve_index(my_card,cj)
                ok= True
            except Exception as e:
                print("Carte invalide")

          
        cjoue = pp.play(cj) #recupere la derniere carte jouée par le joueur
        board.active_cards.append(str(cjoue.value)+str(cjoue.icon))#on ajoute cette carte dans les cartes actives
        
    board.whowon(board.active_cards)#des que tous les joueurs ont joué -> check du gagnant de la manche
    '''affichage des scores en cours'''
    for jou in liste_joueur:
        print("Le joueur ",jou.name," a le score : ",jou.nb_points)
   
    
    '''Transfert des cartes de active cards vers history cards'''
    
    board.history_cards.append(board.active_cards)
    print("Liste History cards") #affiche les plis deja joué
    print (board.history_cards)
    #vu qu'on affiche par pli le nombre de carte est le nombre de plis * le nombre de joueur
    print("le nombre de carte dans history_cards est ",len(board.history_cards*len(liste_joueur))) 

'''Fin du jeu et comptage des points'''

liste_points_finaux,winner = board.cpt_score() #liste_points_finaux : liste avec les scores de tous les joueurs et winner et l'index du joueur gagnant
print("Fin du jeu")
print("Le joueur gagnant est ",winner+1)

'''Affichage des score finaux'''
for i,elem in enumerate(liste_points_finaux):
    print("Le joueur ",str(i+1)," a le score : ",elem)