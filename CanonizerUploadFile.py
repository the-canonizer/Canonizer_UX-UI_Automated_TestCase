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


    def upload_file_with_admin(self):
        self.driver.implicitly_wait(30)
        self.driver.get(UPLOAD_FILE_URL)
        return CanonizerUploadFile(self.driver)

    def upload_file_more_than_5mb(self):
        self.driver.implicitly_wait(30)
        self.driver.get(UPLOAD_FILE_URL)
        image = "/home/vivekkumar/PycharmProjects/Canonizer_UX _Github/UI/10mb.jpg"
        upload_image = self.driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        upload_image.send_keys(image)
        return CanonizerUploadFile(self.driver)

    def uploading_file_less_than_5mb(self):
        self.driver.implicitly_wait(30)
        self.driver.get(UPLOAD_FILE_URL)
        image = "/home/vivekkumar/PycharmProjects/Canonizer_UX _Github/UI/image.png"
        upload_image = self.driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        upload_image.send_keys(image)
        print("wrinting file name")
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        self.driver.find_element(*HomePageIdentifiers.UPLOAD_FILE_NAME).send_keys("test"+add_name)
        self.driver.find_element(*HomePageIdentifiers.UPLOAD_BUTTON).click()
        return CanonizerUploadFile(self.driver)


    def upload_in_create_new_folder(self):
        self.driver.implicitly_wait(30)
        self.driver.get(UPLOAD_FILE_URL)
        self.driver.find_element(By.ID, "createFolderBtn").click()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        self.driver.find_element(By.ID, "Create a Folder_Folder Name").send_keys("new_folder"+add_name)
        action = ActionChains(self.driver)
        action.key_down(Keys.ENTER).perform()
        return CanonizerUploadFile(self.driver)


    def upload_file_in_new_folder(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/section/section/main/div/div/div/form/div/div[2]/div/div[2]/div[2]/div[7]/div/div/div/div/div[1]/span").click()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        image = "/home/vivekkumar/PycharmProjects/Canonizer_UX _Github/UI/image.png"
        upload_image = self.driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        upload_image.send_keys(image)
        self.driver.find_element(*HomePageIdentifiers.UPLOAD_FILE_NAME).send_keys("test"+add_name)
        self.driver.find_element(*HomePageIdentifiers.UPLOAD_BUTTON).click()
        return CanonizerUploadFile(self.driver)
