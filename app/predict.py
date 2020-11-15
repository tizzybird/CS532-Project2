import functools
from .model import classifier

from flask import (
    Blueprint, request
)

bp = Blueprint('model', __name__, url_prefix='/model')


@bp.route('/predict', methods=(['GET']))
def predict():
    output = classifier.classify("dog.jpg")
    print("output", output)
    return str(output)
