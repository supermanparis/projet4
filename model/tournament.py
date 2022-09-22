from database import Database as db
from match import Match


class Tournament:
    """Tournament"""
    def __init__(self, tournament_name, location, start_date, end_date,time_controler, description, nombre_de_tours=4):
        self.tournament_name = tournament_name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.time_controler = time_controler
        self.description = description
        self.nombre_de_tours = nombre_de_tours
        self.rounds = []
        self.players = []
      
    def save(self):
        db.save_tournament(self)
        
# methode qui permet d ajouter la liste des rondes
    def add_round_list(self):
# methode qui permet de creer la liste des joueurs
# depuis la vue permettre a l utilisateur de saisir le liste des joueurs
# ex: "veuillez saisir la liste des joueurs" : joueur 1; puis il le met dans la liste
# des joueurs; joueur 2 ; puis il lemet dans la liste des joueurs, jusqu'a ce qu il termine
# y for yes, N for no, puis Z pour quitter
# Si yes l information est mise dans une liste, puis cette liste est donnée à la méthode qui..
# add_players()
# add_round()
# self.tournament.players = liste_players
# puis ajouter les methodes : 
# 1) si les joueurs ont deja joués ensemble?
# est ce qu un tour à deja été fait (voir algo suisse)
#  puis implementer ces methodes dans le model
# dans la partie vue : une classe menu sans attribut
# creer un methode pour afficher le menu principal ( qui contient par exemple 
# la gestion des tournoi, des joueurs, des ....?) 
# creer une methode pour crere le nom des autres joueurs
# creer une methode ( classe vue), player_vue, tournament_vue, match_vue
# dans cette classe vue, une methode qui nous invote a saisir les données d un joueur
# puis lorque les infos sont saisies, il faut stockercela dans un dico)
# puis le controleur va  s en servir pour créer le joueur
# on peut l'a, puis cette liste de joueursouter a la liste des joueurs peut etre mise dans un 
# tournoi ou bien sauvegardée dans la base de donnée
# créer une partie vue: "saississez les informations d un joueur", puis une foi le joueur saisie,
# le controleur les enregistrera dans la bdd un par un ou en attendant que 
# tous les joueurs soient saisies
# faire des pushs dans git hub
# bien comprendre la session d aujourd'hui
# puis methode pour savoir si les joueurs ont déjé joué?
# est ce que un tour a deja été fait
# ces methode a completer dans la partie model
# vue === un classe menu avec des methodes pour le menuprincipal, methode quitter,
# methode pour créer un joueur, methode pour creer un tournoi, metbhode pour un match


# flake 8 (pour la longeur, creer un fichier qui s appell .flake8 " max length for line" 
# lien vers al solution : https://stackoverflow.com/questions/42325453/per-project-flake8-max-line-length
# pour parametrer le flake8)
# https://flake8.pycqa.org/en/latest/user/options.html#cmdoption-flake8-max-line-length
