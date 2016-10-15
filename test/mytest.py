__author__ = 'jihoon'

import os
import unittest
from selenium import webdriver


class SiteTestCase(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Firefox()

        rootPath = os.path.dirname(os.path.abspath(__file__))
        self.driver = webdriver.PhantomJS(rootPath + '/driver/phantomjs',
                                          service_log_path=rootPath + '/driver/log.txt')

    def tearDown(self):
        self.driver.quit()

    def test_loginPage(self):
        self.driver.get('https://facebook.com')

        self.assertTrue(self.existElement('input#email'))
        self.assertTrue(self.existElement('input#pass'))

    def existElement(self, cssSelector):
        try:
            self.driver.find_element_by_css_selector(cssSelector)
            return True
        except:
            return False


if __name__ == '__main__':
    unittest.main()
