import time

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from CanonizerBase import Page
from Identifiers import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from CanonizerValidationCheckMessages import message
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import *
from selenium import webdriver


class CanonizerPofileUpdatePage(Page):

    def driver(self):
        self.driver = webdriver.Chrome()

    def profile_page(self):
        self.driver.implicitly_wait(30)
        self.driver.get("https://ux-dev.canonizer.com/settings?tab=profile_info")

        return CanonizerPofileUpdatePage(self.driver)

    def enter_first_name(self):
        self.driver.implicitly_wait(30)
        self.driver.get("https://ux-dev.canonizer.com/settings?tab=profile_info")
        self.driver.find_element(By.ID, "firstName").send_keys("testfirstname")
        self.driver.find_element(By.ID, "profileUpdate").click()
        return CanonizerPofileUpdatePage(self.driver)

    def enter_last_name(self):
        self.driver.implicitly_wait(30)
        self.driver.get("https://ux-dev.canonizer.com/settings?tab=profile_info")
        self.driver.find_element(By.ID, "lastName").send_keys("testlastname")
        self.driver.find_element(By.ID, "profileUpdate").click()
        return CanonizerPofileUpdatePage(self.driver)

    def select_date_of_birth(self):
        self.driver.implicitly_wait(30)
        self.driver.get("https://ux-dev.canonizer.com/settings?tab=profile_info")
        self.driver.find_element(By.ID, "profile_info_datepicker").send_keys("2000-02-06")
        self.driver.find_element(By.ID, "profileUpdate").click()
        return CanonizerPofileUpdatePage(self.driver)

    def select_gender(self):
        self.driver.implicitly_wait(30)
        self.driver.get("https://ux-dev.canonizer.com/settings?tab=profile_info")
        self.driver.find_element(By.ID, "female_radio_btn").click()
        self.driver.find_element(By.ID, "profileUpdate").click()
        return CanonizerPofileUpdatePage(self.driver)

    def enter_phone_number(self):
        self.driver.implicitly_wait(30)
        self.driver.get("https://ux-dev.canonizer.com/settings?tab=profile_info")
        self.driver.find_element(By.ID, "phoneNumber").send_keys("7474747474u")
        self.driver.find_element(By.ID, "profileUpdate").click()
        return CanonizerPofileUpdatePage(self.driver)

    def enter_address_1(self):
        self.driver.implicitly_wait(30)
        self.driver.get("https://ux-dev.canonizer.com/settings?tab=profile_info")
        self.driver.find_element(By.ID, "selectAddress_1").send_keys("Hello KittyCafé")
        self.driver.find_element(By.ID, "profileUpdate").click()
        return CanonizerPofileUpdatePage(self.driver)


