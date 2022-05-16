import json
import sys

from PyQt5 import uic
import os
from PyQt5.QtWidgets import QMainWindow, QApplication
import game

class Menu(QMainWindow):
    
    def __init__(self,user_name):
        self.name = user_name
        super(Menu, self).__init__()
        uic.loadUi('ui/2_main_menu.ui', self)
        # self.username_login_page.setText(self.user_name)
        self.play_button_main_menu.clicked.connect(self.play)
        self.time_button_main_menu.clicked.connect(self.setTimer)
        self.quit_button_main_menu.clicked.connect(self.quit)
        # self.progress_main_menu.clicked.connect(self.total_progress)
        # self.progress_main_menu.setProperty("a",self.total_progress())
        # self.progressBar_menu.setProperty(
        #     "value", self.total_progress())  # call menu progressBar -A
        # self.quitButton_2.clicked.connect(self.quit)  # menu page-> quit -A
        # self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        
        self.show()
    
    def play(self):
        self.cams = game.Game(self.name)
        self.cams.show()
    

    # def total_progress(self):
    #     with open('user/'+self.name+'.json', 'r') as jsFile:
    #         user_data = json.loads(jsFile)
    #         self.level = user_data["level"]
    #         a = self.level*100/250
    #         return a


    def setTimer(self):
        t=int(input('Set The Timer:'))
        game.countDown(t)


    def total_level(self):
        pass


    def quit(self):
        # Record Data
        sys.exit()
    
