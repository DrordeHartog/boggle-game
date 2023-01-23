import time
import ex11_utils
from boggle_board_randomizer import *
from typing import List, Dict, Tuple, Iterable, Optional

PATH_UPDATED = 1
PATH_RESET = 2
PATH_NOT_UPDATED = 3

SCORE_FACTOR = 2


class Board:
    def __init__(self):
        self._board = randomize_board(LETTERS)
        self._path: Dict[str: Tuple] = {}

    # maybe we won't do this function!
    def find_all_words(self) -> dict:
        '''find all possible words on the board, return dict where keys are words and
        values are false (will be refrenced as found or not)'''

    @staticmethod
    def check_in_board(coor: Tuple[int]) -> bool:
        '''check that tuple coordinates are in board'''
        return 0 <= coor[0] < BOARD_SIZE and 0 <= coor[1] < BOARD_SIZE

    def cell_content(self, coor: tuple) -> str:
        '''returns cell content as string'''
        return self._board[coor[0]][coor[1]]

    def check_adj(self, coor) -> bool:
        '''checks that coordinates are adjacent to the last value in path'''
        previous_coor = list(self._path.values())[-1]
        return abs(previous_coor[0] - coor[0]) in [0, 1] and abs(previous_coor[1] - coor[1]) in [0, 1]

    def update_path(self, coor: tuple) -> bool:
        """ Recieve coordinates, adds to current path and returns True if the path was updated
            else returns false
        """
        # if coor in self.path reset path
        # if in: add tuple of letter and coor ("letter": (x,y)) to dict
        # else return none
        if self.check_in_board(coor):
            letter = self.cell_content(coor)
            if len(self._path) == 0:
                self._path[letter] = coor
                return True
            # move this functionality to game
            # elif len(self._path) > 0 and coor in self._path:
            #     self.reset_path()
            #     return False
            else:
                previous_coor = list(self._path.values())[-1]
                if self.check_adj(previous_coor):
                    self._path[letter] = coor
                    return True
                return False
        return False

    def get_current_path(self):
        return self._path

    def get_board(self):
        return self._board

    def reset_path(self) -> None:
        """Resets self.path to empty dict
        """
        self._path = {}

    # def check_path_is_word(self) -> bool:
    #     """
    #     checks if the current path is in words dict
    #     :return:
    #     """
    #     return self._path in find_length_n_words(len(self._path), self._board, self.words_dict)


class Game:
    def __init__(self, duration: int = None) -> None:
        self.words_dict = self.create_words_dict()
        self.board = Board()
        self.legal_words = self.words_on_board(self.board, self.words_dict)
        self.current_letters = list(self.board.get_current_path().keys())
        self.score: int = 0
        self.num_words_left = len(self.current_letters)
        self.found_words = []
        self.current_word = "".join(self.current_letters)  # necessary?
        self.start_time = None
        self.time_remaining = duration
        if duration:
            self.start_time = time.time()
        self.is_running = True

    @staticmethod
    def create_words_dict():
        """

        :return:
        """
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
            self.time_remaining = max(
                0, int(self.time_remaining - elapsed_time))

    def update_game(self) -> bool:
        """
        a function that updates the score of the game, if the score was updated returns True
        :return:
        """
        # checking if the path represents a valid word that was not found earlier
        if self.current_word and self.legal_words.get(self.current_word, default=False):
            # updating words dict that the word was found
            self.legal_words[self.current_word] = False
            # resetting the path
            self.board.reset_path()
            # updating the score
            self.score += len(self.current_word)**SCORE_FACTOR
            # adding the word to the list of found words
            self.found_words.append(self.current_word)
            # subtracting the number of words left
            self.num_words_left -= 1
            return True
        return False

    def words_on_board(self, board, words) -> set[str]:
        '''for a given board returns a set of all legal words that are on the board. 
        uses a recursive helper function from ex11_utils.'''
        paths = {}
        cur_path = []
        words = set(words)
        sub_string_set = ex11_utils.make_substring_set(words)
        # search from every square on board all paths of valid words
        # that begin from there using helper function
        for x in range(len(board)):
            for y in range(len(board)):
                ex11_utils._max_score_paths_helper(
                    board, words, sub_string_set, "", [], x, y, paths)
        result = set()
        for key in paths:
            result.add(key)
        return result
