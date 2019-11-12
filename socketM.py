import socket


def sendInfo(addrs: str, port: int, info: str, soc=None):
	if soc is None:
		tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		tcp.connect((addrs, port))
	else:
		tcp = soc

	tcp.send(info.encode('utf8'))
	tcp.close()

def makeServer(addrs: str, port: int, backlog: int = 5):
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp.bind((addrs, port))
	tcp.listen(backlog)
	return tcp

def reciveInfo(tcp):
	msg = tcp.recv(1024)
	return msg.decode('utf8')


def __main():
	print("working")

if __name__ == '__main__':
	__main()
