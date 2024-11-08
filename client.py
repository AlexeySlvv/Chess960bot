from aiogram import types
import g4f
import random

from create_bot import dp

import random
import time

import chess
import chess.svg

from cairosvg import svg2png

random.seed(time.time()*1000)


PIECES = {
    'pawn': 14,
    'knight': 9,
    'bishop': 8,
    'rook': 9,
    'queen': 12,
    'king': 12,
}
PIECES_LIST: list[str] = []


async def do_start(msg: types.Message):
    await msg.answer('Generate random Chess 960 positions')


async def do_help(msg: types.Message):
    await msg.answer('Just send command "random" to generate a position, "piece" to get random chess piece')


async def do_random(msg: types.Message):
    '''Generate Chess 960 posiiton'''
    pos_num = random.randint(1, 960)-1
    board = chess.Board.from_chess960_pos(pos_num)
    svg_data = chess.svg.board(board=board).encode("UTF-8")
    temp_file = f"/tmp/{pos_num}.png"
    svg2png(bytestring=svg_data, write_to=temp_file)
    with open(temp_file, "rb") as board_png:
        await msg.answer(f"Position #{pos_num}")
        await msg.answer_photo(photo=board_png)


async def do_piece(msg: types.Message):
    '''Get random chess piece'''
    #todo: generator

    def get_pieces_list() -> list:
        '''Get random piece list'''
        pieces = list()
        for piece,  value in PIECES.items():
            pieces += [piece]*value
        random.shuffle(pieces)
        return pieces

    global PIECES_LIST
    if not PIECES_LIST:
        PIECES_LIST = get_pieces_list()
    piece = PIECES_LIST.pop()
    with open(f'./pieces/{piece}.svg', encoding='utf8') as f:
        temp_file = f"/tmp/{piece}.png"
        svg2png(bytestring=f.read().encode("UTF-8"), write_to=temp_file)
        with open(temp_file, "rb") as piece_png:
            await msg.answer_photo(photo=piece_png)


def register_client_handlers():
    dp.register_message_handler(do_start, commands=['start'])
    dp.register_message_handler(do_help, commands=['help'])
    dp.register_message_handler(do_random, commands=['random'])
    dp.register_message_handler(do_piece, commands=['piece'])
