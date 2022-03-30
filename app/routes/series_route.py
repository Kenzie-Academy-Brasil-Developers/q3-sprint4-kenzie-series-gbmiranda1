from app.controllers import controllers_series
from flask import Blueprint

bp_series = Blueprint("series", __name__, url_prefix="/series")


bp_series.post("")(controllers_series.create)
bp_series.get("")(controllers_series.getSeries)
bp_series.get("/<int:serie_id>")(controllers_series.getSeriesById)