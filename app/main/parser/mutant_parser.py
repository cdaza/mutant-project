from flask_restx import reqparse, fields
import werkzeug

mutant_parser = reqparse.RequestParser(bundle_errors=True)
mutant_parser.add_argument('dna',
                           location='json',
                           type=list,
                           required=True,
                           help='DNA')
