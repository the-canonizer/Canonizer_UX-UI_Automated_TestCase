import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from CanonizerValidationCheckMessages import message
from CanonizerBase import Page
from CanonizerBase import *
from Identifiers import CampForumIdentifiers, CreateTopicIdentifiers
from Identifiers import *

from selenium.webdriver.common.keys import Keys
import string
import random
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import *
from selenium import webdriver
import Config
from Config import *
from CanonizerLoginPage import CanonizerLoginPage





class CanonizerUploadFile(Page):

    def driver(self):
        self.driver = webdriver.Chrome()
        self.action = ActionChains(self.driver)


    def upload_file_without_userlogin(self):
        self.driver.implicitly_wait(30)
        self.driver.get(UPLOAD_FILE_URL)
        return CanonizerUploadFile(self.driver)

    def upload_file_with_non_admin(self):
        self.driver.implicitly_wait(30)
        CanonizerLoginPage(self.driver).click_on_login_page_button().verify_the_login_with_user2(DEFAULT_USER_2, DEFAULT_PASS_2)
        self.driver.get(UPLOAD_FILE_URL)
        return CanonizerUploadFile(self.driver)

    def upload_file_with_admin(self):
        self.driver.implicitly_wait(30)
        self.driver.get(UPLOAD_FILE_URL)
        return CanonizerUploadFile(self.driver)

    def upload_file_less_than_5mb(self):
        self.driver.implicitly_wait(30)
        self.driver.get(UPLOAD_FILE_URL)
        image = "/home/akash/PycharmProjects/Canonizer_UX _Github/UI/image.png"
        upload_image = self.driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        upload_image.send_keys(image)
        return CanonizerUploadFile(self.driver)

    def upload_file_more_than_5mb(self):
        self.driver.implicitly_wait(30)
        self.driver.get(UPLOAD_FILE_URL)
        image = "/home/akash/PycharmProjects/Canonizer_UX _Github/UI/10mb.jpg"
        upload_image = self.driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        upload_image.send_keys(image)
        return CanonizerUploadFile(self.driver)

    def uploading_file_less_than_5mb(self):
        self.driver.implicitly_wait(30)
        self.driver.get(UPLOAD_FILE_URL)
        image = "/home/akash/PycharmProjects/Canonizer_UX _Github/UI/image.png"
        upload_image = self.driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        upload_image.send_keys(image)
        self.driver.find_element(*ProfileInfoIdentifiersPage.UPLOAD_FILE_NAME).send_keys("test file upload")
        self.driver.find_element(*ProfileInfoIdentifiersPage.UPLOAD_BUTTON).click()
        return CanonizerUploadFile(self.driver)
