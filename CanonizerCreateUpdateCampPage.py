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
from selenium.webdriver.remote.webelement import *
from selenium import webdriver


class CanonizerCreateCampPage(Page):

    def driver(self):
        self.driver = webdriver.Chrome()

    def load_create_camp_page(self):
        self.driver.implicitly_wait(30)
        self.find_element(*CreateCampIdentifiers.CREATE_CAMP_PAGE).click()
        return CanonizerCreateCampPage(self.driver)


    def new_camp_mandatory_fields_are_marked_with_asterisk(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'createNewTopic_cardTitle__NEIpU')))
        except TimeoutException:
            pass
        return \
            self.find_element(*CreateCampIdentifiers.NICK_NAME_ASTERISK) and \
            self.find_element(*CreateCampIdentifiers.CAMP_NAME_ASTERISK) and \
            self.find_element(*CreateCampIdentifiers.PARENT_CAMP_ASTERISK)

    def enter_nick_name(self, nickname):
        self.find_element(*CreateCampIdentifiers.CAMP_NICKNAME).send_keys(nickname)

    def enter_parent_camp_name(self, parent_camp_name):
        self.find_element(*CreateCampIdentifiers.PARENT_CAMP).send_keys(parent_camp_name)

    def enter_camp_name(self, camp_name):
        self.find_element(*CreateCampIdentifiers.CAMP_NAME).send_keys(camp_name)
    def enter_camp_name2(self, camp_name):
        self.find_element(*CreateCampIdentifiers.CAMP_NAME).send_keys(camp_name+"Camp2")

    def enter_keywords(self, keywords):
        self.find_element(*CreateCampIdentifiers.KEYWORDS).send_keys(keywords)

    def enter_note(self, note):
        self.find_element(*CreateCampIdentifiers.CAMP_EDIT_SUMMARY).send_keys(note)

    def enter_camp_about_url(self, camp_about_url):
        self.hover(*CreateCampIdentifiers.CAMP_ABOUT_URL)
        self.find_element(*CreateCampIdentifiers.CAMP_ABOUT_URL).send_keys(camp_about_url)

    def enter_camp_about_nick_name(self, camp_about_nick_name):
        self.hover(*CreateCampIdentifiers.CAMP_ABOUT_NICK_NAME)
        self.find_element(*CreateCampIdentifiers.CAMP_ABOUT_NICK_NAME).send_keys(camp_about_nick_name)

    def click_create_camp_button(self):
        self.driver.implicitly_wait(10)
        self.find_element(*CreateCampIdentifiers.CREATE_CAMP_BUTTON).click()



    def create_camp(self, *args):
        self.driver.implicitly_wait(10)
        args = list(args[0])
        self.enter_camp_name(args[2])
        self.click_create_camp_button()
    def disable_create_camp(self, *args):
        self.driver.implicitly_wait(10)
        args = list(args[0])
        self.enter_camp_name(args[2])
        self.driver.find_element(By.ID, "is_disabled").click()
        self.click_create_camp_button()
    def create_camp2(self, *args):
        args = list(args[0])
        self.enter_nick_name(args[0])
        self.enter_parent_camp_name(args[1])
        self.enter_camp_name2(args[2])
        self.enter_keywords(args[3])
        self.enter_note(args[4])
        self.enter_camp_about_url(args[5])
        self.click_create_camp_button()
    def create_camp_with_valid_data(self, create_camp_list1):
        self.driver.implicitly_wait(10)
        self.create_camp(create_camp_list1)
        return CanonizerCreateCampPage(self.driver)
    def disable_create_camp_with_valid_data(self, create_camp_list1):
        self.driver.implicitly_wait(10)
        self.disable_create_camp(create_camp_list1)
        return CanonizerCreateCampPage(self.driver)
    def create_camp2_with_valid_data(self, create_camp_list1):
        self.create_camp2(create_camp_list1)
        return CanonizerCreateCampPage(self.driver)

    def create_camp_with_blank_camp_name(self, create_camp_list2):
        self.create_camp(create_camp_list2)
        self.hover(*CreateCampIdentifiers.BLANK_CAMP_NAME_ERROR)
        error = self.find_element(*CreateCampIdentifiers.BLANK_CAMP_NAME_ERROR).text
        if error == message['Create_Camp']['BLANK_CAMP_NAME_ERROR']:
            return CanonizerCreateCampPage(self.driver)
        else:
            print("Error not found or is not matching")

    def create_camp_with_duplicate_camp_name(self, create_camp_list_5):
        self.driver.implicitly_wait(10)
        self.create_camp(create_camp_list_5)
        return CanonizerCreateCampPage(self.driver)


    def create_camp_with_invalid_camp_about_url(self,create_camp_list_4 ):
        self.create_camp(create_camp_list_4)
        self.hover(*CreateCampIdentifiers.INVALID_CAMP_ABOUT_URL_ERROR)
        error = self.find_element(*CreateCampIdentifiers.INVALID_CAMP_ABOUT_URL_ERROR).text
        if error == message['Create_Camp']['INVALID_CAMP_ABOUT_URL_ERROR']:
            return CanonizerCreateCampPage(self.driver)
        else:
            print("Error not found or is not matching")

    def camp_cancel_button(self):
        self.hover(*CreateCampIdentifiers.CANCEL_BUTTON)
        self.find_element(*CreateCampIdentifiers.CANCEL_BUTTON).click()
        self.hover(*CreateCampIdentifiers.CANCEL_TITLE)
        return CanonizerCreateCampPage(self.driver)


class CanonizerEditCampPage(Page):
    window_scroll = "window.scrollTo(0, document.body.scrollHeight);"

    def driver(self):
        self.driver = webdriver.Chrome()
        self.action = ActionChains(self.driver)

    def load_camp_manage_edit_page(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/section/section/main/div/div/div/div[1]/div[2]/div[2]/a/span/img").click()
        self.driver.find_element(By.ID, "threedot_dropdown_manage_camp_btn__menu_item_text").click()
        self.driver.find_element(By.XPATH, "/html/body/div[1]/section/section/main/div/div/div[2]/div/div/div[2]/div/div/div[1]/button/span").click()

    def submit_camp_update_with_valid_name(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, "create_new_camp_camp_name").send_keys("camp changed")
        self.driver.find_element(By.ID, "crate-camp-btn").click()
        return CanonizerEditCampPage(self.driver)
    def verify_submitter_nick_name_on_camp_history_page(self):
        self.load_camp_manage_edit_page()
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, 'campHistory_campStatementCollapseButtons__LVwiX')))
        except TimeoutException:
            pass
        text = self.find_element(*CreateCampIdentifiers.SUBMITTER_NICK_NAME_LINK).text
        self.find_element(*CreateCampIdentifiers.SUBMITTER_NICK_NAME_LINK).click()
        self.hover(*CreateCampIdentifiers.USER_PROFILE_NICK_NAME_VERIFY)
        text2 = self.find_element(*CreateCampIdentifiers.USER_PROFILE_NICK_NAME_VERIFY).text
        if text == text2:
            return CanonizerEditCampPage(self.driver)
        else:
            print("Text not matching")

    def verify_submit_camp_update_button(self):
        self.load_camp_manage_edit_page()
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, 'campHistory_campStatementCollapseButtons__LVwiX')))
        except TimeoutException:
            pass
        self.hover(*CreateCampIdentifiers.SUBMIT_CAMP_UPDATE)
        self.find_element(*CreateCampIdentifiers.SUBMIT_CAMP_UPDATE).click()
        self.hover(*CreateCampIdentifiers.CAMP_UPDATE_PAGE_TITLE)
        page_title = self.find_element(*CreateCampIdentifiers.CAMP_UPDATE_PAGE_TITLE).text
        if page_title == message['Create_Camp']['CAMP_UPDATE_PAGE_TITLE']:
            return CanonizerEditCampPage(self.driver)
        else:
            print("Title not found or is not matching")

    def submit_camp_update_with_invalid_url(self, camp_about_url):
        self.verify_submit_camp_update_button()
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, 'campHistory_campStatementCollapseButtons__LVwiX')))
        except TimeoutException:
            pass
            for i in range(0, 60):
                self.find_element(*CreateCampIdentifiers.EDIT_CAMP_URL).send_keys(Keys.BACKSPACE)

        self.find_element(*CreateCampIdentifiers.EDIT_CAMP_URL).send_keys(camp_about_url)
        self.hover(*CreateCampIdentifiers.SUBMIT_UPDATE_BUTTON)
        self.find_element(*CreateCampIdentifiers.SUBMIT_UPDATE_BUTTON).click()
        self.hover(*CreateCampIdentifiers.INVALID_CAMP_ABOUT_URL_ERROR)
        error = self.find_element(*CreateCampIdentifiers.INVALID_CAMP_ABOUT_URL_ERROR).text
        if error == message['Create_Camp']['INVALID_CAMP_ABOUT_URL_ERROR']:
            return CanonizerEditCampPage(self.driver)
        else:
            print("Error not found or is not matching")

    def update_camp_with_duplicate_camp_name(self, duplicate_camp_name):
        self.verify_submit_camp_update_button()
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, 'campHistory_campStatementCollapseButtons__LVwiX')))
        except TimeoutException:
            pass
            for i in range(0, 30):
                self.find_element(*CreateCampIdentifiers.EDIT_CAMP_NAME_FIELD).send_keys(Keys.BACKSPACE)

        self.find_element(*CreateCampIdentifiers.EDIT_CAMP_NAME_FIELD).send_keys(duplicate_camp_name)
        self.hover(*CreateCampIdentifiers.SUBMIT_UPDATE_BUTTON)
        self.find_element(*CreateCampIdentifiers.SUBMIT_UPDATE_BUTTON).click()
        self.hover(*CreateCampIdentifiers.DUPLICATE_CAMP_NAME_ERROR)
        error = self.find_element(*CreateCampIdentifiers.DUPLICATE_CAMP_NAME_ERROR).text
        if error == message['Create_Camp']['BLANK_CAMP_NAME_ERROR']:
            return CanonizerCreateCampPage(self.driver)
        else:
            print("Error not found or is not matching")

    def verify_cancel_button_functionality_on_camp_update_page(self):
        self.verify_submit_camp_update_button()
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, 'campHistory_campStatementCollapseButtons__LVwiX')))
        except TimeoutException:
            pass
        self.hover(*CreateCampIdentifiers.CANCEL_CAMP_UPDATE_BUTTON)
        self.find_element(*CreateCampIdentifiers.CANCEL_CAMP_UPDATE_BUTTON).click()
        self.hover(*CreateCampIdentifiers.CAMP_HISTORY_TITLE)
        page_title = self.find_element(*CreateCampIdentifiers.CAMP_HISTORY_TITLE).text
        if page_title == message['Create_Camp']['CAMP_HISTORY_TITLE']:
            return CanonizerEditCampPage(self.driver)
        else:
            print("Title not found or is not matching")

    def verify_preview_button_functionality_on_camp_update_page(self):
        self.verify_submit_camp_update_button()
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, 'campHistory_campStatementCollapseButtons__LVwiX')))
        except TimeoutException:
            pass
        self.hover(*CreateCampIdentifiers.PREVIEW_BUTTON)
        self.find_element(*CreateCampIdentifiers.PREVIEW_BUTTON).click()
        self.hover(*CreateCampIdentifiers.PREVIEW_TITLE)
        page_title = self.find_element(*CreateCampIdentifiers.PREVIEW_TITLE).text
        if page_title == message['Create_Camp']['PREVIEW_TITLE']:
            return CanonizerEditCampPage(self.driver)
        else:
            print("Title not found or is not matching")

    def verify_fields_on_preview_modal(self):
        self.verify_submit_camp_update_button()
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, 'campHistory_campStatementCollapseButtons__LVwiX')))
        except TimeoutException:
            pass
        text1 = self.find_element(*CreateCampIdentifiers.EDIT_CAMP_NAME_FIELD).text
        self.hover(*CreateCampIdentifiers.EDIT_NICK_NAME)
        text2 = self.find_element(*CreateCampIdentifiers.EDIT_NICK_NAME).text
        self.hover(*CreateCampIdentifiers.EDIT_KEYWORDS)
        text3 = self.find_element(*CreateCampIdentifiers.EDIT_KEYWORDS).text
        self.hover(*CreateCampIdentifiers.EDIT_CAMP_URL)
        text4 = self.find_element(*CreateCampIdentifiers.EDIT_CAMP_URL).text

        self.hover(*CreateCampIdentifiers.PREVIEW_BUTTON)
        self.find_element(*CreateCampIdentifiers.PREVIEW_BUTTON).click()

        self.hover(*CreateCampIdentifiers.PREVIEW_CAMP_NAME_VERIFY)
        text11 = self.find_element(*CreateCampIdentifiers.PREVIEW_CAMP_NAME_VERIFY).text
        self.hover(*CreateCampIdentifiers.PREVIEW_NICK_NAME_VERIFY)
        text22 = self.find_element(*CreateCampIdentifiers.PREVIEW_NICK_NAME_VERIFY).text
        self.hover(*CreateCampIdentifiers.PREVIEW_KEYWORD_VERIFY)
        text33 = self.find_element(*CreateCampIdentifiers.PREVIEW_KEYWORD_VERIFY).text
        self.hover(*CreateCampIdentifiers.PREVIEW_CAMP_ABOUT_URL_VERIFY)
        text44 = self.find_element(*CreateCampIdentifiers.PREVIEW_CAMP_ABOUT_URL_VERIFY).text

        if text1 == text11 and text2 == text22 and text3 == text33 and text4 == text44:
            return CanonizerEditCampPage(self.driver)
        else:
            print("Text not matching")

    def verify_cancel_button_on_preview_modal(self):
        self.verify_submit_camp_update_button()
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, 'campHistory_campStatementCollapseButtons__LVwiX')))
        except TimeoutException:
            pass
        self.hover(*CreateCampIdentifiers.PREVIEW_BUTTON)
        self.find_element(*CreateCampIdentifiers.PREVIEW_BUTTON).click()
        self.hover(*CreateCampIdentifiers.PREVIEW_CANCEL_BUTTON)
        self.find_element(*CreateCampIdentifiers.PREVIEW_CANCEL_BUTTON).click()
        self.hover(*CreateCampIdentifiers.CAMP_UPDATE_PAGE_TITLE)
        page_title = self.find_element(*CreateCampIdentifiers.CAMP_UPDATE_PAGE_TITLE).text
        if page_title == message['Create_Camp']['CAMP_UPDATE_PAGE_TITLE']:
            return CanonizerEditCampPage(self.driver)
        else:
            print("Title not found or is not matching")

    def verify_submitter_nick_name_on_preview_modal(self):
        self.verify_submit_camp_update_button()
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, 'ant-btn ant-btn-primary ant-btn-lg cancel-btn')))
        except TimeoutException:
            pass
        self.find_element(*CreateCampIdentifiers.PREVIEW_BUTTON).click()
        self.hover(*CreateCampIdentifiers.PREVIEW_NICK_NAME_VERIFY)
        text1 = self.find_element(*CreateCampIdentifiers.PREVIEW_NICK_NAME_VERIFY).text
        self.find_element(*CreateCampIdentifiers.PREVIEW_NICK_NAME_VERIFY).click()
        self.hover(*CreateCampIdentifiers.USER_PROFILE_NICK_NAME_VERIFY)
        text2 = self.find_element(*CreateCampIdentifiers.USER_PROFILE_NICK_NAME_VERIFY).text
        if text1 == text2:
            return CanonizerEditCampPage(self.driver)
        else:
            print("Text not matching")

    def verify_compare_camps_button_functionality(self):
        self.load_camp_manage_edit_page()
        self.hover(*CreateCampIdentifiers.COMPARE_CHECKBOX1)
        self.find_element(*CreateCampIdentifiers.COMPARE_CHECKBOX1).click()
        self.hover(*CreateCampIdentifiers.COMPARE_CHECKBOX2)
        self.find_element(*CreateCampIdentifiers.COMPARE_CHECKBOX2).click()

        self.hover(*CreateCampIdentifiers.COMPARE_CAMP_BUTTON)
        self.find_element(*CreateCampIdentifiers.COMPARE_CAMP_BUTTON).click()
        self.hover(*CreateCampIdentifiers.CAMP_HISTORY_COMPARISON)
        page_title = self.find_element(*CreateCampIdentifiers.CAMP_HISTORY_COMPARISON).text
        if page_title == message['Create_Camp']['CAMP_HISTORY_COMPARISON']:
            return CanonizerEditCampPage(self.driver)
        else:
            print("Title not found or is not matching")

    def verify_camps_name_on_camp_history_comparison_page(self):
        self.load_camp_manage_edit_page()
        self.hover(*CreateCampIdentifiers.CAMP_NAME1)
        text1 = self.find_element(*CreateCampIdentifiers.CAMP_NAME1).text
        self.hover(*CreateCampIdentifiers.COMPARE_CHECKBOX1)
        self.find_element(*CreateCampIdentifiers.COMPARE_CHECKBOX1).click()
        self.hover(*CreateCampIdentifiers.CAMP_NAME2)
        text2 = self.find_element(*CreateCampIdentifiers.CAMP_NAME2).text
        self.hover(*CreateCampIdentifiers.COMPARE_CHECKBOX2)
        self.find_element(*CreateCampIdentifiers.COMPARE_CHECKBOX2).click()
        self.hover(*CreateCampIdentifiers.COMPARE_CAMP_BUTTON)
        self.find_element(*CreateCampIdentifiers.COMPARE_CAMP_BUTTON).click()

        self.hover(*CreateCampIdentifiers.COMPARE_CAMP1)
        text3 = self.find_element(*CreateCampIdentifiers.COMPARE_CAMP1).text
        self.hover(*CreateCampIdentifiers.COMPARE_CAMP2)
        text4 = self.find_element(*CreateCampIdentifiers.COMPARE_CAMP2).text
        if text1 == text4 and text2 == text3:
            return CanonizerEditCampPage(self.driver)
        else:
            print("Text not matching")



    def submit_camp_update(self, camp_about_url):
        self.verify_submit_camp_update_button()
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, 'campHistory_campStatementCollapseButtons__LVwiX')))
        except TimeoutException:
            pass
            for i in range(0, 60):
                self.find_element(*CreateCampIdentifiers.EDIT_CAMP_URL).send_keys(Keys.BACKSPACE)

        self.find_element(*CreateCampIdentifiers.EDIT_CAMP_URL).send_keys(camp_about_url)
        self.hover(*CreateCampIdentifiers.SUBMIT_UPDATE_BUTTON)
        self.find_element(*CreateCampIdentifiers.SUBMIT_UPDATE_BUTTON).click()
        self.hover(*CreateCampIdentifiers.INVALID_CAMP_ABOUT_URL_ERROR)
        error = self.find_element(*CreateCampIdentifiers.INVALID_CAMP_ABOUT_URL_ERROR).text
        if error == message['Create_Camp']['INVALID_CAMP_ABOUT_URL_ERROR']:
            return CanonizerEditCampPage(self.driver)
        else:
            print("Error not found or is not matching")



































