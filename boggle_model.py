import time
import ex11_utils
from boggle_board_randomizer import *
from typing import List, Dict, Tuple, Iterable, Optional

WORD_FOUND = 1
NOT_A_WORD = 0
PATH_UPDATED = 2

SCORE_FACTOR = 2


class Board:
    def __init__(self):
        self._board = randomize_board(LETTERS)
        self._path: Dict[str: Tuple] = {}


    @staticmethod
    def check_in_board(coor: Tuple[int]) -> bool:
        '''check that tuple coordinates are in board'''
        return 0 <= coor[0] < BOARD_SIZE and 0 <= coor[1] < BOARD_SIZE

    def __len__(self):
        return len(self._board)

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
        # if in: add tuple of letter and coor ("letter": (x,y)) to dict
        # else return none
        if self.check_in_board(coor):
            letter = self.cell_content(coor)
            if len(self._path) == 0:
                self._path[letter] = coor
                return True
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
    def __init__(self) -> None:
        self.words_dict = self.create_words_dict()
        self.board = Board()
        self.legal_words = self.words_on_board(self.board.get_board(), self.words_dict)
        self.current_letters = list(self.board.get_current_path().keys())
        self.score: int = 0
        self.num_words_left = len(self.current_letters)
        self.found_words = []
        self.current_word = "".join(self.current_letters)  # necessary?
        self.start_time = None

    @staticmethod
    def create_words_dict():
        """

        :return:
        """
        with open('boggle_dict.txt', 'r') as f:
            words_list = {word.strip(): False for word in f}
        return words_list

    def words_on_board(self, board, words):
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
        result = dict()
        for key in paths:
            result[key] = False
        return result

    def update_timer(self) -> None:
        """
        a function that updates the timer
        :return:
        """
        if self.start_time is not None:
            elapsed_time = time.time() - self.start_time
            self.time_remaining = max(
                0, int(self.time_remaining - elapsed_time))

    def submit_word(self):
        if self.legal_words.get(self.current_word, default=False):
            # updating words dict that the word was found
            self.legal_words[self.current_word] = True
            # updating the score
            self.score += len(self.current_word) ** SCORE_FACTOR
            # adding the word to the list of found words
            self.found_words.append(self.current_word)
            # subtracting the number of words left
            self.num_words_left -= 1
            return True
        return False

    def update_game(self, coor) -> int:
        """
        a function that updates the score of the game, returns three values:
        0 - An unsuccesful word submission, board was reset
        1 - A sucessful word submission, board was reset
        2 - A succesful square click, path was updated
        if nothing happened returns None

        :return:
        """
        current_path = self.board.get_current_path()
        # check whether a coor in the path was retyped
        if coor in current_path.values():
            # submit the word
            if self.submit_word():
                self.board.reset_path()
                return WORD_FOUND
            # word was not found reset the path
            self.board.reset_path()
            return NOT_A_WORD
        # a new coor was typed
        elif self.board.update_path(coor):
            return PATH_UPDATED





