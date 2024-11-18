import random

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
from Identifiers import BrowsePageIdentifiers, CampStatementIdentifiers, CreateTopicIdentifiers
from selenium.webdriver.support.ui import Select
import time
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
import sys
from Config import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import *


class CanonizerCampStatementPage(Page):


    def driver(self):
        self.driver = webdriver.Chrome()


    def click_browse_page_button(self):
        """
        This function is to click on the Browse link
        -> Hover to the Browse link
        -> Find the element and click it

        :return:
            Return the result to the main page.
        """
        #title = self.find_element(*BrowsePageIdentifiers.TITLE)
        #print(title)
        if self.find_element(*BrowsePageIdentifiers.BROWSE):
            self.hover(*BrowsePageIdentifiers.BROWSE)
            wait = WebDriverWait(self.driver, 5)
            #wait.until(EC.element_to_be_clickable(*BrowsePageIdentifiers.BROWSE))
            self.find_element(*BrowsePageIdentifiers.BROWSE).click()
            wait = WebDriverWait(self.driver, 5)

    def click_only_my_topics_button(self):
        self.click_browse_page_button()
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        return CanonizerCampStatementPage(self.driver)

    def click_add_camp_statement(self):
        self.driver.implicitly_wait(30)
        self.find_element(*CampStatementIdentifiers.ADD_STATEMENT_BUTTON).click()
        return CanonizerCampStatementPage(self.driver)


    def scroll_down(self):
        self.driver.implicitly_wait(20)
        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        action = ActionChains(self.driver)
        # self.response = requests.get("https://api3.canonizer.com/api/v3/get-all-namespaces")
        # self.r = self.response.json()["data"]
        # print(self.r)
        # self.i = len(self.r)
        self.i = 100
        self.current_name_list = []

        while self.i >= 1:
            action.key_down(Keys.DOWN).perform()
            action.key_down(Keys.DOWN).perform()
            action.key_down(Keys.ENTER).perform()
            print("element selected")
            print(self.i)
            self.i = self.i - 1
            time.sleep(0.4)
            self.current_name = self.driver.find_element(*CampStatementIdentifiers.SELECTED_NAMESPACE).text
            if self.current_name == "sandbox testing":
                print("Got Sandbox")
                print(self.current_name)
                time.sleep(10)
                break



            #time.sleep(0.4)


    def create_new_topic(self):
        self.driver.implicitly_wait(30)
        self.n = random.randint(0, 10000000)
        self.n = str(self.n)
        print(self.n)
        self.driver.find_element(*CreateTopicIdentifiers.CREATE_NEW_TOPIC).click()
        self.driver.find_element(*CreateTopicIdentifiers.EDIT_SUMMARY).send_keys("test_new_topic1")
        self.topic = ("New Topic" + self.n)
        self.driver.find_element(*CreateTopicIdentifiers.TOPIC_NAME).send_keys(self.topic)
        if self.driver.find_element(*CampStatementIdentifiers.NAMESPACE):
            print("Found")
            self.driver.find_element(*CampStatementIdentifiers.NAMESPACE).click()
            print("Clicked on namespace")
        else:
            print("Not Found")
        self.scroll_down()
        print("Testing is here")
        self.driver.find_element(*CreateTopicIdentifiers.CREATE_TOPIC_BUTTON).click()

    def add_camp_statement(self):
        self.driver.implicitly_wait(10)
        self.click_add_camp_statement()
        self.driver.find_element(*CampStatementIdentifiers.STATEMENT_TEXT).send_keys("create new statement")
        self.driver.find_element(*CampStatementIdentifiers.SUBMIT_STATEMENT_BUTTON).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/section/section/main/div/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button[1]/span").click()
        time.sleep(10)
        return CanonizerCampStatementPage(self.driver)

    def add_camp_statement_asterisk(self):
        self.driver.implicitly_wait(20)
        self.click_add_camp_statement()
        if self.driver.find_element(*CampStatementIdentifiers.CAMP_STATEMENT_ASTERISK1):
            if self.driver.find_element(*CampStatementIdentifiers.CAMP_STATEMENT_ASTERISK2):
                pass

        return CanonizerCampStatementPage(self.driver)

    def add_camp_statement_without_mandatory_data(self):
        self.driver.implicitly_wait(30)
        print("came in add_camp_statement_without_manadatory_data")
        self.click_add_camp_statement()
        self.driver.find_element(*CampStatementIdentifiers.EDIT_SUMMARY).send_keys("sample summary")
        self.driver.find_element(*CampStatementIdentifiers.SUBMIT_STATEMENT_BUTTON).click()
        if self.driver.find_element(*CampStatementIdentifiers.SUBMIT_STATEMENT_BUTTON):
           pass
        return CanonizerCampStatementPage(self.driver)

    def add_camp_statement_with_trailing_spaces(self):
        self.driver.implicitly_wait(30)
        self.click_add_camp_statement()
        self.driver.find_element(*CampStatementIdentifiers.STATEMENT_TEXT).send_keys("      create new statement")
        self.driver.find_element(*CampStatementIdentifiers.EDIT_SUMMARY).send_keys("       create new summary")
        self.driver.find_element(*CampStatementIdentifiers.SUBMIT_STATEMENT_BUTTON).click()
        if self.driver.find_element(*CampStatementIdentifiers.SUBMIT_STATEMENT_BUTTON):
            pass
        return CanonizerCampStatementPage(self.driver)

    def add_camp_statement_with_blank_data(self):
        self.driver.implicitly_wait(30)
        self.click_add_camp_statement()
        self.driver.find_element(*CampStatementIdentifiers.SUBMIT_STATEMENT_BUTTON).click()
        if self.driver.find_element(*CampStatementIdentifiers.SUBMIT_STATEMENT_BUTTON):
            pass
        return CanonizerCampStatementPage(self.driver)

    def click_on_add_camp_statement_cancel_button(self):
        self.driver.implicitly_wait(30)
        self.click_add_camp_statement()
        self.driver.find_element(*CampStatementIdentifiers.UPDATE_CANCEL_BUTTON).click()
        if self.driver.find_element(*CampStatementIdentifiers.ADD_STATEMENT_BUTTON):
            pass
        return CanonizerCampStatementPage(self.driver)

    def click_on_camp_statement_preview_button(self):
        self.driver.implicitly_wait(30)
        self.click_add_camp_statement()
        self.driver.find_element(*CampStatementIdentifiers.STATEMENT_TEXT).send_keys("hello statement")
        self.driver.find_element(*CampStatementIdentifiers.EDIT_SUMMARY).send_keys("hello summary")
        self.driver.find_element(*CampStatementIdentifiers.SUBMIT_STATEMENT_BUTTON).click()
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div/div/div/div[2]/div[2]/button[2]").click()
        if self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/span/h3/a/span"):
            pass
        return CanonizerCampStatementPage(self.driver)

    def load_edit_camp_statement(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/div[3]/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/button[1]").click()
        self.driver.find_element(*CampStatementIdentifiers.STATEMENT_TEXT).send_keys("hello statement")
        self.driver.find_element(*CampStatementIdentifiers.EDIT_SUMMARY).send_keys("hello summary")

        if self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[4]/div/div/div/div/div/button[1]/span"):
            pass
        return CanonizerCampStatementPage(self.driver)

    def update_camp_statement_with_mandatory_field(self):
        self.driver.implicitly_wait(30)
        self.driver.get("https://canonizer3.canonizer.com/topic/861-can-1462-test/1-Agreement")
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[3]/div[2]/div/div/div/div/div/div/div[2]/div[2]/button[2]/span").click()
        #create statement
        self.driver.find_element(*CampStatementIdentifiers.STATEMENT_TEXT).send_keys("hello statement")
        self.driver.find_element(*CampStatementIdentifiers.EDIT_SUMMARY).send_keys("hello summary")
        self.driver.find_element(*CampStatementIdentifiers.SUBMIT_STATEMENT_BUTTON).click()

        if self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div/div/div/div[2]/div[2]/div/button[2]/span"):
            pass
        return CanonizerCampStatementPage(self.driver)


    def edit_camp_statement_with_trailing_spaces(self):
        self.driver.implicitly_wait(30)
        self.driver.get("https://canonizer3.canonizer.com/topic/861-can-1462-test/1-Agreement")
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[3]/div[2]/div/div/div/div/div/div/div[2]/div[2]/button[2]/span").click()
        # create statement
        self.driver.find_element(*CampStatementIdentifiers.STATEMENT_TEXT).clear()
        self.driver.find_element(*CampStatementIdentifiers.STATEMENT_TEXT).send_keys("      hello statement")
        self.driver.find_element(*CampStatementIdentifiers.EDIT_SUMMARY).clear()
        self.driver.find_element(*CampStatementIdentifiers.EDIT_SUMMARY).send_keys("     hello summary")
        self.driver.find_element(*CampStatementIdentifiers.SUBMIT_STATEMENT_BUTTON).click()

        if self.driver.find_element(*CampStatementIdentifiers.SUBMIT_STATEMENT_BUTTON):
            pass
        return CanonizerCampStatementPage(self.driver)

    def edit_camp_statement_with_blank_data(self):
        self.driver.implicitly_wait(30)
        self.driver.get("`https://canonizer3.canonizer.com/topic/861-can-1462-test/1-Agreement`")
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[3]/div[2]/div/div/div/div/div/div/div[2]/div[2]/button[2]/span").click()
        # create statement
        self.driver.find_element(*CampStatementIdentifiers.STATEMENT_TEXT).clear()
        self.driver.find_element(*CampStatementIdentifiers.EDIT_SUMMARY).clear()
        self.driver.find_element(*CampStatementIdentifiers.SUBMIT_STATEMENT_BUTTON).click()

        if self.driver.find_element(*CampStatementIdentifiers.SUBMIT_STATEMENT_BUTTON):
            pass
        return CanonizerCampStatementPage(self.driver)

    def compare_camp_statement(self):
        self.driver.implicitly_wait(30)
        self.driver.get("https://canonizer3.canonizer.com/topic/861-can-1462-test/1-Agreement")
        print("editing camp")
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div/div/div/div[2]/div[1]/label/span[1]/input").click()
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[3]/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]/label/span[1]/input").click()
        self.driver.find_element(*CampStatementIdentifiers.COMPARE_STATEMENT_BUTTON).click()
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[3]/div[1]/div/button"):
            pass
        return CanonizerCampStatementPage(self.driver)

    def edit_camp_statement(self):
        self.driver.implicitly_wait(30)
        self.driver.get("https://canonizer3.canonizer.com/browse")
        self.create_new_topic()
        self.driver.find_element(*CampStatementIdentifiers.STATEMENT_TEXT).send_keys("hello statement")
        self.driver.find_element(*CampStatementIdentifiers.EDIT_SUMMARY).send_keys("hello summary")
        self.driver.find_element(*CampStatementIdentifiers.SUBMIT_STATEMENT_BUTTON).click()

        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div/div/div/div[2]/div[2]/button[2]").click()
        self.driver.find_element(*CampStatementIdentifiers.ADD_STATEMENT_BUTTON).click()
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div/div/div/div[2]/div[2]/button[1]/span").click()
        time.sleep(10)
        self.driver.find_element(*CampStatementIdentifiers.STATEMENT_TEXT).send_keys("edit new statement")
        time.sleep(10)
        self.driver.find_element(*CampStatementIdentifiers.EDIT_SUMMARY).send_keys("edit new summary")
        self.driver.find_element(*CampStatementIdentifiers.SUBMIT_STATEMENT_BUTTON).click()
        if self.driver.find_element(*CampStatementIdentifiers.SUBMIT_STATEMENT_BUTTON):
            pass
        return CanonizerCampStatementPage(self.driver)






