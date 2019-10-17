#! /usr/bin/env python3
'''Реализация игры крестики-нолики в классе
'''
#import unittest

class TicTacToe(object):
    '''Класс, содержащий методы игры крестики-нолики
    '''
    winnerConditions = ((1, 2, 3), (4, 5, 6), (7, 8, 9),
                        (1, 4, 7), (2, 5, 8), (3, 6, 9),
                        (1, 5, 9), (3, 5, 7)
                        )
    def __init__(self):
        self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.name_player_1 = "Player #1"
        self.name_player_2 = "Player #2"
        self.playerID = 1
        self.marked_cell = {
            1 : [],
            -1 : [],
        }
        self.step = 0
        #self.show_board()
        #self.play_game()

    def show_board(self):
        '''show_board() показывает состояние поля сражения на момент вызова метода
        '''
        print("\n", end='')
        for iter_row in range(3):
            for iter_col in range(3):
                print(self.board[iter_row][iter_col], end='')
                if iter_col < 2:
                    print(" | ", end='')
            print("\n", end='')
            if iter_row < 2:
                print("-" * 9)
                #print ("\n")

    def ask_names(self):
        '''ask_names() просит представиться обоих игроков
        '''
        #print("\nWrite name for the player #1: ")
        self.name_player_1 = input("\nWrite name for the Player #1:\t")
        #print("\nWrite name for the player #2: ")
        self.name_player_2 = input("\nWrite name for the Player #2:\t")
        print(f"\n========================\n{self.name_player_1}\tvs\t{self.name_player_2}")
        # Проблема с введенными данными и выводом их на экран #Done!

    def change_player(self):
        ''' Изменяет ID текущего игрока
        '''
        self.playerID *= -1

    def check_marked(self, position):
        '''check_marked(position) проверяет position на возможность записи
        в ячейку поля сражения метки X или O
        '''
        if not position.isdigit():
            return False
        if not 1 <= int(position) <= 9:
            return False
        pos_in_list = int(position)
        if (not self.marked_cell[1].count(pos_in_list) and
                not self.marked_cell[-1].count(pos_in_list)):
            return True
        print(f"\n{pos_in_list} is already marked")
        return False

    def change_board(self):
        '''change_board производит изменение состояния поля сражения
        для введенной ячейки
        вызывает метод check_marked(position)
        '''
        marker = "x" if self.playerID == 1 else "o"
        player_cur = self.name_player_1 if self.playerID == 1 else self.name_player_2
        self.show_board()
        position = input(f"{player_cur} enter a position(1-9) of cell to mark: ")
        #while not (position.isdigit()) or not (1 <= int(position) <= 9) or
        #  (set(int(position)).intersection(self.board)):
        while not self.check_marked(position):
            position = input(f"Ooops... {player_cur}, reenter position (digit from 1 to 9):\t")
            #print("we are in while (change_board)")
        else:
            position = int(position)
            #print("we are in else_while (change_board)")
        self.board[(position - 1) // 3][(position - 1) % 3] = marker
        #print("playerID = ")
        #whichKey = self.playerID
        #print(self.playerID)
        #print("\n whichKey = ")
        #print(whichKey)
        #print("\n")
        #print(self.marked_cell.keys())
        #print("\n")
        #print(self.marked_cell.values())
        self.marked_cell[self.playerID].append(position)
        self.change_player()
        self.step += 1
        #self.show_board()
        #return self.check_end()

    def check_end(self):
        '''check_end() проверяет условие окончания игры и выводит результат сражения
            [out] True, if game is over
            [out] False, if game is continue
        '''
        for value in self.marked_cell.values():
            for win_cond in self.winnerConditions:
                if len(set(sorted(value)).intersection(win_cond)) == 3:
                    player_cur = self.name_player_2 if self.playerID == 1 else self.name_player_1
                    print(f"\n{player_cur} is the best of the best in this game just now! =)")
                    self.show_board()
                    return True
        if self.step >= 9:
            print(f"\nGame is over. You are stupid =(")
            self.show_board()
            return True
        return False

    def reset_game(self):
        '''reserGame() запускает игру заново
        '''
        self.__init__()
        self.play_game()

    def play_game(self):
        '''play_game() - это и есть игра в крестики-нолики
        вызывает ask_names(), check_end(), change_board(), reset_game()
        '''
        self.ask_names()
        while not self.check_end():
            self.change_board()
            #print("we are in while")
            #pass
        else:
            new_game = input("Do you want to start new game? [y/n] - ")
            if new_game.count("y"):
                self.reset_game()
            elif new_game.count("n"):
                print("\nGoodBye!\n")
                return True
            else:
                print("\nSorry, I didn't understand. GoodBye!!!")
                return False

if __name__ == "__main__":
    TIC_TAC_TOE = TicTacToe()
    TIC_TAC_TOE.play_game()
