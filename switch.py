# standard imports
import threading

# local imports
from utils import socketM


###
# table = {'ip': ('mac', [port])}
###
table = {}


def addRule(ip: str, mac: str, port: int):
	global table

	if ip not in table:
		table[ip] = (mac, [port])
	elif table[ip][0] != mac:
		# error state
		print("in ip %s has no mac %s, but %s" % (ip, mac, table[ip][0]))
	elif port not in table[ip][1]:
		table[ip][1].append(port)
	else:
		# error state
		print("port already exists for this mac")

def rmRule(ip: str, mac: str, port: int):
	global table

	if ip not in table or table[ip][0] != mac or port not in table[ip][1]:
		# error state
		print("this rule doesn't exists")
	else:
		table[ip][1].remove(port)
		if len(table[ip][1]) == 0:
			del table[ip]

def run():
	thread = threading.Thread(target=_watcher)
	thread.run()
	return thread

def _watcher():
	print("_watcher")
	pass


def __test():
	print(table)
	addRule('192.168.0.1', 'BD-08-A6-B4-9C-79', 8080)
	print(table)
	addRule('192.168.0.1', 'BD-08-A6-B4-9C-79', 8081)
	print(table)
	rmRule('192.168.0.1', 'BD-08-A6-B4-9C-79', 8080)
	print(table)
	run()

if __name__ == "__main__":
	__test()
