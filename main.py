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
from Identifiers *


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
    def test_click_on_join_now(self):
        print("\n" + str(test_cases('TC_CLICK_ON_REGISTER_BUTTON')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).join_now()

        result = self.driver.find_element(*RegistrationPageIdentifiers.REGISTRATION_TITLE).text
        assert "Create your account" in result

    # TC_REGISTER_PAGE_MANDATORY_FIELDS_MARKED_WITH_ASTERISK
    def test_register_page_mandatory_fields_are_marked_with_asterisk(self):
        assert CanonizerRegisterPage(
            self.driver).click_register_button().register_page_mandatory_fields_are_marked_with_asterisk()

    def test_registration_with_valid_credential(self):
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_17)
        result = self.driver.find_element(*RegistrationPageIdentifiers.OTP_SENT).text
        assert "Note : Registration code has been sent to your registered email address." in result

    def test_registration_first_name_with_spaces(self):
        print("\n" + str(test_cases('TC_REGISTER_WITH_BLANK_SPACES_FIRST_NAME')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_18)
        result = self.driver.find_element(*RegistrationPageIdentifiers.OTP_SENT).text
        assert "Note : Registration code has been sent to your registered email address." in result

    # TC_REGISTER_WITH_BLANK_FIRST_NAME
    def test_registration_with_blank_first_name(self, ):
        print("\n" + str(test_cases('TC_REGISTER_WITH_BLANK_FIRST_NAME')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_3)
        result = self.driver.find_element(*RegistrationPageIdentifiers.FIRST_NAME_VALIDATION).text
        assert "Please input your first name!" in result

    # TC_REGISTRATION_WITH_BLANK_EMAIL
    def test_registration_with_blank_email(self):
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_BLANK_EMAIL')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_5)
        result = self.driver.find_element(*RegistrationPageIdentifiers.EMAIL_VALIDATION).text
        assert "Please input your E-mail!" in result

    # TC_REGISTER_WITH_BLANK_LAST_NAME
    def test_registration_with_blank_last_name(self):
        print("\n" + str(test_cases('TC_REGISTER_WITH_BLANK_LAST_NAME')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_4)
        result = self.driver.find_element(*RegistrationPageIdentifiers.LAST_NAME_VALIDATION).text
        assert "Please input your last name!" in result

    # TC_REGISTRATION_WITH_BLANK_PASSWORD
    def test_registration_with_blank_password(self):
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_BLANK_PASSWORD')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_6)
        result = self.driver.find_element(*RegistrationPageIdentifiers.PASSWORD_VALIDATION).text
        assert "Please input your password!" in result

    # TC_REGISTRATION_WITH_INVALID_PASSWORD_LENGTH
    def test_registration_with_invalid_password_length(self):
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_INVALID_PASSWORD_LENGTH')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_7)
        result = self.driver.find_element(*RegistrationPageIdentifiers.PASSWORD_TYPE_VALIDATION).text
        assert "Password must contain small, capital letter, number and special character like Abc@1234." in result

    # TC_REGISTER_WITH_BLANK_SPACES_FIRST_NAME

    # TC_REGISTRATION_WITH_INVALID_EMAIL
    def test_registration_with_invalid_email(self):
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_INVALID_EMAIL')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_14)
        result = self.driver.find_element(*RegistrationPageIdentifiers.VALID_EMAIL).text
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
        result = self.driver.find_element(*RegistrationPageIdentifiers.OTP_SENT).text
        assert "Note : Registration code has been sent to your registered email address." in result

    # TC_VERIFY_THE_FUNCTIONALITY_OF_REGISTRATION_WITH_MOBILE_NUMBER_FIELDS
    def test_verify_the_functionality_0f_registration_with_entering_data_in_mobile_number_field(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_FUNCTIONALITY_OF_REGISTRATION_WITH_MOBILE_NUMBER_FIELDS')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_16)
        result = self.driver.find_element(*RegistrationPageIdentifiers.VALID_PHONE_NUMBER).text
        assert "Please input valid phone number!" in result

    def test_click_on_login_button(self):
        print("\n" + str(test_cases('TC_CLICK_ON_LOGIN_BUTTON')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button()
        CanonizerLoginPage(self.driver).click_on_login_page_button()
        result = self.driver.find_element(*LoginPageIdentifiers.LOGIN_BUTTON_HOMEPAGE).text
        assert "Log In" in result


    # TC_LOGIN_WITH_REGISTERED_CREDENTIALS
    def test_login_with_registered_credentials(self):
        print("\n" + str(test_cases('TC_LOGIN_WITH_REGISTERED_CREDENTIALS')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button()
        CanonizerLoginPage(self.driver).click_on_login_page_button().verify_the_login_functionality_by_entering_the_registered_credential(DEFAULT_USER, DEFAULT_PASS)
        result = self.driver.find_element(*LoginPageIdentifiers.START_TOPIC_BUTTON).text
        assert "Start a Topic" in result

    # TC_VERIFY_THE_LOGIN_WITH_BLANK_EMAIL
    def test_verify_the_login_with_blank_email(self):
        print("\n" + str(test_cases('TC_LOGIN_WITH_REGISTERED_CREDENTIALS')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button()
        CanonizerLoginPage(self.driver).click_on_login_page_button().verify_the_login_with_blank_email("", DEFAULT_PASS)
        result = self.driver.find_element(*LoginPageIdentifiers.EMAIL_VALIDATION).text
        assert "Please input your Email!" in result

    # TC_VERIFY_THE_LOGIN_WITH_BLANK_PASSWORD
    def test_verify_the_login_with_blank_password(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_LOGIN_WITH_BLANK_PASSWORD')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button()
        CanonizerLoginPage(self.driver).click_on_login_page_button().verify_the_login_with_blank_password(DEFAULT_USER, "")
        result = self.driver.find_element(*LoginPageIdentifiers.PASSWORD_VALIDATION).text
        assert "Please input your Password!" in result

    # TC_LOGIN_WITH_INVALID_EMAIL
    def test_login_with_invalid_email(self):
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button()
        CanonizerLoginPage(self.driver).click_on_login_page_button().verify_the_login_with_invalid_email_format(DEFAULT_INVALID_USER, DEFAULT_PASS)
        result = self.driver.find_element(*LoginPageIdentifiers.VALID_EMAIL).text
        assert "Input is not valid!" in result

    # TC_VERIFY_ONE_TIME_REQUEST_CODE_WITH_VALID_CREDENTIALS
    def test_verify_one_time_request_code_with_valid_credentials(self):
        print("\n" + str(test_cases('TC_VERIFY_ONE_TIME_REQUEST_CODE_WITH_VALID_CREDENTIALS')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button()
        CanonizerLoginPage(self.driver).click_on_login_page_button().verify_one_time_request_code_with_valid_credentials(DEFAULT_USER)
        result = self.driver.find_element(*LoginPageIdentifiers.RESEND_OTP).text
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
        result = self.driver.find_element(*CreateTopicIdentifiers.VALID_TOPIC_NAME).text
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
        result = self.driver.find_element(*CreateTopicIdentifiers.SAME_TOPIC_NAME).text
        assert "A Topic with this exact name already exists!" in result

    def test_create_same_topic_name_error_link(self):
        print("\n" + str(test_cases('TC_CREATE_TOPIC_WITH_VALID_DATA')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("new summary", "same topic", DEFAULT_NAMESPACE)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[2]/form/div[1]/div[1]/a").click()
        result = self.driver.find_element(*CreateTopicIdentifiers.SAME_TOPIC_TITLE).text
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
    # ----- UPDATE TOPIC Test Cases Start -----

    # TC_LOAD_TOPIC_HISTORY_PAGE
    def test_load_topic_history_page(self):
        print("\n" + str(test_cases('TC_LOAD_TOPIC_HISTORY_PAGE')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()
        result = self.driver.find_element(*CreateTopicIdentifiers.UPDATE_TOPIC_TITLE).text
        assert "Update Topic" in result

    # TC_VERIFY_TOPIC_NAME_ON_TOPIC_HISTORY_PAGE
    def test_verify_topic_name_on_topic_history_page(self):
        print("\n" + str(test_cases('TC_VERIFY_TOPIC_NAME_ON_TOPIC_HISTORY_PAGE')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()
        assert "/topic/history/" in result.get_url()

    # TC_VERIFY_SUBMITTER_NICK_NAME_LINK_ON_USER_PROFILE
    def test_verify_submitter_nick_name_link_on_user_profile(self):
        print("\n" + str(test_cases('TC_VERIFY_SUBMITTER_NICK_NAME_LINK_ON_USER_PROFILE')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()
        assert "/user/supports/" in result.get_url()

    # TC_VERIFY_SUBMIT_TOPIC_UPDATE_BUTTON
    def test_verify_submit_topic_update_button(self):
        print("\n" + str(test_cases('TC_VERIFY_SUBMIT_TOPIC_UPDATE_BUTTON')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()
        assert "manage/topic/" in result.get_url()

    # TC_UPDATE_TOPIC_WITH_DUPLICATE_NAME
    def test_update_topic_with_duplicate_name(self):
        print("\n" + str(test_cases('TC_UPDATE_TOPIC_WITH_DUPLICATE_NAME')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()
        assert "manage/topic/" in result.get_url()

    # TC_VERIFY_CANCEL_BUTTON_FUNCTIONALITY_ON_TOPIC_UPDATE_PAGE
    def test_verify_cancel_button_functionality_on_topic_update_page(self):
        print("\n" + str(test_cases('TC_VERIFY_CANCEL_BUTTON_FUNCTIONALITY_ON_TOPIC_UPDATE_PAGE')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()
        assert "/topic/history/" in result.get_url()

    # TC_VERIFY_PREVIEW_BUTTON_FUNCTIONALITY_ON_TOPIC_UPDATE_PAGE
    def test_verify_preview_button_functionality_on_topic_update_page(self):
        print("\n" + str(test_cases('TC_VERIFY_PREVIEW_BUTTON_FUNCTIONALITY_ON_TOPIC_UPDATE_PAGE')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()

    # TC_VERIFY_SUBMITTER_NICK_NAME_ON_PREVIEW_MODAL
    def test_verify_submitter_nick_name_on_preview_modal(self):
        print("\n" + str(test_cases('TC_VERIFY_SUBMITTER_NICK_NAME_ON_PREVIEW_MODAL')))
        self.login_to_canonizer_app()
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page(DEFAULT_TOPIC) \
            .verify_submitter_nick_name_on_preview_modal()

    # TC_VERIFY_CANCEL_BUTTON_ON_PREVIEW_MODAL
    def test_verify_cancel_button_on_preview_modal(self):
        print("\n" + str(test_cases('TC_VERIFY_CANCEL_BUTTON_ON_PREVIEW_MODAL')))
        self.login_to_canonizer_app()
        result = CanonizerUpdateTopicPage(self.driver).load_topic_history_page(DEFAULT_TOPIC) \
            .verify_cancel_button_on_preview_modal()
        assert "/manage/topic/" in result.get_url()

    # TC_UPDATE_TOPIC_NAME_AND_VERIFY_SUBMIT_UPDATE_BUTTON
    def test_update_topic_name_and_verify_submit_update_button(self):
        print("\n" + str(test_cases('TC_UPDATE_TOPIC_NAME_AND_VERIFY_SUBMIT_UPDATE_BUTTON')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()
        assert "topic/history/" in result.get_url()
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
        result = self.driver.find_element(*CreateCampIdentifiers.CAMP_NAME_VALIDATION).text
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
    def test_load_camp_manage_edit_page(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerEditCampPage(self.driver).load_camp_manage_edit_page()
        result = self.driver.current_url
        assert "manage/camp" in result


    # TC_UPDATE_CAMP_WITH_INVALID_URL
    def test_submit_camp_update_with_invalid_url(self):
        self.login_to_canonizer_app()
        result = CanonizerEditCampPage(self.driver).load_topic_detail_page(DEFAULT_TOPIC)\
            .submit_camp_update_with_invalid_url(INVALID_CAMP_ABOUT_URL)
        assert "/manage/camp/" in result.get_url()

    # TC_UPDATE_CAMP_WITH_DUPLICATE_CAMP_NAME
    def test_update_camp_with_duplicate_camp_name(self):
        self.login_to_canonizer_app()
        result = CanonizerEditCampPage(self.driver).load_topic_detail_page(DEFAULT_TOPIC)\
            .update_camp_with_duplicate_camp_name(DUPLICATE_CAMP_NAME)
        assert "/manage/camp/" in result.get_url()


    # TC_VERIFY_CANCEL_BUTTON_FUNCTIONALITY_ON_CAMP_UPDATE_PAGE
    def test_verify_cancel_button_functionality_on_camp_update_page(self):
        self.login_to_canonizer_app()
        result = CanonizerEditCampPage(self.driver).load_topic_detail_page(DEFAULT_TOPIC)\
            .verify_cancel_button_functionality_on_camp_update_page()
        assert "/camp/history/" in result.get_url()

    # TC_VERIFY_PREVIEW_BUTTON_FUNCTIONALITY_ON_CAMP_UPDATE_PAGE
    def test_verify_preview_button_functionality_on_camp_update_page(self):
        self.login_to_canonizer_app()
        result = CanonizerEditCampPage(self.driver).load_topic_detail_page(DEFAULT_TOPIC) \
            .verify_preview_button_functionality_on_camp_update_page()
        assert "/manage/camp/" in result.get_url()
     # TC_LOAD_ADD_NEW_CAMP_STATEMENT_PAGE

    def test_camp_statement_button(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        result = self.driver.find_element(*CampStatementIdentifiers.ADD_STATEMENT_BUTTON).text
        assert "Add Statement" in result
    def test_load_camp_statement_page(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampStatementPage(self.driver).click_add_camp_statement()
        result = self.driver.find_element(*CampStatementIdentifiers.ADDING_CAMP_STATEMENT_POP_UP).text
        assert "Adding Camp Statement" in result

    def test_add_camp_statement_with_valid_data(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampStatementPage(self.driver).add_camp_statement()
        result = self.driver.find_element(*CampStatementIdentifiers.EDIT_BASED_ON_THIS).text
        assert "Edit Based On This" in result
    def test_add_camp_statement_page_with_asterisk(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampStatementPage(self.driver).add_camp_statement_asterisk()
        result = self.driver.find_element(*CampStatementIdentifiers.EDIT_BASED_ON_THIS).text
        assert "Edit Based On This" in result

    def test_add_camp_statement_without_mandatory_field(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampStatementPage(self.driver).add_camp_statement_without_mandatory_data()
        result = self.driver.find_element(*CampStatementIdentifiers.PUBLISH_STATEMENT).text
        assert "Publish Statement" in result

    def test_add_camp_statement_with_trailing_spaces(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampStatementPage(self.driver).add_camp_statement_with_trailing_spaces()
        result = self.driver.find_element(*CampStatementIdentifiers.EDIT_BASED_ON_THIS).text
        assert "Edit Based On This" in result

    def test_add_camp_statement_with_blank_data(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampStatementPage(self.driver).add_camp_statement_with_blank_data()
        result = self.driver.find_element(*CampStatementIdentifiers.PUBLISH_STATEMENT).text
        assert "Publish Statement" in result
        
    def test_camp_statement_template(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        campname = self.driver.find_element(*CampStatementIdentifiers.CAMP_NAME_1).text
        self.driver.find_element(*CampStatementIdentifiers.ADD_STATEMENT_BUTTON).click()
        result = self.driver.find_element(*CampStatementIdentifiers.CAMP_NAME_2).text
        assert campname in result
       #EDIT_CAMP_SATEMENT
    def test_load_edit_camp_statement(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampStatementPage(self.driver).add_camp_statement()
        CanonizerCampStatementPage(self.driver).load_edit_camp_statement()
        result = self.driver.current_url
        assert "manage" in result

    def test_edit_camp_statement(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampStatementPage(self.driver).add_camp_statement()
        CanonizerCampStatementPage(self.driver).load_edit_camp_statement()
        CanonizerCampStatementPage(self.driver).edit_camp_statement()
        result = self.driver.current_url
        assert "statement/history" in result
    def test_update_camp_statement_with_mandatory_field(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampStatementPage(self.driver).add_camp_statement()
        CanonizerCampStatementPage(self.driver).load_edit_camp_statement()
        CanonizerCampStatementPage(self.driver).update_camp_statement_with_mandatory_field()
        result = self.driver.current_url
        assert "statement/history" in result

    def test_edit_camp_statement_with_trailing_spaces(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampStatementPage(self.driver).add_camp_statement()
        CanonizerCampStatementPage(self.driver).load_edit_camp_statement()
        CanonizerCampStatementPage(self.driver).edit_camp_statement_with_trailing_spaces()
        result = self.driver.current_url
        assert "statement/history" in result

    def test_edit_camp_statement_with_blank_data(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampStatementPage(self.driver).add_camp_statement()
        CanonizerCampStatementPage(self.driver).load_edit_camp_statement()
        CanonizerCampStatementPage(self.driver).edit_camp_statement_with_blank_data()
        result = self.driver.current_url
        assert "statement/history" in result

    def test_compare_camp_statement(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampStatementPage(self.driver).add_camp_statement()
        CanonizerCampStatementPage(self.driver).load_edit_camp_statement()
        CanonizerCampStatementPage(self.driver).update_camp_statement_with_mandatory_field()
        CanonizerCampStatementPage(self.driver).compare_camp_statement()
        result = self.driver.current_url

        assert "compare" in result
    
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
        result = self.driver.find_element(*CampStatementIdentifiers.TEST_CAMP).text
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
        result = self.driver.find_element(*CampStatementIdentifiers.TEST_CAMP).text
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
        result = self.driver.find_element(*CampStatementIdentifiers.TEST_CAMP).text
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
        result = self.driver.find_element(*CampStatementIdentifiers.TEST_CAMP).text
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
        result = self.driver.find_element(*CampStatementIdentifiers.TEST_CAMP).text
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
        result = self.driver.find_element(*CampStatementIdentifiers.TEST_CAMP).text
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
        result = self.driver.find_element(*CampStatementIdentifiers.TEST_CAMP).text
        assert "test" in result
    def test_load_edit_thread_page(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampForumPage(self.driver).create_thread_with_valid_data()
        CanonizerCampForumPage(self.driver).load_edit_thread_page()

        result = self.driver.find_element(*CampStatementIdentifiers.TEST_CAMP).text
        assert "test" in result

    def test_edit_thread(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampForumPage(self.driver).create_thread_with_valid_data()
        CanonizerCampForumPage(self.driver).edit_thread()
        result = self.driver.find_element(*CampStatementIdentifiers.TEST_CAMP).text
        assert "test" in result
    
# TC_LOAD_ADD_NEWS_FEED_PAGE
    def test_load_add_news_page(self):
        print("\n" + str(test_cases('TC_LOAD_ADD_NEWS_FEED_PAGE')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button().create_topic_with_valid_data("New Topic " + add_name)
        CanonizerAddNewsPage(self.driver).load_add_news_page()
        result = self.driver.current_url
        assert "/addnews/" in result

    # TC_ADD_NEWS_PAGE_MANDATORY_FIELDS_ARE_MARKED_WITH_ASTERISK
    def test_add_news_page_mandatory_fields_are_marked_with_asterisk(self):
        print("\n" + str(test_cases('TC_ADD_NEWS_PAGE_MANDATORY_FIELDS_ARE_MARKED_WITH_ASTERISK')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button().create_topic_with_valid_data("New Topic " + add_name)
        CanonizerAddNewsPage(self.driver).load_add_news_page()
        CanonizerAddNewsPage(self.driver).add_news_page_mandatory_fields_are_marked_with_asterisk()
        assert CanonizerAddNewsPage(self.driver).load_add_news_page(DEFAULT_TOPIC).add_news_page_mandatory_fields_are_marked_with_asterisk()

    # TC_CREATE_NEWS_WITH_VALID_DATA
    def test_create_news_with_valid_data(self):
        print("\n" + str(test_cases('TC_CREATE_NEWS_WITH_VALID_DATA')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button().create_topic_with_valid_data("New Topic " + add_name)
        CanonizerAddNewsPage(self.driver).load_add_news_page()
        CanonizerAddNewsPage(self.driver).create_news_with_valid_data("https://www.google.com/", "Test News")
        result = self.driver.current_url
        assert "/1-Agreement" in result

    # TC_CREATE_NEWS_WITH_BLANK_DISPLAY_TEXT
    def test_create_news_with_blank_display_text(self):
        print("\n" + str(test_cases('TC_CREATE_NEWS_WITH_BLANK_DISPLAY_TEXT')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button().create_topic_with_valid_data("New Topic " + add_name)
        CanonizerAddNewsPage(self.driver).load_add_news_page().create_news_with_valid_data("https://www.google.com/", "   ")
        result = self.driver.find_element(*AddNewsIdentifiers.DISPLAY_TEXT_VALIDATION).text
        assert "Display text is required" in result

    # TC_CREATE_NEWS_WITH_BLANK_LINK
    def test_create_news_with_blank_link(self):
        print("\n" + str(test_cases('TC_CREATE_NEWS_WITH_BLANK_LINK')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button().create_topic_with_valid_data("New Topic " + add_name)
        CanonizerAddNewsPage(self.driver).load_add_news_page().create_news_with_valid_data("  ", " News Test  ")
        result = self.driver.find_element(*AddNewsIdentifiers.LINK_VALIDATION).text
        assert "Link is required." in result
    # TC_NEW_FEED_WITH_BLANK_FIELDS
    def test_create_new_with_blank_fields(self):
        print("\n", str(test_cases('TC_NEW_FEED_WITH_BLANK_FIELDS')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button().create_topic_with_valid_data("New Topic " + add_name)
        CanonizerAddNewsPage(self.driver).load_add_news_page().create_news_with_valid_data("  ", "   ")
        result = self.driver.find_element(*AddNewsIdentifiers.LINK_VALIDATION).text
        assert "Link is required." in result

    # TC_CLICK_ADD_NEWS_CANCEL_BUTTON
    def test_click_add_news_cancel_button(self):
        print("\n" + str(test_cases('TC_CLICK_ADD_NEWS_CANCEL_BUTTON')))
        self.login_to_canonizer_app()
        CanonizerAddNewsPage(self.driver).load_add_news_page(DEFAULT_TOPIC).click_add_news_cancel_button()
        result = self.driver.find_element(*AddNewsIdentifiers.TOPIC).text
        assert "Topic :" in result

    # TC_CREATE_NEWS_WITH_INVALID_LINK_FORMAT
    def test_create_news_with_invalid_link_format(self):
        print("\n" + str(test_cases('TC_CREATE_NEWS_WITH_INVALID_LINK_FORMAT')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button().create_topic_with_valid_data("New Topic " + add_name)
        CanonizerAddNewsPage(self.driver).load_add_news_page().create_news_with_valid_data("https     ", "     News Test")
        result = self.driver.find_element(*AddNewsIdentifiers.LINK_VALIDATION_NOTE).text
        assert "Link is invalid. (Example: https://www.example.com?post=1234)." in result

    # TC_CREATE_NEWS_WITH_ENTER_KEY


    # TC_CREATE_NEWS_WITH_DUPLICATE_DATA
    def test_create_news_with_duplicate_data(self):
        print("\n" + str(test_cases('TC_CREATE_NEWS_WITH_DUPLICATE_DATA')))
        self.login_to_canonizer_app()
        CanonizerAddNewsPage(self.driver).load_add_news_page(DEFAULT_TOPIC).create_news_with_duplicate_data("Test automated news", "https://www.google.com/")
        result = self.driver.find_element(*CampStatementIdentifiers.ADD_STATEMENT_BUTTON).text
        assert "Manage/Edit Camp Statement" not in result

    # TC_CREATE_NEWS_WITH_TRAILING_SPACES
    def test_create_news_with_trailing_spaces(self):
        print("\n", str(test_cases("TC_CREATE_NEWS_WITH_TRAILING_SPACES")))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button().create_topic_with_valid_data("New Topic " + add_name)
        CanonizerAddNewsPage(self.driver).load_add_news_page().create_news_with_valid_data("https://www.google.com     ", "     News Test")
        result = self.driver.current_url
        assert "/1-Agreement" in result

   def test_eventline(self):
        print("\n" + str(test_cases('TC_CREATE_NEWS_WITH_VALID_DATA')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button().create_topic_with_valid_data("New Topic " + add_name)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/section/section/main/div/div/div/div[1]/div[2]/div[2]/a/span/img").click()
        self.driver.find_element(*BrowsePageIdentifiers.EVENTLINE).click()
        result = self.driver.current_url
        assert "eventline" in result
   

   def test_browse_start_topic(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*BrowsePageIdentifiers.START_TOPIC).click()
        result = self.driver.current_url
        assert "/create/topic" in result

    def test_upload_files(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*BrowsePageIdentifiers.UPLOAD_FILES).click()
        result = self.driver.current_url
        assert "/uploadFile" in result

    def test_browse_videos(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*BrowsePageIdentifiers.VIDEOS).click()
        result = self.driver.current_url
        assert "/videos" in result

    def test_browse_help(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*BrowsePageIdentifiers.HELP).click()
        result = self.driver.current_url
        assert "/topic/132-Help/1-Agreement?is_tree_open=1" in result

    def test_browse_notification(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*BrowsePageIdentifiers.NOTIFICATION_BELL).click()
        result = self.driver.find_element(*BrowsePageIdentifiers.NOTIFICATIONS).text
        assert "notifications" in result

    def test_browse_profile_setting(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*BrowsePageIdentifiers.PROFILE_LINK).click()
        result = self.driver.find_element(*BrowsePageIdentifiers.PROFILE_SETTING).text
        assert "Account Settings" in result

    def test_browse_profile_setting_account_setting(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*BrowsePageIdentifiers.PROFILE_LINK).click()
        self.driver.find_element(*BrowsePageIdentifiers.PROFILE_LINK_INFO).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/settings?tab=profile_info" in result

    def test_browse_profile_setting_supported_camps(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*BrowsePageIdentifiers.PROFILE_LINK).click()
        self.driver.find_element(*BrowsePageIdentifiers.SUPPORTED_CAMP).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/settings?tab=direct_supported_camps" in result

    def test_upload_profile_picture(self):
        self.login_to_canonizer_app()
        self.driver.get("https://ux-dev.canonizer.com/settings")
        image = "/home/vivekkumar/PycharmProjects/Canonizer_UX _Github/UI/10mb.jpg"
        upload_image = self.driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        upload_image.send_keys(image)
        self.driver.find_element(*ProfileInfoIdentifiersPage.UPLOAD_IMAGE_OK).click()
        self.driver.find_element(*ProfileInfoIdentifiersPage.SAVE_PROFILE_CHANGES).click()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.IMAGE_UPLOADED_SUCCESFULLY).text
        assert "Profile updated successfully" in result

    def test_view_profile_picture(self):
        self.login_to_canonizer_app()
        self.driver.get("https://ux-dev.canonizer.com/settings")
        self.driver.find_element(*ProfileInfoIdentifiersPage.VIEW_IMAGE).click()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.VIEW_IMAGE_POP_UP).text
        assert "Profile picture" in result

    def test_delete_profile_picture(self):
        self.login_to_canonizer_app()
        self.driver.get("https://ux-dev.canonizer.com/settings")
        self.driver.find_element(*ProfileInfoIdentifiersPage.DELETE_PROFILE_IMAGE).click()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.IMAGE_DELETED_POP_UP).text
        assert "Image Deleted" in result

    def test_delete_profile_picture(self):
        self.login_to_canonizer_app()
        self.driver.get("https://ux-dev.canonizer.com/settings")
        self.driver.find_element(*ProfileInfoIdentifiersPage.DELETE_PROFILE_IMAGE).click()
        self.driver.find_element(*ProfileInfoIdentifiersPage.DELETE_PROFILE_IMAGE).click()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.IMAGE_DELETED_POP_UP).text
        assert "Image Deleted" not in result

    def test_alphabets_for_no_profile_image(self):
        self.login_to_canonizer_app()
        self.driver.get("https://ux-dev.canonizer.com/settings")
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.NO_IMAGE_ALPHABET).text
        assert "AR" in result

   def test_footer_browse_button(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*HomePageIdentifiers.FOOTER_BROWSE).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/browse" in result


    def test_footer_create_topic_button(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*HomePageIdentifiers.FOOTER_CREATE_TOPIC).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/create/topic" in result

    def test_footer_upload_file_button(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*HomePageIdentifiers.FOOTER_UPLOAD).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/uploadFile" in result

    def test_footer_sitemap_button(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*HomePageIdentifiers.FOOTER_SITE_MAP).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/sitemap" in result

    def test_footer_videos_button(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*HomePageIdentifiers.FOOTER_VIDEOS).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/videos" in result

    def test_footer_help_button(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*HomePageIdentifiers.FOOTER_HELP).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/topic/132-Help/1-Agreement?is_tree_open=1" in result

    def test_footer_white_paper_button(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*HomePageIdentifiers.FOOTER_WHITE_PAPER).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/files/2012_amplifying_final.pdf" in result

    def test_footer_jobs_button(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*HomePageIdentifiers.FOOTER_JOBS).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/topic/6-Canonizer-Jobs/1-Agreement?is_tree_open=1" in result

    def test_footer_privacy_policy_button(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*HomePageIdentifiers.FOOTER_PRIVACY).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/privacy-policy" in result

    def test_footer_term_and_services_button(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*HomePageIdentifiers.FOOTER_TERM_CONDITION).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/terms-and-services" in result
   
    def test_footer_upload_file_button(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*HomePageIdentifiers.FOOTER_UPLOAD).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/uploadFile" in result 

    def test_authentication_expiry_for_create_topic(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
       
        self.driver.get("https://ux-dev.canonizer.com/create/topic")
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result

    def test_authentication_expiry_for_create_camp(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        topic_url = self.driver.current_url
        camp_url = topic_url.replace("topic", "camp/create")
        self.driver.get(camp_url)
        #time.sleep(60) one minute hold
        self.driver.get(camp_url)
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result

    def test_authentication_expiry_for_create_statement(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        topic_url = self.driver.current_url
        statement_url = topic_url.replace("topic", "create/statement")
        self.driver.get(statement_url)
        #time.sleep(60) one minute hold
        self.driver.get(statement_url)
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result


    def test_authentication_expiry_for_upload_file(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.get(UPLOAD_FILE_URL)
        #time.sleep(60) one minute hold
        self.driver.get(UPLOAD_FILE_URL)

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result

    def test_authentication_expiry_for_account_setting(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        time.sleep(5)

        self.driver.get(ACCOUNT_SETTING_URL)
        #time.sleep(60) one minute hold
        self.driver.get(ACCOUNT_SETTING_URL)

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result


    def test_authentication_expiry_for_supported_camp(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.get(SUPPORTED_CAMP_URL)
        #time.sleep(60) one minute hold
        self.driver.get(SUPPORTED_CAMP_URL)

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result

    def test_authentication_expiry_for_nicknames(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.get(NICKNAME_URL)
        #time.sleep(60) one minute hold
        self.driver.get(NICKNAME_URL)

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result

    def test_authentication_expiry_for_user_preference(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.get(USER_PREFERENCE_URL)
        #time.sleep(60) one minute hold
        self.driver.get(USER_PREFERENCE_URL)

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result

    def test_authentication_expiry_for_direct_supported_camp(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.get(DIRECT_SUPPORTED_CAMP_URL)
        #time.sleep(60) one minute hold
        self.driver.get(DIRECT_SUPPORTED_CAMP_URL)

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result

    def test_authentication_expiry_for_delegate_supported_camp(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.get(DELEGATE_SUPPORT_URL)
        #time.sleep(60) one minute hold
        self.driver.get(DELEGATE_SUPPORT_URL)

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result

    def test_authentication_expiry_for_subscriptions(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.get(SUBSCRIPTION_URL)
        #time.sleep(60) one minute hold
        self.driver.get(SUBSCRIPTION_URL)

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result

    def test_authentication_social_oauth_verification(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.get(SOCIAL_AUTH)
        #time.sleep(60) one minute hold
        self.driver.refresh()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result

    def test_authentication_change_password(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.get(CHANGE_PASSWORD)
        #time.sleep(60) one minute hold
        self.driver.refresh()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result

    def test_authentication_add_news(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        topic_url = self.driver.current_url
        statement_url = topic_url.replace("topic", "addnews")
        self.driver.get(statement_url)
        #time.sleep(60) one minute hold
        self.driver.get(statement_url)
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result

    def test_authentication_homepage(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        #time.sleep(60) one minute hold
        self.driver.refresh()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result


    def test_authentication_notification_page(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.get(NOTIFICATION_URL)
        #time.sleep(60) one minute hold
        self.driver.refresh()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result

    def test_authentication_header_browse_pge(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.get(BROWSE_PAGE_URL)
        self.driver.refresh()

        try:
          button=self.driver.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
          result = "fail"
        except NoSuchElementException:
          result = "pass"
        assert "pass" in result

    def test_authentication_header_videos(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.get(HEADER_VIDEOS)
        self.driver.refresh()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result

    def test_authentication_header_help(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        #time.sleep(60) one minute hold

        self.driver.get(HELP_URL)
        self.driver.refresh()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result

    def test_authentication_footer_browse(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.find_element(*HomePageIdentifiers.FOOTER_BROWSE).click()

        #time.sleep(60) one minute hold
        self.driver.refresh()

        try:
          button=self.driver.find_element(By.ID, "browse-only-my-topics")
          result = "fail"
        except NoSuchElementException:
          result = "pass"
        assert "pass" in result

    def test_authentication_footer_create_topic(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.find_element(*HomePageIdentifiers.FOOTER_CREATE_TOPIC.click()
        #time.sleep(60) one minute hold
        self.driver.refresh()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result

    def test_authentication_footer_upload_file(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.find_element(*HomePageIdentifiers.FOOTER_UPLOAD.click()
        #time.sleep(60) one minute hold
        self.driver.refresh()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result

    def test_authentication_footer_videos(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.find_element(*HomePageIdentifiers.FOOTER_VIDEOS.click()
        #time.sleep(60) one minute hold
        self.driver.refresh()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/videos" in result

    def test_authentication_footer_help(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.find_element(*HomePageIdentifiers.FOOTER_HELP.click()
        #time.sleep(60) one minute hold
        self.driver.refresh()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/topic/132-Help/1-Agreement?is_tree_open=1" in result

    def test_authentication_footer_white_paper(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.find_element(*HomePageIdentifiers.FOOTER_WHITE_PAPER.click()
        #time.sleep(60) one minute hold
        self.driver.refresh()
        old_window = self.driver.current_window_handle

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/files/2012_amplifying_final.pdf" in result

    def test_authentication_footer_policy(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.find_element(*HomePageIdentifiers.FOOTER_PRIVACY.click()
        #time.sleep(60) one minute hold
        self.driver.refresh()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/privacy-policy" in result

    def test_authentication_footer_terms_and_services(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.find_element(*HomePageIdentifiers.FOOTER_TERM_CONDITION.click()
        #time.sleep(60) one minute hold
        self.driver.refresh()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/terms-and-services" in result



    def test_authentication_topic_history(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.get("https://ux-dev.canonizer.com/topic/history/6669-Test-dlkskndlksndl")
        #time.sleep(60) one minute hold
        self.driver.refresh()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" not in result

    def test_statement_image_more_than_5mb(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.get("https://ux-dev.canonizer.com/manage/statement/8215-update")
        image_statement = "/home/vivekkumar/PycharmProjects/Canonizer_UX _Github/UI/10mb.jpg"
        upload_image = self.driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        upload_image.send_keys(image_statement)

        result = self.driver.find_element(*CampStatementIdentifiers.IMAGE_SIZE_EXCEEDED).text
        assert "Alert: Image size exceed" in result

    def test_statement_image_more_than_5mb_note(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.get("https://ux-dev.canonizer.com/manage/statement/8215-update")
        result = self.driver.find_element(*CampStatementIdentifiers.IMAGE_SIZE_NOTE).text

        assert "Note: You can drag and drop image files into the editor. The maximum allowed file size is 5 MB." in result

    def test_upload_file_without_userlogin(self):
        self.driver.implicitly_wait(30)
        self.driver.get(UPLOAD_FILE_URL)
        result = self.driver.current_url
        assert "login" in result

    def test_upload_file_with_non_admin(self):
        self.driver.implicitly_wait(30)
        #self.login_to_canonizer_app()
        CanonizerLoginPage(self.driver).click_on_login_page_button().verify_the_login_with_user2(DEFAULT_USER_2, DEFAULT_PASS_2)
        self.driver.get(UPLOAD_FILE_URL)
        result = self.driver.current_url
        assert "login" in result

    def test_upload_file_with_admin(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.get(UPLOAD_FILE_URL)
        result = self.driver.current_url
        assert "uploadFile" in result

    
    def teardown_method(self):

        self.driver.close()


if __name__ == "__main__":
