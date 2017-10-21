import time
from termcolor import colored


class Race(object):
    """
        Represents a race with a text, speed, etc ...
    """

    final_text = ""
    actual_text = ""
    speed = None  # = len(final_text) / time
    wrongs = None
    start_time = None
    end_time = None
    full_time = None

    def __init__(self, text):
        self.final_text = text
        self.start_time = time.time()

    # Colores the typed text in red and the rest in black
    def color_typed_text(self):
        tmp = self.final_text.split(self.actual_text)
        print("tmp0", tmp[0])
        print("tmp1", tmp[1])
        return colored(self.actual_text, "red") + tmp[1]

    def check_if_win(self):
        if self.actual_text == self.final_text:
            self.end_time = time.time()
            self.full_time = self.end_time - self.start_time
            self.speed = len(self.final_text) / self.full_time
