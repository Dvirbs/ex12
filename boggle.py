import tkinter as tki
from typing import Callable, Dict, List, Any
import boggle_board_randomizer

BUTTON_HOVER_COLOR = 'gray'
REGULAR_COLOR = 'lightgray'
BUTTON_ACTIVE_COLOR = 'slateblue'

BUTTON_STYLE = {"font": ("Courier", 30),
                "borderwidth": 1,
                "relief": tki.RAISED,
                "bg": REGULAR_COLOR,
                "activebackground": BUTTON_ACTIVE_COLOR}
board = boggle_board_randomizer.randomize_board()


class BoggleGUI:
    _buttons: Dict[str, tki.Button] = {}

    def __init__(self) -> None:
        root = tki.Tk()
        root.title('boggle')
        root.resizable(False, False)  # nobody can change the height and length
        self._main_window = root

        self._outer_frame = tki.Frame(root, bg=REGULAR_COLOR,
                                      highlightbackground=REGULAR_COLOR,
                                      highlightthickness=5)
        self._outer_frame.pack(side=tki.TOP, fill=tki.BOTH, expand=True)

        self._display_label = tki.Label(self._outer_frame, font=("Courier", 30),
                                        bg=REGULAR_COLOR, width=23, relief="ridge")
        self._display_label.pack(side=tki.TOP, fill=tki.BOTH)

        self._lower_frame = tki.Frame(self._outer_frame)
        self._lower_frame.pack(side=tki.TOP, fill=tki.BOTH, expand=True)

        self._create_buttons_in_lower_frame()
        self._main_window.bind("<Key>", self._key_pressed)

    def run(self) -> None:
        self._main_window.mainloop()

    def set_display(self, display_text: str) -> None:
        self._display_label["text"] = display_text

    def set_button_commend(self, button_name: str, cmd) -> None:
        pass

    def get_button_chars(self) -> List[str]:
        pass

    def _board_list(self):
        L = []
        for row in board:
            for col in row:
                L.append(col)
        return L

    def _create_buttons_in_lower_frame(self) -> None:

        for i in range(4):
            tki.Grid.columnconfigure(self._lower_frame, i, weight=1)  # type: ignore

        for i in range(4):
            tki.Grid.rowconfigure(self._lower_frame, i, weight=1)  # type: ignore

        board_list = self._board_list()
        self._make_button(board_list[0], 0, 0)
        self._make_button(board_list[1], 0, 1)
        self._make_button(board_list[2], 0, 2)
        self._make_button(board_list[3], 0, 3)
        self._make_button(board_list[4], 1, 0)
        self._make_button(board_list[5], 1, 1)
        self._make_button(board_list[6], 1, 2)
        self._make_button(board_list[7], 1, 3)
        self._make_button(board_list[8], 2, 0)
        self._make_button(board_list[9], 2, 1)
        self._make_button(board_list[10], 2, 2)
        self._make_button(board_list[11], 2, 3)
        self._make_button(board_list[12], 3, 0)
        self._make_button(board_list[11], 3, 1)
        self._make_button(board_list[13], 3, 2)
        self._make_button(board_list[14], 3, 3)

    def _make_button(self, button_char: str, row: int, col: int,
                     rowspan: int = 1, columnspan: int = 1):
        button = tki.Button(self._lower_frame, text=button_char, **BUTTON_STYLE)
        button.grid(row=row, column=col, rowspan=rowspan, columnspan=columnspan, sticky=tki.NSEW)
        self._buttons[button_char] = button

        def _on_enter(event: Any) -> None:
            button['background'] = BUTTON_HOVER_COLOR

        def _on_leave(event: Any) -> None:
            button['background'] = REGULAR_COLOR

        button.bind("<Enter>", _on_enter)
        button.bind("<Leave>", _on_leave)
        return button

    def _key_pressed(self, event: Any) -> None:
        """the callback method for when a key is pressed.
        It'll simulate a button press on the right button."""
        if event.char in self._buttons:
            self._simulate_button_press(event.char)
        elif event.keysym == "Return":
            self._simulate_button_press("=")

    def _simulate_button_press(self, button_char: str) -> None:
        """make a button light up as if it is pressed,
        and then return to normal"""
        button = self._buttons[button_char]
        button["bg"] = BUTTON_ACTIVE_COLOR


if __name__ == "__main__":
    cg = BoggleGUI()
    cg.set_display("TEST MODE")
    cg.run()
