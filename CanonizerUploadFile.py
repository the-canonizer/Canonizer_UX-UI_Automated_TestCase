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

    def open_upload_file_manager(self):
        self.driver.implicitly_wait(30)
        self.driver.get(UPLOAD_FILE_URL)
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(UploadFileIdentifiers.CREATE_FOLDER_BUTTON)
        )
        return CanonizerUploadFile(self.driver)

    def search_uploaded_files(self, query):
        self.set_input_value(UploadFileIdentifiers.SEARCH_INPUT, query)
        return CanonizerUploadFile(self.driver)

    def reset_upload_filters(self):
        self.find_element(*UploadFileIdentifiers.RESET_BUTTON).click()
        return CanonizerUploadFile(self.driver)

    def switch_to_list_view(self):
        self.find_element(*UploadFileIdentifiers.LIST_VIEW_TOGGLE).click()
        return CanonizerUploadFile(self.driver)

    def switch_to_grid_view(self):
        self.find_element(*UploadFileIdentifiers.GRID_VIEW_TOGGLE).click()
        return CanonizerUploadFile(self.driver)

    def open_first_file_menu_if_available(self):
        menus = self.driver.find_elements(*UploadFileIdentifiers.FILE_MENU_THREE_DOTS)
        if not menus:
            return False
        menus[0].click()
        return True

    def file_menu_has_actions(self):
        has_view = len(self.driver.find_elements(*UploadFileIdentifiers.FILE_ACTION_VIEW)) > 0
        has_download = len(self.driver.find_elements(*UploadFileIdentifiers.FILE_ACTION_DOWNLOAD)) > 0
        has_delete = len(self.driver.find_elements(*UploadFileIdentifiers.FILE_ACTION_DELETE)) > 0
        return has_view or has_download or has_delete

    def open_delete_modal_and_cancel(self):
        self.find_element(*UploadFileIdentifiers.FILE_ACTION_DELETE).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(UploadFileIdentifiers.DELETE_MODAL_CANCEL)
        )
        self.find_element(*UploadFileIdentifiers.DELETE_MODAL_CANCEL).click()
        return CanonizerUploadFile(self.driver)
