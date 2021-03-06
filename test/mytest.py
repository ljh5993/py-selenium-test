__author__ = 'jihoon'

import os
import sys
import unittest
from selenium import webdriver


class SiteTestCase(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Firefox()

        if sys.platform == 'darwin':
            driverPath = os.path.dirname(os.path.abspath(__file__)) + '/driver/phantomjs_mac'
        else:
            driverPath = os.path.dirname(os.path.abspath(__file__)) + '/driver/phantomjs_linux'

        self.driver = webdriver.PhantomJS(driverPath)


    def tearDown(self):
        self.driver.quit()


    def existElement(self, cssSelector):
        try:
            self.driver.find_element_by_css_selector(cssSelector)
            return True
        except:
            return False


    def test_loginPage(self):

        self.driver.get('https://facebook.com')

        self.assertTrue(self.existElement('input#email'))
        self.assertTrue(self.existElement('input#pass'))

    
    def test_ohter(selfs):
        pass


if __name__ == '__main__':
    unittest.main()
