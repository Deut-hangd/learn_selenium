#coding=utf-8
from selenium import webdriver
import os,time
driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('0622/drop_down.html')
driver.get(file_path)
driver.implicitly_wait(3)
m = driver.find_element_by_id("ShippingMethod")
time.sleep(3)
m.find_element_by_xpath('/html/body/select/option[3]').click()
time.sleep(3)
driver.quit()