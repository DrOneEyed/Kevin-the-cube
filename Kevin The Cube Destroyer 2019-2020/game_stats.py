class GameStats():
    def __init__(self,Invad_set):
        self.Invad_set = Invad_set
        self.reset_stats()
        self.game_active = False

        self.high_score= 1000000
        
    def reset_stats(self):
        self.ships_left = self.Invad_set.ship_limit
        self.score = 0
        self.level = 1
