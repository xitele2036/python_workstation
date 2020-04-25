# $language = "python"
# $interface = "1.0"

# 官方的实例可以在未连接任何服务器的情况下进行ssh连接
import json, time, datetime, os
import webbrowser as web

IP = "192.168.102.1"
def_username = "szhw" # 默认用户名
def_password = "Changeme_123" # 默认密码
new_username = "root" # 默认用户名
new_password = "Xitele_123" # 默认密码
local_path = "https://" + str(IP) #请替换你需要的网址

#配置Chrome浏览器的路径
chromepath = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
#注册浏览器类型
web.register('chrome', None, web.BackgroundBrowser(chromepath))

#连接一个已经存在的COM口
rt = crt.Session.ConnectInTab("/S " + "Serial-COM26")
rt.Screen.Send("\r")
rt.Screen.WaitForString("#")
#打开Chrome并连接
driver = web.get("chrome").open(local_path)
driver.find_element_by_id('luci_username').click() # 点击用户名输入框
driver.find_element_by_id('luci_username').send_keys(def_username) # 自动敲入用户名
driver.find_element_by_id('luci_password').click() # 点击密码输入框
driver.find_element_by_id('luci_password').send_keys(def_password) # 自动敲入密码
driver.find_element_by_id('login_button').click() # 点击“登录”按钮
crt.Sleep(8000)


