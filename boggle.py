import boggle_board_randomizer
import boggle_gui
import boggle_model
import ex11_utils

BOARD_SIZE = 4

# receive text and create dict of words


def create_words_dict() -> dict():
    """opens file of all legal words and copies to dict for game to validate against,, values will be False"""
    d = {}
    with open("boggle-game\boggle_dict.txt") as f:
        ...
    pass
