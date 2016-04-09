import socket
import subprocess
import os
import psutil
import hashlib
import time
import datetime

darkiceConnection = False

def is_connected(urlToCheck):
    try:
        host = socket.gethostbyname(urlToCheck)
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False

def has_soundcard():
    info_device = subprocess.check_output(['aplay', '-l'])
    if info_device.find("card 1: CODEC [USB") != -1:
        return True
    return False

def has_streaming_connection(darkicePidPath):
    try:
        with open(darkicePidPath, 'read') as f:
            proc = psutil.Process(int(f.read()))
            if proc.status() in [psutil.STATUS_RUNNING, psutil.STATUS_SLEEPING]:
                return True
    except:
        pass
    return False

def only_silence():
    # TODO check if the only input is silence
    return False

def fileMd5(full_path):
    return hashlib.md5(open(full_path, 'rb').read()).hexdigest()

def textToFile(text, path):
    with open(path, 'w') as f:
        f.write('%s' % text)

def killDarkice(dumpfilePath, dataPath):
    subprocess.call(['killall', 'darkice'])
    if os.path.isfile(dumpfilePath):
        os.rename(dumpfilePath, dataPath + 'dumpfile.' + currentTimeToStr() + '.ogg')

def currentTimeToStr():
    now = datetime.datetime.now()
    return str(now.year) + '-' + str(now.month) + '-' + str(now.day) + '-' + str(now.hour) + '-' + str(now.minute) + '-' + str(now.second)
