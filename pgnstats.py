import os
import chess.pgn

PGN_DIR = './pgn/'
MOVES = {
    'P': 0,
    'N': 0,
    'B': 0,
    'R': 0,
    'Q': 0,
    'K': 0,
}
TOTAL = 0


if __name__ == "__main__":
    from pprint import pprint

    for pgn_file in os.listdir(PGN_DIR):
        print(pgn_file)
        with open(os.path.join(PGN_DIR, pgn_file), encoding='utf8') as pgn_f:
            while game := chess.pgn.read_game(pgn_f):
                for move in game.mainline():
                    san = move.san()
                    if san[0] in MOVES:
                        MOVES[san[0]] += 1
                    else:
                        MOVES['P'] += 1
                    TOTAL +=1

    print(TOTAL)
    for k, v in MOVES.items():
        MOVES[k] = (v, round((100*v) / TOTAL))
    pprint(MOVES)
