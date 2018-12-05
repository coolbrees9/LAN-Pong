
import select
import socket

class NetworkHandler:

	def __init__(self, port=42069, bport=42069):
		self.readport = port
		self.bport = bport
		self.timeout = 0.01

		self.mySock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.mySock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
		self.mySock.bind(("", self.readport))
		self.mySock.setblocking(0)

	def broadcast(self, msg):
		self.mySock.sendto(msg.encode(), ("255.255.255.255", self.bport))

	def send(self, msg, addr):
		self.mySock.sendto(msg.encode(), (addr, self.bport))

	def read(self):
		readers, writers, errored = select.select([self.mySock], [], [], self.timeout)
		if readers:
			data, (addr, port) = readers[0].recvfrom(256)
			return data.decode(), addr
		return "", ""

