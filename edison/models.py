from datetime import datetime
from random import randint


class Psychic():

    def __init__(self, title, psy_number, credibility=0, attempt=0):
        self.title = title
        self.psy_number =  psy_number
        self.credibility = credibility
        self.attempt = attempt

    def attempt_set(self):
        self.attempt += 1
        return self.attempt


    def credibility_set(self, user_num, psy_num):
        if int(user_num) == psy_num:
            self.credibility += 1
        return self.credibility

