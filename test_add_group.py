# -*- coding: utf-8 -*-

from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from group import Group
import unittest, time


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        url = "C:\\Users\\User\\Study\\Soft\\chromedriver.exe"
        self.wd = webdriver.Chrome(url)

    # TEST1 Create new group
    def test_add_group(self):
        wd = self.wd
        self.open_homepage(wd)
        self.login(wd, uname="admin", passwd="secret")
        self.open_group_page(wd)
        self.create_new_group(wd)
        self.fill_group_content(wd, Group(gr_name="group11", gr_params="grouplogo", gr_comment="comment"))
        self.submit_group(wd)
        self.open_group_page(wd)
        time.sleep(2)
        self.logout_addressbook(wd)

    def test_add_null_group(self):
        wd = self.wd
        self.open_homepage(wd)
        self.login(wd, uname="admin", passwd="secret")
        self.open_group_page(wd)
        self.create_new_group(wd)
        self.fill_group_content(wd, Group(gr_name="", gr_params="", gr_comment=""))
        self.submit_group(wd)
        self.open_group_page(wd)
        time.sleep(2)
        self.logout_addressbook(wd)

    # Methods list
    def logout_addressbook(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def submit_group(self, wd):
        wd.find_element_by_name("submit").click()

    def fill_group_content(self, wd, group):
        # Fill group name
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.gr_name)
        # Fill group params
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.gr_params)
        #  Fill group comment
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.gr_comment)

    def create_new_group(self, wd):
        wd.find_element_by_name("new").click()

    def open_group_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, uname, passwd):
        wd.find_element_by_name("user").send_keys(uname)
        wd.find_element_by_xpath("//body").click()
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").send_keys(passwd)
        wd.find_element_by_xpath("//body").click()
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_homepage(self, wd):
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def tearDown(self):
        self.wd.close()
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
