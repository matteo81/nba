#!/usr/bin/env python
from nba_api.stats.endpoints import (
    commonteamroster,
    commonplayerinfo,
    playercareerstats,
    boxscoretraditionalv2,
    teamgamelog,
    teamplayerdashboard,
)
from nba_api.stats.static import teams, players
from nba_api.stats.library.parameters import PerModeDetailed
from sys import exit
from datetime import datetime
from json.decoder import JSONDecodeError
import operator
import tabulate
import click


def ft_to_cm(ft):
    return round(2.54 * sum(map(operator.mul, map(int, ft.split("-")), [12, 1])))


@click.group()
def cli():
    pass


def get_roster(team_abbr):
    roster = commonteamroster.CommonTeamRoster(
        teams.find_team_by_abbreviation(team_abbr.lower())["id"]
    )
    return roster.get_data_frames()[0]


def get_players():
    pass


@cli.command("team", help="Show team details.")
@click.argument("team_abbr")
@click.option("--stats", "-s", is_flag=True, default=False, help="Show team stats")
def team(team_abbr, stats):
    try:
        if stats:
            print_team_stats(team_abbr)
        else:
            print_team(team_abbr)
    except TypeError:
        print("Team not found")
        exit(0)


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
            "MIN",
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
                "MIN",
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
            ),
        )
    )


@cli.command("player")
@click.argument("team_abbr")
@click.argument("number", required=False)
def get_player(team_abbr, number):
    if not number:
        try:
            return print_team(team_abbr)
        except TypeError:
            player = players.find_players_by_full_name(team_abbr)[0]
            return print_player_info(player["id"])

    try:
        p = get_roster(team_abbr)
        player = p[p.NUM == number]
        return print_player_info(player.PLAYER_ID)
    except JSONDecodeError:
        print("Player number not found!")


def print_boxscore(b):
    tabulate.PRESERVE_WHITESPACE = True
    outb = b[
        ["PLAYER", "MIN", "FG", "FG3", "FT", "REB", "AST", "STL", "BLK", "TO", "PF", "PTS"]
    ]
    print(tabulate.tabulate(outb, headers="keys", showindex="never"))
    tabulate.PRESERVE_WHITESPACE = False


@cli.command("boxscore")
@click.argument("team_abbr")
def boxscore(team_abbr):
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

    for team_name, dataframe in b.groupby("TEAM_ABBREVIATION"):
        print(team_name)
        print_boxscore(dataframe)


if __name__ == "__main__":
    cli()
