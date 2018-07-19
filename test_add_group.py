# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class AddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(firefox_binary="c:/Program Files/Mozilla Firefox/firefox.exe")
        self.wd.implicitly_wait(5)
    
    def test_add_group(self):
        wd = self.wd
        self.open_homepage(wd)
        self.login(wd, username="admin", password="secret")
        self.open_group_page(wd)
        self.create_group(wd, name="test_group", header="group_header", footer="group_footer")
        self.return_to_group_page(wd)
        self.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.open_homepage(wd)
        self.login(wd, username="admin", password="secret")
        self.open_group_page(wd)
        self.create_group(wd, name="", header="", footer="")
        self.return_to_group_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("LOGOUT").click()

    def return_to_group_page(self, wd):
        wd.find_element_by_link_text("GROUPS").click()

    def create_group(self, wd, name, header, footer):
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(footer)
        # submit creation
        wd.find_element_by_name("submit").click()

    def open_group_page(self, wd):
        wd.find_element_by_link_text("GROUPS").click()

    def open_homepage(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
