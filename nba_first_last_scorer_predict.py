import pandas as pd
import numpy as np
from nba_api.stats.endpoints import leaguegamefinder, playbyplayv2
from nba_api.stats.static import teams

def get_team_id(team_abbreviation):
    nba_teams = teams.get_teams()
    return [t for t in nba_teams if t['abbreviation'] == team_abbreviation][0]['id']

def analyze_scoring_tendencies(team_id, num_games=20):
    # Busca os últimos jogos da equipe
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team_id)
    games = gamefinder.get_data_frames()[0]
    recent_games = games.head(num_games)
    
    first_point_count = 0
    last_point_count = 0
    
    for game_id in recent_games['GAME_ID']:
        pbp = playbyplayv2.PlayByPlayV2(game_id=game_id).get_data_frames()[0]
        
        # Filtra apenas jogadas que resultaram em pontuação (EVENTMSGTYPE 1 ou 3)
        scoring_plays = pbp[pbp['EVENTMSGTYPE'].isin([1, 3])].dropna(subset=['SCORE'])
        
        if not scoring_plays.empty:
            # Verifica primeiro ponto
            if str(team_id) in str(scoring_plays.iloc[0]['PLAYER1_TEAM_ID']):
                first_point_count += 1
            
            # Verifica último ponto
            if str(team_id) in str(scoring_plays.iloc[-1]['PLAYER1_TEAM_ID']):
                last_point_count += 1
                
    return {
        "prob_first": first_point_count / num_games,
        "prob_last": last_point_count / num_games
    }

def predict_matchup(team_a_abbr, team_b_abbr):
    id_a = get_team_id(team_a_abbr)
    id_b = get_team_id(team_b_abbr)
    
    print(f"Analisando tendências para {team_a_abbr} vs {team_b_abbr}...")
    stats_a = analyze_scoring_tendencies(id_a)
    stats_b = analyze_scoring_tendencies(id_b)
    
    # Predição Simples: Quem tem maior frequência histórica recente
    first_pred = team_a_abbr if stats_a['prob_first'] > stats_b['prob_first'] else team_b_abbr
    last_pred = team_a_abbr if stats_a['prob_last'] > stats_b['prob_last'] else team_b_abbr
    
    print("\n--- Resultado da Predição ---")
    print(f"Primeiro Ponto: {first_pred} (Freq: {max(stats_a['prob_first'], stats_b['prob_first']):.2%})")
    print(f"Último Ponto: {last_pred} (Freq: {max(stats_a['prob_last'], stats_b['prob_last']):.2%})")

