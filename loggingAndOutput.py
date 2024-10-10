# made by Ira
"""
logging data and stuff
"""

import threading


class Logging:
    def __init__(self, yesLogging):
        self.noLogging = not yesLogging

    # actually print the stuff
    def print(self, text, end):
        print(text, end=f'{end}')

    # for information not necessary for the user
    def log(self, text, end):
        if self.noLogging:
            return 1
        t1 = threading.Thread(target=self.print, args=(f"\x1b[3m \033[1;33;48m{text}", end,))
        t1.start()

    # for error-type warnings and indications
    def error(self, text):
        end = '\n'
        t2 = threading.Thread(target=self.print, args=(f'\033[1;31;48m{text}', end,))
        t2.start()

    # for user-relavent stuff that they would want to see
    def say(self, text):
        end = '\n'
        t3 = threading.Thread(target=self.print, args=(f"\033[1;32;48m{text}", end,))
        t3.start()
