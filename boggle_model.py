from ex11_utils import *
from boggle_board_randomizer import randomize_board

BOARD_SIZE = 4


class Board:
    def __init__(self, legal_words: dict):
        self.board = randomize_board(BOARD_SIZE)

        self.words_dict = {}
        self.path: dict = {}
    # maybe we wont do this function!

    def find_all_words(self) -> dict:
        '''find all possible words on the board, return dict where keys are words and
        values are false (will be refrenced as found or not)'''

    def check_in_board(self, coor: tuple) -> bool:
        '''check that tuple coordinates are in board'''

    def cell_content(self, coor: tuple) -> bool:
        '''returns cell content as string'''

        ...

    def check_adj(self, tuple) -> bool:
        '''checks that coordinates are adjascent to the last value in path'''
        ...

    def ceate_path(self, coor: tuple) -> str:
        '''recieves coordinates, adds to current path and returns letter'''
        # if coor in self.path reset path
        # if in: add tuple of letter and coor ("letter": (x,y)) to dict
        # else return none
        ...

    def reset_path(self) -> None:
        '''resets self.path to empty dict '''
        ...

    def check_path_is_word() -> bool:
        '''checks if the current path is in words dict '''


class game:
    def __init__(self) -> None:
        board = Board()
        score = 0


# receieve tuple (x,y)
# return letter
#
