from http import HTTPStatus

from flask import current_app
from flask_restx import Resource, marshal

from ..model.mutant_model import MutantModel
from ..parser.mutant_parser import mutant_parser

api = MutantModel.api


@api.route("/mutant")
@api.response(int(HTTPStatus.UNAUTHORIZED), "Unauthorized.")
class UploadFile(Resource):
    @api.expect(mutant_parser)
    def post(self):
        """
        Endpoint para validar secuencias de ADN
        """

        message = "hello mutant"
        return message
