from tinydb import TinyDB


class Database:
    """Database (tour) """

    db = TinyDB('db.json')
    players_table = db.table('players')
    tournament_table = db.table('tournament')
    round_table = db.table('round')
    match_table = db.table('match')
    # idem pour tournoi avec : tournament_table =
 
    def serialize_match(cls, match):
        '''serializer un match'''
        serialized = match.__dict__
        return serialized

    @classmethod
    def save_match(cls, match):
        '''sauver un match '''
        cls.match_table.insert(cls.serialize_match(cls, match))
      
    def serialize_player(cls, player):
        '''serializer un joueur'''
        serialized = player.__dict__
        return serialized

    @classmethod
    def save_player(cls, player):
        '''sauver un joueur '''
        cls.players_table.insert(cls.serialize_player(cls, player))

    @classmethod
    def get_all_players(cls):
        serialized_players = cls.players_table.all()
        return serialized_players

    def serialize_tournament(cls, tournament):
        '''sérializer un tournoi '''
        serialized = tournament.__dict__
        return serialized

    @classmethod
    def save_tournament(cls, tournament):
        '''sauver un tournoi '''
        cls.tournament_table.insert(cls.serialize_tournament(cls, tournament))

    @classmethod
    def create_tournament(cls, tournament):
        '''créer un tournoi '''
        cls.tournament_table.insert(cls.serialize_tournament(cls, tournament))

    def serialize_round(cls, round):
        '''serializer une ronde'''
        serialized = round.__dict__
        return serialized

    # pour serilaizer une ronde:
    @classmethod
    def save_round(cls, round):

        cls.round_table.insert(cls.serialize_round(cls, round))


'''
    # pour updater un jouer:
    @classmethod
    def update_player(cls, player):
     
        cls.players_table.update(cls.serialize_player(cls, player))

    # pour supprimer un jouer:
    @classmethod
    def remove_player(cls, player):
    
        cls.players_table.remove(cls.serialize_player(cls, player))

def update_player(self):

    #fenchurch ?
    
        db = TinyDB('db.json')
        players_table = db.table('players')
        players_table.update({'nom du ': self.player_name,'prenom': 
        self.player_first_name,'sexe': self.player_sexe})
    
    def remove_player(self):
        
        db = TinyDB('db.json')
        players_table = db.table('players')
        players_table.remove({'nom du ': self.player_name,'prenom': 
        self.player_first_name,'sexe': self.player_sexe})
    







 Load_data




SAUVEGARDE/CHARGEMENT DES DONNÉES
Nous devons pouvoir sauvegarder et charger l'état du programme à tout moment 
entre deux actions de l'utilisateur. À un moment donné, nous utiliserons 
probablement une base de données, mais pour l'instant, nous avons besoin de 
quelque chose de simple. Nous réfléchissons encore à la meilleure façon d'y 
parvenir de notre côté – Charlie, notre assistant informatique, vous tiendra 
au courant !

'''
