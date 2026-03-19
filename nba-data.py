from nba_api.stats.endpoints import teaminfocommon
from nba_api.stats.static import teams
import time

# Get the lsit of teamn names and team ids to identify team in the API

team_id = teams.get_teams()
for i in team_id:
    s = ""
    s = f"{i['full_name']} - {str(i['id'])}\n"
    print(s)
    time.sleep(1)
# Get the 
#input_team = input("Enter the team id: ")
#team_id = int(input_team)
team_inf = teaminfocommon.TeamInfoCommon(
    team_id = 1610612766
)

print(team_inf)