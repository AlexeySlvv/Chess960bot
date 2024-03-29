from aiogram import Bot
from aiogram.dispatcher import Dispatcher

from aiogram.contrib.fsm_storage.memory import MemoryStorage

import argparse

parser = argparse.ArgumentParser(description='Chess960 generate telegram bot')
parser.add_argument('-t', '--token', help='Bot token file')

# token
try:
    args = parser.parse_args()
    with open(args.token, mode='r') as t_f:
        TOKEN = t_f.read().strip()
        bot = Bot(token=TOKEN)
        storage = MemoryStorage()
        dp = Dispatcher(bot, storage=storage)
except Exception as e:
    print('Token file error:', str(e))
    exit()
