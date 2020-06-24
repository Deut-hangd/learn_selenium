#coding=utf-8
from selenium import webdriver
import os,time
driver = webdriver.Firefox()
file_path = "file:///" + os.path.abspath("0624/upload.html")
driver.get(file_path)
#定位上传按钮,添加本地文件
driver.find_element_by_name("file").send_keys('E:\\pythonCode\\0624\\upload.html')
time.sleep(3)
driver.quit()

