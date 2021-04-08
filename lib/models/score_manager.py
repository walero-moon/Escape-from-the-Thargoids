import json
import os
from .score import Score

class ScoreManager():
    def __init__(self, filename='scores.json'):
        self._scores = []
        self._filename = filename

        if not os.path.exists(filename):
            return None

        with open(filename, 'r') as f:
            json_data = json.load(f)

            for score in json_data:
                to_append = Score()
                to_append.name = score['name']
                to_append.km = score['km']
                to_append.kills = score['kills']
                to_append.kill_score = score['kill_score']

                self._scores.append(to_append)

    def get_score_by_name(self, score_name: str) -> object:
        """ Returns a score instance based on its name """
        for score in self._scores:
            if score.name == score_name:
                return score
        return None
    
    def add_score(self, score: object):
        """ Creates a score instance and adds it to the list of scores """
        self._scores.append(score)
    
    def save(self):
        """ Serializes list scores and saves to a JSON file """
        with open(self._filename, 'w') as f:
            json.dump([score.json for score in self._scores], f)
    
    @property
    def scores(self):
        """ List of all score objects """
        return self._scores