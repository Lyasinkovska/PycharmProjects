import socket, sys

args = sys.argv
with socket.socket() as client_socket:
	host = args[1]
	port = int(args[2])
	address = (host, port)
	client_socket.connect(address)
	client_socket.send(args[3].encode())
	response = client_socket.recv(1024)
	print(response.decode())
	client_socket.close()



