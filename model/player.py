from database import Database as db


class Player:
    """Player."""
    def __init__(self, player_name, player_first_name, player_birthdate,
                 player_sexe, player_ranking, color='red'):
        """Has a : name, first name, birthdate, sexe, ranking"""
        self.player_name = player_name
        self.player_first_name = player_first_name
        self.player_birthdate = player_birthdate
        self.player_sexe = player_sexe
        self.player_ranking = player_ranking
        
    def save(self):
        db.save_player(self)
    
    @classmethod
    def all_players(cls):
        serialized_players = db.get_all_players()
        return serialized_players
    
    
    

        
        
'''
        
    def update(self):
        db.update_player(self)
    
    def remove(self):
        db.remove_player(self)
        
''' 
 