#import pandas as pd
import os
from datetime import datetime
#league dash team stats endpoint to get team stats for the current season
from nba_api.stats.endpoints import leaguedashteamstats

# Get the current season in the format "YYYY-YY"
def get_current_season():
    year = datetime.today().year
    month = datetime.today().month
    if (month >= 10): #season starts in october
        start = year
        end = start + 1
    else:
        start = year - 1
        end = start + 1
    # Make end a string to use the last 2 digits
    return f"{start}-{str(end)[-2:]}" 

#NEVER FORGET THE IF __name__ == "__main__": STATEMENT, OTHERWISE THIS CODE WILL RUN EVERY TIME YOU IMPORT THIS FILE 
if __name__ == "__main__":
    # Get team points per game and points allowed per game
    # save it to a text file
    def get_team_stats(season):
        team_stats = leaguedashteamstats.LeagueDashTeamStats(
            season = season,
         per_mode_detailed='PerGame' # Get stats per game
        )
        team_data = team_stats.get_data_frames()[0]

        # logic to get ppg and pal
        ppg_leaderboard = team_data[['TEAM_ID','TEAM_NAME', 'PTS', 'PLUS_MINUS']]
        ppg_leaderboard = ppg_leaderboard.rename(columns={'PTS': 'PPG'})

        # pal = ppg - plus_minus
        ppg_leaderboard['PAL'] = round(ppg_leaderboard['PPG'] - ppg_leaderboard['PLUS_MINUS'],1)
        ppg_leaderboard = ppg_leaderboard.drop(columns=['PLUS_MINUS'])

        # textfile better format than csv for this data
        aligned_inf = ppg_leaderboard.to_string(index=False)
    
        # Going to save to 'Accessible_data' folder
        folder = 'Accessible_data'
        file_name = 'NBA_PPG_PAL.txt'
        file_path = os.path.join('data', folder, file_name)
        with open(file_path, 'w') as f:
            f.write(aligned_inf)
    
        # Going to save as a .csv as well
        folder = 'Accessible_data'
        file_name = 'NBA_PPG_PAL.csv'
        file_path = os.path.join('data', folder, file_name)
        ppg_leaderboard.to_csv(file_path, index=False)

        return aligned_inf
    #function calls
    season = get_current_season()
    team_data = get_team_stats(season)
    print(team_data)

    