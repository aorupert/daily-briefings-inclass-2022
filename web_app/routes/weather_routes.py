from flask import Blueprint, request, jsonify

from app.weather_service import get_hourly_forecasts

weather_routes = Blueprint("weather_routes", __name__)


@weather_routes.route("/api/weather/forecast.json")
#this is the path for which the following function should apply
def weather_forecast_api():
    print("WEATHER FORECAST (API)...")
    print("URL PARAMS:", dict(request.args))

    country_code = request.args.get("country_code") or "US"
    #country_code = request.args["country_code"] or "US" #may not always work
    zip_code = request.args.get("zip_code") or "20057"

    results = get_hourly_forecasts(country_code=country_code, zip_code=zip_code)
    if results:
        return jsonify(results)
    else:
        return jsonify({"message":"Invalid Geography. Please try again."}), 404