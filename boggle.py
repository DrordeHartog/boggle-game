from typing import Callable
from boggle_gui import *
from boggle_model import *
from boggle_gui import *

BOARD_SIZE = 4

# receive text and create dict of words

class Boggle:
    def __init__(self) -> None:
        self._game = Game()
        self._gui = GUI(self._game.board.get_board())
        for location in self._gui.get_square_locations():
            action = self.create_square_functionality(location)
            self._gui.set_square_command(location, action)

    def create_square_functionality(self, location):
        def update_gui() -> None:
            update_type = self._game.board.update_path(location)
            if update_type == PATH_UPDATED:
                self._gui.press_square(location)
            elif update_type == WORD_FOUND:
                self._gui.add_found_word(self._gui.get_get_display_label())
                self._gui.update_display_label('Found a word!')
                self._gui.set_score(self._game.score)
                self._gui.reset_path_gui()
                self._gui.reset_display_label()
            elif update_type == NOT_A_WORD:
                self._gui.update_display_label('Not a Word')
                self._gui.reset_path_gui()
            elif update_type == PATH_UPDATED:
                self._gui.press_square(self._game.board.get_current_path()[-1])

        return update_gui

    def run(self) -> None:
        self._gui.run()

if __name__ == "__main__":
    boggle = Boggle()
    boggle.run()

