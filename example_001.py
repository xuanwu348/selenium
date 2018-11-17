#coding:utf-8

from selenium import webdriver
import os
import time


browers = webdriver.Chrome()
url = "http://www.baidu.com"
browers.get(url)

browers.find_element_by_id("kw").send_keys("python")
browers.find_element_by_id("su").click()

time.sleep(5)
browers.quit()
