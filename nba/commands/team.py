import tabulate

from nba_api.stats.endpoints import teamplayerdashboard
from nba_api.stats.static import teams
from nba_api.stats.library.parameters import PerModeDetailed

from nba.commands.common import get_roster, ft_to_cm


def print_team(team_abbr):
    p = get_roster(team_abbr)
    p["HEIGHT_CM"] = p["HEIGHT"].apply(ft_to_cm)
    p["WEIGHT_KG"] = p["WEIGHT"].apply(lambda x: round(0.453_592 * int(x)))
    outp = p[["NUM", "PLAYER", "POSITION", "AGE", "HEIGHT", "WEIGHT_KG", "EXP"]]
    print(tabulate.tabulate(outp, headers="keys", showindex="never"))


def print_team_stats(team_abbr):
    tid = teams.find_team_by_abbreviation(team_abbr.lower())["id"]
    df = teamplayerdashboard.TeamPlayerDashboard(
        tid, per_mode_detailed=PerModeDetailed.per_game
    ).get_data_frames()[1]

    def splits(row):
        return "/".join(
            [str(round(row[field] * 100)) for field in ("FG_PCT", "FG3_PCT", "FT_PCT")]
        )

    df["SCORING"] = df.apply(lambda row: splits(row), axis=1)
    outdf = df[
        [
            "PLAYER_NAME",
            "GP",
            "MIN",
            "SCORING",
            "PTS",
            "REB",
            "AST",
            "TOV",
            "STL",
            "BLK",
        ]
    ]

    print(
        tabulate.tabulate(
            outdf.sort_values("MIN", ascending=False),
            headers="keys",
            showindex="never",
            floatfmt=".1f",
        )
    )
