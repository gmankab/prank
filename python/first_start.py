import os
import requests as r
import json

bot = ''


def t(arg):  # request to telegram api
    return json.loads(r.get(bot + arg).text)


def pe():
    input('press enter to continue\n')


while True:
    if 'token.txt' in os.listdir('../data'):
        file = open('token.txt', 'r')
        TOKEN = file.read()
        if TOKEN != '':
            break

    file = open('token.txt', 'w')
    print('input token and press enter,',
          'or create token.txt in prank/data folder, input token there and press enter',
          sep='\n')
    TOKEN = input()
    if TOKEN != '':
        print('checking token')
        bot = f'https://api.telegram.org/bot{TOKEN}/'
        if t('getUpdates')['ok']:
            print('success')
            break
        else:
            print('incorrect token')
