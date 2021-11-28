from graphics_nsi import*
import random

#Window size
HEIGHT=800
WIDTH=800

# ROWS*COLUMNS must be a multiplier of 2
ROWS = 5
COLUMNS = 4

CARD_MARGIN=10
CARD_WIDTH=(WIDTH-(CARD_MARGIN*COLUMNS))/COLUMNS
CARD_HEIGHT= (HEIGHT-(CARD_MARGIN*ROWS))/ROWS
print("taille d'une carte : " + str(CARD_WIDTH) + " " + str(CARD_HEIGHT) )

#init cards
cards = [i for i in range(ROWS*COLUMNS//2) for j in range(2)]
validedCards = [0] * len(cards)
#random.shuffle(cards)



def memory():

    #display the Board Game
    for i in range(COLUMNS):
        for j in range(ROWS):
            drawCase(i,j)

    #Game loop
    while True :

        clic1=wait_clic()
        clic1X, clic1Y = getValueClic(clic1)
        #print(clic1X, clic1Y)
        aff_pol(str(cards[clic1X*(COLUMNS+1)+clic1Y]),40,Point(clic1.x,clic1.y),pink,text_bold=False,text_italic=False)

        bool = True
        while bool:
            clic2=wait_clic()
            clic2X, clic2Y = getValueClic(clic2)
            #print(clic2X, clic2Y)
            if clic1X != clic2X or clic1Y != clic2Y :
                bool = False
        aff_pol(str(cards[clic2X*(COLUMNS+1)+clic2Y]),40,Point(clic2.x,clic2.y),pink,text_bold=False,text_italic=False)

        #check win
        if cards[clic1X*(COLUMNS+1)+clic1Y] == cards[clic2X*(COLUMNS+1)+clic2Y]:
            validedCards[clic1X*(COLUMNS+1)+clic1Y] = 1
            validedCards[clic2X*(COLUMNS+1)+clic2Y] = 1


def getValueClic(clic):
    i = int((clic.x)/(CARD_WIDTH + CARD_MARGIN))
    j = int((clic.y)/(CARD_HEIGHT + CARD_MARGIN))
    return i,j

def drawCase(i,j):
    x=i*(CARD_WIDTH + CARD_MARGIN) + CARD_WIDTH/2
    y=j*(CARD_HEIGHT + CARD_MARGIN) + CARD_HEIGHT/2

    draw_fill_rectangle(Point(x,y),CARD_WIDTH,CARD_HEIGHT,white)

def main():
    init_graphic(WIDTH,HEIGHT)
    memory()
    wait_escape()
    return 0

main()
