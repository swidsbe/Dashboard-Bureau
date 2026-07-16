import requests

from config.settings import LATITUDE, LONGITUDE

API_URL = "https://api.open-meteo.com/v1/forecast"


def fetch_weather():
    """Récupère la météo actuelle via l'API Open-Meteo (gratuite, sans clé).
    Retourne un dictionnaire avec température, ressenti et code météo,
    ou None en cas d'erreur réseau."""
    params = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "current": "temperature_2m,apparent_temperature,weather_code,is_day",
        "timezone": "auto",
    }
    try:
        response = requests.get(API_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        current = data.get("current", {})
        return {
            "temperature": current.get("temperature_2m"),
            "feels_like": current.get("apparent_temperature"),
            "weather_code": current.get("weather_code"),
            "is_day": current.get("is_day", 1),
        }
    except requests.RequestException:
        return None
