from database import Database as db
#from match import Match


class Round:
    """Round (tour) """
    def __init__(self, round_name, round_start_time, 
                 round_end_time, match_list=None):
    
        self.round_name = round_name
        self.round_start_time = round_start_time
        self.round_end_time = round_end_time
        self.match_list = match_list
    
    def save(self):
        db.save_round(self)
    
    def add_match(self, match):
        self.match_list.append(match)
        
