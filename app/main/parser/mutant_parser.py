from flask_restx import reqparse
import werkzeug

mutant_parser = reqparse.RequestParser()
mutant_parser.add_argument('dna',
                           action='split',
                           type=list,
                           required=True,
                           help='Por favor envia una secuencia de ADN')
