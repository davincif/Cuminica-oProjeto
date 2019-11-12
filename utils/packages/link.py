class LinkPackage:
	mac_source
	mac_dest
	info

	def __init__(self, mac_source: str, mac_dest: str, info):
		# checking
		try:
			self._validate_mac(mac_source)
			self._validate_mac(mac_dest)

			self._validate_info(info)
		except Exception as err:
			raise err

		# setting
		self.mac_source = mac_source
		self.mac_dest = mac_dest
		self.info = info

	def __str__(self):
		return '%s -> %s' % (self.mac_source, self.mac_source)

	def _validate_mac(self, mac):
		pass

	def _validate_info(self, info):
		pass


if __name__ == '__main__':
	pack = Package('32f.1h2.hjfd.2', 'kjashd.bua89.askjd', 'infomation')
	print(pack)
