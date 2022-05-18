import json
import sys
from PyQt5 import uic
import time
from PyQt5.QtWidgets import QMainWindow, QApplication
import menu
class Game(QMainWindow):


    def __init__(self,user_name):
        self.user_name = user_name
        self.level = 1
        
        super(Game, self).__init__()
        uic.loadUi('ui/3_game_screen.ui', self)
        # self.flash_card_game_screen.clicked.connect(self.card) 
        
        # Added

        # Kelimeleri getirmek icin
        #self.language_flash_card_game_screen.setText(self.name.word_list)
        self.exit_login_page.clicked.connect(self.exit)
        #self.level_game_screen.setText(str(self.level))
        # self.back_game_screen.clicked.connect(self.back)
        self.count_true = 0
        self.count_false = 0
        self.index = 0
        self.word_list = []
        # self.i = 0                                    # self indexi kullanmak yeterli buna gerek yok. butun self.i leri self.index yaptim sikinti cikmadi
        self.true_button_game_screen.clicked.connect(self.true)
        self.false_button_game_screen.clicked.connect(self.false)
        self.level_game_screen.setText("Level " + str(self.level))                  #defaultta ekran acilinca 0 yazmasi icin
        self.show()
        self.card()

    def card(self):
        self.index = 0
        with open('word_list.json', encoding = 'utf-8') as f:
            self.data = json.load(f)
 
        level_w = self.level*20+1
        # take 20 words from word_list.json and add them to word_list
        for item in range(level_w-20, level_w):
            self.word_list.append([self.data[str(item)]['Dutch Word'], self.data[str(item)]['English Word']])
             
        self.num_of_true_game_screen.setText(str(self.count_true))
        self.num_of_false_game_screen.setText(str(self.count_false))
        self.language_flash_card_game_screen_2.setText(self.word_list[self.index][0])
        self.language_flash_card_game_screen.setText('Netherlands')
   

    def progress(self):
        pass   

    def level_update(self):
        js_file_name = 'user/'+self.user_name+'.json'
        with open('user/'+self.user_name+'.json', 'r') as jsFile:
            user_data = json.load(jsFile)
            user_data['username'] = self.user_name
            user_data['level'] = self.level
            #user_data['time'] = self.count_t
        with open(js_file_name, 'w') as jsFile:
            jsFile.write(json.dumps(user_data, indent=4))
            

        

    def true(self):

        # Timer
        self.count_true +=1
        
        self.true_button_game_screen.setEnabled(True)
        self.false_button_game_screen.setEnabled(True)
        
        self.num_of_true_game_screen.setText(str(self.count_true))
        self.progress_game_screen.setProperty("value",self.count_true*5)
        self.language_flash_card_game_screen_2.setText(self.word_list[self.index][1])
        self.language_flash_card_game_screen.setText('English')                      #asagiyi aktif etsem English word gorunmuyor, comment yapinca da English word te kaliyor
        self.word_list.remove(self.word_list[self.index])

        if self.count_false + self.count_true > 20:                                 #burayi degistirince 20 den sonra false azaldi ekranda
            self.count_false -= 1
            self.num_of_false_game_screen.setText(str(self.count_false))
        
        if self.count_true == 20:
            self.level +=1
            self.count_true = 0
            self.count_false = 0
            self.level_update()
            self.level_game_screen.setText("Level " + str(self.level))            # ekranda level 1 seklinde yazmak icin
            self.card()
        
        

        # self.language_flash_card_game_screen_2.setText(self.word_list[self.index][0])
        # self.language_flash_card_game_screen.setText('Netherlands')
                    

    def false(self):
        self.true_button_game_screen.setEnabled(True)
        self.false_button_game_screen.setEnabled(True)

        b = self.word_list.pop(self.index)
        self.word_list.append(b)
        self.word_list.append(self.word_list[self.index])
        if self.index < 20:
            self.count_false += 1
        self.num_of_false_game_screen.setText(str(self.count_false))
        self.index += 1

        self.language_flash_card_game_screen_2.setText(self.word_list[self.index][1])
        self.language_flash_card_game_screen.setText('English')                        #asagiyi aktif etsem English word gorunmuyor, comment yapinca da English word te kaliyor

        # self.language_flash_card_game_screen_2.setText(self.word_list[self.index][0])
        # self.language_flash_card_game_screen.setText('Netherlands')
        
    

    def countDown(self,t):
        while t:
            secs = t
            timer = '{:02d}'.format(secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
            self.word_list.setText(self.word_list[self.index][1])
    # print('Flip Card!')

    def total_time(self):
        pass


    def back(self):
        self.level_update()
        self.cams = menu.Menu(self.name)
        self.cams.show()
        self.close()
        
    def exit(self):
        self.level_update()
        sys.exit()







