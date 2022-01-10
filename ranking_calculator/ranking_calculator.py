from typing import Dict


def get_team_points(score: str) -> Dict[str, int]:
    """ Gets the team's points based on a given score.

    Parameters
    ----------
    score : str
        containing the final score of the match

    Returns
    -------
    dict : containing the name of the team and the points obtained
    """

    t1, t2 = score.strip().split(", ")
    t1_name, t1_score = t1.rsplit(" ", 1)
    t2_name, t2_score = t2.rsplit(" ", 1)

    if t1_score == t2_score:
        t1_score = 1
        t2_score = 1
    elif t1_score > t2_score:
        t1_score = 3
        t2_score = 0
    else:
        t1_score = 0
        t2_score = 3

    return {
        t1_name: int(t1_score),
        t2_name: int(t2_score)
    }



def sort_ranking(ranking: Dict[str, int]) -> Dict[str, str]:
    """ Sorts a given ranking based on points and name.

    Parameters
    ----------
    ranking : dict[str, int]
        containing the teams with their respective points

    Returns
    -------
    dict[str, str] : with their elements sorted and their respective unit
    """

    ranking = dict(sorted(ranking.items(), key=lambda kv: (-kv[1], kv[0])))

    return {
        k: f"{v} pts" if v != 1 else f"{v} pt"
        for k, v in ranking.items()
    }


def get_ranking(filename: str) -> Dict[str, str]:
    """ Gets the ranking of a league from the scores file.

    Parameters
    ----------
    filename : str
        the name of the file to use

    Returns
    -------
    dict[str, str] : containing the points of each team

    """

    ranking = {}

    try:
        with open("./files/" + filename, "r") as scores:
            for score in scores:
                team_pts = get_team_points(score)
                ranking = {
                    k: team_pts.get(k, 0) + ranking.get(k, 0)
                    for k in set(team_pts) | set(ranking)
                }
    except FileNotFoundError:
        raise FileNotFoundError(f"File `{filename}` not found.")

    return sort_ranking(ranking)
