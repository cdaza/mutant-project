from http import HTTPStatus

from flask_restx import Resource

from ..model.stat_model import StatsModel
from ..service.stats_service import get_stats

api = StatsModel.api


@api.route("/stats")
@api.response(int(HTTPStatus.UNAUTHORIZED), "Unauthorized.")
class Stats(Resource):
    def get(self):
        """
        Endpoint stats
        """

        return get_stats()
