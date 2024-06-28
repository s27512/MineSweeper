import unittest
from app import create_board, reveal_cell


class TestMinesweeperGame(unittest.TestCase):

    def setUp(self):
        self.rows = 8
        self.cols = 8
        self.mines = 10

    def test_board_creation(self):
        board = create_board(self.rows, self.cols, self.mines)
        self.assertEqual(len(board), self.rows)
        for row in board:
            self.assertEqual(len(row), self.cols)
        mine_count = sum(row.count('M') for row in board)
        self.assertEqual(mine_count, self.mines)

    def test_cell_revealing(self):
        board = create_board(self.rows, self.cols, self.mines)
        revealed = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        reveal_cell(0, 0, board, revealed)
        self.assertTrue(revealed[0][0])

        reveal_cell(0, 0, board, revealed)
        self.assertTrue(revealed[0][1])
        self.assertTrue(revealed[1][0])
        self.assertTrue(revealed[1][1])

    def test_flagging(self):

        flags = [[False for _ in range(self.cols)] for _ in range(self.rows)]

        flags[0][0] = True
        self.assertTrue(flags[0][0])

        flags[0][0] = False
        self.assertFalse(flags[0][0])


if __name__ == '__main__':
    unittest.main()

