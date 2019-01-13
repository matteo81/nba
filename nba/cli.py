"""
Main CLI entry point
"""
import click
from . import __version__ as VERSION

from nba.commands.boxscore import print_boxscore
from nba.commands.team import print_team, print_team_stats
from nba.commands.player import print_player_info
from nba.commands.common import get_roster
from json.decoder import JSONDecodeError


@click.group()
@click.version_option(version=VERSION)
def cli():
    pass


@cli.command("boxscore", help='Show the latest boxscore of the specified team')
@click.argument("team_abbr")
def boxscore(team_abbr):
    print_boxscore(team_abbr)


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


def main():
    cli()
