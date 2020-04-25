import configparser
import os

class ReadConfig(object):
	def __init__(self):

		self.conf_dir = os.path.abspath('config.ini')
		self.cf = configparser.ConfigParser()
		self.cf.read(self.conf_dir)

	def getConfVal(self,section,option):
		return self.cf.get(section,option)

if __name__ == '__main__':
	cff = ReadConfig()
	dut_ip = cff.getConfVal("DUT","DUT_IP")
	ssh_ip = cff.getConfVal("SSH","ssh_user1")
	print(dut_ip)
	print(ssh_ip)
