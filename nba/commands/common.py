import operator
from nba_api.stats.endpoints import commonteamroster
from nba_api.stats.static import teams


def ft_to_cm(ft):
    return round(2.54 * sum(map(operator.mul, map(int, ft.split("-")), [12, 1])))


def get_roster(team_abbr):
    roster = commonteamroster.CommonTeamRoster(
        teams.find_team_by_abbreviation(team_abbr.lower())["id"]
    )
    return roster.get_data_frames()[0]
