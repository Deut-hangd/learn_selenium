#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException,UnexpectedTagNameException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from time import sleep
import os
driver = webdriver.Firefox()
driver.implicitly_wait(30)
file_path = 'file:///' + os.path.abspath('0622/send.html')
driver.get(file_path)
driver.find_element_by_xpath("/html/body/input").click()
sleep(3)
driver.switch_to_alert().send_keys('webdriver')
sleep(3)
driver.switch_to_alert().accept()
sleep(5)
driver.quit()