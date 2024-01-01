import berserk

with open('Projekty/lichess_API_token.txt', 'r') as file:
    api_token = file.read().strip()

# Authentication with Personal Token
session = berserk.TokenSession(api_token)
client = berserk.Client(session=session)
