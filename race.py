import time
from termcolor import colored


class Race(object):
    """
        Represents a race with a text, speed, etc ...
    """
    actual_text = ""
    wrongs = 0
    start_time = None

    def __init__(self, text):
        self.final_text = text



    def check_if_win(self):
        if self.actual_text == self.final_text:
            self.end_time = time.time()
            self.full_time = self.end_time - self.start_time
            self.speed = len(self.final_text) / self.full_time

            return True

    def check_key_pressed(self, key_pressed):
        print("key pressed :", key_pressed)

        if self.actual_text:
            if key_pressed == self.final_text.split(self.actual_text)[1][0]: #lettre suivante
                self.actual_text += key_pressed
            else:
                self.wrongs += 1

        else: # If it's the first iteration
            if key_pressed == self.final_text[0]:  # first letter
                self.actual_text += key_pressed
            else:
                self.wrongs += 1


    def get_statistics(self):
        """
        Speed / Wrongs / Fatests stroke / most missed stokes /time
        :return:
        """
        speed = len(self.final_text) / self.full_time

        return {
            "speed":speed,
            "wrongs" : self.wrongs,
            "time": self.full_time
        }
