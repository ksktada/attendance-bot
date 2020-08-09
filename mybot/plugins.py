from slackbot.bot import respond_to, default_reply
import re

@respond_to('hi', re.IGNORECASE)
def hi(message):
    message.reply('I can understand hi or HI!')
    # react with thumb up emoji
    message.react('+1')

@respond_to(r'(^[0-9]:[0-5][0-9])')
def input_time(message, mes):
    print(message._body)
    message.reply('time! {}'.format(mes))

@default_reply
def mes(message):
    print(message.body)
    message.reply('...')