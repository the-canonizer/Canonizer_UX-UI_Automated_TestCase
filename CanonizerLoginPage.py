import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from CanonizerBase import Page
from CanonizerValidationCheckMessages import message
from Identifiers import LoginPageIdentifiers
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import *
from selenium import webdriver
from Config import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CanonizerLoginPage(Page):
    """
    Class Name : CanonizerLoginPage
    Description : Test the functionality of the Login and Logout Page
                  Forgot Password Functionality also needs to be added on this Page.
    Attributes: None
    """

    def driver(self):
        self.driver = webdriver.Chrome()
        self.action = ActionChains(self.driver)
    def click_on_login_page_button(self):
        """
        This function is to click on the login button
        -> Hover to the Login button
        -> Find the element and click it
        :return:
        Return the result to the main page.
        """
        self.hover(*LoginPageIdentifiers.LOGIN_PAGE_BUTTON)
        self.find_element(*LoginPageIdentifiers.LOGIN_PAGE_BUTTON).click()
        return CanonizerLoginPage(self.driver)

    def enter_email(self, user):
        """
        "Enter User Email to the Email Box."
        Args:
            :param user: Email ID of the User
        :return:
            SEND_KEYS is equivalent to entering keys using keyboard. And control return to the calling program.
        """
        self.find_element(*LoginPageIdentifiers.EMAIL).send_keys(user)

    def enter_password(self, password):
        """
        This function is to entering the user password to the password field and return control.
        Args:
            :param password: Password of the User
        :return:
            After entering the password to the Password field. Function return control.
        """
        self.find_element(*LoginPageIdentifiers.PASSWORD).send_keys(password)

    def click_login_button(self):
        """
        This function verify if the login page loads properly
        :return:
            Once the page is loaded, return result to the main program.
        """
        self.find_element(*LoginPageIdentifiers.SUBMIT).click()

    def login(self, user, password):
        """
        This function is to click the login button and return result to the main program.
        Args:
            :param user: Email ID of the User
            :param password: Password of the User
        :return:
            After Entering the Username and Password, function clicks on the login button and returns the control.
        """
        self.enter_email(user)
        self.enter_password(password)
        self.click_login_button()

    def login_with_valid_user(self, user, password):
        """
        This function is a part of test case, test_login_with_valid_user and it verifies using valid username and
        password, application works properly and take the user to the home page.
        Args:
            :param user: Email ID of the User
            :param password: Password of User
        :return:
            Retrun the result to the main program
        """
        self.login(user, password)

        return CanonizerLoginPage(self.driver)

    def login_page_mandatory_fields_are_marked_with_asterisk(self):
        """
        This Function checks, if Mandatory fields on Register Page Marked with *
        First Name, Last Name, Email, Password, Confirm Password are Mandatory Fields

        :return: the element value

        """
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'ant-form-item-required')))
        except TimeoutException:
            pass
        return \
            self.find_element(*LoginPageIdentifiers.EMAIL_ASTRK) and \
            self.find_element(*LoginPageIdentifiers.PASSWORD_ASTRK)

    def click_on_login_button(self):
        self.driver.implicitly_wait(30)
        self.hover(*LoginPageIdentifiers.LOGIN_BUTTON)
        self.find_element(*LoginPageIdentifiers.LOGIN_BUTTON).click()
        self.driver.implicitly_wait(30)
        return CanonizerLoginPage(self.driver)

    def verify_the_login_page(self, email, password):
        #self.click_on_login_button()
        self.find_element(*LoginPageIdentifiers.EMAIL).clear()
        self.find_element(*LoginPageIdentifiers.EMAIL).send_keys(email)
        self.find_element(*LoginPageIdentifiers.PASSWORD).send_keys(password)
        self.find_element(*LoginPageIdentifiers.SUBMIT).click()

    def click_on_close_icon_button(self):
        self.click_on_login_button()
        self.hover(*LoginPageIdentifiers.CLOSE_BUTTON)
        self.find_element(*LoginPageIdentifiers.CLOSE_BUTTON).click()
        self.hover(*LoginPageIdentifiers.LOGIN_BUTTON)
        title = self.find_element(*LoginPageIdentifiers.LOGIN_BUTTON).text
        if title == message['Login_Page']['LOGIN_TITLE']:
            return CanonizerLoginPage(self.driver)
        else:
            print("Error message not found")

    def verify_the_login_with_invalid_email_format(self, default_invalid_user, default_pass):
        self.verify_the_login_page(default_invalid_user, default_pass)
        return CanonizerLoginPage(self.driver)


    def verify_the_login_with_blank_email(self, blank_email, password):
        self.verify_the_login_page(blank_email, password)
        return CanonizerLoginPage(self.driver)

    def verify_the_login_with_blank_password(self, default_user, blank_password):
        self.verify_the_login_page(default_user, blank_password)
        self.hover(*LoginPageIdentifiers.BLANK_PASSWORD_ERROR)
        error = self.find_element(*LoginPageIdentifiers.BLANK_PASSWORD_ERROR).text
        if error == message['Login_Page']['BLANK_PASSWORD']:
            return CanonizerLoginPage(self.driver)

    def verify_the_login_functionality_by_entering_the_registered_credential(self, default_user, default_pass):
        self.driver.implicitly_wait(30)
        self.verify_the_login_page(default_user, default_pass)
        return CanonizerLoginPage(self.driver)

    def verify_the_forget_password_button(self):
        #self.click_on_login_button()
        self.hover(*LoginPageIdentifiers.FORGET_PASSWORD)
        self.find_element(*LoginPageIdentifiers.FORGET_PASSWORD).click()
        self.find_element(*LoginPageIdentifiers.FORGET_PASSWORD_TITLE).click()
        return CanonizerLoginPage(self.driver)

    def verify_the_remember_me_checkbox(self, default_user, default_pass):
        self.click_on_login_button()
        self.find_element(*LoginPageIdentifiers.EMAIL).clear()
        self.find_element(*LoginPageIdentifiers.EMAIL).send_keys(default_user)
        self.find_element(*LoginPageIdentifiers.PASSWORD).send_keys(default_pass)
        self.find_element(*LoginPageIdentifiers.CHECK_BOX).click()
        self.find_element(*LoginPageIdentifiers.SUBMIT).click()

        return CanonizerLoginPage(self.driver)

    def click_on_register_now_button_on_login_page(self):
        self.find_element(*LoginPageIdentifiers.REGISTER_NOW_LINK).click()

        return CanonizerLoginPage(self.driver)


    def verify_one_time_request_code(self, default_user):
        self.find_element(*LoginPageIdentifiers.EMAIL).clear()
        self.find_element(*LoginPageIdentifiers.EMAIL).send_keys(default_user)
        self.find_element(*LoginPageIdentifiers.REQUEST_CODE).click()

    def verify_one_time_request_code_with_invalid_email(self, default_user):
        self.driver.implicitly_wait(30)
        self.verify_one_time_request_code(default_user)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, "login_form_username_help")))
        return CanonizerLoginPage(self.driver)

    def verify_one_time_request_code_with_valid_credentials(self, default_user):
        self.driver.implicitly_wait(30)

        self.verify_one_time_request_code(default_user)
        return CanonizerLoginPage(self.driver)

    def verifying_facebook_link(self):
        self.find_element(*LoginPageIdentifiers.FACEBOOK_LINK).click()
        return CanonizerLoginPage(self.driver)


    def verifying_google_link(self):
        self.driver.implicitly_wait(10)
        self.find_element(*LoginPageIdentifiers.GOOGLE_LINK).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, "headingText")))
        return CanonizerLoginPage(self.driver)


    def verifying_twitter_link(self):
        self.click_on_login_button()
        self.find_element(*LoginPageIdentifiers.TWITTER_LINK).click()
        self.hover(*LoginPageIdentifiers.TWITTER_TITLE)
        title = self.find_element(*LoginPageIdentifiers.TWITTER_TITLE).text
        if title == message['Login_Page']['TWITTER_TITLE']:
            return CanonizerLoginPage(self.driver)
        else:
            print("Title not found")

    def verifying_linkedin_link(self):
        self.click_on_login_button()
        self.find_element(*LoginPageIdentifiers.LINKEDIN_LINK).click()
        self.hover(*LoginPageIdentifiers.LINKEDIN_TITLE)
        title = self.find_element(*LoginPageIdentifiers.LINKEDIN_TITLE).text
        if title == message['Login_Page']['LINKEDIN_TITLE']:
            return CanonizerLoginPage(self.driver)
        else:
            print("Title not found")

    def verifying_github_link(self):
        self.click_on_login_button()
        self.find_element(*LoginPageIdentifiers.GITHUB_LINK).click()
        self.driver.implicitly_wait(20)
        return CanonizerLoginPage(self.driver)
