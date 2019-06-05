from datetime import datetime
from datetime import date
from random import randint
import spotify_module
import util_module as ut
from importlib import reload
import time


dic_cmds = {}

def loadCmds():
    lines = open('src/cmds.txt', 'r', encoding='UTF-8').readlines()
    for  line in lines:
        line = line.replace('\n','')
        parts = line.split('|')
        dic_cmds.update({parts[0].lower() : parts[1].lower()})
def executeCmd(txt):
    print("CMD: "+txt)
    if False:
        a="a"
    elif txt=='askhour':
        now = datetime.now()
        return str('São ' + str(now.hour) + ' horas e ' + str(now.minute) + ' minutos')
    elif txt=='askdate':
        now = date.today()
        return 'Hoje é dia ' + str(now.day) +' '+ ut.days[now.weekday()] +' de ' + ut.months[now.month-1] + ' de ' + str(now.year)
    elif txt=='telljoke':
        return getJoke()
    elif txt=='nextmusic' or txt=='prevmusic':
        reload(spotify_module)
        return spotify_module.execSpotify(txt)
    else:
        return 'Não entendi'

def evaluateCmd(text):
    loadCmds()
    print("Text: "+text)
    if text.lower() in dic_cmds:
        return dic_cmds[text.lower()]
    else:
        return ''

def getJoke():
    lines = open('src/jokes.txt', 'r', encoding='UTF-8').read()
    jokes = lines.split("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    return jokes[randint(0,len(jokes))]
