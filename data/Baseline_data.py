import sys
import os
# This tells Python to look one folder up (the root)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import draft_data
from models.Baseline import team1, team2
season = draft_data.get_current_season()
print(season)
print(f"{team1} vs {team2} in the {season} season")