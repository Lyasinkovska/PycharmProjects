import socket
import sys
import itertools
import json


class PasswordHacker:

	def __init__(self):
		self.args = sys.argv




def file_opening():
	path = '/home/liudaska/PycharmProjects/Password Hacker/Password Hacker/task/hacking/passwords.txt'
	with open(path, 'r', encoding='utf-8') as file:
		return [line.strip() for line in file.readlines()]


def password_generator(lines):
	for line in lines:
		passwords = map(''.join, itertools.product(*zip(line.upper(), line.lower())))
		for password in passwords:
			yield password



with socket.socket() as client_socket:
	host = args[1]
	port = int(args[2])
	address = (host, port)
	lines = file_opening()
	pass_generator = password_generator(lines)
	client_socket.connect(address)
	for password in pass_generator:
		client_socket.send(password.encode('utf-8'))
		response = client_socket.recv(1024)
		if response.decode('utf-8') == 'Connection success!':
			print(password)
			break
		else:
			continue
	client_socket.close()
