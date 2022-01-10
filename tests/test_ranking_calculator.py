import os
import subprocess
from string import ascii_lowercase
from random import choice
from unittest import TestCase
from ranking_calculator.ranking_calculator import get_ranking


DEMO_SCORES = """Grouches 4, FC Awesome 2
FC Awesome 1, Snakes 0
Grouches 2, Snakes 2
Snakes 2, Lions 4
FC Awesome 2, Lions 1
FC Awesome 4, Grouches 3
Snakes 4, Grouches 0
Grouches 0, FC Awesome 0
Tarantulas 0, Lions 2
Lions 0, FC Awesome 2
Lions 4, Snakes 2
Grouches 2, Lions 2
"""

DEMO_OUTPUT = {
    "FC Awesome": "13 pts",
    "Lions":     "10 pts",
    "Grouches":  "6 pts",
    "Snakes":    "4 pts",
    "Tarantulas":"0 pts",
}


class TestRankingCalculator(TestCase):
    """
    Test the Ranking Calculator
    """

    def setUp(self) -> None:
        """
        Setup a temporary file
        """
        self.filename = ''.join(choice(ascii_lowercase) for _ in range(10))
        with open(f"./files/{self.filename}", "w+") as file:
            file.write(DEMO_SCORES)

    def test_ranking(self) -> None:
        self.assertDictEqual(DEMO_OUTPUT, get_ranking(self.filename))

    def test_file_not_found(self):
        self.assertRaises(FileNotFoundError, get_ranking, "___")

    def test_filename_not_passed(self):
        result = subprocess.call(
            "python3 -m ranking_calculator",
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            shell=True
        )
        self.assertNotEqual(result, 0)

    def tearDown(self) -> None:
        """
        Delete the file
        """
        if os.path.exists(f"./files/{self.filename}"):
            os.remove(f"./files/{self.filename}")
