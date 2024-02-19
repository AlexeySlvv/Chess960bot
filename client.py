from aiogram import types
import g4f

from create_bot import dp

import random
import time

import chess
import chess.svg

from cairosvg import svg2png

random.seed(time.time()*1000)


async def do_start(msg: types.Message):
    await msg.answer('Generate random Chess 960 positions')


async def do_help(msg: types.Message):
    await msg.answer('Just send command "random" to generate a position')


async def do_random(msg: types.Message):
    pos_num = random.randint(1, 960)-1
    board = chess.Board.from_chess960_pos(pos_num)
    svg_data = chess.svg.board(board=board).encode("UTF-8")
    temp_file = f"/tmp/{pos_num}.png"
    svg2png(bytestring=svg_data, write_to=temp_file)
    with open(temp_file, "rb") as board_png:
        await msg.answer(f"Position #{pos_num}")
        await msg.answer_photo(photo=board_png)


def register_client_handlers():
    dp.register_message_handler(do_start, commands=['start'])
    dp.register_message_handler(do_help, commands=['help'])
    dp.register_message_handler(do_random, commands=['random'])
