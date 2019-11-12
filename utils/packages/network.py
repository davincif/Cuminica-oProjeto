class NetPackage:
	ip_source
	ip_dest
	info

	def __init__(self, ip_source: str, ip_dest: str, info):
		# checking
		try:
			self._validate_ip(dest[0])
			self._validate_ip(origin[0])

			self._validate_info(info)
		except Exception as err:
			raise err

		# setting
		self.ip_dest = ip_dest
		self.ip_dest = ip_dest
		self.info = info

	def __str__(self):
		return '%s -> %s' % (self.ip_source, self.ip_source)

	def _validate_ip(self, ip):
		pass

	def _validate_info(self, info):
		pass


if __name__ == '__main__':
	pack = Package('123.345.1.4', '634.1.4.6', 'infomation')
	print(pack)
