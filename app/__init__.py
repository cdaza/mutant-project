from flask import Blueprint
from flask_restx import Api

from .main.controller.mutant_controller import api as mutant_ctrl

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Mutant detect API',
          version='0.1',
          description='Mutant detect API. Is an API to identify DNA mutations'
          )

api.add_namespace(mutant_ctrl, path='/api/v1')
