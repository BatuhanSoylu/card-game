def build_card():
    deck=[]
    card_point=[]
    types_of_card=['spade','heart','diamond','club']
    for i in range(0,4):
        for j in range(1,14):
            new_item=(types_of_card[i])+str(j) # creating a cart
            card_point.append(j)  # create point list
            deck.append(new_item)
    return deck,card_point

def y(cardd,card_point,self):
    import random
    from PyQt5 import QtWidgets, uic
    from PyQt5.QtGui import QPixmap



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


def shuffle():
    card=build_card()
    #gamer_number=int(self.comboBox.currentText())
    # random_number=random.randint(0,51)
    cardd=card[0]
    card_point=card[1]
    return cardd,card_point
