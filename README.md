# ETCMC Uptime push
This is a simple python script which will check if your ETCMC process is running and if there is a change in etcpow_balance.txt.enc file recently

## Before using
- Install [python](https://www.python.org/downloads/) on your device
- [Make sure to have **python** and **pip** loaded in your path variables](https://datatofish.com/add-python-to-windows-path/)
- Install **psutil** library with **pip** (*pip install psutil*)
- Clone the repository or download the **etcmc_push.py** script and **etcmc_push_config_sample.py**
- Rename **etcmc_push_config_sample.py** to **etcmc_push_config.py** and make sure it is in the same directory with **etcmc_push.py**
- If needed change the path defined in **etcpowBalanceFile** variable in your **etcmc_push_config.py** script, to be the correct full path to etcpow_balance.txt.enc

## Option 1: Use with Uptime Kuma
- You should have [Uptime Kuma](https://github.com/louislam/uptime-kuma) installed up and running
- Add New Monitor in Uptime Kuma, choosing **Push** for Monitor type
- Copy the generated Push URL from Uptime Kuma monitor in your **etcmc_push_config.py** file, replacing the value in **uptimeEndpoint** variable

## Option 2: Use with Healthchecks.io
- Signup and create a project in [Healthchecks.io](https://healthchecks.io/)
- Add Check 
- Copy the generated Ping URL in your **etcmc_push_config.py** file, replacing the value in **uptimeEndpoint** variable

## Additional options
- If you want you can change number of minutes, which will be compared to etcpow_balance.txt.enc file last modification date. Do it by changing the **etcpowBalanceMinutes** variable in your **etcmc_push_config.py** script. *Default value is 2 minutes*
- If you want to set how often the script will check that the node is running properly, you can by editing the **secondsBetweenChecks** value  in your **etcmc_push_config.py** script. *Default value is 60 seconds*

## How to use
- Just double-click on **etcmc_push.py** script to start it and leave the console running

**ETC wallet for donations:**
0xa2d643a1D969A2A7758453e720e5944594FaD2E2