from flask_restx import Namespace


class MutantModel:
    api = Namespace('Mutant endpoint', description="Mutant service")