import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from logic_utils import check_guess


def test_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_win():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"