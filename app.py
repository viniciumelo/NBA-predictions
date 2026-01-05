import streamlit as st
import pandas as pd
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder

st.set_page_config(page_title="NBA Predictions - Listagem", layout="wide")

st.title("🏀 NBA Data Explorer")
st.markdown("Carregando dados diretamente da API oficial da NBA.")

