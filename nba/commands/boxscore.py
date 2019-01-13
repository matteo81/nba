from nba_api.stats.endpoints import (
    boxscoretraditionalv2,
    teamgamelog,
)
from nba_api.stats.static import teams
import tabulate


def print_boxscore(team_abbr):
    game_id = (
        teamgamelog.TeamGameLog(
            teams.find_team_by_abbreviation(team_abbr.lower())["id"]
        )
        .get_data_frames()[0]
        .iloc[0]
        .Game_ID
    )

    b = (
        boxscoretraditionalv2.BoxScoreTraditionalV2(game_id)
        .get_data_frames()[0]
        .dropna()
    )
    b["PLAYER"] = b["PLAYER_NAME"].apply(
        lambda s: s.ljust(b.PLAYER_NAME.str.len().max(), " ")
    )
    b.MIN = b.MIN.str.rjust(5, "0")
    for field in ["FGM", "FGA", "FG3M", "FG3A", "FTM", "FTA"]:
        b[field] = b[field].fillna(0).astype(int)

    b["FG"] = (b["FGM"].map(str) + "-" + b["FGA"].map(str)).str.pad(5)
    b["FG3"] = (b["FG3M"].map(str) + "-" + b["FG3A"].map(str)).str.pad(5)
    b["FT"] = (b["FTM"].map(str) + "-" + b["FTA"].map(str)).str.pad(5)

    for team_name, bscore in b.groupby("TEAM_ABBREVIATION"):
        print(team_name)

        tabulate.PRESERVE_WHITESPACE = True
        outb = bscore[
            ["PLAYER", "MIN", "FG", "FG3", "FT", "REB", "AST", "STL", "BLK", "TO", "PF", "PTS"]
        ]
        print(tabulate.tabulate(outb, headers="keys", showindex="never"))
        tabulate.PRESERVE_WHITESPACE = False



