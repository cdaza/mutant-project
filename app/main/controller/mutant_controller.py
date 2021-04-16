from http import HTTPStatus

from flask import current_app
from flask import request
from flask_restx import Resource, fields

from ..model.mutant_model import MutantModel
from ..parser.mutant_parser import mutant_parser
from ..service.mutant_service import validate_sequence

api = MutantModel.api
dna = MutantModel.dna


@api.route("/mutant")
@api.response(int(HTTPStatus.UNAUTHORIZED), "Unauthorized.")
class UploadFile(Resource):
    @api.expect(dna)
    def post(self):
        """
        Endpoint to validate DNA sequences
        """

        args = mutant_parser.parse_args()
        list_dna = args['dna']
        is_mutant, message = validate_sequence(list_dna)
        if is_mutant:
            return message, 200
        return message, 403
