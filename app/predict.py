import functools

from flask import (
    Blueprint, request
)

bp = Blueprint('model', __name__, url_prefix='/model')

@bp.route('/predict', methods=(['GET']))
def predict():
    return "predicting"