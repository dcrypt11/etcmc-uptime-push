# ETCMC Uptime Kuma push
This is a simple python script which will check if your ETCMC process is running and if there is a change in etcpow_balance.txt.enc file recently
## Before using
- You should have [Uptime Kuma](https://github.com/louislam/uptime-kuma) up and running
- Install [python](https://www.python.org/downloads/) on your device
- [Make sure to have **python** and **pip** loaded in your path variables](https://datatofish.com/add-python-to-windows-path/)
- Install **psutil** library with **pip** (*pip install psutil*)
- Clone the repository or download the **etcmc-push.py** script
- Add New Monitor in Uptime Kuma, choosing **Push** for Monitor type
- Copy the generated Push URL from Uptime Kuma monitor in your downloaded **etcmc-push.py** script, replacing the value in **uptimeEndpoint** variable
- If needed change the path defined in **etcpowBalanceFile** variable in your downloaded **etcmc-push.py** script, to be the correct full path to etcpow_balance.txt.enc

## Additional options
- If you want you can change number of minutes, which will be compared to etcpow_balance.txt.enc file last modification date. Do it by changing the **etcpowBalanceMinutes** variable in your downloaded **etcmc-push.py** script. *Default value is 2 minutes*
- If you want to set how often the script will check that the node is running properly, you can by editing the **secondsBetweenChecks** value  in your downloaded **etcmc-push.py** script. *Default value is 60 seconds*

## How to use
- Just double-click on **etcmc-push.py** script to start it and leave the console running

**ETC wallet for donations:**
0xa2d643a1D969A2A7758453e720e5944594FaD2E2