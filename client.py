import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 8080))
message = "SendFromClient"
client.send(message.encode('utf-8'))
from_server = client.recv(4096)
client.close()
print(from_server)