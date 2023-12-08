#!/usr/bin/python
import psutil
import time
import urllib.request
import os
from datetime import datetime, timedelta


contents = open("etcmc_push_config.json").read()
config = eval(contents)

def check_running():
    timeNow = datetime.now()
    pnames = ['geth.exe']

    for pname in pnames:
        pname = pname.lower()
        pRunning = False
        for p in psutil.process_iter(attrs=['name']):
            if pname in p.info['name'].lower():
                pRunning = True


        if not pRunning:
            print(f'{timeNow} {pname} is not running')
            return

    time_mod = os.path.getmtime(config['etcpowBalanceFile'])

    etcpowBalanceMinutes = config['etcpowBalanceMinutes']

    if datetime.fromtimestamp(time_mod) < timeNow - timedelta(minutes=etcpowBalanceMinutes):
        print(f'{timeNow}cetcpow_balance not changed for more than {etcpowBalanceMinutes} minutes')
        return

    try:
        urllib.request.urlopen(config['uptimeEndpoint'])
    except Exception as e:
        print(e.reason)

    print(f'{timeNow} ETCMC node is running')


while True:
    check_running()
    time.sleep(config['secondsBetweenChecks'])