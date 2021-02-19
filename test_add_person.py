# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from add_person import AddPerson
import unittest, time


class TestAddPerson(unittest.TestCase):
    def setUp(self):
        url = "C:\\Users\\User\\Study\\Soft\\chromedriver.exe"
        self.wd = webdriver.Chrome(url)

# tests
    def test_add_person(self):
        wd = self.wd
        self.login(wd)
        self.open_add_person_form(wd)
        self.add_person_content(wd, AddPerson(f_name="f_name3", m_name="m_name", l_name="l_name", nick="nick",
                                                title="title", company="comp", address="address 123",
                                                h_phone="12345678901", mob_phone="1", work_phone="+123123qwert",
                                                fax="-", mail1="qwer@qwe.qw", mail2="qwe@qwe", mail3="qwe",
                                                site="https://qwe.we/qwe", bday="31", bmonth="February", byear="2500",
                                                aday="2", amonth="February", ayear="1200", address2="add 123",
                                                phone2="1234 1234 1234 1234 1234 1234 1234qwer 1234 1234 1234 1234 1234 1234 1234", notes="note"
                                                ))
        time.sleep(2)
        self.logout(wd)

    def test_add_person2(self):
        wd = self.wd
        self.login(wd)
        self.open_add_person_form(wd)
        self.add_person_content(wd, AddPerson(f_name="f_name1233", m_name="m_name1234", l_name="l_name46134", nick="nick1235",
                                                title="", company="", address="123",
                                                h_phone="12345678901", mob_phone="1", work_phone="+123123qwert",
                                                fax="-", mail1="qwer@qwe.qw", mail2="qwe@qwe", mail3="qwe",
                                                site="https://qwe.we/qwe", bday="31", bmonth="February", byear="2500",
                                                aday="2", amonth="February", ayear="1200", address2="add 123",
                                                phone2="1234 1234 1234 1234 1234 1234 1234qwer 1234 1234 1234 1234 1234 1234 1234", notes="note"
                                                ))
        time.sleep(2)
        self.logout(wd)
# methods
    def login(self, wd, uname="admin", password="secret"):
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(uname)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//body").click()
        wd.find_element_by_xpath("//form[@id='LoginForm']/label").click()
        wd.find_element_by_xpath("//body").click()
        wd.find_element_by_xpath("//form[@id='LoginForm']/label[2]").click()
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_add_person_form(self, wd):
        wd.find_element_by_link_text("add new").click()

    def add_person_content(self, wd, add_person):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(add_person.f_name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(add_person.m_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(add_person.l_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(add_person.nick)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(add_person.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(add_person.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(add_person.address)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(add_person.h_phone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(add_person.mob_phone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(add_person.work_phone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(add_person.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(add_person.mail1)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(add_person.mail2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(add_person.mail3)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(add_person.site)
        wd.find_element_by_name("bday").click()
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(add_person.bday)
        wd.find_element_by_name("bday").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(add_person.bmonth)
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(add_person.byear)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(add_person.aday)
        wd.find_element_by_name("aday").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(add_person.amonth)
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(add_person.ayear)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("new_group").click()
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(add_person.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(add_person.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(add_person.notes)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        wd.find_element_by_link_text("home page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

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
