from config.settings import LOCATION_NAME
from utils.weather_codes import get_weather_icon_and_label


def weather_card_html(weather):
    """Construit le HTML de la carte Météo à partir des données
    renvoyées par services/weather_service.py."""

    if weather is None or weather.get("temperature") is None:
        return """
        <div class="db-card db-weather-card">
            <div class="db-weather-error">Météo indisponible</div>
        </div>
        """

    icon, label = get_weather_icon_and_label(weather["weather_code"])
    temperature = weather["temperature"]
    feels_like = weather["feels_like"]

    return f"""
    <div class="db-card db-weather-card">
        <div class="db-weather-location">{LOCATION_NAME}</div>
        <div class="db-weather-main">
            <span class="db-weather-icon">{icon}</span>
            <span class="db-weather-temp">{temperature:.0f}°</span>
        </div>
        <div class="db-weather-detail">{label} — Ressenti {feels_like:.0f}°</div>
    </div>
    """
