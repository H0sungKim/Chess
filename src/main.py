from Engine import *
import pygame, sys
from pygame.locals import *
import os


def main() :

    engine = Engine()

    moveCase = []

    # Color
    white = (255,255,255)
    red = (255, 128, 128)
    green = (128, 255, 128)
    lightBrown = (240, 217, 181)
    darkBrown = (181, 136, 99)

    size = 320
    tileSize = size * 3 // 8

    isClickedFlag = False

    pygame.init()
    pygame.display.set_caption("Chess")
    pygame.display.set_icon(pygame.image.load(os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), "res"), "chess-board.png")))
    myScreen = pygame.display.set_mode((size * 4, size * 3))
    myScreen.fill(white)

    def drawPiece(x, y) :
        piece = engine.getPiece(x, y)
        if piece == 0 :
            return
        
        nameConvertor = {"K":"wking", "Q":"wqueen", "R":"wrook", "B":"wbishop", "N":"wknight", "P":"wpawn", "k":"bking", "q":"bqueen", "r":"brook", "b":"bbishop", "n":"bknight", "p":"bpawn"}

        pieceImage = pygame.transform.scale(pygame.image.load(os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), "res"), f"{nameConvertor[piece]}.png")), (tileSize, tileSize))
        myScreen.blit(pieceImage, (tileSize*y, tileSize*x))

    def drawBoard() :
        for i in range(8) :
            for j in range(8) :
                if (i+j)%2 == 0 :
                    pygame.draw.rect(myScreen, lightBrown, (tileSize*j, tileSize*i, tileSize, tileSize))
                    drawPiece(i, j)
                else :
                    pygame.draw.rect(myScreen, darkBrown, (tileSize*j, tileSize*i, tileSize, tileSize))
                    drawPiece(i, j)

    def drawMovePoint(x, y) :
        pygame.draw.circle(myScreen, red, (tileSize*y + tileSize//2, tileSize*x + tileSize//2), tileSize//8)

    def drawBackgroundSelected(x, y) :
        pygame.draw.rect(myScreen, green, (tileSize*y, tileSize*x, tileSize, tileSize))
        drawPiece(x, y)

    drawBoard()

    while True :
        for event in pygame.event.get() :
            if event.type == pygame.MOUSEBUTTONDOWN :
                mouseX, mouseY = pygame.mouse.get_pos()
                y = mouseX//tileSize
                x = mouseY//tileSize
                # print(pygame.mouse.get_pos())
                # print(x, y)
                if 0<=x<=7 and 0<=y<=7 :
                    
                    if isClickedFlag :
                        if (x, y) in moveCase :
                            engine.movePiece(selectedPiece[0], selectedPiece[1], x, y)
                        isClickedFlag = False
                        moveCase.clear()
                        drawBoard()
                    else :
                        if engine.getColor(x, y) == engine.turn :
                            selectedPiece = (x, y)
                            drawBackgroundSelected(x, y)
                            for i in engine.getLegalMove(x, y, True) :
                                drawMovePoint(i[0], i[1])
                                moveCase.append(i)
                            isClickedFlag = True    

            if event.type == pygame.MOUSEBUTTONUP :
                x, y = pygame.mouse.get_pos()
                # print(pygame.mouse.get_pos())
                # print(x//tileSize, y//tileSize)
            if event.type == QUIT :
                pygame.quit()
                sys.exit()

        pygame.display.update()

if __name__ == '__main__':
    main()