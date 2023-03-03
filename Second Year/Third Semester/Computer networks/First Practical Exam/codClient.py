import socket, struct
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.8.104", 1234))

gameEnded = False
while (not gameEnded):
	i = int(input("i = "))
	j = int(input("j = "))
	s.send(struct.pack('!i', i))
	s.send(struct.pack('!i', j))
	res = s.recv(1)
	if res == 'W':
		print("You won!")
		gameEnded = True
	elif res == '0': 
		print("Didn't hit :(")
	elif res == 'X':
		print("You hit a part of an airplane!")
	elif res == 'H':
		print("You hit the head of the airplane!")

s.close()
