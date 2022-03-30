from http import HTTPStatus
from flask import jsonify, request
from app.models.series_models import Series

series_columns = ["id", "serie", "seasons", "released_date", "genre", "imdb_rating"]

def getSeries():
    try:
        Series.createTableModels()
        data = Series.getSeries()
        return jsonify({"data": [dict(zip(series_columns, serie)) for serie in data]}), HTTPStatus.OK
    except:
        return {"error": "Error"}, HTTPStatus.NOT_FOUND

def getSeriesById(serie_id):
    try:
        Series.createTableModels()
        data = Series.getByIdSeries(serie_id)
        return {"data": dict(zip(series_columns, data))}, HTTPStatus.OK
    except:
        return {"error": "Error"}, HTTPStatus.NOT_FOUND

def create():
    try:
        Series.createTableModels()
        payload = request.get_json()
        payload = Series(**payload)
        serie = Series.createSeries(payload)
        print(serie)
        return {"data": dict(zip(series_columns, serie))}, HTTPStatus.CREATED
    except:
        return {"error": "Error"}, HTTPStatus.NOT_FOUND