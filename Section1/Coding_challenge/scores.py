"""_summary_

    Returns:
        A list of the top ten teams with the highest scores.
"""

team_scores = {
    'Team A': 90,
    'Team B': 67,
    'Team C': 45,
    'Team D': 81,
    'Team E': 28,
    'Team F': 53,
    'Team G': 76,
    'Team H': 96,
    'Team I': 38,
    'Team J': 15,
    'Team K': 59,
    'Team L': 72,
    'Team M': 86,
    'Team N': 10,
    'Team O': 61,
    'Team P': 99,
    'Team Q': 42,
    'Team R': 78,
    'Team S': 23,
    'Team T': 52
}


def get_value(team):
    return team_scores[team]

count = 1
for team in sorted(team_scores, key=get_value, reverse=True):
    if count < 11:
        print(f"{team}: {team_scores[team]}")
        count += 1
