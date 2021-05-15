import pandas as pd



def get_players_raw():
    df = pd.read_csv('NBA-Files/players.csv')
    return df

def get_teams_raw():
    df = pd.read_csv('NBA-Files/teams.csv')
    return df

def get_ranking_raw():
    df = pd.read_csv('NBA-Files/ranking.csv')
    return df

def get_games_raw():
    df = pd.read_csv('NBA-Files/games.csv')
    return df

def get_game_details_raw():
    df = pd.read_csv('NBA-Files/games_details.csv')
    return df