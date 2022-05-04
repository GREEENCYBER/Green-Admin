# coded by iranian black hat hacker
# develope by green cyber
# team: wolf cyber security
# instagrame: greeen_cyber
# ream instagrame: wolf_cyber_security_team






from requests import get
from colorama import Fore as color 
import os
from time import sleep
##############################################
os.system("clear")
print(color.RED+"""
 ██████  ██████  ███████ ███████ ███    ██     ██████   ██████  ██████  ████████ ███████ ██████  
██       ██   ██ ██      ██      ████   ██     ██   ██ ██    ██ ██   ██    ██    ██      ██   ██ 
██   ███ ██████  █████   █████   ██ ██  ██     ██████  ██    ██ ██████     ██    █████   ██████  
██    ██ ██   ██ ██      ██      ██  ██ ██     ██      ██    ██ ██   ██    ██    ██      ██   ██ 
 ██████  ██   ██ ███████ ███████ ██   ████     ██       ██████  ██   ██    ██    ███████ ██   ██ 
                                                                                                 
                                                                                                 

""")
sleep(3)

print(color.LIGHTBLUE_EX+"""
   ☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣
   ♱  coded by: green cyber                     ♱
   ♱  team: wolf cyber security                 ♱ 
   ♱  instagrame: greeen_cyber                  ♱ 
   ♱  team instagrame: wolf_cyber_security_team ♱              
   ☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣                                                                                              
""")

sleep(2)

site = input(color.GREEN+"Enter Your Target Site Url: ")
site = "http://"+site

urls = input(color.LIGHTGREEN_EX+"Enter a urls files: ")





urls = open(urls,"r").read().splitlines()


for url in urls:
    full_address = site+"/"+url
    respowns = get(full_address)
    if respowns.status_code == 200:
        print(f"{color.GREEN} {full_address} is Exists ==========> 200 ")
    else:
        print(f"{color.RED} {full_address} not found! ===========> 400")