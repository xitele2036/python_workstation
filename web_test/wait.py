#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import time
from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

optons = webdriver.ChromeOptions()
optons.add_argument('disable-infobars')
driver = webdriver.Chrome(chrome_options=optons)
driver.maximize_window()
driver.get("https://www.baidu.com")

start = datetime.datetime.now()
print(start)
#WebDriverWait(driver,10).until(lambda x:x.find_element_by_id("kw"))
driver.find_element_by_id("kw").send_keys("snake")
driver.find_element_by_id("su").click()
end = datetime.datetime.now()
print(end)
print("程序运行时间："+str((end-start).seconds)+"秒")
#driver.quit()