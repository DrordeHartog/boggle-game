import time
from ex11_utils import *
from boggle_board_randomizer import *
from typing import List, Dict, Tuple, Iterable, Optional


class Board:
    def __init__(self, legal_words: dict):
        self.board = randomize_board(LETTERS)
        self.words_dict = legal_words
        self.path: Dict[str: Tuple] = {}

    # maybe we won't do this function!
    def find_all_words(self) -> dict:
        '''find all possible words on the board, return dict where keys are words and
        values are false (will be refrenced as found or not)'''
        pass

    def check_in_board(self, coor: Tuple[int]) -> bool:
        '''check that tuple coordinates are in board'''
        return 0 <= coor[0] < BOARD_SIZE and 0 <= coor[1] < BOARD_SIZE

    def cell_content(self, coor: tuple) -> str:
        '''returns cell content as string'''
        return self.board[coor[0]][coor[1]]

    def check_adj(self, coor) -> bool:
        '''checks that coordinates are adjascent to the last value in path'''
        previous_coor = list(self.path.values())[-1]
        return abs(previous_coor[0] - coor[0]) in [0, 1] and abs(previous_coor[1] - coor[1]) in [0, 1]

    def update_path(self, coor: tuple) -> True:
        '''recieves coordinates, adds to current path and returns True if the path was updated
            else returns false'''
        # if coor in self.path reset path
        # if in: add tuple of letter and coor ("letter": (x,y)) to dict
        # else return none
        if self.check_in_board(coor):
            letter = self.cell_content(coor)
            if len(self.path) == 0:
                self.path[letter] = coor
                return True
            elif len(self.path) > 0 and coor in self.path:
                self.reset_path()
                return False
            else:
                previous_coor = list(self.path.values())[-1]
                if self.check_adj(previous_coor):
                    self.path[letter] = coor
                    return True
                return False
        return False


    def reset_path(self) -> None:
        '''resets self.path to empty dict '''
        self.path = {}
        return

    def check_path_is_word(self) -> bool:
        '''checks if the current path is in words dict '''
        return self.path in find_length_n_words(len(self.path), self.board, self.words_dict)

class Game:
    def __init__(self, is_time_limit: bool = False, duration: int = None) -> None:
        self.board = Board()
        self.score: int = 0
        self.num_words_left = 0
        self.words_left = True
        self.start_time = None
        self.time_remaining = duration
        if duration:
            self.start_time = time.time()

    def create_words_list(self):
        with open('boggle.txt', 'r') as f:
            words_list = {word.strip(): False for word in f}
        return words_list

    def update_timer(self) -> None:
        """
        a function that updates the timer
        :return:
        """
        if self.start_time is not None:
            elapsed_time = time.time() - self.start_time
            self.time_remaining = max(0, int(self.time_remaining - elapsed_time))

    def update_score(self) -> bool:
        self.score += len(self.board.path)
        return len(self.board.path) > 0


