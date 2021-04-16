from http import HTTPStatus

from flask import current_app
from flask_restx import Resource, marshal

from ..model.mutant_model import MutantModel

api = MutantModel.api


@api.route("/mutant")
@api.response(int(HTTPStatus.UNAUTHORIZED), "Unauthorized.")
class UploadFile(Resource):
    def post(self):
        """
        Mutant service
        """

        message = "hello mutant"
        return message
