# net_utils.py

import subprocess
import platform

import time

def ping(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ' '.join(['ping', param, '1', host])

    with subprocess.Popen([command], shell=True, stdout=subprocess.PIPE) as proc:
        message = proc.stdout.read()

    return message.decode('utf-8').replace('\n', ' ')

