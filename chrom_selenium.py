from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import getpass

brower = webdriver.Chrome()
try:
    brower.get("https://www.baidu.com/")
    tag_input = brower.find_element_by_id("kw")
    tag_input.send_keys("python selenium")
    brower.find_element_by_id("su").click()
    brower.get("https://pan.baidu.com/")
    brower.implicitly_wait(5)
    #time.sleep(2)
    brower.find_element_by_xpath('//p[@title="帐号密码登录"]').click()
    #brower.find_element_by_id("TANGRAM__PSP_4__footerULoginBtn").click
    #brower.find_element_by_css_selector("html#myhtml body div#login-container "\
    #"div.login-main div.login-sdk-v4 div.header-login div.tang-pass-footerBar p#" \
    #"TANGRAM__PSP_4__footerULoginBtn.tang-pass-footerBarULogin.pass-link").click()
    username = input("Please input your username:")
    userpasswd = getpass.getpass("Please input your password:")
    brower.find_element_by_id("TANGRAM__PSP_4__userName").send_keys(str(username))
    brower.find_element_by_id("TANGRAM__PSP_4__password").send_keys(userpasswd)
    brower.find_element_by_id("TANGRAM__PSP_4__submit").click()
    
    
    
    
    
finally:
    time.sleep(10)
    brower.quit()
