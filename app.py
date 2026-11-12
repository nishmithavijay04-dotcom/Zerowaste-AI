"""ZeroWaste Kitchen - run with:  streamlit run app.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import streamlit as st

st.set_page_config(page_title="ZeroWaste Kitchen", page_icon="🌿", layout="wide", initial_sidebar_state="expanded")

from ui import theme, ctx, shell
from views import dashboard, waste_log, forecast_risk, planner, redistribute, partners, settings

if not os.environ.get("ZW_NO_CSS"): theme.inject()
st.session_state["_card_n"] = 0
ctx.init()
ctx.persist_widget_state()
st.logo("static/logo.svg", icon_image="static/logo_icon.svg", size="large")

P = st.Page
ctx.PAGES.update({
    "dashboard": P(dashboard.render, title="Dashboard", icon=":material/dashboard:", url_path="dashboard", default=True),
    "waste_log": P(waste_log.render, title="Waste Log", icon=":material/receipt_long:", url_path="waste-log"),
    "forecast": P(forecast_risk.render, title="Forecast & Risk", icon=":material/monitoring:", url_path="forecast"),
    "planner": P(planner.render, title="Menu Planner", icon=":material/restaurant_menu:", url_path="planner"),
    "redistribute": P(redistribute.render, title="Redistribution", icon=":material/volunteer_activism:", url_path="redistribution"),
    "partners": P(partners.render, title="Partners", icon=":material/location_on:", url_path="partners"),
    "settings": P(settings.render, title="Settings & Data", icon=":material/settings:", url_path="settings"),
})
nav = st.navigation({
    "OVERVIEW": [ctx.PAGES["dashboard"], ctx.PAGES["waste_log"], ctx.PAGES["forecast"]],
    "OPERATIONS": [ctx.PAGES["planner"], ctx.PAGES["redistribute"], ctx.PAGES["partners"]],
    "SYSTEM": [ctx.PAGES["settings"]],
})
shell.sidebar_extras()
if st.session_state.get("_toast"):
    st.toast(st.session_state.pop("_toast"), icon="✅")
nav.run()
