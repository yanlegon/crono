from datetime import datetime
from time import sleep
import colorama
from colorama import Fore
import pytz
import sys
from pwn import *
date = datetime.now()

BANNER= f"""{Fore.BLUE}
   ___ _ __ ___  _ __   ___  
  / __| '__/ _ \| '_ \ / _ \ 
 | (__| | | (_) | | | | (_) |
  \___|_|  \___/|_| |_|\___/  {Fore.GREEN}Made by: {Fore.RED}d3ku07

    {Fore.GREEN}Today is: {Fore.BLUE}{date.strftime("%B/%d %H:%M %p %Y")}                          
{Fore.RESET}                                                                                 
"""

def calculate_time(limit=0):
    seconds = 0
    minutes = 0
    hour = 0
    limit = int(limit)
    total_sec = 0
    print(BANNER)
    p1 = log.progress("Crono")
    while True:
        if limit != 0 and limit == total_sec-1:
            print(f"{Fore.GREEN}Time limit reached{Fore.RESET}")
            return
        if seconds == 60:
            minutes += 1
            seconds = 0
        if minutes == 60:
            hour += 1
            minutes = 0
        p1.status(f"{Fore.GREEN}{hour}{Fore.RESET}:{Fore.GREEN}{minutes}{Fore.RESET}:{Fore.GREEN}{seconds}{Fore.RESET}")
        seconds += 1
        total_sec += 1
        sleep(1)

def crono():
    if not len(sys.argv) > 1:
        print(Fore.RED+"Run --help argument for help"+Fore.RESET)
        return
    elif len(sys.argv) >= 2:
        if len(sys.argv) == 2:
            if sys.argv[1] == "--help":
                help = f'''
                {Fore.GREEN}Usage: {Fore.RESET} python3 crono <time> <Time unit>
                {Fore.BLUE}Time units support: {Fore.RESET}
                        -s -> Seconds
                        -m -> Minutes
                        -h -> Hours
                        --free -> to run with unlimited time count
                {Fore.GREEN}Example: {Fore.RESET} python3 crono 3 -m or python3 crono --free
                '''
                print(help)
                return
            elif sys.argv[1] == "--free":
                calculate_time()
        elif len(sys.argv) == 3:
            if sys.argv[2] == "-s":
                calculate_time(sys.argv[1])
            elif sys.argv[2] == "-m":
                limit = int(sys.argv[1])*60
                calculate_time(limit)
            elif sys.argv[2] == "-h":
                limit = int(sys.argv[1])*(60**2)
crono()