players = [
    {"name": "Player1", "kills": 45, "deaths": 15},
    {"name": "Player2", "kills": 20, "deaths": 25},
    {"name": "Player3", "kills": 50, "deaths": 20},
    {"name": "Player4", "kills": 10, "deaths": 10}
]

sorted_players = sorted(players, key=lambda x: x["kills"] / x["deaths"], reverse=True)
for player in sorted_players:
    print(f"{player['name']} K/D: {player['kills'] / player['deaths']:.2f}")