# /usr/bin/env python3

#import unittest

class Tic_Tac_Toe(object):
    winnerConditions = ( (1,2,3), (4,5,6), (7,8,9),
                         (1,4,7), (2,5,8), (3,6,9),
                         (1,5,9), (3,5,9)
                        )
    def __init__(self):
        self.board = [[1,2,3], [4,5,6], [7,8,9]]
        self.namePlayer_1 = "Player #1 "
        self.namePlayer_2 = "Player #2 "
        self.playerID = 1
        self.markedCell = {
                             1 : [],
                            -1 : [],
                          }
        self.step = 0
        #self.showBoard()
        self.game()
    
    def showBoard(self):
        print ("\n")
        for iter_row in range(3):
            for iter_col in range(3):
                print(self.board[iter_row][iter_col], end = '')
                if iter_col < 2:
                    print(" | ", end = '')
            print("\n", end = '')
            if (iter_row < 2):
                print ("-" * 9)
                #print ("\n")
    
    def askNamesOfPlayers(self):
        #print("\nWrite name for the player #1: ")
        self.namePlayer_1 = input("\nWrite name for the Player #1: ")
        #print("\nWrite name for the player #2: ")
        self.namePlayer_2 = input("\nWrite name for the Player #2: ")
        print(f"\n\n{self.namePlayer_1} vs {self.namePlayer_2}")  #Проблема с введенными данными и выводом их на экран
    
    def changeBoard(self):
        marker = "x" if self.playerID == 1 else "o"
        playerCurrent = self.namePlayer_1 if self.playerID == 1 else self.namePlayer_2
        self.showBoard()
        position = input(f"{playerCurrent} enter a position(1-9) of cell to mark: ")
        while not (position.isdigit()) or not (1 <= int(position) <= 9):
            position = input(f"Ooops... {playerCurrent}, please reenter position (digit from 1 to 9)")
            print("we are in while (changeBoard)")
        else:   
            position = int(position)
            print("we are in else_while (changeBoard)")
        self.board[(position - 1) // 3][(position - 1) % 3] = marker
        #print("playerID = ")
        #whichKey = self.playerID
        #print(self.playerID)
        #print("\n whichKey = ")
        #print(whichKey)
        #print("\n")
        #print(self.markedCell.keys())
        #print("\n")
        #print(self.markedCell.values())
        self.markedCell[self.playerID].append(position)
        self.playerID *= -1
        self.step += 1
        #self.showBoard()
        return self.checkEnd()
    
    def checkEnd(self):
        ''' 
            [out] True, if game is over
            [out] False, if game is continue 
        '''
        for key, value in self.markedCell.items():
            for win_cond in self.winnerConditions:
                if len(set(sorted(value)).intersection(win_cond)) == 3:
                    playerCurrent = self.namePlayer_2 if self.playerID == 1 else self.namePlayer_1
                    print (f"\n{playerCurrent} is the best of the best in this game just now! =)\n")
                    self.showBoard()
                    return True
        if self.step >= 9:
            print (f"\nGame is over. You are stupid =(\n")
            self.showBoard()
            return True
        return False
    
    def resetGame(self):
        self.__init__()

    def game(self):
        self.askNamesOfPlayers()
        while not (self.checkEnd()):
            self.changeBoard()
            print("we are in while")
            #pass
        else:
            newGame = input("Do you want to start new game? [y/n] - ")
            if newGame.count("y"):
                self.resetGame()
            elif newGame.count("n"):
                print("\nGoodBye!\n")
                return True
            else:
                print("\nSorry, I didn't understand. GoodBye!!!")
                return False
ticTacToe = Tic_Tac_Toe()
#ticTacToe.game()

