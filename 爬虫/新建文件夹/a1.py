import time,imp,a2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#driver=''
global driver
driver = webdriver.Chrome()
driver.get("http://t.cn/R9U4xwG")

while True:
    imp.reload(a2)
    a2.test()
    print ('done')
    
    time.sleep(5)
