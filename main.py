__doc__ = """

This bot is a deep learner and we mean deep.

"""

import random
import logging
logging.basicConfig()
import time

from telegram.ext import Updater, MessageHandler, Filters

HTTP_TOKEN = '215078551:AAEt8VcnxYhr_z1RPYXHJtWni-YgqoHZp2k'

VERSION_ONE_DEEP_LEARNING_MODEL = [
    'awwww yeeah',
]

log = logging.getLogger()
log.setLevel(logging.DEBUG)


def router(bot, update):
    """Just responds to "to confirm"."""
    message = update.message.text
    if 'confirm' not in update.message.text or '@' not in message:
        return
    time.sleep(random.choice(range(10)))
    log.debug(repr(update))
    sentence = random.choice([
        'confirmed.',
        'can confirms.',
        'confirmed by multiple sources.',
        'the rat farm said so',
        'looks like it.'
    ])
    bot.sendMessage(
        update.message.chat_id,
        text='@' + update.message.from_user.username + ' ' + sentence)


def register_handlers(updater):
    updater.dispatcher.add_handler(
        MessageHandler(
            filters=[Filters.text],
            callback=router))


def main():
    updater = Updater(token=HTTP_TOKEN)
    register_handlers(updater)

    log.info('beginning polling...')
    try:
        updater.start_polling(clean=True)
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        log.info('quitting...')
        updater.stop()


if __name__ == '__main__':
    from ipdb import launch_ipdb_on_exception
    with launch_ipdb_on_exception():
        main()
