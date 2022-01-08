import boggle_board_randomizer
from boggle import BoggleGUI
from game import Game


class BoggleControl:
    def __init__(self):
        self.board = boggle_board_randomizer.randomize_board()
        self._game = Game(self.board)
        self.gui = BoggleGUI(self.board)

        for button in self.gui.get_button_chars():
            self.gui.set_button_commend(button, self.create_button_action(button))
        self.gui.set_display('')

    def create_button_action(self, button):
        button_text = self.gui.get_text(button)
        if button_text == 'ADD_WORD':
            def add_word_func():
                correct_word, wrong_word = self._game.add_word()
                if correct_word:
                    self.gui.set_taken_word_list(correct_word)
                else:
                    self.gui.set_wrong_word_list(wrong_word)
                self.gui.set_display('')
            return add_word_func

        def letter_func():
            cell = self.gui.get_button_location(button)
            display = self._game.bottom_clicked(cell)
            self.gui.set_display(display)
        return letter_func

    def run(self):
        self.gui.run()


if __name__ == '__main__':
    BoggleControl().run()
