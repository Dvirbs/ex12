from typing import *
from ex12_utils import is_valid_path
from ex12_utils import path_find_word
import boggle_board_randomizer
from boggle import BoggleGUI


def load_words(txt):
    with open(txt) as f:
        lines = f.readlines()
        return lines


class Game:
    def __init__(self, board):
        self.__path: List[Tuple] = []
        self.__board = board
        self.__score = 0
        self.__current_display: str = ''
        self.__words = load_words('boggle_dict.txt')  # TODO the boggle controll/game shoud update this field every turn

    def set_game(self):
        self.__current_display = ''
        self.__path = []

    def get_display(self):
        return self.__current_display

    def get_board(self):
        return self.__board

    def add_word(self):
        possible_word = path_find_word(self.__board, self.get_path())
        word = is_valid_path(self.__board, self.__path, self.__words)
        if word:
            self.update_score()
            # TODO build function that update the score in the gui
        print(self.__path)
        self.set_new_path()
        self.__current_display = ''
        return word, possible_word



    def set_new_path(self):
        self.__path = []

    def get_path(self):
        return self.__path

    def update_score(self):
        self.__score += len(self.__path) ** 2

    def update_path(self, cell):
        self.__path.append(cell)

    def is_clicked_possible(self, clicked):
        if len(self.__path) == 0:
            return True
        l_row, l_col = self.__path[-1]
        c_row, c_col = clicked
        if l_row == c_row and l_col == c_col:
            return False
        if 0 <= abs(l_row - c_row) <= 1 and 0 <= abs(l_col - c_col) <= 1:
            return True

    def bottom_clicked(self, cell_location):
        # TODO connect the latter location in the gui to the function
        if self.is_clicked_possible(cell_location):
            self.update_path(cell_location)
            y, x = cell_location
            self.__current_display += self.__board[y][x]

        return self.__current_display


