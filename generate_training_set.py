#!/usr/bin/env python3

import chess
import chess.pgn
import os
from state import State

def get_dateset(num_samples=None):
    X, Y = [], []
    games_count = 0
    for fn in os.listdir("data"):
        pgn = open(os.path.join("data", fn))
        while 1:
            try:
                game = chess.pgn.read_game(pgn)
            except Exception:
                break
            print("parsing game {}, got {} examples".format(games_count, len(X)))
            games_count += 1
            value = {'1/2-1/2':0, '1-0':1, '0-1':-1}[game.headers['Result']]
            board = game.board()
            for move in game.mainline_moves():
                board.push(move)
                ser = State(board).serialize()[0, :, :]
                X.append(ser)
                Y.append(value)
            if num_samples is not None and len(X) > num_samples:
                return X, Y
    return X, Y

if __name__ == "__main__":
    X, Y = get_dateset(1000)
