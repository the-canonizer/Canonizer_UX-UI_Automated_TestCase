import unittest
from datetime import datetime
from subprocess import run
# import HtmlTestRunner
import requests
import xmlrunner as xmlrunner
from selenium.webdriver.common import keys
from xmlrunner import *
from selenium.webdriver.common.keys import Keys
from urllib3.util import response
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import TimeoutException


from Config import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import string
import random
import time

import pytest
from CanonizerTestCases import test_cases
from CanonizerAddEditNewsPage import CanonizerAddNewsPage
from CanonizerBrowsePage import CanonizerBrowsePage
from CanonizerCampForum import CanonizerCampForumPage
from CanonizerCampStatementPage import CanonizerCampStatementPage
from CanonizerCreateUpdateCampPage import CanonizerCreateCampPage, CanonizerEditCampPage
from CanonizerCreateUpdateTopicPage import CanonizerCreateNewTopic, CanonizerUpdateTopicPage

from CanonizerLoginPage import CanonizerLoginPage
from CanonizerRegistrationPage import CanonizerRegisterPage
from Identifiers import RegistrationPageIdentifiers, CreateTopicIdentifiers


class TestPages:

    def setup_method(self):
        """
            Initialize the Things
            :return:
        """
        driver_location = DEFAULT_CHROME_DRIVER_LOCATION
        options = webdriver.ChromeOptions()
        options.binary_location = DEFAULT_BINARY_LOCATION
        # will run all the test cases
        # options.add_argument('headless')

        options.add_argument("--start-maximized")
        # options.add_argument("/home/vivekkumar/.config/google-chrome/profile")

        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver = webdriver.Chrome()
        self.driver.get(DEFAULT_BASE_URL)
        self.driver.implicitly_wait(30)

    def driver(self):
        # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver = webdriver.Chrome()
        self.action = ActionChains(self.driver)

    def login_to_canonizer_app(self):
        """
            This Application will allow you to login to canonizer App on need basis
        :param flag:
        :return:
        """
        # result = CanonizerLoginPage(self.driver).click_login_page_button().login_with_valid_user(DEFAULT_USER, DEFAULT_PASS).get_url()
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button()
        CanonizerLoginPage(self.driver).click_on_login_page_button().verify_the_login_functionality_by_entering_the_registered_credential(DEFAULT_USER, DEFAULT_PASS)
        self.driver.maximize_window()


    def test_login_to_canonizer(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        result = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/div[2]/section/div/button/span[1]").text
        assert "Browse More" in result
    def test_click_on_register_button(self):
        print("\n" + str(test_cases('TC_CLICK_ON_REGISTER_BUTTON')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button()

        result = self.driver.find_element(*RegistrationPageIdentifiers.REGISTRATION_TITLE).text
        assert "Create your account" in result

    # TC_REGISTER_PAGE_MANDATORY_FIELDS_MARKED_WITH_ASTERISK
    def test_register_page_mandatory_fields_are_marked_with_asterisk(self):
        assert CanonizerRegisterPage(
            self.driver).click_register_button().register_page_mandatory_fields_are_marked_with_asterisk()

    def test_registration_with_valid_credential(self):
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_17)
        result = self.driver.find_element(By.ID, "otp-note-text").text
        assert "Note : Registration code has been sent to your registered email address." in result

    def test_registration_first_name_with_spaces(self):
        print("\n" + str(test_cases('TC_REGISTER_WITH_BLANK_SPACES_FIRST_NAME')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_18)
        result = self.driver.find_element(By.ID, "otp-note-text").text
        assert "Note : Registration code has been sent to your registered email address." in result

    # TC_REGISTER_WITH_BLANK_FIRST_NAME
    def test_registration_with_blank_first_name(self, ):
        print("\n" + str(test_cases('TC_REGISTER_WITH_BLANK_FIRST_NAME')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_3)
        result = self.driver.find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
        assert "Please input your first name!" in result

    # TC_REGISTRATION_WITH_BLANK_EMAIL
    def test_registration_with_blank_email(self):
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_BLANK_EMAIL')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_5)
        result = self.driver.find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
        assert "Please input your E-mail!" in result

    # TC_REGISTER_WITH_BLANK_LAST_NAME
    def test_registration_with_blank_last_name(self):
        print("\n" + str(test_cases('TC_REGISTER_WITH_BLANK_LAST_NAME')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_4)
        result = self.driver.find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
        assert "Please input your last name!" in result

    # TC_REGISTRATION_WITH_BLANK_PASSWORD
    def test_registration_with_blank_password(self):
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_BLANK_PASSWORD')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_6)
        result = self.driver.find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
        assert "Please input your password!" in result

    # TC_REGISTRATION_WITH_INVALID_PASSWORD_LENGTH
    def test_registration_with_invalid_password_length(self):
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_INVALID_PASSWORD_LENGTH')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_7)
        result = self.driver.find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
        assert "Password must contain small, capital letter, number and special character like Abc@1234." in result

    # TC_REGISTER_WITH_BLANK_SPACES_FIRST_NAME

    # TC_REGISTRATION_WITH_INVALID_EMAIL
    def test_registration_with_invalid_email(self):
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_INVALID_EMAIL')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_14)
        result = self.driver.find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
        assert "Please enter a valid email address." in result

    # TC_CHECK_LOGIN_PAGE_OPEN_CLICK_ON_LOGIN_HERE_LINK
    def test_check_login_page_open_click_login_here_link(self):
        print("\n" + str(test_cases('TC_CHECK_LOGIN_PAGE_OPEN_CLICK_ON_LOGIN_HERE_LINK')))
        result = CanonizerRegisterPage(self.driver).check_login_page_open_click_login_here_link().get_url()
        assert "" in result

    # TC_VERIFY_THE_FUNCTIONALITY_OF_REGISTRATION_WITH_MANDATORY_FIELDS
    def test_verify_the_functionality_of_registration_with_entering_data_in_mandatory_fields(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_FUNCTIONALITY_OF_REGISTRATION_WITH_MANDATORY_FIELDS')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_15)
        result = self.driver.find_element(By.ID, "otp-note-text").text
        assert "Note : Registration code has been sent to your registered email address." in result

    # TC_VERIFY_THE_FUNCTIONALITY_OF_REGISTRATION_WITH_MOBILE_NUMBER_FIELDS
    def test_verify_the_functionality_0f_registration_with_entering_data_in_mobile_number_field(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_FUNCTIONALITY_OF_REGISTRATION_WITH_MOBILE_NUMBER_FIELDS')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_16)
        result = self.driver.find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
        assert "Please input valid phone number!" in result

    def test_click_on_login_button(self):
        print("\n" + str(test_cases('TC_CLICK_ON_LOGIN_BUTTON')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button()
        CanonizerLoginPage(self.driver).click_on_login_page_button()
        result = self.driver.find_element(By.ID, "login-btn").text
        assert "Log In" in result


    # TC_LOGIN_WITH_REGISTERED_CREDENTIALS
    def test_login_with_registered_credentials(self):
        print("\n" + str(test_cases('TC_LOGIN_WITH_REGISTERED_CREDENTIALS')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button()
        CanonizerLoginPage(self.driver).click_on_login_page_button().verify_the_login_functionality_by_entering_the_registered_credential(DEFAULT_USER, DEFAULT_PASS)
        result = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/header/div/nav/ul/li[1]/a/span[1]").text
        assert "Start a Topic" in result

    # TC_VERIFY_THE_LOGIN_WITH_BLANK_EMAIL
    def test_verify_the_login_with_blank_email(self):
        print("\n" + str(test_cases('TC_LOGIN_WITH_REGISTERED_CREDENTIALS')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button()
        CanonizerLoginPage(self.driver).click_on_login_page_button().verify_the_login_with_blank_email("", DEFAULT_PASS)
        result = self.driver.find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
        assert "Please input your Email!" in result

    # TC_VERIFY_THE_LOGIN_WITH_BLANK_PASSWORD
    def test_verify_the_login_with_blank_password(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_LOGIN_WITH_BLANK_PASSWORD')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button()
        CanonizerLoginPage(self.driver).click_on_login_page_button().verify_the_login_with_blank_password(DEFAULT_USER, "")
        result = self.driver.find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
        assert "Please input your Password!" in result

    # TC_LOGIN_WITH_INVALID_EMAIL
    def test_login_with_invalid_email(self):
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button()
        CanonizerLoginPage(self.driver).click_on_login_page_button().verify_the_login_with_invalid_email_format(DEFAULT_INVALID_USER, DEFAULT_PASS)
        result = self.driver.find_element(By.CLASS_NAME, "ant-form-item-explain-error").text
        assert "Input is not valid!" in result

    # TC_VERIFY_ONE_TIME_REQUEST_CODE_WITH_VALID_CREDENTIALS
    def test_verify_one_time_request_code_with_valid_credentials(self):
        print("\n" + str(test_cases('TC_VERIFY_ONE_TIME_REQUEST_CODE_WITH_VALID_CREDENTIALS')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button()
        CanonizerLoginPage(self.driver).click_on_login_page_button().verify_one_time_request_code_with_valid_credentials(DEFAULT_USER)
        result = self.driver.find_element(By.ID, "resent-otp-btn").text
        assert "Resend OTP" in result

                # ----- CREATE TOPIC Test Cases Start -----

    # TC_CLICK_CREATE_TOPIC_WITH_USER_LOGIN
    def test_click_create_new_topic_page_button(self):
        print("\n" + str(test_cases('TC_CLICK_CREATE_TOPIC_WITH_USER_LOGIN')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        result = self.driver.current_url
        assert "/create/topic" in result

    # TC_CLICK_CREATE_TOPIC_WITHOUT_USER_LOGIN
    def test_click_create_topic_without_user_login(self):
        print("\n" + str(test_cases('TC_CLICK_CREATE_TOPIC_WITHOUT_USER_LOGIN')))
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        CanonizerCreateNewTopic(self.driver).click_create_topic_button_without_login()
        result = self.driver.current_url
        assert "/login?returnUrl=%2Fcreate%2Ftopic" in result

    # TC_CREATE_TOPIC_WITH_BLANK_TOPIC_NAME
    def test_create_topic_with_blank_topic_name(self):
        print("\n" + str(test_cases('TC_CREATE_TOPIC_WITH_BLANK_TOPIC_NAME')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_blank_topic()
        result = self.driver.find_element(By.ID, "create_new_topic_topic_name_help").text
        assert "Enter a valid Topic Name" in result

    # TC_CREATE_NEW_TOPIC_WITH_VALID_DATA
    def test_create_topic_name_with_valid_data(self):
        print("\n" + str(test_cases('TC_CREATE_TOPIC_WITH_VALID_DATA')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        result = self.driver.current_url
        assert "1-Agreement" in result

    def test_create_same_topic_name_with_valid_data(self):
        print("\n" + str(test_cases('TC_CREATE_TOPIC_WITH_VALID_DATA')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_same_topic("same topic")
        result = self.driver.find_element(By.CLASS_NAME, "ant-typography text-canRed font-medium text-base !mb-2").text
        assert "A Topic with this exact name already exists!" in result

    def test_create_same_topic_name_error_link(self):
        print("\n" + str(test_cases('TC_CREATE_TOPIC_WITH_VALID_DATA')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("new summary", "same topic", DEFAULT_NAMESPACE)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[2]/form/div[1]/div[1]/a").click()
        result = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[1]/div/div[1]/div/div/div/div[1]/span[2]").text
        assert "same topic" in result
    # TC_CREATE_NEW_TOPIC_WITH_SPECIAL_CHARS
    def test_create_topic_with_special_chars(self):
        print("\n", str(test_cases('TC_CREATE_NEW_TOPIC_WITH_SPECIAL_CHARS')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_special_chars("New Topic&^&#$(# " + add_name)
        result = self.driver.current_url
        assert "topic" in result

    # TC_CREATE_NEW_WITHOUT_MANDATORY_FIELDS_DATA
    def test_create_topic_without_entering_mandatory_fields(self):
        print("\n", str(test_cases('TC_CREATE_NEW_WITHOUT_MANDATORY_FIELDS_DATA')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_without_entering_mandatory_fields(" ")
        result = self.driver.current_url        
        assert "create/topic" in result
    
    def teardown_method(self):

        self.driver.close()


if __name__ == "__main__":
