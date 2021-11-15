#! /usr/bin/python

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class DispenseNow(unittest.TestCase):
    def setUp(self):
        # create a new chrome session
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("http://localhost:8080/")

    def test_dispense_by_click(self):
        # get the dispense button
        dispense_field = self.driver.find_elements_by_link_text("Dispense Now")
        dispense_field[0].click()

        #now searching title from new page after dispense now and find element by title
        newURL = self.driver.window_handles[0]
        self.driver.switch_to.window(newURL)
        self.driver.find_elements_by_xpath('//*[@title="Dispense!!"]')

        #go back to previous page and find element by title
        self.driver.back()
        self.driver.find_elements_by_xpath('//*[@title="Technical Challenge for CDS"]')
        #print(self.driver.current_url)

    def tearDown(self):
        # close the  browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

