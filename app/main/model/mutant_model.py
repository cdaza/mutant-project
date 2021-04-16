from flask_restx import Namespace


class MutantModel:
    api = Namespace('Mutant Endpoint', description="Servicio para la deteccion de mutantes")
