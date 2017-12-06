from socket import *

host = "challenges.hackvent.hacking-lab.com"
s = socket(AF_INET, SOCK_STREAM)
s.connect((host, 23))
flag = open('flag.txt', 'w')
active = False
print('Aquiring flag')
print('Please wait...')
while True:
	data = s.recv(2048)
	if active == True:
		flag.write(data)

	if "OWN." in data:
		active = True
		print('Flag saving activated')
	if data.encode('utf-8') == "":
		print('Flag aquired. see in flag.txt')
		break