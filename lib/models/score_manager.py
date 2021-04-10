import json
import os
from .score import Score

class ScoreManager():
    def __init__(self, filename='scores.json', file_location=''):
        self._scores = []
        self._filename = filename

        file_location = f'{file_location}/' if file_location != '' else ''
        if not os.path.exists(f'{file_location}{filename}'):
            return None


        with open(f'{file_location}{filename}', 'r') as f:
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

    def add_score_dict(self, score: dict):
        """ Adds a score dict to the scores """
        new_score = Score()
        new_score.name = score['name']
        new_score.km = score['km']
        new_score.kills = score['kills']
        new_score.kill_score = score['kill_score']
        self._scores.append(new_score)
    
    def add_score(self, score: object):
        """ Adds a score instance and adds it to the list of scores """
        self._scores.append(score)
    
    def save(self, directory=''):
        """ Serializes list scores and saves to a JSON file """
        # Checks if directory is empty
        directory = f'{directory}/' if directory != '' else ''

        with open(f'{directory}{self._filename}', 'w') as f:
            to_json = sorted([score.json for score in self._scores], 
            key=lambda score: score['total'], reverse=True)

            json.dump(to_json, f, indent=2)
    
    @property
    def scores(self):
        """ List of all score objects """
        return self._scores.sort(key=self.sort)
    
    def print(self):
        print(self._scores)