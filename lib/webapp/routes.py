from flask import render_template, Blueprint, request, jsonify
from ..models.score_manager import ScoreManager

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    """ Renders the main website page """
    manager = ScoreManager()
    return jsonify([s.json for s in manager._scores])