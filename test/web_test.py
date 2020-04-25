#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib.parse import urlencode
import requests
from urllib import request
from selenium import webdriver



if __name__ == "__main__":
    browser = webdriver.Chrome()
    browser.get("https://www.bing.com")
#    print(browser.page_source)
#    browser.close()
    input = browser.find_element_by_id('sb_form_q')
    input.send_keys('python')
    push = browser.find_element_by_id('sb_form_go')
    push.click()