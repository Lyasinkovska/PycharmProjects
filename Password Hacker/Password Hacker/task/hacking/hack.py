import socket
import sys
import itertools


def password_generator():
	alphabet1 = 'abcdefghijklmnopqrstuvwxyz0123456789'
	i = 1
	while True:
		for password in itertools.product(alphabet1, repeat=i):
			yield ''.join(password)
		i += 1


args = sys.argv
with socket.socket() as client_socket:
	host = args[1]
	port = int(args[2])
	address = (host, port)
	client_socket.connect(address)

	pass_generator = password_generator()
	for password in pass_generator:
		client_socket.send(password.encode())
		response = client_socket.recv(1024)
		if response.decode() == 'Connection success!':
			print(password)
			break

	client_socket.close()