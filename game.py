import json
import sys
import game
from PyQt5 import uic, QtWidgets
import os
from PyQt5.QtWidgets import QMainWindow, QApplication

class Game(QMainWindow):
    def __init__(self, name):
        self.name = name
        super(Game, self).__init__()
        uic.loadUi('ui/3_game_screen.ui', self)
        self.flash_card_game_screen.clicked.connect(self.card)      
        self.show()

    def card(self):
        word_list = []
        # with open...
        pass

    def true(self):
        count = 0
        pass

    def false(self):
        count = 0
        pass

    def countDown(self):
        pass

    def total_time(self):
        pass

    def back(self):
        pass

    def exit(self):
        pass

    def progress(self):
        pass


    