class TransportPackage:
	port_source
	port_dest
	info

	def __init__(self, port_source: str, port_dest: str, info):
		# checking
		try:
			self._validate_port(dest[1])
			self._validate_port(origin[1])

			self._validate_info(info)
		except Exception as err:
			raise err

		# setting
		self.port_source = mac
		self.port_source = dest
		self.info = info

	def __str__(self):
		return '%s -> %s' % (self.port_source, self.port_source)

	def _validate_port(self, port):
		pass

	def _validate_info(self, info):
		pass


if __name__ == '__main__':
	pack = Package(61234, 8327, 'infomation')
	print(pt)
