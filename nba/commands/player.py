from datetime import datetime
import tabulate
from nba_api.stats.endpoints import commonplayerinfo, playercareerstats


def print_player_info(player_id):
    player_info = commonplayerinfo.CommonPlayerInfo(
        player_id=player_id
    ).get_data_frames()[0]

    for field, label in {
        "DISPLAY_FIRST_LAST": "Name",
        "HEIGHT": "Height",
        "WEIGHT": "Weight",
        "SEASON_EXP": "Experience",
        "POSITION": "Position",
    }.items():
        print(f"{label:>10}: {player_info[field].to_string(index=False)}")

    age = datetime.now() - datetime.fromisoformat(
        player_info["BIRTHDATE"].to_string(index=False)
    )
    print(f"{'Age':>10}: {round(age.days / 365, 1)}")
    print(
        "{:>10}: {} ({}, {})\n".format(
            "Draft",
            *(
                player_info[field].to_string(index=False)
                for field in ["DRAFT_YEAR", "DRAFT_ROUND", "DRAFT_NUMBER"]
            ),
        )
    )

    stats = playercareerstats.PlayerCareerStats(player_id, "PerGame").get_data_frames()[
        0
    ]
    outp = stats[
        [
            "SEASON_ID",
            "TEAM_ABBREVIATION",
            "PTS",
            "REB",
            "AST",
            "STL",
            "BLK",
            "TOV",
            "FG_PCT",
            "FG3_PCT",
            "FT_PCT",
            "GP",
            "MIN"
        ]
    ]
    print(
        tabulate.tabulate(
            outp,
            headers=[
                "SEASON",
                "TEAM",
                "PTS",
                "REB",
                "AST",
                "STL",
                "BLK",
                "TOV",
                "FG_PCT",
                "FG3_PCT",
                "FT_PCT",
                "GP",
                "MIN"
            ],
            showindex="never",
            floatfmt=(
                ".1f",
                ".1f",
                ".1f",
                ".1f",
                ".1f",
                ".1f",
                ".1f",
                ".1f",
                ".3f",
                ".3f",
                ".3f",
                ".1f",
                ".1f"
            ),
        )
    )

