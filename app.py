import streamlit as st
import pandas as pd
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder

st.set_page_config(page_title="NBA Predictions - Listagem", layout="wide")

st.title("🏀 NBA Data Explorer")
st.markdown("Carregando dados diretamente da API oficial da NBA.")

# Função para carregar times (cache para não sobrecarregar a API)
@st.cache_data
def get_nba_teams():
    nba_teams = teams.get_teams()
    return pd.DataFrame(nba_teams)

# Sidebar para filtros
st.sidebar.header("Filtros")
data_type = st.sidebar.selectbox("O que deseja visualizar?", ["Times", "Últimos Jogos"])

if data_type == "Times":
    df_teams = get_nba_teams()
    st.subheader("Listagem de Times")
    st.dataframe(df_teams, use_container_width=True)

elif data_type == "Últimos Jogos":
    st.subheader("Últimos 10 Jogos da Liga")
    # Busca jogos recentes da liga
    gamefinder = leaguegamefinder.LeagueGameFinder(league_id_nullable='00')
    games = gamefinder.get_data_frames()[0]
    st.table(games.head(10)[['TEAM_NAME', 'GAME_DATE', 'MATCHUP', 'WL', 'PTS']])

st.info("Dica: Use os filtros na lateral para navegar entre os dados.")