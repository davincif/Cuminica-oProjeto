class Package:
	mac: int
	destConn: (str, int)
	originConn: (str, int)
	info: str

	def __init__(self, mac: int, origin: (str, int), dest: (str, int), info: str):
		# checking
		try:
			self._validate_mac(mac)
			if type(dest) is not tuple or len(dest) != 2 or type(origin) is not tuple or len(origin) != 2:
				raise TypeError('"dest" and "origin" must be a typle (str, int) with ip and port')

			self._validate_ip(dest[0])
			self._validate_ip(origin[0])

			self._validate_port(dest[1])
			self._validate_port(origin[1])

			self._validate_info(info)
		except Exception as err:
			raise err

		# setting
		self.mac = mac
		self.destConn = dest
		self.originConn = origin
		self.info = info

	def __str__(self):
		return 'mac: %s, %s -> %s ==> %s' % (self.mac, str(self.destConn), str(self.originConn), self.info)

	def _validate_mac(self, mac):
		pass

	def _validate_ip(self, ip):
		pass

	def _validate_port(self, port):
		pass

	def _validate_info(self, info):
		pass


if __name__ == '__main__':
	pt = Package('ahksdkjh', ('913.132.4.1', 20349), ('32f.1h2.hjfd.2', 8082), 'infomation')
	print(pt)
