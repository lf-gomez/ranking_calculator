import fire
from .ranking_calculator import get_ranking


def main():
    fire.Fire(get_ranking)


if __name__ == "__main__":
    main()
