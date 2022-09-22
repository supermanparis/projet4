from tinydb import TinyDB


class Player:
    """Player."""
    def __init__(self, player_name, player_first_name, player_birthdate, 
                 player_sexe, player_ranking, color ='red'):
        """Has a : name, first name, birthdate, sexe, ranking"""
        self.player_name = player_name
        self.player_first_name = player_first_name
        self.player_birthdate = player_birthdate
        self.player_sexe = player_sexe
        self.player_ranking = player_ranking
        
    def save_player(self):
        
        db = TinyDB('db.json')
        players_table = db.table('players')
        players_table.insert({'nom': self.player_name, 'prenom': 
            self.player_first_name, 'sexe': self.player_sexe})