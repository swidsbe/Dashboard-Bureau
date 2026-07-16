import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
from streamlit_autorefresh import st_autorefresh

from services.weather_service import fetch_weather
from components.clock import clock_card_html
from components.weather import weather_card_html
from config.settings import WEATHER_REFRESH_MINUTES


st.set_page_config(
    page_title="Dashboard Bureau",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def load_css(path: str):
    css_path = Path(path)
    if css_path.exists():
        st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)


load_css("assets/css/style.css")

# Recharge l'application toutes les WEATHER_REFRESH_MINUTES pour
# rafraîchir la météo.
st_autorefresh(interval=WEATHER_REFRESH_MINUTES * 60 * 1000, key="weather_autorefresh")

weather_data = fetch_weather()

page_html = f"""
<html>
<head>
<style>
:root {{
    --sage: #8A9A82;
    --anthracite: #2E2E2E;
    --offwhite: #F5F1EA;
    --wood: #A9784C;
}}

html, body {{
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    background-color: var(--offwhite);
    font-family: 'Helvetica Neue', Arial, sans-serif;
}}

.db-wrapper {{
    width: 100vw;
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 5vh;
}}

.db-card {{
    background-color: #FFFFFF;
    border-radius: 40px;
    border: 2px solid var(--sage);
    box-shadow: 0 8px 30px rgba(46, 46, 46, 0.08);
    width: 85%;
    max-width: 900px;
    padding: 40px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}}

.db-time {{
    font-size: 8vw;
    font-weight: 700;
    color: var(--anthracite);
    letter-spacing: 2px;
}}

.db-date {{
    margin-top: 15px;
    font-size: 2vw;
    font-weight: 400;
    color: var(--anthracite);
    text-transform: capitalize;
}}

.db-accent {{
    width: 80px;
    height: 4px;
    background-color: var(--wood);
    border-radius: 2px;
    margin-top: 20px;
}}

.db-weather-location {{
    font-size: 1.6vw;
    color: var(--anthracite);
    opacity: 0.7;
    text-transform: uppercase;
    letter-spacing: 2px;
}}

.db-weather-main {{
    display: flex;
    align-items: center;
    gap: 20px;
    margin-top: 10px;
}}

.db-weather-icon {{
    font-size: 6vw;
}}

.db-weather-temp {{
    font-size: 6vw;
    font-weight: 700;
    color: var(--anthracite);
}}

.db-weather-detail {{
    margin-top: 10px;
    font-size: 1.6vw;
    color: var(--anthracite);
}}

.db-weather-error {{
    font-size: 2vw;
    color: var(--anthracite);
}}
</style>
</head>
<body>
    <div class="db-wrapper">
        {clock_card_html()}
        {weather_card_html(weather_data)}
    </div>
</body>
</html>
"""

components.html(page_html, height=1200, scrolling=False)
