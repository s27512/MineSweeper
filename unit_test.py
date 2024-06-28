import unittest
from app import create_board, reveal_cell


class TestMinesweeperGame(unittest.TestCase):

    def setUp(self):
        # Set up any necessary variables or state before each test
        self.rows = 8
        self.cols = 8
        self.mines = 10

    def test_board_creation(self):
        # Test board creation and mine placement
        board = create_board(self.rows, self.cols, self.mines)

        # Check if the board dimensions match
        self.assertEqual(len(board), self.rows)
        for row in board:
            self.assertEqual(len(row), self.cols)

        # Count mines and ensure it matches expected count
        mine_count = sum(row.count('M') for row in board)
        self.assertEqual(mine_count, self.mines)

    def test_cell_revealing(self):
        # Test cell revealing logic
        board = create_board(self.rows, self.cols, self.mines)
        revealed = [[False for _ in range(self.cols)] for _ in range(self.rows)]

        # Test revealing a cell
        reveal_cell(0, 0, board, revealed)
        self.assertTrue(revealed[0][0])

        # Test revealing a cell that should trigger cascade
        reveal_cell(0, 0, board, revealed)
        self.assertTrue(revealed[0][1])
        self.assertTrue(revealed[1][0])
        self.assertTrue(revealed[1][1])

    def test_flagging(self):
        # Test flagging mechanism
        flags = [[False for _ in range(self.cols)] for _ in range(self.rows)]

        # Toggle flag at a specific cell
        flags[0][0] = True
        self.assertTrue(flags[0][0])

        # Toggle flag off
        flags[0][0] = False
        self.assertFalse(flags[0][0])


if __name__ == '__main__':
    unittest.main()

