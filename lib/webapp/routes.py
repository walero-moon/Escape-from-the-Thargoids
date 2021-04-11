import json
from flask import render_template, Blueprint, request, jsonify
from ..models.score_manager import ScoreManager
from ..models.score import Score

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    """ Displays a table with all scores """
    scores = {}

    try:
        with open('lib/webapp/server_scores.json', 'r') as f:
            scores = json.load(f)
    except FileNotFoundError:
        return render_template('index.html', file=False)
    
    return render_template('index.html', scores=scores, file=True)

@routes.route('/json')
def score_json():
    """ Sends the json representation of all scores """
    manager = ScoreManager()
    return jsonify([s.json for s in manager._scores])

@routes.route('/json', methods=['POST', 'PUT'])
def create_score():
    """ Creates a new score from JSON data """
    manager = ScoreManager(filename='server_scores.json', file_location='lib/webapp')
    data = request.get_json()
    manager.add_score_dict(data)
    manager.save('lib/webapp')

    return 'Added to database', 200