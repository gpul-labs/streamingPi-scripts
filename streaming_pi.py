#! /usr/bin/python
# -*- coding: utf-8 -*-

import utils
import socket
from ledhandler import LedHandler
import subprocess
import time
import os

STREAMING_URL = 'streaming.cuacfm.org'
DARKICE_CFG_PATH = '/home/pi/darkice.cfg'
DATA_PATH = '/home/pi/.StreamingPi/'

if not os.path.exists(DATA_PATH):
    os.makedirs(DATA_PATH)

darkicePidPath = DATA_PATH + 'darkice.pid'

leds = LedHandler()

if not utils.is_connected(STREAMING_URL):
    print 'estado 1 - sin internet'
    leds.noInternet()
    exit()

if not utils.has_soundcard():
    print 'estado 2 - sin sonido'
    leds.noSoundCard()
    exit()

if not utils.has_streaming_connection(darkicePidPath):
    subprocess.call(['killall', 'darkice'])
    darkiceProcess = subprocess.Popen(['darkice', '-c', DARKICE_CFG_PATH])
    print 'running darkice with pid ' + str(darkiceProcess.pid)
    with open(darkicePidPath, 'w') as f:
        f.write('%d' % darkiceProcess.pid)
    time.sleep(2)

if not utils.has_streaming_connection(darkicePidPath):
    print 'estado 3 - sin conexión streaming'
    leds.noConnection()
    exit()

# emiting
if utils.only_silence():
    print 'estado 4 - sólo se recoge silencio'
    leds.onlySilence()
else:
    # all OK
    print 'estado 5 - todo bien'
    leds.good()
