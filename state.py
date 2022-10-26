#!/usr/bin/env python3

import chess

class State:
    def __init__(self):
        self.board = chess.Board()

    def edges(self):
        return list(self.board.generate_legal_moves())

    def value(self):
        return 1

if __name__ == "__main__":
    s = State()
    print(s.edges())
