import berserk
import time
import pandas as pd

with open('../Lichess_API_token.txt', 'r') as file:
    api_token = file.read().strip()

# Authentication with Personal Token
session = berserk.TokenSession(api_token)
client = berserk.Client(session=session)

def top_200_players(prefType):
    best_players = client.users.get_leaderboard(prefType, count=200)
    best_players = pd.DataFrame(best_players)
    best_players_names = best_players['username']
    return best_players_names
  
# Top 200 Ultra-Bullet players
best_ultrabullet_players_names = top_200_players("ultraBullet")

# Top 200 Bullet players
best_bullet_players_names = top_200_players("bullet")

# Top 200 Blitz players
best_blitz_players_names = top_200_players("blitz")

# Top 200 Rapid players
best_rapid_players_names = top_200_players("rapid")

# Top 200 Classic players
best_classical_players_names = top_200_players("classical")



def get_games_for_players(player_series, pref_type, game_count=20):
    all_games = pd.DataFrame()
    batch_size = 10  # Ilość graczy do pobrania na raz
    player_list = player_series.tolist()  # Konwersja Series na listę
    for i in range(0, len(player_list), batch_size):
        batch_players = player_list[i:i + batch_size]
        for name in batch_players:
            success = False
            while not success:
                try:
                    games = client.games.export_by_player(username=name, as_pgn=False,rated=True, max=game_count, perf_type=pref_type, moves=True, pgn_in_json=True, tags=True, clocks=True, evals=True, opening=True, finished=True, literate=True)
                    if games:  # Upewnienie się, że istnieją gry dla danego gracza
                        games_df = pd.DataFrame(games)
                        all_games = pd.concat([all_games, games_df], ignore_index=True)
                    success = True
                except:
                    print(f"Rate limit reached. Waiting for 70 seconds before retrying!")
                    time.sleep(70)
    return all_games


blitz_games = get_games_for_players(best_blitz_players_names, "blitz")
rapid_games = get_games_for_players(best_rapid_players_names, "rapid")
bullet_games = get_games_for_players(best_bullet_players_names, "bullet")
ultrabullet_games = get_games_for_players(best_ultrabullet_players_names, "ultraBullet")
classical_games = get_games_for_players(best_classical_players_names, "classical")

all_games_frames = [blitz_games, rapid_games, bullet_games, ultrabullet_games, classical_games]
all_games = pd.concat(all_games_frames, ignore_index=True)

selected_columns = ['id', 'rated', 'variant', 'speed', 'perf', 'status', 'players', 'winner', 'opening', 'moves', 'pgn', 'analysis', 'createdAt', 'lastMoveAt']
subset_data = all_games.loc[:, selected_columns]
subset_data.to_json('games_data.json', orient='records')