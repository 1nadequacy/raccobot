__doc__ = """

This bot is a deep learner and we mean deep.

"""

import random
import logging
import time

from telegram.ext import Updater

HTTP_TOKEN = '215078551:AAEt8VcnxYhr_z1RPYXHJtWni-YgqoHZp2k'

VERSION_ONE_DEEP_LEARNING_MODEL = [
    'awwww yeeah',
]

log = logging.getLogger()
log.setLevel(logging.DEBUG)


def catch_all(bot, update):
    log.debug(repr(update))
    bot.sendMessage(update.message.chat_id, text=random.choice(VERSION_ONE_DEEP_LEARNING_MODEL))


if __name__ == '__main__':
    updater = Updater(token=HTTP_TOKEN)
    updater.dispatcher.addTelegramMessageHandler(catch_all)
    updater.dispatcher.addTelegramRegexHandler('.*', catch_all)
    log.info('beginning polling...')
    try:
        updater.start_polling()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        log.info('quitting...')
        updater.stop()
