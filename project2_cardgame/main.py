from PyQt5 import QtWidgets,uic
from PyQt5.QtGui import QPixmap
import sys
import functions
import random

class Card(QtWidgets.QWidget):
    def __init__(self):
        super(Card, self).__init__()
        uic.loadUi('cardgame.ui',self)
        self.pushButton.clicked.connect(self.give)
        self.pushButton_2.clicked.connect(self.showpoint)
        self.point_1=[]
        self.point_2=[]
        self.point_3=[]
        self.point_4=[]
    def give(self):
        card=functions.build_card()
        gamer_number=int(self.comboBox.currentText())
        cardd=card[0]
        card_point=card[1]


        if gamer_number==2:   # bunu functıon veya class mantıgında ıncele
            random_number = random.randint(0, 51)
            random_number_2 = random.randint(0, 50)

            gamer1card = cardd[random_number]
            gamer1point = card_point[random_number]
            self.point_1.append(gamer1point)
            gamer2card = cardd[random_number_2]
            gamer2point = card_point[random_number_2]
            self.point_2.append(gamer2point)

            pixmap1 = QPixmap('decks\{}.png'.format(gamer1card))
            self.label.setPixmap(pixmap1)
            pixmap2 = QPixmap('decks\{}.png'.format(gamer2card))
            self.label_3.setPixmap(pixmap2)
            self.label_6.setText("Gamer 1 ")
            self.label_7.setText("Gamer 2 ")

            cardd.pop(random_number)
            card_point.pop(random_number)

            cardd.pop(random_number_2)
            card_point.pop(random_number_2)


        elif gamer_number==3:
            random_number = random.randint(0, 51)
            random_number_2 = random.randint(0, 50)
            random_number_3= random.randint(0,49)

            # excel dosyasını olustur
            gamer1card = cardd[random_number]
            gamer1point = card_point[random_number]
            self.point_1.append(gamer1point)
            gamer2card = cardd[random_number_2]
            gamer2point = card_point[random_number_2]
            self.point_2.append(gamer2point)
            gamer3card = cardd[random_number_3]
            gamer3point = card_point[random_number_3]
            self.point_3.append(gamer3point)

            pixmap1=QPixmap('decks\{}.png'.format(gamer1card))
            self.label.setPixmap(pixmap1)
            pixmap2=QPixmap('decks\{}.png'.format(gamer2card))
            self.label_3.setPixmap(pixmap2)
            pixmap3=QPixmap('decks\{}.png'.format(gamer3card))
            self.label_4.setPixmap(pixmap3)

            self.label_6.setText("Gamer 1 ")
            self.label_7.setText("Gamer 2 ")
            self.label_5.setText("Gamer 3 ")


            cardd.pop(random_number)
            card_point.pop(random_number)
            cardd.pop(random_number_2)
            card_point.pop(random_number_2)
            cardd.pop(random_number_3)
            card_point.pop(random_number_3)


        elif gamer_number==4:
            random_number = random.randint(0, 51)
            random_number_2 = random.randint(0, 50)
            random_number_3 = random.randint(0, 49)
            random_number_4 = random.randint(0, 48)

            # excel dosyasını olustur
            gamer1card = cardd[random_number]
            gamer1point = card_point[random_number]
            self.point_1.append(gamer1point)
            gamer2card = cardd[random_number_2]
            gamer2point = card_point[random_number_2]
            self.point_2.append(gamer2point)
            gamer3card = cardd[random_number_3]
            gamer3point = card_point[random_number_3]
            self.point_3.append(gamer3point)
            gamer4card = cardd[random_number_4]
            gamer4point = card_point[random_number_4]
            self.point_4.append(gamer4point)

            pixmap1=QPixmap('decks\{}.png'.format(gamer1card))
            self.label.setPixmap(pixmap1)
            pixmap2=QPixmap('decks\{}.png'.format(gamer2card))
            self.label_3.setPixmap(pixmap2)
            pixmap3=QPixmap('decks\{}.png'.format(gamer3card))
            self.label_4.setPixmap(pixmap3)
            pixmap4=QPixmap('decks\{}.png'.format(gamer4card))
            self.label_2.setPixmap(pixmap4)

            self.label_6.setText("Gamer 1 ")
            self.label_7.setText("Gamer 2 ")
            self.label_5.setText("Gamer 3 ")
            self.label_8.setText("Gamer 4 ")


            cardd.pop(random_number)
            card_point.pop(random_number)
            cardd.pop(random_number_2)
            card_point.pop(random_number_2)
            cardd.pop(random_number_3)
            card_point.pop(random_number_3)
            cardd.pop(random_number_4)
            card_point.pop(random_number_4)


        return self.point_1,self.point_2,self.point_3,self.point_4


    def showpoint(self):
        pointone=0
        for i in self.point_1:
            pointone = i+pointone

        pointsecond=0
        for j in self.point_2:
            pointsecond = j+pointsecond

        pointhird=0
        for z in self.point_3:
            pointhird = z+pointhird

        poinfourth=0
        for k in self.point_4:
            poinfourth = k+poinfourth

        gamer_number=int(self.comboBox.currentText())

        if gamer_number==2:
            self.label_9.setText("Gamer 1 = {}\nGamer 2 = {} ".format(pointone,pointsecond))
        elif gamer_number==3:
            self.label_9.setText("Gamer 1 = {}\nGamer 2 = {}\nGamer 3 = {}".format(pointone,pointsecond,pointhird))
        elif gamer_number==4:
            self.label_9.setText("Gamer 1 = {}\nGamer 2 = {}\nGamer 3 = {}\nGamer 4 = {}".format(pointone,pointsecond,pointhird,poinfourth))



app = QtWidgets.QApplication(sys.argv)
window = Card()
window.show()
app.exec_()





