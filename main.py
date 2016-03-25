__doc__ = """

This bot is a deep learner and we mean deep.

"""

import random
import logging
logging.basicConfig()
import time

from telegram.ext import Updater

HTTP_TOKEN = '215078551:AAEt8VcnxYhr_z1RPYXHJtWni-YgqoHZp2k'

VERSION_ONE_DEEP_LEARNING_MODEL = [
    'awwww yeeah',
]

log = logging.getLogger()
log.setLevel(logging.DEBUG)


command_name_to_fn = {}


def on_command(command_name=None):
    assert command_name is not None
    def decorated_function(function):
        command_name_to_fn[command_name] = function
        return function
    return decorated_function


def catch_all_messages(bot, update):
    log.debug(repr(update))
    bot.sendMessage(update.message.chat_id, text=random.choice(VERSION_ONE_DEEP_LEARNING_MODEL))


def router(bot, update):
    """Since our bot runs in privacy mode off, we have to route our own messages to commands."""
    callback = catch_all_messages
    message_str = update.message.text
    if message_str.startswith(bot.name):
        # it's a command
        command = message_str[len(bot.name):].strip().split()[0]
        if command.startswith(u'/'):
            command_name = command[1:]
            callback = command_name_to_fn.get(command_name, catch_all_messages)
        else:
            log.info(u'unknown command: ' + command + u'. routing update to catch_all')

    callback(bot, update)

def register_handlers(updater):
    updater.dispatcher.addTelegramMessageHandler(router)


@on_command(command_name=u'hi')
def respond_to_a_hi(bot, update):
    bot.sendMessage(update.message.chat_id, text='hi ' + update.message.from_user.name)


if __name__ == '__main__':
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
