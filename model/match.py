from database import Database as db


class Match:
    """Match"""
    def __init__(self, player_1, player_1_score, player_2, player_2_score):
    
        self.player_1 = player_1
        self.player_1_score = player_1_score
        self.player_2 = player_2
        self.player_2_score = player_2_score
    
    def match_name(self):
        return ([self.player_1, self.player_1_score],[self.player_2, self.player_2_score])
    
    def save(self):
        db.save_match(self)

# pour les méthodes :
# Lorsqu'un tour est terminé, le gestionnaire du 
# tournoi saisit les résultats de chaque match avant de générer les paires suivantes. 
# Le gagnant reçoit 1 point, le perdant 0 point. Si un match se termine par un match nul,
# chaque joueur reçoit 1/2 point.
# Un match unique doit être stocké sous la forme d'un tuple contenant deux listes, chacune contenant
# deux éléments : une référence à une instance de joueur et un score. Les matchs multiples doivent être 
# stockés sous forme de liste sur l'instance du tour. 


        
        
        
"""
TOURS/MATCHS
        
Chaque tour est une liste de matchs. Chaque match consiste en une paire de joueurs avec 
un champ de résultats pour chaque joueur. Lorsqu'un tour est terminé, le gestionnaire du 
tournoi saisit les résultats de chaque match avant de générer les paires suivantes. 
Le gagnant reçoit 1 point, le perdant 0 point. Si un match se termine par un match nul,
chaque joueur reçoit 1/2 point.

Un match unique doit être stocké sous la forme d'un tuple contenant deux listes, chacune contenant
deux éléments : une référence à une instance de joueur et un score. Les matchs multiples doivent être 
stockés sous forme de liste sur l'instance du tour. 

En plus de la liste des correspondances, chaque instance du tour doit contenir un champ de nom. 
Actuellement, nous appelons nos tours "Round 1", "Round 2", etc. Elle doit également contenir 
un champ Date et heure de début et un champ Date et heure de fin, qui doivent tous deux être automatiquement 
remplis lorsque l'utilisateur crée un tour et le marque comme terminé. Les instances de round doivent 
être stockées dans une liste sur l'instance de tournoi à laquelle elles appartiennent.

        """