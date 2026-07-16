import streamlit as st
from pathlib import Path

from components.clock import render_clock


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

render_clock()
