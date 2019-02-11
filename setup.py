import urllib
import subprocess
import os
import time


ps = subprocess.Popen(['iwconfig'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
try:
		output = subprocess.check_output(('grep', 'ESSID'), stdin=ps.stdout)
		if "off/any" in output:
			print('DOWN')
			ssid = ""
			passw = ""
			subprocess.call('sudo bash configInterface.sh', shell=True)
			subprocess.call(["sudo", "bash", "setWiFi.sh", str(ssid), str(passw)])
			subprocess.call('sudo wpa_cli -i wlan0 reconfigure', shell=True)
		else:
			print('UP')
except subprocess.CalledProcessError:
    # grep did not match any lines
    print("No wireless networks connected")

#ssid = ""`
#passw = ""
#subprocess.call('sudo bash configInterface.sh', shell=True)
#subprocess.call(["sudo", "bash", "setWiFi.sh", str(ssid), str(passw)])
#subprocess.call('sudo wpa_cli -i wlan0 reconfigure', shell=True)

#subprocess.call('sudo nano /etc/network/interfaces', shell=True)
#subprocess.call('sudo nano /etc/wpa_supplicant/wpa_supplicant.conf', shell=True)
