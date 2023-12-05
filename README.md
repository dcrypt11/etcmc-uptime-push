# ETCMC Uptime push
This is a simple python script which will check if your ETCMC process is running and if there is a change in etcpow_balance.txt.enc file recently

## Setup
- Download to your node the [latest etcmc_push.exe and etcmc_push_config_sample.json](https://github.com/dcrypt11/etcmc-uptime-kuma-push/releases/latest) from the repository releases
- Rename **etcmc_push_config_sample.json** to **etcmc_push_config.json** and make sure it is in the same directory with **etcmc_push.exe**
- Make sure the path set in **etcpowBalanceFile** variable in your etcmc_push_config.json file is the correct full path to etcpow_balance.txt.enc. By default, it can be one of those:
    - C:\Program Files (x86)\ETCMC ETC NODE LAUNCHER 1920x1080\ETCMC_GUI\ETCMC_GETH\etcpow_balance.txt.enc
    - C:\Program Files (x86)\ETCMC ETC NODE LAUNCHER 1024x600\ETCMC_GUI\ETCMC_GETH\etcpow_balance.txt.enc

## Option 1: Use with Uptime Kuma
- You should have [Uptime Kuma](https://github.com/louislam/uptime-kuma) installed up and running
- Add New Monitor in Uptime Kuma, choosing **Push** for Monitor type
- Copy the generated Push URL from Uptime Kuma monitor in your **etcmc_push_config.json** file, replacing the value for **uptimeEndpoint** variable

## Option 2: Use with Healthchecks.io
- Signup and create a project in [Healthchecks.io](https://healthchecks.io/)
- Add Check 
- Copy the generated Ping URL in your **etcmc_push_config.json** file, replacing the value for **uptimeEndpoint** variable

## How to use
- After setting **uptimeEndpoint**, just double-click on **etcmc_push.exe** to start it and leave the console running

## Additional options
- If you want you can change number of minutes, which will be compared to etcpow_balance.txt.enc file last modification date. Do it by changing the **etcpowBalanceMinutes** variable in your **etcmc_push_config.py** script. *Default value is 2 minutes*
- If you want to set how often the script will check that the node is running properly, you can by editing the **secondsBetweenChecks** value  in your **etcmc_push_config.py** script. *Default value is 60 seconds*

## Optionally you can manually install and run the script, with these steps
- Install [python](https://www.python.org/downloads/) on your device
- [Make sure to have **python** and **pip** loaded in your path variables](https://datatofish.com/add-python-to-windows-path/)
- Install **psutil** library with **pip** (*pip install psutil*)
- Clone the repository or download the **src/etcmc_push.py** script and **src/etcmc_push_config_sample.json**
- Rename **etcmc_push_config_sample.json** to **etcmc_push_config.json** and make sure it is in the same directory with **etcmc_push.py**
- If needed change the path defined in **etcpowBalanceFile** variable in your **etcmc_push_config.json** file, to be the correct full path to etcpow_balance.txt.enc

**ETC wallet for donations:**
0xa2d643a1D969A2A7758453e720e5944594FaD2E2