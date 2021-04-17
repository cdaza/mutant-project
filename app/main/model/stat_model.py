from flask_restx import Namespace


class StatsModel:
    api = Namespace('Stats', description="Get stats")
