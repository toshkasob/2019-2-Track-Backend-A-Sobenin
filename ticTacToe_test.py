#! /usr/bin/env python3

#ticTacToe_test.py
import unittest
from unittest import mock
from ticTacToe import TicTacToe

class TestTicTacToe(unittest.TestCase):

    def test_init(self):
        '''Тест для инициализации игры крестики-нолики
        '''
        game = TicTacToe()
        test_passed = True
        for position in range(9):
            if (game.board[position // 3][position % 3] != (position + 1)
                    or game.name_player_1 != "Player #1"
                    or game.name_player_2 != "Player #2"
                    or game.playerID != 1
                    or game.marked_cell[1].__len__()
                    or game.marked_cell[-1].__len__()
                    or game.step
               ):
                test_passed = False
        self.assertEqual(test_passed, True)

    def test_change_player(self):
        game = TicTacToe()
        playerID_start = game.playerID
        for step in range(9):
            self.assertEqual(game.playerID, playerID_start * ((-1) ** step))
            game.change_player()

    def test_check_marked(self):
        game = TicTacToe()
        game.board = [["x", "o", 3], [4, "x", 6], [7, "o", "x"]]
        game.marked_cell[1] = [5, 1, 9]
        game.marked_cell[-1] = [2, 8]
        #   x o 3
        #   4 x 6
        #   7 o x
        test_str = "seven"
        self.assertEqual(game.check_marked(test_str), False)
        test_char = 'x'
        self.assertEqual(game.check_marked(test_char), False)
        test_less_1 = '0'
        self.assertEqual(game.check_marked(test_less_1), False)
        test_over_9 = '10'
        self.assertEqual(game.check_marked(test_over_9), False)
        test_marked_cell = '5'
        self.assertEqual(game.check_marked(test_marked_cell), False)
        test_marked_cell = '2'
        self.assertEqual(game.check_marked(test_marked_cell), False)
        test_correct = '7'
        self.assertEqual(game.check_marked(test_correct), True)

    def test_show_board(self):
        pass

    def test_change_board(self):
        for playerID_cur in [-1, 1]:
            marker = "x" if playerID_cur == 1 else "o"
            for position in range(9):
                game = TicTacToe()
                game.playerID = playerID_cur
                board_current = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
                board_current[position // 3][position % 3] = marker
                position_cur = position + 1
                with mock.patch('builtins.input', return_value=f"{position_cur}"):
                    game.change_board()
                    self.assertEqual(game.board, board_current)


    def test_check_end(self):
        pass

    def test_game(self):
        pass

if __name__ == "__main__":
    unittest.main()
    