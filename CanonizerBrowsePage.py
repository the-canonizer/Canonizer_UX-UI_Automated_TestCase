#from selenium.webdriver import Keys, ActionChains
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
#from webdriver_manager.core import driver

from selenium.common.exceptions import TimeoutException
from CanonizerBase import Page
from Identifiers import BrowsePageIdentifiers, CreateTopicIdentifiers
from selenium.webdriver.support.ui import Select
import time
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


import sys


class CanonizerBrowsePage(Page):

    def driver(self):
        self.driver = webdriver.Chrome()
        self.action = ActionChains(self.driver)
    def click_browse_page_button(self):
        """
        This function is to click on the Browse link
        -> Hover to the Browse link
        -> Find the element and click it

        :return:
            Return the result to the main page.
        """
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, "menu-item-2").click()
        return CanonizerBrowsePage(self.driver)


    def click_only_my_topics_button(self):
        self.driver.implicitly_wait(30)
        print("Going  at browse page")
        #self.click_browse_page_button()
        print("came at browse page")
        time.sleep(10)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        return CanonizerBrowsePage(self.driver)


    def scroll_down(self):
        self.driver.implicitly_wait(10)
        action = ActionChains(self.driver)

        self.i = 100
        self.current_name_list = []

        while self.i >= 1:
            action.key_down(Keys.DOWN).perform()
            action.key_down(Keys.DOWN).perform()
            action.key_down(Keys.ENTER).perform()
            self.i = self.i - 1
            time.sleep(0.4)
            self.current_name = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/section/main/div/form/div/div[1]/div[1]/div/div/div/div/div[2]/div/span[2]").text
            if self.current_name == "sandbox testing":
                time.sleep(10)
                break
            self.driver.find_element(By.XPATH, "/html/body/div[1]/section/section/main/div/form/div/div[1]/div[1]/div/div/div/div/div[2]/div/span[2]").click()
    def select_dropdown_value(self):
        self.driver.implicitly_wait(20)
        self.click_browse_page_button()
        self.find_element(*BrowsePageIdentifiers.NAMESPACE).click()
        self.scroll_down()
        return CanonizerBrowsePage(self.driver)


    def search_topic_tag(self):
        self.driver.implicitly_wait(30)
        self.click_browse_page_button()
        self.driver.find_element(By.XPATH, "/html/body/div[1]/section/section/main/div/form/div/div[1]/div[2]/div/div/div/div/div[2]/div/div/div/div/input").send_keys("History")
        action = ActionChains(self.driver)
        action.key_down(Keys.ENTER).perform()
        return CanonizerBrowsePage(self.driver)

    def search_archived_camp(self):
        self.driver.implicitly_wait(30)
        if self.driver.find_element(By.ID, "name-space-dropdown"):
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div").click()
            self.scroll_sandbox()
        else:
            print("not found")

        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/aside/div/div/div[1]/div[2]/div/div[6]/div/label/span[1]/input").click()
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/ul/li[1]/a/span[1]").click()

        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div/div[3]/div[2]/label/span[1]/input").click()

        return CanonizerBrowsePage(self.driver)

    def algo_dropdown_filter(self):
        self.driver.implicitly_wait(30)
        print("testing")
        self.driver.find_element(By.CLASS_NAME, "ant-btn ant-btn-default xl:w-[277px] text-canBlack border border-canGrey2 py-2.5 lg:px-5 !h-[44px] refine-btn lg:!text-sm !text-sm font-medium flex items-center justify-between gap-2.5 rounded-lg bg-canGray")
        #self.driver.find_element(*CreateTopicIdentifiers.REFINE_BUTTON_FILTER).click()

        return CanonizerBrowsePage(self.driver)


