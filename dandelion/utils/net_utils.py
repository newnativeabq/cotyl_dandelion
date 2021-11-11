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


def pretty_print_post(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in 
    this function because it is programmed to be pretty 
    printed and may differ from the actual request.

    From: https://stackoverflow.com/questions/20658572/python-requests-print-entire-http-request-raw
    """
    print('{}\n{}\r\n{}\r\n\r\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))