import unittest
from app import app, create_board, reveal_cell
from flask import session

class TestMinesweeperGame(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_start_game(self):
        response = self.app.post('/start_game', data={'player_name': 'TestPlayer'})
        self.assertEqual(response.status_code, 302)  # Redirect to index
        with self.app.session_transaction() as sess:
            self.assertEqual(sess['player_name'], 'TestPlayer')

    def test_create_board(self):
        board = create_board(8, 8, 10)
        mine_count = sum(row.count('M') for row in board)
        self.assertEqual(mine_count, 10)
        for row in board:
            self.assertEqual(len(row), 8)

    def test_reveal_cell(self):
        board = create_board(8, 8, 10)
        revealed = [[False for _ in range(8)] for _ in range(8)]
        reveal_cell(0, 0, board, revealed)
        self.assertTrue(revealed[0][0])

if __name__ == '__main__':
    unittest.main()
