import os
import requests as r
import json


bot = ''


def check_os():
    from platform import system, release
    if system() != 'Windows':
        print('prank soft is for windows only, your os is:',
              system(), sep='\n')
    else:
        if release().isdigit() and int(release()) < 10:
            print('prank soft supports only windows 10 and higher')


def t(arg):  # request to telegram api
    return json.loads(r.get(bot + arg).text)


def pe():
    input('press enter to continue\n')


while True:
    if 'token.txt' in os.listdir('../data'):
        file = open(os.path.relpath('../data/token.txt'), 'r')
        TOKEN = file.read()
        print(f'{TOKEN}')
        bot = f'https://api.telegram.org/bot{TOKEN}/'
        if t('getUpdates')['ok']:
            break
        else:
            print('incorrect token')
            pe()
        pass

    print('input token and press enter,',
          'or create token.txt in prank/data folder, put token there and press enter',
          sep='\n')
    TOKEN = input()
    if TOKEN != '':
        print('checking token')
        bot = f'https://api.telegram.org/bot{TOKEN}/'
        if t('getUpdates')['ok']:
            print('success')
            file = open('../data/token.txt', 'r')
            file.write(TOKEN)
            break
        else:
            print('incorrect token')
            pe()
