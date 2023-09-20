#!/usr/bin/python
import psutil
import time
import urllib.request
import os
from datetime import datetime, timedelta

uptimeEndpoint = 'http://192.168.68.64:3001/api/push/z8ym7s19OS?status=up&msk=OK&ping='
etcpowBalanceFile = "C:\Program Files (x86)\ETCMC ETC NODE LAUNCHER 1920x1080\ETCMC_GUI\ETCMC_GETH\etcpow_balance.txt.enc"

etcpowBalanceMinutes = 2
secondsBetweenChecks = 60
    

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

    time_mod = os.path.getmtime(etcpowBalanceFile)

    if datetime.fromtimestamp(time_mod) < timeNow - timedelta(minutes=etcpowBalanceMinutes):
        print(f'{timeNow}cetcpow_balance not changed for more than {etcpowBalanceMinutes} minutes')
        return

    try:
        urllib.request.urlopen(uptimeEndpoint)
    except urllib.error.HTTPError as e:
        print(e.reason)

    print(f'{timeNow} ETCMC node is running')


while True:
    check_running()
    time.sleep(secondsBetweenChecks)