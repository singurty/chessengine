#!/usr/bin/env python3

import chess
import chess.pgn
import os
from state import State

for fn in os.listdir("data"):
    pgn = open(os.path.join("data", fn))
    while 1:
        try:
            game = chess.pgn.read_game(pgn)
        except Exception:
            break
        value = {'1/2-1/2':0, '1-0':1, '0-1':-1}[game.headers['Result']]
        print(value)
        board = game.board()
        for move in game.mainline_moves():
            board.push(move)
            print(value, State(board).serialize()[0, :, :])
