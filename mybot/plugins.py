from slackbot.bot import respond_to
import re

@respond_to('hi', re.IGNORECASE)
def hi(message):
    message.reply('I can understand hi or HI!')
    # react with thumb up emoji
    message.react('+1')

@respond_to(':[0-5][0-9]')
def input_time(message):
    message.reply('time!')
