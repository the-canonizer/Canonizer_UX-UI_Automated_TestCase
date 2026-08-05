import unittest
from datetime import datetime
from subprocess import run
import requests
import xmlrunner as xmlrunner
from selenium.webdriver.common import keys
from xmlrunner import *
from selenium.webdriver.common.keys import Keys
from urllib3.util import response
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from Identifiers import *


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
from CanonizerAddEditNewsPage import CanonizerEditNewsPage
from CanonizerBrowsePage import CanonizerBrowsePage
from CanonizerCampForum import CanonizerCampForumPage
from CanonizerCampStatementPage import CanonizerCampStatementPage
from CanonizerCreateUpdateCampPage import CanonizerCreateCampPage, CanonizerEditCampPage
from CanonizerCreateUpdateTopicPage import CanonizerCreateNewTopic, CanonizerUpdateTopicPage
from CanonizerAccountPage import CanonizerPofilePage
from CanonizerProfileUpdatePage import CanonizerPofileUpdatePage
from CanonizerUploadFile import CanonizerUploadFile
from CanonizerAdvancedSettingsPage import CanonizerAdvancedSettingsPage
from CanonizerSearchPage import CanonizerSearchPage


from CanonizerLoginPage import CanonizerLoginPage
from CanonizerAuthenticationPage import CanonizerAuthenticationPage
from CanonizerRegistrationPage import CanonizerRegisterPage
from CanonizerAccountPage import CanonizerPofilePage
from Identifiers import RegistrationPageIdentifiers, CreateTopicIdentifiers


class TestPages:

    """End-to-end Canonizer UI coverage grouped by feature area."""
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

        self.driver = webdriver.Chrome()
        self.driver.get(DEFAULT_BASE_URL)
        self.driver.implicitly_wait(30)

    def driver(self):
        self.driver = webdriver.Chrome()
        self.action = ActionChains(self.driver)

    def login_to_canonizer_app(self):
        """
            This Application will allow you to login to canonizer App on need basis
        :param flag:
        :return:
        """
        self.driver.implicitly_wait(30)
        CanonizerLoginPage(self.driver).click_on_login_page_button().verify_the_login_functionality_by_entering_the_registered_credential(DEFAULT_USER, DEFAULT_PASS)
        self.driver.maximize_window()


    # Authentication and registration flow tests.
    def test_login_to_canonizer(self):
        """Test case: Login to canonizer."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        result = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/div[2]/section/div/button/span[1]").text
        assert "Browse More" in result
    def test_click_on_join_now(self):
        """Test case: Click on join now."""
        print("\n" + str(test_cases('TC_CLICK_ON_REGISTER_BUTTON')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).join_now()

        result = self.driver.find_element(*RegistrationPageIdentifiers.REGISTRATION_TITLE).text
        assert "Create your account" in result

    # TC_REGISTER_PAGE_MANDATORY_FIELDS_MARKED_WITH_ASTERISK
    def test_register_page_mandatory_fields_are_marked_with_asterisk(self):
        """Test case: Register page mandatory fields are marked with asterisk."""
        assert CanonizerRegisterPage(
            self.driver).click_register_button().register_page_mandatory_fields_are_marked_with_asterisk()


    def test_registration_with_valid_credential(self):
        """Test case: Registration with valid credential."""
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_17)
        result = self.driver.find_element(*RegistrationPageIdentifiers.OTP_SENT).text
        assert "Note : Registration code has been sent to your registered email address." in result

    def test_registration_first_name_with_spaces(self):
        """Test case: Registration first name with spaces."""
        print("\n" + str(test_cases('TC_REGISTER_WITH_BLANK_SPACES_FIRST_NAME')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_18)
        result = self.driver.find_element(*RegistrationPageIdentifiers.OTP_SENT).text
        assert "Note : Registration code has been sent to your registered email address." in result

    # TC_REGISTER_WITH_BLANK_FIRST_NAME
    def test_registration_with_blank_first_name(self, ):
        """Test case: Registration with blank first name."""
        print("\n" + str(test_cases('TC_REGISTER_WITH_BLANK_FIRST_NAME')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_3)
        result = self.driver.find_element(*RegistrationPageIdentifiers.FIRST_NAME_VALIDATION).text
        assert "Please input your first name!" in result

    # TC_REGISTRATION_WITH_BLANK_EMAIL
    def test_registration_with_blank_email(self):
        """Test case: Registration with blank email."""
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_BLANK_EMAIL')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_5)
        result = self.driver.find_element(*RegistrationPageIdentifiers.EMAIL_VALIDATION).text
        assert "Please input your E-mail!" in result

    # TC_REGISTER_WITH_BLANK_LAST_NAME
    def test_registration_with_blank_last_name(self):
        """Test case: Registration with blank last name."""
        print("\n" + str(test_cases('TC_REGISTER_WITH_BLANK_LAST_NAME')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_4)
        result = self.driver.find_element(*RegistrationPageIdentifiers.LAST_NAME_VALIDATION).text
        assert "Please input your last name!" in result

    # TC_REGISTRATION_WITH_BLANK_PASSWORD
    def test_registration_with_blank_password(self):
        """Test case: Registration with blank password."""
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_BLANK_PASSWORD')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_6)
        result = self.driver.find_element(*RegistrationPageIdentifiers.PASSWORD_VALIDATION).text
        assert "Please input your password!" in result

    # TC_REGISTRATION_WITH_INVALID_PASSWORD_LENGTH
    def test_registration_with_invalid_password_length(self):
        """Test case: Registration with invalid password length."""
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_INVALID_PASSWORD_LENGTH')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_7)
        result = self.driver.find_element(*RegistrationPageIdentifiers.PASSWORD_TYPE_VALIDATION).text
        assert "Password must contain small, capital letter, number and special character like Abc@1234." in result

    # TC_REGISTER_WITH_BLANK_SPACES_FIRST_NAME

    # TC_REGISTRATION_WITH_INVALID_EMAIL
    def test_registration_with_invalid_email(self):
        """Test case: Registration with invalid email."""
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_INVALID_EMAIL')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_14)
        result = self.driver.find_element(*RegistrationPageIdentifiers.VALID_EMAIL).text
        assert "Please enter a valid email address." in result

    # TC_CHECK_LOGIN_PAGE_OPEN_CLICK_ON_LOGIN_HERE_LINK
    def test_check_login_page_open_click_login_here_link(self):
        """Test case: Check login page open click login here link."""
        print("\n" + str(test_cases('TC_CHECK_LOGIN_PAGE_OPEN_CLICK_ON_LOGIN_HERE_LINK')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button()
        CanonizerRegisterPage(self.driver).check_login_page_open_click_login_here_link()
        result = self.driver.current_url
        assert "login" in result

    # TC_VERIFY_THE_FUNCTIONALITY_OF_REGISTRATION_WITH_MANDATORY_FIELDS
    def test_verify_the_functionality_of_registration_with_entering_data_in_mandatory_fields(self):
        """Test case: Verify the functionality of registration with entering data in mandatory fields."""
        print("\n" + str(test_cases('TC_VERIFY_THE_FUNCTIONALITY_OF_REGISTRATION_WITH_MANDATORY_FIELDS')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_15)
        result = self.driver.find_element(*RegistrationPageIdentifiers.OTP_SENT).text
        assert "Note : Registration code has been sent to your registered email address." in result

    # TC_VERIFY_THE_FUNCTIONALITY_OF_REGISTRATION_WITH_MOBILE_NUMBER_FIELDS
    def test_verify_the_functionality_0f_registration_with_entering_data_in_mobile_number_field(self):
        """Test case: Verify the functionality 0f registration with entering data in mobile number field."""
        print("\n" + str(test_cases('TC_VERIFY_THE_FUNCTIONALITY_OF_REGISTRATION_WITH_MOBILE_NUMBER_FIELDS')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_16)
        result = self.driver.find_element(*RegistrationPageIdentifiers.VALID_PHONE_NUMBER).text
        assert "Please input valid phone number!" in result

    def test_click_on_login_button(self):
        """Test case: Click on login button."""
        print("\n" + str(test_cases('TC_CLICK_ON_LOGIN_BUTTON')))
        self.driver.implicitly_wait(30)
        CanonizerLoginPage(self.driver).click_on_login_page_button()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "login-submit-btn")))
        result = self.driver.current_url
        assert "login" in result


    # TC_LOGIN_WITH_REGISTERED_CREDENTIALS
    def test_login_with_registered_credentials(self):
        """Test case: Login with registered credentials."""
        print("\n" + str(test_cases('TC_LOGIN_WITH_REGISTERED_CREDENTIALS')))
        self.driver.implicitly_wait(30)
        CanonizerLoginPage(self.driver).click_on_login_page_button().verify_the_login_functionality_by_entering_the_registered_credential(DEFAULT_USER, DEFAULT_PASS)
        result = self.driver.find_element(*LoginPageIdentifiers.START_TOPIC_BUTTON).text
        assert "Start a Topic" in result

    # TC_VERIFY_THE_LOGIN_WITH_BLANK_EMAIL
    def test_verify_the_login_with_blank_email(self):
        """Test case: Verify the login with blank email."""
        print("\n" + str(test_cases('TC_LOGIN_WITH_REGISTERED_CREDENTIALS')))
        self.driver.implicitly_wait(30)
        CanonizerLoginPage(self.driver).click_on_login_page_button().verify_the_login_with_blank_email("", DEFAULT_PASS)
        result = self.driver.find_element(*LoginPageIdentifiers.EMAIL_VALIDATION).text
        assert "Please input your Email!" in result

    # TC_VERIFY_THE_LOGIN_WITH_BLANK_PASSWORD
    def test_verify_the_login_with_blank_password(self):
        """Test case: Verify the login with blank password."""
        print("\n" + str(test_cases('TC_VERIFY_THE_LOGIN_WITH_BLANK_PASSWORD')))
        self.driver.implicitly_wait(30)
        CanonizerLoginPage(self.driver).click_on_login_page_button().verify_the_login_with_blank_password(DEFAULT_USER, "")
        result = self.driver.find_element(*LoginPageIdentifiers.PASSWORD_VALIDATION).text
        assert "Please input your Password!" in result

    # TC_LOGIN_WITH_INVALID_EMAIL
    def test_login_with_invalid_email(self):
        """Test case: Login with invalid email."""
        self.driver.implicitly_wait(30)
        CanonizerLoginPage(self.driver).click_on_login_page_button().verify_the_login_with_invalid_email_format(DEFAULT_INVALID_USER, DEFAULT_PASS)
        result = self.driver.find_element(*LoginPageIdentifiers.VALID_EMAIL).text
        assert "Input is not valid!" in result

    # TC_VERIFY_ONE_TIME_REQUEST_CODE_WITH_VALID_CREDENTIALS
    def test_verify_one_time_request_code_with_valid_credentials(self):
        """Test case: Verify one time request code with valid credentials."""
        print("\n" + str(test_cases('TC_VERIFY_ONE_TIME_REQUEST_CODE_WITH_VALID_CREDENTIALS')))
        self.driver.implicitly_wait(30)
        CanonizerLoginPage(self.driver).click_on_login_page_button().verify_one_time_request_code(DEFAULT_USER)
        result = self.driver.find_element(*LoginPageIdentifiers.RESEND_OTP).text
        assert "Resend OTP" in result

    def test_login_page_mandatory_fields_are_marked_with_asterisk(self):
        """Test case: Login page mandatory fields are marked with asterisk."""
        login_page = CanonizerLoginPage(self.driver).click_on_login_page_button()
        assert login_page.mandatory_fields_are_marked()

    def test_login_remember_me_is_selected_by_default(self):
        """Test case: Login remember me is selected by default."""
        login_page = CanonizerLoginPage(self.driver).click_on_login_page_button()
        assert login_page.remember_me_is_selected()

    def test_login_register_now_link(self):
        """Test case: Login register now link."""
        CanonizerLoginPage(self.driver).click_on_login_page_button().open_registration_from_login()
        assert "/registration" in self.driver.current_url
        assert self.driver.find_element(
            *RegistrationPageIdentifiers.REGISTRATION_TITLE
        ).is_displayed()

    def test_forgot_password_link(self):
        """Test case: Forgot password link."""
        CanonizerLoginPage(self.driver).click_on_login_page_button().open_forgot_password()
        assert "/forgot-password" in self.driver.current_url
        assert self.driver.find_element(
            *AuthenticationFlowIdentifiers.FORGOT_TITLE
        ).is_displayed()

    @pytest.mark.parametrize(
        "provider", ["facebook", "google", "linkedin", "github"]
    )
    def test_login_social_provider_is_available(self, provider):
        """Test case: Login social provider is available."""
        login_page = CanonizerLoginPage(self.driver).click_on_login_page_button()
        social_button = login_page.social_login_providers()[provider]
        assert social_button.is_displayed()
        assert social_button.is_enabled()

    def test_logout(self):
        """Test case: Logout."""
        self.login_to_canonizer_app()
        CanonizerLoginPage(self.driver).logout()
        assert self.driver.find_element(
            *LoginPageIdentifiers.LOGGED_OUT_LOGIN_LINK
        ).is_displayed()

    def test_forgot_password_with_blank_email(self):
        """Test case: Forgot password with blank email."""
        CanonizerLoginPage(self.driver).click_on_login_page_button().open_forgot_password()
        auth_page = CanonizerAuthenticationPage(self.driver)
        auth_page.submit_forgot_password_email("")
        assert auth_page.forgot_password_error() == "Please input your E-mail!"

    def test_forgot_password_with_invalid_email(self):
        """Test case: Forgot password with invalid email."""
        CanonizerLoginPage(self.driver).click_on_login_page_button().open_forgot_password()
        auth_page = CanonizerAuthenticationPage(self.driver)
        auth_page.submit_forgot_password_email("not-an-email")
        assert auth_page.forgot_password_error() == "Please enter a valid email address."

    def test_forgot_password_with_unregistered_email(self):
        """Test case: Forgot password with unregistered email."""
        CanonizerLoginPage(self.driver).click_on_login_page_button().open_forgot_password()
        auth_page = CanonizerAuthenticationPage(self.driver)
        auth_page.submit_forgot_password_email(UNREGISTERED_EMAIL)
        error = auth_page.forgot_password_error()
        assert error != ""

    def test_close_login_modal(self):
        """Test case: Close login modal."""
        CanonizerLoginPage(self.driver).click_on_login_page_button().click_on_close_icon_button()
        assert self.driver.find_element(*LoginPageIdentifiers.LOGIN_BUTTON).is_displayed()

    def test_forgot_password_otp_with_invalid_code(self):
        """Test case: Forgot password otp with invalid code."""
        CanonizerLoginPage(self.driver).click_on_login_page_button().open_forgot_password()
        auth_page = CanonizerAuthenticationPage(self.driver)
        auth_page.submit_forgot_password_email(DEFAULT_USER).wait_for_otp_page()
        auth_page.enter_otp("111111").submit_otp()
        error = self.driver.find_element(*AuthenticationFlowIdentifiers.OTP_ERROR).text
        assert error != ""

    def test_forgot_password_otp_with_blank_code(self):
        """Test case: Forgot password otp with blank code."""
        CanonizerLoginPage(self.driver).click_on_login_page_button().open_forgot_password()
        auth_page = CanonizerAuthenticationPage(self.driver)
        auth_page.submit_forgot_password_email(DEFAULT_USER).wait_for_otp_page()
        auth_page.submit_otp()
        error = self.driver.find_element(*AuthenticationFlowIdentifiers.OTP_ERROR).text
        assert error != ""

    def test_resend_forgot_password_otp(self):
        """Test case: Resend forgot password otp."""
        CanonizerLoginPage(self.driver).click_on_login_page_button().open_forgot_password()
        auth_page = CanonizerAuthenticationPage(self.driver)
        auth_page.submit_forgot_password_email(DEFAULT_USER).wait_for_otp_page()
        auth_page.resend_otp()
        assert self.driver.find_element(*AuthenticationFlowIdentifiers.OTP_TITLE).is_displayed()

    def test_reset_password_with_mismatched_passwords(self):
        """Test case: Reset password with mismatched passwords."""
        CanonizerLoginPage(self.driver).click_on_login_page_button().open_forgot_password()
        auth_page = CanonizerAuthenticationPage(self.driver)
        auth_page.submit_forgot_password_email(DEFAULT_USER).wait_for_otp_page()
        auth_page.enter_otp("111111").submit_otp()
        auth_page.fill_reset_password("Test@12345", "Different@12345")
        self.driver.find_element(*AuthenticationFlowIdentifiers.RESET_SUBMIT).click()
        assert auth_page.reset_confirmation_error() == "Confirm Password does not match!"

    def test_registration_with_blank_confirm_password(self):
        """Test case: Registration with blank confirm password."""
        register_page = CanonizerRegisterPage(self.driver).click_on_register_button()
        register_page.fill_registration_form(
            "Automation",
            "User",
            random_char(10) + "@example.com",
            "",
            DEFAULT_PASSWORD,
            "",
        )
        self.driver.find_element(
            *RegistrationPageIdentifiers.CONFIRM_PASSWORD
        ).send_keys(Keys.TAB)
        register_page.submit_registration()
        error = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                RegistrationPageIdentifiers.CONFIRM_PASSWORD_VALIDATION
            )
        ).text
        assert error == "Please confirm your password!"

    def test_registration_with_mismatched_passwords(self):
        """Test case: Registration with mismatched passwords."""
        register_page = CanonizerRegisterPage(self.driver).click_on_register_button()
        register_page.fill_registration_form(
            "Automation",
            "User",
            random_char(10) + "@example.com",
            "",
            DEFAULT_PASSWORD,
            "Different@123",
        ).submit_registration()
        error = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                RegistrationPageIdentifiers.CONFIRM_PASSWORD_VALIDATION
            )
        ).text
        assert error == "Confirm Password does not match!"

    def test_registration_with_invalid_mobile_number(self):
        """Test case: Registration with invalid mobile number."""
        register_page = CanonizerRegisterPage(self.driver).click_on_register_button()
        register_page.fill_registration_form(
            "Automation",
            "User",
            random_char(10) + "@example.com",
            "12345",
            DEFAULT_PASSWORD,
            DEFAULT_PASSWORD,
        ).submit_registration()
        error = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                RegistrationPageIdentifiers.PHONE_VALIDATION
            )
        ).text
        assert error == "Contact number must be at least 10 digits!"

    def test_registration_social_providers_are_available(self):
        """Test case: Registration social providers are available."""
        register_page = CanonizerRegisterPage(self.driver).click_on_register_button()
        providers = register_page.social_signup_providers()
        assert set(providers) == {"facebook", "google", "linkedin", "github"}
        assert all(button.is_displayed() and button.is_enabled() for button in providers.values())

                # ----- CREATE TOPIC Test Cases Start -----
    # Topic creation and topic lifecycle tests.

    # TC_CLICK_CREATE_TOPIC_WITH_USER_LOGIN
    def test_click_create_new_topic_page_button(self):
        """Test case: Click create new topic page button."""
        print("\n" + str(test_cases('TC_CLICK_CREATE_TOPIC_WITH_USER_LOGIN')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        result = self.driver.current_url
        assert "/create/topic" in result

    # TC_CLICK_CREATE_TOPIC_WITHOUT_USER_LOGIN
    def test_click_create_topic_without_user_login(self):
        """Test case: Click create topic without user login."""
        print("\n" + str(test_cases('TC_CLICK_CREATE_TOPIC_WITHOUT_USER_LOGIN')))
        self.driver.implicitly_wait(30)
        CanonizerCreateNewTopic(self.driver).click_create_topic_button_without_login()
        result = self.driver.current_url
        assert "/login?returnUrl=%2Fcreate%2Ftopic" in result

    # TC_CREATE_TOPIC_WITH_BLANK_TOPIC_NAME
    def test_create_topic_with_blank_topic_name(self):
        """Test case: Create topic with blank topic name."""
        print("\n" + str(test_cases('TC_CREATE_TOPIC_WITH_BLANK_TOPIC_NAME')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_blank_topic()
        result = self.driver.find_element(*CreateTopicIdentifiers.VALID_TOPIC_NAME).text
        assert "Topic name cannot start with a space" in result

    # TC_CREATE_NEW_TOPIC_WITH_VALID_DATA
    def test_create_topic_name_with_valid_data(self):
        """Test case: Create topic name with valid data."""
        print("\n" + str(test_cases('TC_CREATE_TOPIC_WITH_VALID_DATA')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        result = self.driver.current_url
        assert "1-Agreement" in result

    def test_create_same_topic_name_with_valid_data(self):
        """Test case: Create same topic name with valid data."""
        print("\n" + str(test_cases('TC_CREATE_TOPIC_WITH_VALID_DATA')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_same_topic("same topic")
        result = self.driver.find_element(*CreateTopicIdentifiers.SAME_TOPIC_NAME).text
        assert "A Topic with this exact name already exists!" in result

    def test_create_same_topic_name_error_link(self):
        """Test case: Create same topic name error link."""
        print("\n" + str(test_cases('TC_CREATE_TOPIC_WITH_VALID_DATA')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("new summary", "same topic")
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[2]/form/div[1]/div[1]/a").click()
        result = self.driver.find_element(*CreateTopicIdentifiers.SAME_TOPIC_TITLE).text
        assert "same topic" in result
    # TC_CREATE_NEW_TOPIC_WITH_SPECIAL_CHARS
    def test_create_topic_with_special_chars(self):
        """Test case: Create topic with special chars."""
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
        """Test case: Create topic without entering mandatory fields."""
        print("\n", str(test_cases('TC_CREATE_NEW_WITHOUT_MANDATORY_FIELDS_DATA')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_without_entering_mandatory_fields(" ")
        result = self.driver.current_url        
        assert "create/topic" in result

    def test_create_topic_mandatory_fields_are_marked_with_asterisk(self):
        """Test case: Create topic mandatory fields are marked with asterisk."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        page = CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        assert page.topic_page_mandatory_fields_are_marked_with_asterisk()

    def test_create_topic_with_trailing_spaces(self):
        """Test case: Create topic with trailing spaces."""
        print("\n" + str(test_cases('TC_CREATE_NEW_TOPIC_WITH_TRAILING_SPACES')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_name_with_trailing_space("New Topic")
        result = self.driver.current_url
        assert "topic" in result

    def test_create_topic_using_enter_key(self):
        """Test case: Create topic using enter key."""
        print("\n" + str(test_cases('TC_CREATE_NEW_TOPIC_WITH_ENTER_KEY')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_name_with_enter_key("summary", "New Topic " + add_name, "sandbox testing")
        result = self.driver.current_url
        assert "topic" in result

    def test_create_topic_with_only_mandatory_fields(self):
        """Test case: Create topic with only mandatory fields."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_entering_data_only_in_mandatory_fields(
            "summary",
            "New Topic " + add_name,
            "sandbox testing",
        )
        result = self.driver.current_url
        assert "topic" in result

    def test_cancel_create_topic(self):
        """Test case: Cancel create topic."""
        print("\n" + str(test_cases('TC_CLICK_ON_CANCEL_BUTTON')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).click_on_cancel_button()
        result = self.driver.find_element(*CreateTopicIdentifiers.MAIN_PAGE).text
        assert "Select Namespace" in result
    # ----- UPDATE TOPIC Test Cases Start -----
    # Topic update and topic history tests.

    # TC_LOAD_TOPIC_HISTORY_PAGE
    def test_load_topic_history_page(self):
        """Test case: Load topic history page."""
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
        """Test case: Verify topic name on topic history page."""
        print("\n" + str(test_cases('TC_VERIFY_TOPIC_NAME_ON_TOPIC_HISTORY_PAGE')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()

        result = self.driver.current_url
        assert add_name in result

    # TC_VERIFY_SUBMITTER_NICK_NAME_LINK_ON_USER_PROFILE
    def test_verify_submitter_nick_name_link_on_user_profile(self):
        """Test case: Verify submitter nick name link on user profile."""
        print("\n" + str(test_cases('TC_VERIFY_SUBMITTER_NICK_NAME_LINK_ON_USER_PROFILE')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()

        result = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/section/main/div/div/div[2]/div/div/div[2]/div/div[1]/p[6]/span").text
        assert "$%$%$%$%" in result

    # TC_VERIFY_SUBMIT_TOPIC_UPDATE_BUTTON
    def test_verify_submit_topic_update_button(self):
        """Test case: Verify submit topic update button."""
        print("\n" + str(test_cases('TC_VERIFY_SUBMIT_TOPIC_UPDATE_BUTTON')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()
        CanonizerUpdateTopicPage(self.driver).verify_submit_topic_update_button()

        result = self.driver.find_element(By.ID, "create-topic-btn").text

        assert "Update Topic" in result


    # TC_VERIFY_CANCEL_BUTTON_FUNCTIONALITY_ON_TOPIC_UPDATE_PAGE
    def test_verify_cancel_button_functionality_on_topic_update_page(self):
        """Test case: Verify cancel button functionality on topic update page."""
        print("\n" + str(test_cases('TC_VERIFY_CANCEL_BUTTON_FUNCTIONALITY_ON_TOPIC_UPDATE_PAGE')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()
        CanonizerUpdateTopicPage(self.driver).verify_cancel_button_functionality_on_topic_update_page()

        result = self.driver.current_url

        assert "/topic/history/" in result


    # TC_UPDATE_TOPIC_NAME_AND_VERIFY_SUBMIT_UPDATE_BUTTON
    def test_update_topic_name(self):
        """Test case: Update topic name."""
        print("\n" + str(test_cases('TC_UPDATE_TOPIC_NAME_AND_VERIFY_SUBMIT_UPDATE_BUTTON')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()
        CanonizerUpdateTopicPage(self.driver).update_topic_name()

        result = self.driver.current_url

        assert "topic/history/" in result

    def test_topic_update_preview(self):
        """Test case: Topic update preview."""
        print("\n" + str(test_cases('TC_VERIFY_PREVIEW_BUTTON_FUNCTIONALITY_ON_TOPIC_UPDATE_PAGE')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()
        CanonizerUpdateTopicPage(self.driver).verify_preview_button_functionality_on_topic_update_page()
        result = self.driver.find_element(*UpdateTopicIdentifiers.TOPIC_PREVIEW_TITLE).text
        assert "Topic Preview" in result

    def test_topic_preview_cancel(self):
        """Test case: Topic preview cancel."""
        print("\n" + str(test_cases('TC_VERIFY_CANCEL_BUTTON_ON_PREVIEW_MODAL')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()
        CanonizerUpdateTopicPage(self.driver).verify_cancel_button_on_preview_modal()
        result = self.driver.current_url
        assert "topic/history" in result

    def test_topic_preview_submitter_nickname(self):
        """Test case: Topic preview submitter nickname."""
        print("\n" + str(test_cases('TC_VERIFY_SUBMITTER_NICK_NAME_ON_PREVIEW_MODAL')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()
        CanonizerUpdateTopicPage(self.driver).verify_submitter_nick_name_on_preview_modal()
        result = self.driver.current_url
        assert "/profile/" in result

    def test_compare_topic_versions(self):
        """Test case: Compare topic versions."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()
        CanonizerUpdateTopicPage(self.driver).verify_compare_topics_button_functionality()
        result = self.driver.current_url
        assert "compare" in result

    def test_topic_comparison_agreement_link(self):
        """Test case: Topic comparison agreement link."""
        print("\n" + str(test_cases('TC_VERIFY_AGREEMENT_LINK_ON_TOPIC_COMPARISON_PAGE')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()
        CanonizerUpdateTopicPage(self.driver).verify_agreement_link_on_topic_comparison_page()
        result = self.driver.current_url
        assert "1-Agreement" in result

    def test_topic_comparison_create_camp_button(self):
        """Test case: Topic comparison create camp button."""
        print("\n" + str(test_cases('TC_VERIFY_CREATE_CAMP_BUTTON_FUNCTIONALITY_ON_TOPIC_COMPARISON_PAGE')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()
        CanonizerUpdateTopicPage(self.driver).verify_create_camp_button_functionality_on_topic_comparison_page()
        result = self.driver.current_url
        assert "/camp/create/" in result

    def test_topic_comparison_create_topic_button(self):
        """Test case: Topic comparison create topic button."""
        print("\n" + str(test_cases('TC_VERIFY_CREATE_TOPIC_BUTTON_FUNCTIONALITY_ON_TOPIC_COMPARISON_PAGE')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()
        CanonizerUpdateTopicPage(self.driver).verify_create_topic_button_functionality_on_topic_comparison_page()
        result = self.driver.current_url
        assert "/create/topic" in result

    def test_topic_comparison_back_button(self):
        """Test case: Topic comparison back button."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()
        CanonizerUpdateTopicPage(self.driver).verify_back_arrow_icon_on_topic_comparison_page()
        result = self.driver.current_url
        assert "/topic/history/" in result

    def test_topic_history_view_this_version(self):
        """Test case: Topic history view this version."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()
        CanonizerUpdateTopicPage(self.driver).verify_view_this_version_button_functionality()
        result = self.driver.current_url
        assert "/topic/" in result
    # TC_LOAD_CREATE_CAMP_PAGE
    # Camp creation and camp management tests.
    def test_load_create_camp_page(self):
        """Test case: Load create camp page."""
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
        """Test case: Create camp with valid data."""
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
        """Test case: Create camp with blank camp name."""
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
        """Test case: Create camp with duplicate camp name."""
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
        """Test case: Create camp with invalid camp about url."""
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
        """Test case: Create camp without entering data in mandatory fields."""
        print("\n" + str(test_cases('TC_CREATE_CAMP_WITHOUT_ENTERING_DATA_IN_MANDATORY_FIELDS')))
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_duplicate_camp_name(CREATE_CAMP_LIST_2)
        result = self.driver.current_url
        assert "/camp/create/" in result

    def test_create_camp_mandatory_fields_are_marked_with_asterisk(self):
        """Test case: Create camp mandatory fields are marked with asterisk."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        page = CanonizerCreateCampPage(self.driver).load_create_camp_page()
        assert page.new_camp_mandatory_fields_are_marked_with_asterisk()

    def test_cancel_create_camp(self):
        """Test case: Cancel create camp."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().camp_cancel_button()
        result = self.driver.current_url
        assert "topic" in result

    def test_create_camp_with_only_mandatory_fields(self):
        """Test case: Create camp with only mandatory fields."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        result = self.driver.current_url
        assert "topic" in result

    def test_update_camp_with_valid_data(self):
        """Test case: Update camp with valid data."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerEditCampPage(self.driver).load_camp_manage_edit_page().submit_camp_update_with_valid_name()
        result = self.driver.current_url
        assert "manage/camp" in result

    def test_verify_submit_camp_update_button(self):
        """Test case: Verify submit camp update button."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        result = CanonizerEditCampPage(self.driver).verify_submit_camp_update_button()
        assert "/manage/camp/" in result.get_url()

    def test_camp_preview_fields(self):
        """Test case: Camp preview fields."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        result = CanonizerEditCampPage(self.driver).verify_fields_on_preview_modal()
        assert result is not None

    def test_camp_preview_cancel(self):
        """Test case: Camp preview cancel."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        result = CanonizerEditCampPage(self.driver).verify_cancel_button_on_preview_modal()
        assert "/manage/camp/" in result.get_url()

    def test_camp_preview_submitter_nickname(self):
        """Test case: Camp preview submitter nickname."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        result = CanonizerEditCampPage(self.driver).verify_submitter_nick_name_on_preview_modal()
        assert result is not None

    def test_compare_camp_versions(self):
        """Test case: Compare camp versions."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        result = CanonizerEditCampPage(self.driver).verify_compare_camps_button_functionality()
        assert "compare" in result.get_url()

    def test_camp_comparison_displays_both_versions(self):
        """Test case: Camp comparison displays both versions."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        result = CanonizerEditCampPage(self.driver).verify_camps_name_on_camp_history_comparison_page()
        assert result is not None

    def test_load_camp_manage_edit_page(self):
        """Test case: Load camp manage edit page."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerEditCampPage(self.driver).load_camp_manage_edit_page()
        result = self.driver.current_url
        assert "manage/camp" in result

    def test_add_statement_for_archived_camp(self):
        """Test case: Add statement for archived camp."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerEditCampPage(self.driver).load_camp_manage_edit_page()
        CanonizerEditCampPage(self.driver).add_statement_for_archived_camp()
        
        if self.driver.find_element(*CampStatementIdentifiers.ADD_STATEMENT_BUTTON).is_enabled():
           result = "fail"
        else:
           result = "pass"
        assert "pass" in result


    # TC_UPDATE_CAMP_WITH_INVALID_URL
    def test_submit_camp_update_with_invalid_url(self):
        """Test case: Submit camp update with invalid url."""
        self.login_to_canonizer_app()
        result = CanonizerEditCampPage(self.driver).load_topic_detail_page(DEFAULT_TOPIC)\
            .submit_camp_update_with_invalid_url(INVALID_CAMP_ABOUT_URL)
        assert "/manage/camp/" in result.get_url()

    # TC_UPDATE_CAMP_WITH_DUPLICATE_CAMP_NAME
    def test_update_camp_with_duplicate_camp_name(self):
        """Test case: Update camp with duplicate camp name."""
        self.login_to_canonizer_app()
        result = CanonizerEditCampPage(self.driver).load_topic_detail_page(DEFAULT_TOPIC)\
            .update_camp_with_duplicate_camp_name(DUPLICATE_CAMP_NAME)
        assert "/manage/camp/" in result.get_url()


    # TC_VERIFY_CANCEL_BUTTON_FUNCTIONALITY_ON_CAMP_UPDATE_PAGE
    def test_verify_cancel_button_functionality_on_camp_update_page(self):
        """Test case: Verify cancel button functionality on camp update page."""
        self.login_to_canonizer_app()
        result = CanonizerEditCampPage(self.driver).load_topic_detail_page(DEFAULT_TOPIC)\
            .verify_cancel_button_functionality_on_camp_update_page()
        assert "/camp/history/" in result.get_url()

    # TC_VERIFY_PREVIEW_BUTTON_FUNCTIONALITY_ON_CAMP_UPDATE_PAGE
    def test_verify_preview_button_functionality_on_camp_update_page(self):
        """Test case: Verify preview button functionality on camp update page."""
        self.login_to_canonizer_app()
        result = CanonizerEditCampPage(self.driver).load_topic_detail_page(DEFAULT_TOPIC) \
            .verify_preview_button_functionality_on_camp_update_page()
        assert "/manage/camp/" in result.get_url()
    # TC_LOAD_ADD_NEW_CAMP_STATEMENT_PAGE
    # Camp statement creation and editing tests.

    def test_camp_statement_button(self):
        """Test case: Camp statement button."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        result = self.driver.find_element(*CampStatementIdentifiers.ADD_STATEMENT_BUTTON).text
        assert "Add Statement" in result
    def test_load_camp_statement_page(self):
        """Test case: Load camp statement page."""
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
        """Test case: Add camp statement with valid data."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampStatementPage(self.driver).add_camp_statement()
        result = self.driver.find_element(*CampStatementIdentifiers.EDIT_BASED_ON_THIS).text
        assert "Edit Based on This" in result
    def test_add_camp_statement_page_with_asterisk(self):
        """Test case: Add camp statement page with asterisk."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampStatementPage(self.driver).add_camp_statement_asterisk()
        result = self.driver.find_element(*CampStatementIdentifiers.PUBLISH_BUTTON).text
        assert "Publish Statement" in result

    def test_add_camp_statement_without_mandatory_field(self):
        """Test case: Add camp statement without mandatory field."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampStatementPage(self.driver).add_camp_statement_without_mandatory_data()
        result = self.driver.find_element(*CampStatementIdentifiers.PUBLISH_BUTTON).text
        assert "Publish Statement" in result

    def test_add_camp_statement_with_trailing_spaces(self):
        """Test case: Add camp statement with trailing spaces."""
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
        """Test case: Add camp statement with blank data."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampStatementPage(self.driver).add_camp_statement_with_blank_data()
        result = self.driver.find_element(*CampStatementIdentifiers.PUBLISH_STATEMENT).text
        assert "Publish Statement" in result

    def test_cancel_create_camp_statement(self):
        """Test case: Cancel create camp statement."""
        print("\n" + str(test_cases('TC_CLICK_ON_STATEMENT_CANCEL_BUTTON')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampStatementPage(self.driver).click_on_add_camp_statement_cancel_button()
        result = self.driver.current_url
        assert "topic" in result

    def test_preview_camp_statement(self):
        """Test case: Preview camp statement."""
        print("\n" + str(test_cases('TC_CLICK_ON_STATEMENT_PREVIEW_BUTTON')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampStatementPage(self.driver).click_on_camp_statement_preview_button()
        result = self.driver.find_element(*CampStatementIdentifiers.ADD_STATEMENT_TITLE).text
        assert "Add Camp Statement" in result
        
    def test_camp_statement_template(self):
        """Test case: Camp statement template."""
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
        """Test case: Load edit camp statement."""
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
        """Test case: Edit camp statement."""
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
        """Test case: Update camp statement with mandatory field."""
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
        """Test case: Edit camp statement with trailing spaces."""
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
        """Test case: Edit camp statement with blank data."""
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
        """Test case: Compare camp statement."""
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
        """Test case: Click create thread button."""
        print("\n" + str(test_cases('TC_CLICK_CREATE_THREAD_BUTTON')))
        self.login_to_canonizer_app()
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)

        CanonizerCampForumPage(self.driver).click_start_thread_button()
        result = self.driver.current_url
        assert "/threads" in result

    # TC_CREATE_THREAD_WITH_VALID_DATA
    def test_create_thread_with_valid_data(self):
        """Test case: Create thread with valid data."""
        print("\n" + str(test_cases('TC_CREATE_THREAD_WITH_VALID_DATA')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampForumPage(self.driver).create_thread_with_valid_data()
        result = self.driver.current_url
        assert "forum" in result

    # TC_CREATE_THREAD_WITH_BLANK_TITLE
    def test_create_thread_with_blank_title(self):
        """Test case: Create thread with blank title."""
        print("\n" + str(test_cases('TC_CREATE_THREAD_WITH_BLANK_TITLE')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampForumPage(self.driver).create_thread_with_blank_title_name(" ")
        result = self.driver.find_element(*CampForumIdentifiers.THREAD_TITLE_HELP).text
        assert "test" in result

    # TC_CREATE_THREAD_WITH_SPECIAL_CHARS
    def test_create_thread_with_special_chars(self):
        """Test case: Create thread with special chars."""
        print("\n" + str(test_cases('TC_CREATE_THREAD_WITH_SPECIAL_CHARS')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampForumPage(self.driver).create_thread_with_special_chars("test@$#@$#@$")
        result = self.driver.current_url
        assert "forum" in result

    # TC_CREATE_THREAD_WITH_BLANK_MANDATORY_FIELDS
    def test_create_thread_with_blank_mandatory_fields(self):
        """Test case: Create thread with blank mandatory fields."""
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
        """Test case: Create thread with duplicate title."""
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
        """Test case: Create thread with valid data with enter key."""
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
        """Test case: Create thread with trailing spaces."""
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
        """Test case: Load edit thread page."""
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
        """Test case: Edit thread."""
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
   
    def test_create_post(self):
        """Test case: Create post."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampForumPage(self.driver).create_thread_with_valid_data()
        CanonizerCampForumPage(self.driver).thread_post_with_valid_data()

        result = self.driver.find_element(By.ID, "card-title").text
        assert "test" in result

    def test_edit_post(self):
        """Test case: Edit post."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampForumPage(self.driver).create_thread_with_valid_data()
        CanonizerCampForumPage(self.driver).thread_post_with_valid_data()
        result = CanonizerCampForumPage(self.driver).verify_post_edit_functionality("updated post reply")
        assert result is not None

    def test_delete_post(self):
        """Test case: Delete post."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampForumPage(self.driver).create_thread_with_valid_data()
        CanonizerCampForumPage(self.driver).thread_post_with_valid_data()
        result = CanonizerCampForumPage(self.driver).test_verify_post_delete_functionality()
        assert result is not None

    # Camp forum thread filter tests.
    def test_load_my_threads_page(self):
        """Test case: Load my threads page."""
        print("\n" + str(test_cases('TC_LOAD_MY_THREADS_PAGE')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        topic_name = "New Topic " + add_name
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data(topic_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampForumPage(self.driver).create_thread_with_valid_data()
        CanonizerCampForumPage(self.driver).load_my_threads_page()
        result = self.driver.current_url
        assert "forum" in result and self.driver.find_element(*CampForumIdentifiers.MY_THREADS_BUTTON).is_displayed()

    def test_load_my_participation_page(self):
        """Test case: Load my participation page."""
        print("\n" + str(test_cases('TC_LOAD_MY_PARTICIPATION_PAGE')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        topic_name = "New Topic " + add_name
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data(topic_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampForumPage(self.driver).create_thread_with_valid_data()
        CanonizerCampForumPage(self.driver).load_my_participation_page()
        result = self.driver.current_url
        assert "forum" in result and self.driver.find_element(*CampForumIdentifiers.MY_PARTICIPATION).is_displayed()

    def test_load_top_10_threads_page(self):
        """Test case: Load top 10 threads page."""
        print("\n" + str(test_cases('TC_LOAD_TOP_10_THREADS_PAGE')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        topic_name = "New Topic " + add_name
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data(topic_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampForumPage(self.driver).create_thread_with_valid_data()
        CanonizerCampForumPage(self.driver).load_top_10_threads_page()
        result = self.driver.current_url
        assert "forum" in result and self.driver.find_element(*CampForumIdentifiers.TOP_10_THREADS).is_displayed()
   
    # Camp forum and thread/post tests.

# TC_LOAD_ADD_NEWS_FEED_PAGE
    # News feed creation and validation tests.
    def test_load_add_news_page(self):
        """Test case: Load add news page."""
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
        """Test case: Add news page mandatory fields are marked with asterisk."""
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
        """Test case: Create news with valid data."""
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
        """Test case: Create news with blank display text."""
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
        """Test case: Create news with blank link."""
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
        """Test case: Create new with blank fields."""
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
        """Test case: Click add news cancel button."""
        print("\n" + str(test_cases('TC_CLICK_ADD_NEWS_CANCEL_BUTTON')))
        self.login_to_canonizer_app()
        CanonizerAddNewsPage(self.driver).load_add_news_page(DEFAULT_TOPIC).click_add_news_cancel_button()
        result = self.driver.find_element(*AddNewsIdentifiers.TOPIC).text
        assert "Topic :" in result

    # TC_CREATE_NEWS_WITH_INVALID_LINK_FORMAT
    def test_create_news_with_invalid_link_format(self):
        """Test case: Create news with invalid link format."""
        print("\n" + str(test_cases('TC_CREATE_NEWS_WITH_INVALID_LINK_FORMAT')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button().create_topic_with_valid_data("New Topic " + add_name)
        CanonizerAddNewsPage(self.driver).load_add_news_page().create_news_with_valid_data("https     ", "     News Test")
        result = self.driver.find_element(*AddNewsIdentifiers.LINK_VALIDATION_NOTE).text
        assert "Link is invalid. (Example: https://www.example.com?post=1234)." in result

    # TC_CREATE_NEWS_WITH_ENTER_KEY
    def test_create_news_using_enter_key(self):
        """Test case: Create news using enter key."""
        print("\n" + str(test_cases('TC_CREATE_NEWS_WITH_ENTER_KEY')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button().create_topic_with_valid_data("New Topic " + add_name)
        CanonizerAddNewsPage(self.driver).load_add_news_page().create_news_with_enter_key("Test News", "https://www.google.com/")
        result = self.driver.current_url
        assert "/1-Agreement" in result


    # TC_CREATE_NEWS_WITH_DUPLICATE_DATA
    def test_create_news_with_duplicate_data(self):
        """Test case: Create news with duplicate data."""
        print("\n" + str(test_cases('TC_CREATE_NEWS_WITH_DUPLICATE_DATA')))
        self.login_to_canonizer_app()
        CanonizerAddNewsPage(self.driver).load_add_news_page(DEFAULT_TOPIC).create_news_with_duplicate_data("Test automated news", "https://www.google.com/")
        result = self.driver.find_element(*CampStatementIdentifiers.ADD_STATEMENT_BUTTON).text
        assert "Manage/Edit Camp Statement" not in result

    # TC_CREATE_NEWS_WITH_TRAILING_SPACES
    def test_create_news_with_trailing_spaces(self):
        """Test case: Create news with trailing spaces."""
        print("\n", str(test_cases("TC_CREATE_NEWS_WITH_TRAILING_SPACES")))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button().create_topic_with_valid_data("New Topic " + add_name)
        CanonizerAddNewsPage(self.driver).load_add_news_page().create_news_with_valid_data("https://www.google.com     ", "     News Test")
        result = self.driver.current_url
        assert "/1-Agreement" in result

    # Edit news form coverage tests.
    def test_load_edit_news_page(self):
        """Test case: Load edit news page."""
        print("\n" + str(test_cases('TC_LOAD_EDIT_NEWS_PAGE')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        topic_name = "New Topic " + add_name
        CanonizerCreateNewTopic(self.driver).click_create_topic_button().create_topic_with_valid_data(topic_name)
        CanonizerAddNewsPage(self.driver).load_add_news_page().create_news_with_valid_data("https://www.google.com/", "Test News")
        CanonizerEditNewsPage(self.driver).load_edit_news_page(topic_name)
        assert self.driver.find_element(*AddNewsIdentifiers.DISPLAY_TEXT).is_displayed()
        assert self.driver.find_element(*AddNewsIdentifiers.LINK).is_displayed()

    def test_click_edit_news_cancel_button(self):
        """Test case: Click edit news cancel button."""
        print("\n" + str(test_cases('TC_CLICK_EDIT_NEWS_CANCEL_BUTTON')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        topic_name = "New Topic " + add_name
        CanonizerCreateNewTopic(self.driver).click_create_topic_button().create_topic_with_valid_data(topic_name)
        CanonizerAddNewsPage(self.driver).load_add_news_page().create_news_with_valid_data("https://www.google.com/", "Test News")
        CanonizerEditNewsPage(self.driver).load_edit_news_page(topic_name).click_edit_news_cancel_button()
        result = self.driver.find_element(*AddNewsIdentifiers.TOPIC).text
        assert "Topic :" in result

    def test_update_news_with_blank_display_text(self):
        """Test case: Update news with blank display text."""
        print("\n" + str(test_cases('TC_UPDATE_NEWS_WITH_BLANK_DISPLAY_TEXT')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        topic_name = "New Topic " + add_name
        CanonizerCreateNewTopic(self.driver).click_create_topic_button().create_topic_with_valid_data(topic_name)
        CanonizerAddNewsPage(self.driver).load_add_news_page().create_news_with_valid_data("https://www.google.com/", "Test News")
        CanonizerEditNewsPage(self.driver).load_edit_news_page(topic_name).update_news_with_blank_display_text("https://www.google.com/")
        result = self.driver.find_element(*AddNewsIdentifiers.BLANK_DISPLAY_TEXT_ERROR).text
        assert "Display text is required" in result

    def test_update_news_with_blank_link(self):
        """Test case: Update news with blank link."""
        print("\n" + str(test_cases('TC_UPDATE_NEWS_WITH_BLANK_LINK')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        topic_name = "New Topic " + add_name
        CanonizerCreateNewTopic(self.driver).click_create_topic_button().create_topic_with_valid_data(topic_name)
        CanonizerAddNewsPage(self.driver).load_add_news_page().create_news_with_valid_data("https://www.google.com/", "Test News")
        CanonizerEditNewsPage(self.driver).load_edit_news_page(topic_name).update_news_with_blank_link("Updated News")
        result = self.driver.find_element(*AddNewsIdentifiers.BLANK_LINK_ERROR).text
        assert "Link is required." in result

    def test_edit_news_with_valid_data(self):
        """Test case: Edit news with valid data."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        topic_name = "New Topic " + add_name
        CanonizerCreateNewTopic(self.driver).click_create_topic_button().create_topic_with_valid_data(topic_name)
        CanonizerAddNewsPage(self.driver).load_add_news_page().create_news_with_valid_data("https://www.google.com/", "Original News")
        CanonizerEditNewsPage(self.driver).load_edit_news_page(topic_name).update_news("Updated News", "https://www.example.com/")
        result = self.driver.current_url
        assert "/topic/" in result

    def test_edit_news_with_invalid_link(self):
        """Test case: Edit news with invalid link."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        topic_name = "New Topic " + add_name
        CanonizerCreateNewTopic(self.driver).click_create_topic_button().create_topic_with_valid_data(topic_name)
        CanonizerAddNewsPage(self.driver).load_add_news_page().create_news_with_valid_data("https://www.google.com/", "Original News")
        CanonizerEditNewsPage(self.driver).load_edit_news_page(topic_name).update_news("Updated News", "https     ")
        result = self.driver.find_element(*AddNewsIdentifiers.LINK_VALIDATION_NOTE).text
        assert "Link is invalid. (Example: https://www.example.com?post=1234)." in result

    def test_edit_news_with_trailing_spaces(self):
        """Test case: Edit news with trailing spaces."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        topic_name = "New Topic " + add_name
        CanonizerCreateNewTopic(self.driver).click_create_topic_button().create_topic_with_valid_data(topic_name)
        CanonizerAddNewsPage(self.driver).load_add_news_page().create_news_with_valid_data("https://www.google.com/", "Original News")
        CanonizerEditNewsPage(self.driver).load_edit_news_page(topic_name).update_news("  Updated News  ", "https://www.google.com/    ")
        result = self.driver.current_url
        assert "/topic/" in result

    def test_create_news_available_for_child_camps(self):
        """Test case: Create news available for child camps."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button().create_topic_with_valid_data("New Topic " + add_name)
        page = CanonizerAddNewsPage(self.driver).load_add_news_page()
        page.create_news_with_enter_key("News Child Camp", "https://www.google.com/")
        result = self.driver.current_url
        assert "/topic/" in result

    # Browse, discovery, and event timeline tests.
    def test_eventline(self):
        """Test case: Eventline."""
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
        """Test case: Browse start topic."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*BrowsePageIdentifiers.START_TOPIC).click()
        result = self.driver.current_url
        assert "/create/topic" in result

    def test_browse_only_my_topics(self):
        """Test case: Browse only my topics."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerBrowsePage(self.driver).click_browse_page_button().click_only_my_topics_button()
        result = self.driver.current_url
        assert "browse" in result

    def test_browse_namespace_filter(self):
        """Test case: Browse namespace filter."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerBrowsePage(self.driver).select_dropdown_value()
        result = self.driver.find_element(*BrowsePageIdentifiers.NAMESPACE).text
        assert result != ""

    def test_browse_algorithm_filter(self):
        """Test case: Browse algorithm filter."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerBrowsePage(self.driver).click_browse_page_button().algo_dropdown_filter()
        result = self.driver.current_url
        assert "browse" in result

    def test_browse_search_by_topic_tag(self):
        """Test case: Browse search by topic tag."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerBrowsePage(self.driver).search_topic_tag()
        result = self.driver.current_url
        assert "browse" in result

    def test_advanced_search_topic_tab_navigation(self):
        """Test case: Advanced search topic tab navigation."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerSearchPage(self.driver).open_all_results("tree").click_sidebar_tab("/search/topic")
        result = self.driver.find_element(*SearchPageIdentifiers.TOPIC_HEADING).text
        assert "Topic" in result

    def test_advanced_search_camp_tab_navigation(self):
        """Test case: Advanced search camp tab navigation."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerSearchPage(self.driver).open_all_results("tree").click_sidebar_tab("/search/camp")
        result = self.driver.find_element(*SearchPageIdentifiers.CAMP_HEADING).text
        assert "Camp" in result

    def test_advanced_search_camp_statement_tab_navigation(self):
        """Test case: Advanced search camp statement tab navigation."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerSearchPage(self.driver).open_all_results("tree").click_sidebar_tab("/search/camp_statement")
        result = self.driver.find_element(*SearchPageIdentifiers.CAMP_STATEMENT_HEADING).text
        assert "Camp Statement" in result

    def test_advanced_search_nickname_tab_navigation(self):
        """Test case: Advanced search nickname tab navigation."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerSearchPage(self.driver).open_all_results("tree").click_sidebar_tab("/search/nickname")
        result = self.driver.find_element(*SearchPageIdentifiers.NICKNAME_HEADING).text
        assert "Nickname" in result

    def test_advanced_search_topic_review_filter_route(self):
        """Test case: Advanced search topic review filter route."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerSearchPage(self.driver).open_topic_results("tree", "asof=review")
        result = self.driver.current_url
        assert "asof=review" in result and "/search/topic" in result

    def test_advanced_search_camp_bydate_filter_route(self):
        """Test case: Advanced search camp bydate filter route."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerSearchPage(self.driver).open_camp_results("tree", "asof=bydate")
        result = self.driver.current_url
        assert "asof=bydate" in result and "/search/camp" in result

    def test_advanced_search_topic_pagination_visibility(self):
        """Test case: Advanced search topic pagination visibility."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        page = CanonizerSearchPage(self.driver).open_topic_results("tree")
        result = page.is_pagination_visible()
        assert result

    # Upload and profile media tests.
    def test_upload_files(self):
        """Test case: Upload files."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*BrowsePageIdentifiers.UPLOAD_FILES).click()
        result = self.driver.current_url
        assert "/uploadFile" in result

    def test_browse_videos(self):
        """Test case: Browse videos."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*BrowsePageIdentifiers.VIDEOS).click()
        result = self.driver.current_url
        assert "/videos" in result

    def test_browse_help(self):
        """Test case: Browse help."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*BrowsePageIdentifiers.HELP).click()
        result = self.driver.current_url
        assert "/topic/132-Help/1-Agreement?is_tree_open=1" in result

    def test_browse_notification(self):
        """Test case: Browse notification."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*BrowsePageIdentifiers.NOTIFICATION_BELL).click()
        result = self.driver.find_element(*BrowsePageIdentifiers.NOTIFICATIONS).text
        assert "notifications" in result

    def test_browse_profile_setting(self):
        """Test case: Browse profile setting."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*BrowsePageIdentifiers.PROFILE_LINK).click()
        result = self.driver.find_element(*BrowsePageIdentifiers.PROFILE_SETTING).text
        assert "Account Settings" in result

    def test_browse_profile_setting_account_setting(self):
        """Test case: Browse profile setting account setting."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*BrowsePageIdentifiers.PROFILE_LINK).click()
        self.driver.find_element(*BrowsePageIdentifiers.PROFILE_LINK_INFO).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/settings?tab=profile_info" in result

    def test_browse_profile_setting_supported_camps(self):
        """Test case: Browse profile setting supported camps."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*BrowsePageIdentifiers.PROFILE_LINK).click()
        self.driver.find_element(*BrowsePageIdentifiers.SUPPORTED_CAMP).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/settings?tab=direct_supported_camps" in result

    def test_upload_profile_picture(self):
        """Test case: Upload profile picture."""
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
        """Test case: View profile picture."""
        self.login_to_canonizer_app()
        self.driver.get("https://ux-dev.canonizer.com/settings")
        self.driver.find_element(*ProfileInfoIdentifiersPage.VIEW_IMAGE).click()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.VIEW_IMAGE_POP_UP).text
        assert "Profile picture" in result

    def test_delete_profile_picture(self):
        """Test case: Delete profile picture."""
        self.login_to_canonizer_app()
        self.driver.get("https://ux-dev.canonizer.com/settings")
        self.driver.find_element(*ProfileInfoIdentifiersPage.DELETE_PROFILE_IMAGE).click()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.IMAGE_DELETED_POP_UP).text
        assert "Image Deleted" in result

    def test_delete_profile_picture_when_no_image_exists(self):
        """Test case: Delete profile picture when no image exists."""
        self.login_to_canonizer_app()
        self.driver.get("https://ux-dev.canonizer.com/settings")
        self.driver.find_element(*ProfileInfoIdentifiersPage.DELETE_PROFILE_IMAGE).click()
        self.driver.find_element(*ProfileInfoIdentifiersPage.DELETE_PROFILE_IMAGE).click()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.IMAGE_DELETED_POP_UP).text
        assert "Image Deleted" not in result

    def test_alphabets_for_no_profile_image(self):
        """Test case: Alphabets for no profile image."""
        self.login_to_canonizer_app()
        self.driver.get("https://ux-dev.canonizer.com/settings")
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.NO_IMAGE_ALPHABET).text
        assert "AR" in result

    # Footer and public navigation tests.
    def test_footer_browse_button(self):
        """Test case: Footer browse button."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*HomePageIdentifiers.FOOTER_BROWSE).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/browse" in result


    def test_footer_create_topic_button(self):
        """Test case: Footer create topic button."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*HomePageIdentifiers.FOOTER_CREATE_TOPIC).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/create/topic" in result

    def test_footer_upload_file_button(self):
        """Test case: Footer upload file button."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*HomePageIdentifiers.FOOTER_UPLOAD).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/uploadFile" in result

    def test_footer_sitemap_button(self):
        """Test case: Footer sitemap button."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*HomePageIdentifiers.FOOTER_SITE_MAP).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/sitemap" in result

    def test_footer_videos_button(self):
        """Test case: Footer videos button."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*HomePageIdentifiers.FOOTER_VIDEOS).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/videos" in result

    def test_footer_help_button(self):
        """Test case: Footer help button."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*HomePageIdentifiers.FOOTER_HELP).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/topic/132-Help/1-Agreement?is_tree_open=1" in result

    def test_footer_white_paper_button(self):
        """Test case: Footer white paper button."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*HomePageIdentifiers.FOOTER_WHITE_PAPER).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/files/2012_amplifying_final.pdf" in result

    def test_footer_jobs_button(self):
        """Test case: Footer jobs button."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*HomePageIdentifiers.FOOTER_JOBS).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/topic/6-Canonizer-Jobs/1-Agreement?is_tree_open=1" in result

    def test_footer_privacy_policy_button(self):
        """Test case: Footer privacy policy button."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*HomePageIdentifiers.FOOTER_PRIVACY).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/privacy-policy" in result

    def test_footer_term_and_services_button(self):
        """Test case: Footer term and services button."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*HomePageIdentifiers.FOOTER_TERM_CONDITION).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/terms-and-services" in result
   
    def test_footer_upload_file_button_repeat_navigation(self):
        """Test case: Footer upload file button repeat navigation."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*HomePageIdentifiers.FOOTER_UPLOAD).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/uploadFile" in result 

    # Authentication expiry and protected-route checks.
    def test_authentication_expiry_for_create_topic(self):
        """Test case: Authentication expiry for create topic."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.get("https://ux-dev.canonizer.com/create/topic")
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result

    def test_authentication_expiry_for_create_camp(self):
        """Test case: Authentication expiry for create camp."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        topic_url = self.driver.current_url
        camp_url = topic_url.replace("topic", "camp/create")
        self.driver.get(camp_url)
        self.driver.get(camp_url)
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result

    def test_authentication_expiry_for_create_statement(self):
        """Test case: Authentication expiry for create statement."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        topic_url = self.driver.current_url
        statement_url = topic_url.replace("topic", "create/statement")
        self.driver.get(statement_url)
        self.driver.get(statement_url)
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result


    def test_authentication_expiry_for_upload_file(self):
        """Test case: Authentication expiry for upload file."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.get(UPLOAD_FILE_URL)
        self.driver.get(UPLOAD_FILE_URL)

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result

    def test_authentication_expiry_for_account_setting(self):
        """Test case: Authentication expiry for account setting."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerPofilePage(self.driver).profile_button()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result


    def test_authentication_expiry_for_supported_camp(self):
        """Test case: Authentication expiry for supported camp."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        CanonizerPofilePage(self.driver).profile_page_direct_supported_camp_tab()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result

    def test_authentication_expiry_for_nicknames(self):
        """Test case: Authentication expiry for nicknames."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerPofilePage(self.driver).profile_page_nickname_tab()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result

    def test_authentication_expiry_for_user_preference(self):
        """Test case: Authentication expiry for user preference."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerPofilePage(self.driver).profile_page_preferences_tab()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result

    def test_authentication_expiry_for_direct_supported_camp(self):
        """Test case: Authentication expiry for direct supported camp."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        CanonizerPofilePage(self.driver).profile_page_direct_supported_camp_tab()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result

    def test_authentication_expiry_for_delegate_supported_camp(self):
        """Test case: Authentication expiry for delegate supported camp."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerPofilePage(self.driver).profile_page_delegate_supported_camp_tab()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result

    def test_authentication_expiry_for_subscriptions(self):
        """Test case: Authentication expiry for subscriptions."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerPofilePage(self.driver).profile_page_mysubscription_tab()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result

    def test_authentication_social_oauth_verification(self):
        """Test case: Authentication social oauth verification."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerPofilePage(self.driver).profile_page_account_setting_social_auth_tab()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result

    def test_authentication_change_password(self):
        """Test case: Authentication change password."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerPofilePage(self.driver).profile_page_account_setting_password_tab()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result

    def test_authentication_add_news(self):
        """Test case: Authentication add news."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        topic_url = self.driver.current_url
        statement_url = topic_url.replace("topic", "addnews")
        self.driver.get(statement_url)
        self.driver.get(statement_url)
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result

    def test_authentication_homepage(self):
        """Test case: Authentication homepage."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.refresh()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result


    def test_authentication_notification_page(self):
        """Test case: Authentication notification page."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.get(NOTIFICATION_URL)
        self.driver.refresh()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result

    def test_authentication_notification_delete(self):
        """Test case: Authentication notification delete."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.get(NOTIFICATION_URL)
        self.driver.find_element(*BrowsePageIdentifiers.DELETE_NOTIFICATION).click()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result


    def test_authentication_header_browse_pge(self):
        """Test case: Authentication header browse pge."""
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
        """Test case: Authentication header videos."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.get("https://ux-dev.canonizer.com/videos")
        self.driver.refresh()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result

    def test_authentication_header_help(self):
        """Test case: Authentication header help."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.get(HELP_URL)
        self.driver.refresh()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result

    def test_authentication_footer_browse(self):
        """Test case: Authentication footer browse."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.find_element(*HomePageIdentifiers.FOOTER_BROWSE).click()
        self.driver.refresh()

        try:
          button=self.driver.find_element(By.ID, "browse-only-my-topics")
          result = "fail"
        except NoSuchElementException:
          result = "pass"
        assert "pass" in result

    def test_authentication_footer_create_topic(self):
        """Test case: Authentication footer create topic."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.find_element(*HomePageIdentifiers.FOOTER_CREATE_TOPIC).click()
        self.driver.refresh()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result

    def test_authentication_footer_upload_file(self):
        """Test case: Authentication footer upload file."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.find_element(*HomePageIdentifiers.FOOTER_UPLOAD).click()
        self.driver.refresh()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result

    def test_authentication_footer_videos(self):
        """Test case: Authentication footer videos."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.find_element(*HomePageIdentifiers.FOOTER_VIDEOS).click()
        self.driver.refresh()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/videos" in result

    def test_authentication_footer_help(self):
        """Test case: Authentication footer help."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.find_element(*HomePageIdentifiers.FOOTER_HELP).click()
        self.driver.refresh()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/topic/132-Help/1-Agreement?is_tree_open=1" in result

    def test_authentication_footer_white_paper(self):
        """Test case: Authentication footer white paper."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.find_element(*HomePageIdentifiers.FOOTER_WHITE_PAPER).click()
        self.driver.refresh()
        old_window = self.driver.current_window_handle

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/files/2012_amplifying_final.pdf" in result

    def test_authentication_footer_policy(self):
        """Test case: Authentication footer policy."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.find_element(*HomePageIdentifiers.FOOTER_PRIVACY).click()
        self.driver.refresh()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/privacy-policy" in result

    def test_authentication_footer_terms_and_services(self):
        """Test case: Authentication footer terms and services."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.find_element(*HomePageIdentifiers.FOOTER_TERM_CONDITION).click()
        self.driver.refresh()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/terms-and-services" in result



    def test_authentication_topic_history(self):
        """Test case: Authentication topic history."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.get("https://ux-dev.canonizer.com/topic/history/6669-Test-dlkskndlksndl")
        self.driver.refresh()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" not in result

    def test_statement_image_more_than_5mb(self):
        """Test case: Statement image more than 5mb."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.get("https://ux-dev.canonizer.com/manage/statement/8215-update")
        image_statement = "/home/vivekkumar/PycharmProjects/Canonizer_UX _Github/UI/10mb.jpg"
        upload_image = self.driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        upload_image.send_keys(image_statement)

        result = self.driver.find_element(*CampStatementIdentifiers.IMAGE_SIZE_EXCEEDED).text
        assert "Alert: Image size exceed" in result

    def test_statement_image_more_than_5mb_note(self):
        """Test case: Statement image more than 5mb note."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.get("https://ux-dev.canonizer.com/manage/statement/8215-update")
        result = self.driver.find_element(*CampStatementIdentifiers.IMAGE_SIZE_NOTE).text

        assert "Note: You can drag and drop image files into the editor. The maximum allowed file size is 5 MB." in result

    def test_upload_file_without_userlogin(self):
        """Test case: Upload file without userlogin."""
        self.driver.implicitly_wait(30)
        CanonizerUploadFile(self.driver).upload_file_without_userlogin()
        result = self.driver.current_url
        assert "login" in result

    def test_upload_file_with_admin(self):
        """Test case: Upload file with admin."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerUploadFile(self.driver).upload_file_with_admin()
        result = self.driver.current_url
        assert "uploadFile" in result


    def test_upload_file_less_than_5mb(self):
        """Test case: Upload file less than 5mb."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerUploadFile(self.driver).uploading_file_less_than_5mb()
        result = self.driver.current_url
        assert "uploadFile" in result

    def test_upload_file_more_than_5mb(self):
        """Test case: Upload file more than 5mb."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerUploadFile(self.driver).upload_file_more_than_5mb()
        result = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/section/main/div/div/div/form/div/div[2]/div/div[2]/div[1]/span/div[2]/div/div/div/div/p").text
        assert "This file is exceeding the max limit and will not be uploaded" in result

    def test_upload_in_create_new_folder(self):
        """Test case: Upload in create new folder."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerUploadFile(self.driver).upload_in_create_new_folder()
        result = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/section/main/div/div/div/form/div/div[2]/div/div[1]/div/div[2]/button/span[1]").text
        assert "Upload New File" in result

    def test_upload_file_in_new_folder(self):
        """Test case: Upload file in new folder."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerUploadFile(self.driver).upload_in_create_new_folder()
        CanonizerUploadFile(self.driver).upload_file_in_new_folder()
        result = self.driver.current_url
        assert "uploadFile" in result

    def test_upload_file_manager_search_and_reset(self):
        """Test case: Upload file manager search and reset."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        page = CanonizerUploadFile(self.driver).open_upload_file_manager()
        page.search_uploaded_files("test")
        page.reset_upload_filters()
        result = self.driver.find_element(*UploadFileIdentifiers.SEARCH_INPUT).get_attribute("value")
        assert result == ""

    def test_upload_file_manager_toggle_views(self):
        """Test case: Upload file manager toggle views."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        page = CanonizerUploadFile(self.driver).open_upload_file_manager()
        page.switch_to_list_view()
        page.switch_to_grid_view()
        result = self.driver.find_element(*UploadFileIdentifiers.CREATE_FOLDER_BUTTON).is_displayed()
        assert result

    def test_upload_file_manager_file_actions_menu(self):
        """Test case: Upload file manager file actions menu."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        page = CanonizerUploadFile(self.driver).open_upload_file_manager()
        opened = page.open_first_file_menu_if_available()
        if opened:
            result = page.file_menu_has_actions()
        else:
            result = self.driver.find_element(*UploadFileIdentifiers.CREATE_FOLDER_BUTTON).is_displayed()
        assert result

    def test_upload_file_manager_delete_modal_cancel(self):
        """Test case: Upload file manager delete modal cancel."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        page = CanonizerUploadFile(self.driver).open_upload_file_manager()
        opened = page.open_first_file_menu_if_available()
        if opened and len(self.driver.find_elements(*UploadFileIdentifiers.FILE_ACTION_DELETE)) > 0:
            page.open_delete_modal_and_cancel()
        result = self.driver.find_element(*UploadFileIdentifiers.CREATE_FOLDER_BUTTON).is_displayed()
        assert result

    def test_profile_page_name_change(self):
        """Test case: Profile page name change."""
            # Profile, account settings, and preference tests.
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.get(PROFILE_PAGE)
        self.driver.find_element(*ProfileInfoIdentifiersPage.FIRST_NAME).send_keys("ing")
        self.driver.find_element(*ProfileInfoIdentifiersPage.SAVE_PROFILE_CHANGES).click()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.USERNAME_UPPER).text

        assert "Akashing" in result

    def test_cafe_text_in_address_bar(self):
        """Test case: Cafe text in address bar."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.get(PROFILE_PAGE)
        self.driver.find_element(*ProfileInfoIdentifiersPage.ADDRESS_LINE).send_keys("Café,")
        self.driver.find_element(*ProfileInfoIdentifiersPage.SAVE_PROFILE_CHANGES).click()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.PROFILE_UPDATED_POP_UP).text

        assert "Profile updated successfully." in result

    def test_topic_name_in_recent_activities(self):
        """Test case: Topic name in recent activities."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("Recent Topic" + add_name)
        self.driver.get(DEFAULT_BASE_URL)
        result = self.driver.find_element(*CreateTopicIdentifiers.RECENT_TOPIC_NAME).text
        assert "Recent Topic" in result

    def test_categories_page(self):
        """Test case: Categories page."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.get(TOPIC_TAG_URL)
        categories = self.driver.find_elements(*BrowsePageIdentifiers.TOPIC_TAG)
        for x in categories:
            if x.text == "Relationships":
               result = "Relationships"
               break
            else:
               result = "tag does not exist"

        assert "Relationships" in result

    def test_elastic_search_count(self):
        """Test case: Elastic search count."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.get(TOPIC_SEARCH_URL)
        result = self.driver.find_element(*BrowsePageIdentifiers.TOPIC_SEARCH_COUNT).text
        assert "1121" in result

    def test_videos_thumbnail(self):
        """Test case: Videos thumbnail."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.get("https://ux-dev.canonizer.com/videos")
        result = self.driver.find_element(*BrowsePageIdentifiers.VIDEOS_THUMBNAIL).get_attribute("src")
        thumnail_link = "https://ux-dev.canonizer.com/_next/image?url=https%3A%2F%2Fux-dev.canonizer.com%2Ffiles%2Fvideos%2Fconsciousness%2Fintroduction_thumb.png&w=3840&q=75"
        assert thumnail_link in result

    def test_tree_search_crash(self):
        """Test case: Tree search crash."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.get(TREE_SEARCH_URL)
        result = self.driver.find_element(*BrowsePageIdentifiers.ELASTIC_SEARCH_URL).text
        assert "Search Results for " in result

    def test_agree_search_crash(self):
        """Test case: Agree search crash."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.get(AGREE_SEARCH_URL)
        result = self.driver.find_element(*BrowsePageIdentifiers.ELASTIC_SEARCH_URL).text
        assert "Search Results for " in result

    def test_support_camp_error_first_time(self):
        """Test case: Support camp error first time."""
        print("\n" + str(test_cases('TC_CREATE_CAMP_WITH_VALID_DATA')))
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        self.driver.find_element(*SupportValueIdentifiers.MANAGE_SUPPORT).click()
        self.driver.find_element(*SupportValueIdentifiers.DELEGATE_SUPPORT_SUBMIT).click()

        result = self.driver.find_element(*SupportValueIdentifiers.SUPPORT_POP_UP).text
        assert "Thank you for adding your support to camp" in result

    def test_notifications_filters_matrix(self):
        """Test case: Notifications filters matrix."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerAdvancedSettingsPage(self.driver).open_notifications().notifications_apply_filters()
        result = self.driver.find_element(*AdvancedSettingsIdentifiers.NOTIFICATIONS_LIST).is_displayed()
        assert result

    def test_notifications_mark_all_read_cancel(self):
        """Test case: Notifications mark all read cancel."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerAdvancedSettingsPage(self.driver).open_notifications().open_mark_all_read_modal().cancel_mark_all_read_modal()
        result = self.driver.find_element(*AdvancedSettingsIdentifiers.NOTIFICATIONS_TITLE).is_displayed()
        assert result

    def test_notifications_delete_all_cancel(self):
        """Test case: Notifications delete all cancel."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerAdvancedSettingsPage(self.driver).open_notifications().open_delete_all_modal().cancel_delete_all_modal()
        result = self.driver.find_element(*AdvancedSettingsIdentifiers.NOTIFICATIONS_TITLE).is_displayed()
        assert result

    def test_notifications_load_more_if_available(self):
        """Test case: Notifications load more if available."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        was_clicked = CanonizerAdvancedSettingsPage(self.driver).open_notifications().click_load_more_if_available()
        result = self.driver.find_element(*AdvancedSettingsIdentifiers.NOTIFICATIONS_LIST).is_displayed()
        assert result or (was_clicked is False)

    def test_direct_supported_search(self):
        """Test case: Direct supported search."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerAdvancedSettingsPage(self.driver).open_direct_supported().search_direct_supported("test")
        result = self.driver.find_element(*AdvancedSettingsIdentifiers.DIRECT_TABLE).is_displayed()
        assert result

    def test_direct_supported_remove_modal_cancel(self):
        """Test case: Direct supported remove modal cancel."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerAdvancedSettingsPage(self.driver).open_direct_supported().open_direct_remove_modal().cancel_support_remove_modal()
        result = self.driver.find_element(*AdvancedSettingsIdentifiers.DIRECT_TABLE).is_displayed()
        assert result

    def test_delegated_supported_search(self):
        """Test case: Delegated supported search."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerAdvancedSettingsPage(self.driver).open_delegated_supported().search_delegated_supported("test")
        result = self.driver.find_element(*AdvancedSettingsIdentifiers.DELEGATED_TABLE).is_displayed()
        assert result

    def test_delegated_supported_remove_modal_cancel(self):
        """Test case: Delegated supported remove modal cancel."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerAdvancedSettingsPage(self.driver).open_delegated_supported().open_delegated_remove_modal().cancel_support_remove_modal()
        result = self.driver.find_element(*AdvancedSettingsIdentifiers.DELEGATED_TABLE).is_displayed()
        assert result

    def test_preferences_topic_tag_search(self):
        """Test case: Preferences topic tag search."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerAdvancedSettingsPage(self.driver).open_preferences().search_preference_tags("test")
        result = self.driver.find_element(*AdvancedSettingsIdentifiers.PREFERENCE_TAGS_CONTAINER).is_displayed()
        assert result

    def test_social_auth_link_controls_visible(self):
        """Test case: Social auth link controls visible."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        page = CanonizerAdvancedSettingsPage(self.driver).open_social_auth()
        result = page.social_link_button_count()
        assert result >= 1

    def test_create_topic_edit_draft_crash(self):
        """Test case: Create topic edit draft crash."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("//New Topic " + add_name)
        CanonizerCreateCampPage(self.driver).load_create_camp_page().create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        CanonizerCampStatementPage(self.driver).click_add_camp_statement()
        self.driver.find_element(*CampStatementIdentifiers.STATEMENT_TEXT).send_keys("create new statement")
        self.driver.find_element(*CampStatementIdentifiers.SAVE_DRAFT).click()
        statement = self.driver.current_url
        topic = statement.replace("create/statement", "topic")
        self.driver.get(topic)
        self.driver.find_element(*CampStatementIdentifiers.SAVE_DRAFT).click()
        result = self.driver.find_element(*CampStatementIdentifiers.EDIT_DRAFT).text

        assert "Save As Draft" in result


    def test_profile_page_nickname_tab(self):
        """Test case: Profile page nickname tab."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerPofilePage(self.driver).profile_page_nickname_tab()

        result = self.driver.find_element(*ProfileInfoIdentifiersPage.NICKNAME).text
        assert "NICKNAMES" in result

    def test_profile_page_preferences_tab(self):
        """Test case: Profile page preferences tab."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerPofilePage(self.driver).profile_page_preferences_tab()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.PREFERENCE).text
        assert "PREFERENCES" in result

    def test_profile_page_direct_supported_camp_tab(self):
        """Test case: Profile page direct supported camp tab."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerPofilePage(self.driver).profile_page_direct_supported_camp_tab()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.DIRECT_SUPPORTED).text
        assert "DIRECT SUPPORTED CAMPS" in result

    def test_profile_page_delegate_supported_camp_tab(self):
        """Test case: Profile page delegate supported camp tab."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerPofilePage(self.driver).profile_page_delegate_supported_camp_tab()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.DELEGATE_SUPPORT).text
        assert "DELEGATED SUPPORTED CAMPS" in result
    def test_profile_page_mysubscription_tab(self):
        """Test case: Profile page mysubscription tab."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerPofilePage(self.driver).profile_page_mysubscription_tab()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.MY_SUBCRIPTION).text
        assert "My Subscriptions" in result

    def test_profile_page_account_setting_social_auth_tab(self):
        """Test case: Profile page account setting social auth tab."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerPofilePage(self.driver).profile_page_account_setting_social_auth_tab()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.SOCIAL_AUTH).text
        assert "SOCIAL AUTH" in result

    def test_profile_page_account_setting_password_tab(self):
        """Test case: Profile page account setting password tab."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerPofilePage(self.driver).profile_page_account_setting_password_tab()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.CHANGE_PASSWORD).text
        assert "CHANGE PASSWORD" in result

    def test_update_first_name(self):
        """Test case: Update first name."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerPofileUpdatePage(self.driver).enter_first_name()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.PROFILE_UPDATED_POP_UP).text

        assert "Profile updated successfully." in result


    def test_update_last_name(self):
        """Test case: Update last name."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerPofileUpdatePage(self.driver).enter_last_name()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.PROFILE_UPDATED_POP_UP).text

        assert "Profile updated successfully." in result

    def test_update_date_of_birth(self):
        """Test case: Update date of birth."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerPofileUpdatePage(self.driver).select_date_of_birth()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.PROFILE_UPDATED_POP_UP).text

        assert "Profile updated successfully." in result

    def test_update_gender(self):
        """Test case: Update gender."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerPofileUpdatePage(self.driver).select_gender()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.PROFILE_UPDATED_POP_UP).text

        assert "Profile updated successfully." in result

    def test_update_phone_number(self):
        """Test case: Update phone number."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerPofileUpdatePage(self.driver).enter_phone_number()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.PROFILE_UPDATED_POP_UP).text

        assert "Profile updated successfully." in result

    def test_update_address_1(self):
        """Test case: Update address 1."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerPofileUpdatePage(self.driver).enter_address_1()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.PROFILE_UPDATED_POP_UP).text
        assert "Profile updated successfully." in result

    def test_profile_setting_public_crash(self):
        """Test case: Profile setting public crash."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerPofilePage(self.driver).profile_page_public_crash()
        self.driver.find_element(*ProfileInfoIdentifiersPage.PREFERENCE_SAVE_BUTTON).click()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.PROFILE_UPDATED_POP_UP).text

        assert "Profile updated successfully." in result

    def test_asp_old_urls_for_topics(self):
        """Test case: Asp old urls for topics."""
            # Legacy URL coverage for backward compatibility.
        self.driver.implicitly_wait(30)
        self.driver.get(OLD_ASP_TOPIC_URL)
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/topic/105-Consciousness-Consensus-Projct/1-Agreement?is_tree_open=0" in result

    def test_asp_old_urls_for_camps(self):
        """Test case: Asp old urls for camps."""
        self.driver.implicitly_wait(30)
        self.driver.get(OLD_ASP_CAMP_URL)
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/topic/6669-Test-dlkskndlksndl/1-Agreement?is_tree_open=0" in result

    def test_asp_old_urls_for_support(self):
        """Test case: Asp old urls for support."""
        self.driver.implicitly_wait(30)
        self.driver.get(OLD_ASP_SUPPORT_URL)
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/topic/97-Mormon-Spirits/1-Agreement?is_tree_open=0" in result

    
    def teardown_method(self):

        self.driver.close()

if __name__ == "__main__":
   print("ended")
