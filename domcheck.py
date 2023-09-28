#z
#leet`z
import socket
import threading
import os
import platform
from colorama import Fore,Style

green = Fore.GREEN
red = Fore.RED
reset = Style.RESET_ALL

if platform == "win32":
    os.system("color")
elif platform == "nt":
    os.system("cls")
else:
    os.system("clear")

zner = f"""
▓█████▄  ▒█████   ███▄ ▄███▓ ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀
▒██▀ ██▌▒██▒  ██▒▓██▒▀█▀ ██▒▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ 
░██   █▌▒██░  ██▒▓██    ▓██░▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ 
░▓█▄   ▌▒██   ██░▒██    ▒██ ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ 
░▒████▓ ░ ████▓▒░▒██▒   ░██▒▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄
 ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒░   ░  ░░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒
 ░ ▒  ▒   ░ ▒ ▒░ ░  ░      ░  ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░
 ░ ░  ░ ░ ░ ░ ▒  ░      ░   ░         ░  ░░ ░   ░   ░        ░ ░░ ░ 
   ░        ░ ░         ░   ░ ░       ░  ░  ░   ░  ░░ ░      ░  ░   
 ░                          ░                       ░               
                    Mass Domain To IP + IP Checker
                  Super Fast - Good Quality - FREE
             Leet`z - t.me/leetzch - github.com/leetzch

                            Copyright Z
"""

def zdomcheck(domain, thread_z):
    try:
       for site in domain:
           try:
              ip = socket.gethostbyname(site)
              sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
              sock.settimeout(2)
              check = sock.connect_ex((ip, 80))
              if check == 0:
                 print(f"{green}--| {site} => [{ip}] [LIVE]{reset}")
                 open("good.txt", "a").write(ip+"\n")
              else:
                 print(f"{red}--| {site} => [{ip}] [DEAD]{reset}")





           except:
              pass
    except ValueError as e:
       print(e)

if __name__ == "__main__":
   print(zner)
   try:
       list = input(f"--| root@z[list]: ")
       threads = input(f"--| root@z[thread]: ")
       print("")
       domain = open(list).read().splitlines()
       nullthread = []
       try:
          for i in range(int(threads)):
              thread_z = domain[i::int(threads)]
              thread = threading.Thread(target=zdomcheck, args=(thread_z, i+1))
              nullthread.append(thread)
              thread.start()

          for thread in nullthread:
              thread.join()
       except ValueError as e:
          print(e)

   except KeyboardInterrupt:
       print(f"\n{red}--: CTRL-C Detected, stopped.")
