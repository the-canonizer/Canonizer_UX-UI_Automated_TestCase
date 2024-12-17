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
    
    # TC_LOAD_CREATE_CAMP_PAGE
    def test_load_create_camp_page(self):
        print("\n" + str(test_cases('TC_LOAD_CREATE_CAMP_PAGE')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page()
        result = self.driver.current_url
        assert "/camp/create/" in result
        # TC_CREATE_CAMP_WITH_VALID_DATA
    def test_create_camp_with_valid_data(self):
        print("\n" + str(test_cases('TC_CREATE_CAMP_WITH_VALID_DATA')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        result = self.driver.current_url
        assert "topic" in result

    # TC_CREATE_CAMP_WITH_BLANK_CAMP_NAME
    def test_create_camp_with_blank_camp_name(self):
        print("\n" + str(test_cases('TC_CREATE_CAMP_WITH_BLANK_CAMP_NAME')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_blank_camp_name(CREATE_CAMP_LIST_2)
        result = self.driver.find_element(By.ID, "create_new_camp_camp_name_help").text
        assert "Please enter camp name!" in result

    # TC_CREATE_CAMP_WITH_DUPLICATE_CAMP_NAME
    def test_create_camp_with_duplicate_camp_name(self):
        print("\n" + str(test_cases('TC_CREATE_CAMP_WITH_DUPLICATE_CAMP_NAME')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_duplicate_camp_name(CREATE_CAMP_LIST_5)
        result = self.driver.current_url
        assert "/camp/create/" in result

    # TC_CREATE_CAMP_WITH_INVALID_CAMP_ABOUT_URL
    def test_create_camp_with_invalid_camp_about_url(self):
        print("\n" + str(test_cases('TC_CREATE_CAMP_WITH_INVALID_CAMP_ABOUT_URL')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_duplicate_camp_name(CREATE_CAMP_LIST_4)
        result = self.driver.current_url
        assert "/camp/create/" in result
    
    # TC_CREATE_CAMP_WITHOUT_ENTERING_DATA_IN_MANDATORY_FIELDS
    def test_create_camp_without_entering_data_in_mandatory_fields(self):
        print("\n" + str(test_cases('TC_CREATE_CAMP_WITHOUT_ENTERING_DATA_IN_MANDATORY_FIELDS')))
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_duplicate_camp_name(CREATE_CAMP_LIST_2)
        result = self.driver.current_url
        assert "/camp/create/" in result
    
     # TC_LOAD_ADD_NEW_CAMP_STATEMENT_PAGE

    def test_camp_statement_button(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        result = self.driver.find_element(By.ID, "add-camp-statement-btn").text
        assert "Add Statement" in result
    def test_load_camp_statement_page(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampStatementPage(self.driver).click_add_camp_statement()
        result = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/section/main/div/div/div[2]/div/div/div/header/div[1]").text
        assert "Adding Camp Statement" in result

    def test_add_camp_statement_with_valid_data(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampStatementPage(self.driver).add_camp_statement()
        result = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/section/main/div/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button[1]/span").text
        assert "Edit Based On This" in result
    def test_add_camp_statement_page_with_asterisk(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampStatementPage(self.driver).add_camp_statement_asterisk()
        result = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/section/main/div/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button[1]/span").text
        assert "Edit Based On This" in result

    def test_add_camp_statement_without_mandatory_field(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampStatementPage(self.driver).add_camp_statement_without_mandatory_data()
        result = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/section/main/div/div/div[2]/div/div/div/form/div/div[3]/div/div/div/div/div/button[2]/span[1]").text
        assert "Publish Statement" in result

    def test_add_camp_statement_with_trailing_spaces(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampStatementPage(self.driver).add_camp_statement_with_trailing_spaces()
        result = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/section/main/div/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button[1]/span").text
        assert "Edit Based On This" in result

    def test_add_camp_statement_with_blank_data(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampStatementPage(self.driver).add_camp_statement_with_blank_data()
        result = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/section/main/div/div/div[2]/div/div/div/form/div/div[3]/div/div/div/div/div/button[2]/span[1]").text
        assert "Publish Statement" in result
    
   def test_click_create_thread_button(self):
        print("\n" + str(test_cases('TC_CLICK_CREATE_THREAD_BUTTON')))
        self.login_to_canonizer_app()
        CanonizerCampForumPage(self.driver).load_camp_forum_page(DEFAULT_TOPIC)
        CanonizerCampForumPage(self.driver).click_create_thread_button()
        result = self.driver.current_url
        assert "/threads/create" in result

    # TC_CREATE_THREAD_WITH_VALID_DATA
    def test_create_thread_with_valid_data(self):
        print("\n" + str(test_cases('TC_CREATE_THREAD_WITH_VALID_DATA')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampForumPage(self.driver).create_thread_with_valid_data()
        result = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/section/section/main/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr/td[1]/div/a/span").text
        assert "test" in result

    # TC_CREATE_THREAD_WITH_BLANK_TITLE
    def test_create_thread_with_blank_title(self):
        print("\n" + str(test_cases('TC_CREATE_THREAD_WITH_BLANK_TITLE')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampForumPage(self.driver).create_thread_with_blank_title_name()
        result = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/section/section/main/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr/td[1]/div/a/span").text
        assert "test" in result

    # TC_CREATE_THREAD_WITH_SPECIAL_CHARS
    def test_create_thread_with_special_chars(self):
        print("\n" + str(test_cases('TC_CREATE_THREAD_WITH_SPECIAL_CHARS')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampForumPage(self.driver).create_thread_with_special_chars()
        result = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/section/section/main/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr/td[1]/div/a/span").text
        assert "test" in result

    # TC_CREATE_THREAD_WITH_BLANK_MANDATORY_FIELDS
    def test_create_thread_with_blank_mandatory_fields(self):
        print("\n" + str(test_cases('TC_CREATE_THREAD_WITH_BLANK_MANDATORY_FIELDS')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampForumPage(self.driver).create_thread_with_blank_mandatory_fields()
        result = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/section/section/main/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr/td[1]/div/a/span").text
        assert "test" in result

    # TC_CREATE_THREAD_WITH_DUPLICATE_TITLE
    def test_create_thread_with_duplicate_title(self):
        print("\n" + str(test_cases('TC_CREATE_THREAD_WITH_DUPLICATE_TITLE')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampForumPage(self.driver).create_thread_with_duplicate_title()
        result = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/section/section/main/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr/td[1]/div/a/span").text
        assert "test" in result

    # TC_CREATE_THREAD_WITH_VALID_DATA_WITH_ENTER_KEY
    def test_create_thread_with_valid_data_with_enter_key(self):
        print("\n" + str(test_cases('TC_CREATE_THREAD_WITH_VALID_DATA_WITH_ENTER_KEY')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampForumPage(self.driver).create_thread_with_valid_data_with_enter_key()
        result = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/section/section/main/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr/td[1]/div/a/span").text
        assert "test" in result

    # TC_CREATE_THREAD_WITH_TRAILING_SPACES
    def test_create_thread_with_trailing_spaces(self):
        print("\n" + str(test_cases('TC_CREATE_THREAD_WITH_TRAILING_SPACES')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampForumPage(self.driver).create_thread_with_trailing_spaces()
        result = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/section/section/main/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr/td[1]/div/a/span").text
        assert "test" in result
    
   def test_browse_start_topic(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(By.ID, "create-topic-text").click()
        result = self.driver.current_url
        assert "/create/topic" in result

    def test_upload_files(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(By.ID, "menu-item-2").click()
        result = self.driver.current_url
        assert "/uploadFile" in result

    def test_browse_videos(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(By.ID, "menu-item-6").click()
        result = self.driver.current_url
        assert "/videos" in result

    def test_browse_help(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(By.ID, "menu-item-4").click()
        result = self.driver.current_url
        assert "/topic/132-Help/1-Agreement?is_tree_open=1" in result

    def test_browse_notification(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(By.XPATH, "/html/body/div[1]/section/header/div/nav/ul/li[11]/span/span").click()
        result = self.driver.find_element(By.ID, "notification-title").text
        assert "notifications" in result

    def test_browse_profile_setting(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(By.ID, "profile_link").click()
        result = self.driver.find_element(By.ID, "link-profile-info").text
        assert "Account Settings" in result

    def test_browse_profile_setting_account_setting(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(By.ID, "profile_link").click()
        self.driver.find_element(By.ID, "link-profile-info").click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/settings?tab=profile_info" in result

    def test_browse_profile_setting_supported_camps(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(By.ID, "profile_link").click()
        self.driver.find_element(By.ID, "link-supported-camps").click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/settings?tab=direct_supported_camps" in result 

   def test_footer_browse_button(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(By.ID, "footer-explore-link-1").click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/browse" in result


    def test_footer_create_topic_button(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(By.ID, "footer-explore-link-3").click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/create/topic" in result

    def test_footer_upload_file_button(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(By.ID, "footer-explore-link-5").click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/uploadFile" in result

    def test_footer_sitemap_button(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(By.ID, "footer-explore-link-10").click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/sitemap" in result

    def test_footer_videos_button(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(By.ID, "footer-explore-link-13").click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/videos" in result

    def test_footer_help_button(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(By.ID, "footer-learn-more-link-4").click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/topic/132-Help/1-Agreement?is_tree_open=1" in result

    def test_footer_white_paper_button(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(By.ID, "footer-learn-more-link-6").click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/files/2012_amplifying_final.pdf" in result

    def test_footer_jobs_button(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(By.ID, "footer-learn-more-link-8").click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/topic/6-Canonizer-Jobs/1-Agreement?is_tree_open=1" in result

    def test_footer_privacy_policy_button(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(By.ID, "footer-learn-more-link-9").click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/privacy-policy" in result

    def test_footer_term_and_services_button(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(By.ID, "footer-learn-more-link-10").click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/terms-and-services" in result
   
    def test_footer_upload_file_button(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(By.ID, "footer-explore-link-5").click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/uploadFile" in result 

  def teardown_method(self):

        self.driver.close()


if __name__ == "__main__":
