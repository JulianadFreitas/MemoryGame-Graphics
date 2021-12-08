from graphics import *
import random
from time import sleep

cards=[]
back_cards = []
spots = 0
errors = 0

def main(Title: str, Width: int, Height: int):
    c1 = Card("/home/julianafreitas/FURG/AED1/memoryGame/images/js.png", 1)
    insert_cards(c1)
    c2 = Card("/home/julianafreitas/FURG/AED1/memoryGame/images/c.png", 2)
    insert_cards(c2)
    c3 = Card("/home/julianafreitas/FURG/AED1/memoryGame/images/py.png", 3)
    insert_cards(c3)
    c4 = Card("/home/julianafreitas/FURG/AED1/memoryGame/images/java.png", 4)
    insert_cards(c4)

    # Tela
    win = GraphWin(Title, Width, Height)
    background(win)

    # Elementos
    introduction(win)
    SortRandle(cards)
    show_cards(win)

    #Fechamento
    sleep(5)
    win.getMouse()
    win.close()

def background(win): 
    c = Image(Point(420, 300), '/home/julianafreitas/FURG/AED1/memoryGame/images/roxo.png')  
    c.draw(win)

def introduction(win):
    text_title = Text(Point(430,70), "JOGO DA MEMÓRIA DOS DEV's")
    text_title.setTextColor('White')
    text_title.setSize(23)
    text_title.setStyle('bold')
    text_title.draw(win)
    text_intro = Text(Point(450,140), "Você deve memorizar os cards dispostos e encontrar \n os pares referentes as diferentes linguagens de programação")
    text_intro.setTextColor('White')
    text_intro.draw(win)
    text_intro.setSize(15)
    text_rules = Text(Point(450,190), "Você terá quatro chances e ganhará o jogo caso pontuar ao menos 9 pontos \n e só poderá errar uma vez!!")
    text_rules.setTextColor('White')
    text_rules.setSize(14)
    text_rules.setStyle('bold')
    text_rules.draw(win)

class Card:
    def __init__(self, img, id):
        self.img = img
        self.id = id

def insert_cards(card):
    cards.append(card)
    return cards.append(card)

#Embaralha a lista de cards
def SortRandle(sequence):
    return random.shuffle(sequence)

# Mostra as cartas na mesa
def show_cards(win):
    for card in cards:
        back_cards.append('/home/julianafreitas/FURG/AED1/memoryGame/images/back.gif')

    card1_p=[240, 430]
    card2_p=[360, 430]
    card3_p=[480, 430]
    card4_p=[600, 430]
    card5_p=[240, 300]
    card6_p=[360, 300]
    card7_p=[480, 300]
    card8_p=[600, 300]

    card1 = Image(Point(240, 430), cards[0].img)
    card1_back = Image(Point(240, 430), back_cards[0])
    card1.draw(win)
    card1_back.draw(win)
    card2 = Image(Point(360, 430), cards[1].img)
    card2_back = Image(Point(360, 430), back_cards[1])     
    card2.draw(win) 
    card2_back.draw(win)   
    card3 = Image(Point(480, 430), cards[2].img)  
    card3_back = Image(Point(480, 430), back_cards[2])  
    card3.draw(win)
    card3_back.draw(win)
    card4 = Image(Point(600, 430), cards[3].img)  
    card4_back = Image(Point(600, 430), back_cards[3]) 
    card4.draw(win)
    card4_back.draw(win)
    card5 = Image(Point(240, 300), cards[4].img) 
    card5.draw(win)
    card5_back = Image(Point(240, 300), back_cards[4])  
    card5_back.draw(win)
    card6 = Image(Point(360, 300), cards[5].img)
    card6_back = Image(Point(360, 300), back_cards[5])    
    card6.draw(win)
    card6_back.draw(win)
    card7 = Image(Point(480, 300), cards[6].img)
    card7_back = Image(Point(480, 300), back_cards[6])  
    card7.draw(win)
    card7_back.draw(win)
    card8 = Image(Point(600, 300), cards[7].img)
    card8_back = Image(Point(600, 300), back_cards[7])
    card8.draw(win)
    card8_back.draw(win)

    def calc_result(win):
        df = Image(Point(420, 300), '/home/julianafreitas/FURG/AED1/memoryGame/images/game_over.png')  
        df.draw(win)
        
        if spots > 9 and errors <= 1:
            text_win = Text(Point(420,450), "Parabéns, você Ganhou :D !")
            text_win.setTextColor('White')
            text_win.setSize(25)
            text_win.setStyle('bold')
            text_win.draw(win)
            sleep(5) 
        else:
            text_lost = Text(Point(420,450), "Você Perdeu :,( !")
            text_lost.setTextColor('White')
            text_lost.setSize(25)
            text_lost.setStyle('bold')
            text_lost.draw(win) 
            sleep(5)

    def select_cards(win):
        clickeds = []
        jogada = 0
        chances = 0
        p1 = []
        
        while chances < 4:
            text_pontos = Text(Point(80,25), "Pontuação: {}".format(spots))
            text_pontos.setTextColor('White')
            text_pontos.undraw()
            text_pontos.setSize(18)
            text_pontos.setStyle('bold')
            text_pontos.draw(win)

            def verifica():
                global errors
                global spots
                if clickeds[0].id == clickeds[1].id:
                    spots += 3
                    return False
                else: 
                    if spots == 0:
                        spots=0
                    else:
                        spots -= 3
                    errors += 1
                    return True
        
            while jogada < 2:
                mouse = win.getMouse()
                x = mouse.getX()
                y = mouse.getY()
                if x >= 196 and x <= 288 and y>=364 and y <= 496:
                    clickeds.append(cards[0])
                    card1_back.undraw()
                    card1.undraw()
                    card1.draw(win)
                    if len(clickeds) == 2:
                        result = verifica()
                        if result:
                            sleep(2)
                            card1s = Image(Point(240, 430), cards[0].img)
                            card1_backs = Image(Point(240, 430), back_cards[7])
                            card1s.undraw()
                            card1_backs.draw(win)
                            back = Image(Point(p1[0], p1[1]), '/home/julianafreitas/FURG/AED1/memoryGame/images/back.gif')
                            back.draw(win)
                    else: 
                        p1 = card1_p
                    jogada += 1

                elif x >= 316 and x <= 404 and y>=364 and y <= 496:
                    clickeds.append(cards[1])
                    card2_back.undraw()
                    card2.undraw()
                    card2.draw(win)
                    if len(clickeds) == 2:
                        result = verifica()
                        if result:
                            sleep(2)
                            card2s = Image(Point(360, 430), cards[1].img)
                            card2_backs = Image(Point(360, 430), back_cards[7])
                            card2s.undraw()
                            card2_backs.draw(win)
                            back = Image(Point(p1[0], p1[1]), '/home/julianafreitas/FURG/AED1/memoryGame/images/back.gif')
                            back.draw(win)
                    else: 
                        p1 = card2_p                   
                    jogada += 1
                    
                elif x >= 436 and x <= 524 and y>=364 and y <= 496:
                    clickeds.append(cards[2])
                    card3_back.undraw()
                    card3.undraw()
                    card3.draw(win)
                    if len(clickeds) == 2:
                        result = verifica()
                        if result:
                            sleep(2)
                            card3s = Image(Point(480, 430), cards[2].img)
                            card3_backs = Image(Point(480, 430), back_cards[7])
                            card3s.undraw()
                            card3_backs.draw(win)
                            back = Image(Point(p1[0], p1[1]), '/home/julianafreitas/FURG/AED1/memoryGame/images/back.gif')
                            back.draw(win)
                    else: 
                        p1 = card3_p
                    jogada += 1
            
                elif x >= 556 and x <= 644 and y>=364 and y <= 496:
                    clickeds.append(cards[3])
                    card4_back.undraw()
                    card4.undraw()
                    card4.draw(win)
                    if len(clickeds) == 2:
                        result = verifica()
                        if result:
                            sleep(2)
                            card4s = Image(Point(600, 430), cards[3].img)
                            card4_backs = Image(Point(600, 430), back_cards[7])
                            card4s.undraw()
                            card4_backs.draw(win)
                            back = Image(Point(p1[0], p1[1]), '/home/julianafreitas/FURG/AED1/memoryGame/images/back.gif')
                            back.draw(win)
                    else: 
                        p1 = card4_p
                    jogada += 1
                    
                elif x >= 196 and x <= 288 and y>=234 and y <= 366: 
                    clickeds.append(cards[4])
                    card5_back.undraw()
                    card5.undraw()
                    card5.draw(win)
                    if len(clickeds) == 2:
                        result = verifica()
                        if result:
                            sleep(2)
                            card5s = Image(Point(240, 300), cards[4].img)
                            card5_backs = Image(Point(240, 300), back_cards[7])
                            card5s.undraw()
                            card5_backs.draw(win)
                            back = Image(Point(p1[0], p1[1]), '/home/julianafreitas/FURG/AED1/memoryGame/images/back.gif')
                            back.draw(win)
                    else: 
                        p1 = card5_p
                    jogada += 1
                   
                elif x >= 316 and x <= 404 and y>=234 and y <= 366:
                    clickeds.append(cards[5])
                    card6_back.undraw()
                    card6.undraw()
                    card6.draw(win)
                    if len(clickeds) == 2:
                        result = verifica()
                        if result:
                            sleep(2)
                            card6s = Image(Point(360, 300), cards[5].img)
                            card6_backs = Image(Point(360, 300), back_cards[7])
                            card6s.undraw()
                            card6_backs.draw(win)
                            back = Image(Point(p1[0], p1[1]), '/home/julianafreitas/FURG/AED1/memoryGame/images/back.gif')
                            back.draw(win)
                    else: 
                        p1 = card6_p
                    jogada += 1
                    
                elif x >= 436 and x <= 524 and y>=234 and y <= 366:
                    clickeds.append(cards[6])
                    card7_back.undraw()
                    card7.undraw()
                    card7.draw(win)
                    if len(clickeds) == 2:
                        result = verifica()
                        if result:
                            sleep(2)
                            card7s = Image(Point(480, 300), cards[6].img)
                            card7_backs = Image(Point(480, 300), back_cards[7])
                            card7s.undraw()
                            card7_backs.draw(win)
                            back = Image(Point(p1[0], p1[1]), '/home/julianafreitas/FURG/AED1/memoryGame/images/back.gif')
                            back.draw(win)
                    else: 
                        p1 = card7_p
                    jogada += 1
                    
                elif x >= 556 and x <= 644 and y>=234 and y <= 366:
                    clickeds.append(cards[7])
                    card8_back.undraw()
                    card8.undraw()
                    card8.draw(win)
                    if len(clickeds) == 2:
                        result = verifica()
                        if result:
                            sleep(2)
                            card8s = Image(Point(600, 300), cards[7].img)
                            card8_backs = Image(Point(600, 300), back_cards[7])
                            card8s.undraw()
                            card8_backs.draw(win)
                            back = Image(Point(p1[0], p1[1]), '/home/julianafreitas/FURG/AED1/memoryGame/images/back.gif')
                            back.draw(win)
                    else: 
                        p1 = card8_p
                    jogada += 1
            jogada = 0
            text_pontos.undraw()
            chances += 1
            p1 = []
            clickeds = []
        text_pontos.draw(win)
    select_cards(win)
    calc_result(win) 
main("Memory Game", 840, 640)
