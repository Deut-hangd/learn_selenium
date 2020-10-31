from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, os

class Baidu01(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"
        self.verficationErrors = []
        self.accept_next_alert = True

    def test_hao(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("hao123").click()
        time.sleep(2)
        try:
            self.assertEqual(u'hao123_上网从这里开始', driver.title)
        except:
            self.savescreenshot(driver, 'hao.png')

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verficationErrors)

    def savescreenshot(self, driver, file_name):
        if not os.path.exists('./image'):
            os.makedirs('./image')

        now = time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
        driver.get_screenshot_as_file('./image/' + now + '-' + file_name)
        time.sleep(1)

unittest.main(verbosity=2)
