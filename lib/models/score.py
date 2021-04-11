class Score():
    """ Holds player scores """
    def __init__(self):
        self.name = ''
        self.km = 0
        self.kills = 0
        self.kill_score = 0

    @property
    def total(self) -> int:
        """ Returns the total score """
        return round(self.km + self.kills + self.kill_score)
    
    @property
    def json(self) -> dict:
        """ Returns a json serializable version of the class """
        return {
            'name': self.name,
            'km': self.km,
            'kills': self.kills,
            'kill_score': self.kill_score,
            'total': self.total
        }