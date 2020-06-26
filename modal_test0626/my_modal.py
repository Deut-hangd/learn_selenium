#coding=utf-8
from selenium import webdriver
from time import sleep
import os
import selenium.webdriver.support.ui as ui
#启动火狐浏览器
driver = webdriver.Firefox()
#获取文件路径
file_path = "file:///" + os.path.abspath("0623/modal.html")
#访问本地文件
driver.get(file_path)
#通过 id 定位元素
driver.find_element_by_id("show_modal").click()
sleep(3)
#定位并点击,触发事件
link = driver.find_element_by_id("myModal").find_element_by_id("click")
link.click()
sleep(3)
#定位并点击关闭模态窗口按钮
button = driver.find_element_by_class_name("modal-footer").find_elements_by_tag_name("button")
button[0].click()
sleep(2)

