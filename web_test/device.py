from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
import  time 
from time import sleep
import paramiko
# from prettytable import PrettyTable
from selenium.webdriver.common.action_chains import ActionChains
import os
from prettytable import PrettyTable
import datetime

class LoginPage_device():
	def __init__(self):
		self.User="szhw"
		self.PassWord="Changeme_123"
		self.URL="https://192.168.102.1"
		self.driver="Chrome"

	device_management_loc = (By.ID, "Devicepage_Select") #设备管理
	device_name_loc = (By.ID, "input_device_name")
	device_remark_loc = (By.ID, "input_remark")
	device_click_loc = (By.XPATH, ".//*[@id='div_device_config']/div[1]/div/div[5]/button/span")
	
	def  SSH_login(self,CMD):
  		import paramiko
  		ssh = paramiko.SSHClient()
  		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 跳过了远程连接中选择‘是’的环节,
  		ssh.connect(self.URL[8:], 22, "jason","Xitele@123")
  		stdin, stdout, stderr = ssh.exec_command(CMD)
  		result = stdout.readlines()
  		re2 = str(result)
  		r2 = re2[9:-4]
  		ssh.close()
  		return r2
	def find_element(self,*loc):
		return self.driver.find_element(*loc)
#登录页面元素ID
	username_loc = (By.ID, "luci_username")
	password_loc = (By.ID, "luci_password")
	login_loc = (By.ID, "login_button")			
	def Web_Login(self):
		from time import sleep
		if str(self.driver) == "Chrome":
			self.driver =webdriver.Chrome()
		self.SSH_login("cfg.lua set usermanage.@user_cfg[0].login_web_browser=nothing")
		self.driver.maximize_window()
		self.driver.get(self.URL)
		self.driver.timeout = 60
		self.find_element(*self.username_loc).clear()
		self.find_element(*self.username_loc).send_keys(self.User)
		self.find_element(*self.password_loc).clear()
		self.find_element(*self.password_loc).send_keys(self.PassWord)
		self.find_element(*self.login_loc).click()
		time.sleep(3)
	def device_nameandremark(self,name,remark):
		self.find_element(*self.device_management_loc).click()
		time.sleep(6)
		self.find_element(*self.device_name_loc).clear()
		self.find_element(*self.device_name_loc).send_keys(name)
		self.find_element(*self.device_remark_loc).clear()
		self.find_element(*self.device_remark_loc).send_keys(remark)
		self.find_element(*self.device_click_loc).click()
		time.sleep(30)
		data = self.find_element(*self.device_name_loc).get_attribute('value')
		data1 = self.find_element(*self.device_remark_loc).get_attribute('value')
		result = self.SSH_login("cfg.lua  get system.@system[0].hostname")
		result1 = self.SSH_login("cfg.lua get system.@system[0].remark")
		if str(data) == str(name)==str(result) and  str(data1) == str(remark)==str(result1):
			x = PrettyTable(["名称","SET","WEB","SSH","RESULT"])
			x.add_row(["device_name",name,data,result,"PASS"])
			x.add_row(["device_remark",remark,data1,result1,"PASS"])
			print(x)
		else:
			x = PrettyTable(["名称","SET","WEB","SSH","RESULT"])
			x.add_row(["device_name",name,data,result,"FAIL"])
			x.add_row(["device_remark",remark,data1,result1,"FAIL"])
			print(x)
#同步时间 按钮	
	device_sync_time_loc = (By.ID, "button_synchronize_with_local_time")
	device_sync_time_click_loc = (By.XPATH, ".//*[@id='button_local_time_sure']/span")
	def sync_time(self):
		self.find_element(*self.device_management_loc).click()
		time.sleep(6)
		self.find_element(*self.device_sync_time_loc).click()
		self.find_element(*self.device_sync_time_click_loc).click()
		time.sleep(30)
		data = self.find_element(By.ID,"span_local_time").text
		data3 = self.find_element(By.ID,"input_timezone").get_attribute('value')
		print("设备时间:",data)
		print("设备时区:",data3)
		print ("本地pc时间:",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

	device_reboot_loc = (By.XPATH, ".//*[@id='button_reboot']/span")
	device_reboot_click_loc = (By.XPATH, ".//*[@id='div_reboot']/div/div[3]/button[1]/span/a")
	device_reset_loc = (By.XPATH, ".//*[@id='button_reset']/span")
	device_reset_click_loc = (By.XPATH, ".//*[@id='button_reset_sure']/span")
	device_Upgrade_loc = (By.XPATH, ".//*[@id='div_device_config']/div[2]/div/button/span/span")
	device_Upgrade_click_loc = (By.XPATH, "//*[@id='device_page']/div/div/div/div/div[2]/div[1]/form/div/div[1]/div/div/input[2]")
	reboot__loc=(By.XPATH,"/html/body/div/div[2]/div[2]/div/div/h2")
	def Reboot(self):
		self.find_element(*self.device_management_loc).click()
		time.sleep(6)	
		self.find_element(*self.device_reboot_loc).click()
		self.find_element(*self.device_reboot_click_loc).click()
		time.sleep(3)
		aa =self.find_element(*self.reboot__loc).text
		print("升级页面显示字段:",aa)
		time.sleep(5)
		import os
		p=os.popen("ping 192.168.2.36 -n 10")
		x=p.read()
		print("点重启后的ping结果",x)
		p.close()		
	def DefaultFactory(self):
		self.find_element(*self.device_management_loc).click()
		time.sleep(6)
		self.find_element(*self.device_reset_loc).click()
		self.find_element(*self.device_reset_click_loc).click()
	def Upgrade(self):
		self.find_element(*self.device_management_loc).click()
		time.sleep(6)
		self.find_element(*self.device_Upgrade_loc).click()
		time.sleep(5)
		self.find_element(By.ID,"keep").click()
#		path =os.path.abspath('../image/')
		file_path=r'F:\R3固件\R3_V1.0.1130.dakota_huawei_Debug_20190522.img'
#		file_path=str(path)+"新建文本文档.img"
		self.find_element(By.ID,"image").send_keys(file_path)
		self.find_element(*self.device_Upgrade_click_loc).click()
		time.sleep(30)
		qq=self.find_element(By.XPATH,".//*[@id='device_page']/div/div/div/div/div[1]/p").text
		print(qq)
		self.find_element(By.XPATH,".//*[@id='device_page']/div/div/div/div/div[2]/div/form[2]/input[4]").click()
		time.sleep(3)
		q=self.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/div/div/h2").text
		print(q)
	icon_timezone_loc=(By.ID,"icon_timezone")#时区下拉
	timezone_select_loc=(By.XPATH,".//*[@id='ul_timezone']/li[1]")
	def Time_Zone(self):
		for QWE in range(1,601) :
			self.find_element(*self.device_management_loc).click()
			self.find_element(*self.icon_timezone_loc).click()
			TIME_xpath = self.timezone_select_loc[1][:-2]+str(QWE)+str(*self.timezone_select_loc[1][-1:])
			self.timezone_select_loc=(self.timezone_select_loc[0],TIME_xpath)
			print(self.timezone_select_loc)
			self.find_element(*self.timezone_select_loc).click()
			self.find_element(*self.device_click_loc).click()
			time.sleep(20)
			self.timezone_select_loc=(By.XPATH,".//*[@id='ul_timezone']/li[1]")
			nowtime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
			data = self.find_element(By.ID,"span_local_time").text
			data3 = self.find_element(By.ID,"input_timezone").get_attribute('value')
			d2 = datetime.datetime.strptime(data, '%Y/%m/%d %H:%M:%S')
			d1 = datetime.datetime.strptime(nowtime, '%Y-%m-%d %H:%M:%S')
			data = self.find_element(By.ID,"span_local_time").text
			data3 = self.find_element(By.ID,"input_timezone").get_attribute('value')
			dd = d1 -d2			
			x1 = PrettyTable(["设备时间","PC时间","设备时区","时间差值"])
			x1.add_row([data,nowtime,data3,dd])
			print(x1)
		
cc = LoginPage_device()
cc.Web_Login()
# cc.device_nameandremark("CHENXUESHAN","DAWEI")
#cc.sync_time()
#cc.Reboot()
#cc.Upgrade()
#cc.Reset()
#cc.Time_Zone()
# cc.device_nameandremark("CHENXUESHAN9999999","DAWE999999I")
# cc.device_nameandremark("CHENXUESHANAAAAA","DAWEIAAAAAA")
cc.Time_Zone()

