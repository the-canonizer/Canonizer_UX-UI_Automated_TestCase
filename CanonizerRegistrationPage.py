import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from CanonizerBase import Page
from CanonizerValidationCheckMessages import message
from Identifiers import RegistrationPageIdentifiers


class CanonizerRegisterPage(Page):
    """
    Class Name: CanonizerRegisterPage

    """

    def click_register_button(self):
        """
        -> Hover the control towards the register button. Identifiers are loaded from Identifiers Class
        -> Find the register button and Click on it.

        :return:
            Return the control to the main Program
        """

        self.hover(*RegistrationPageIdentifiers.REGISTER)
        self.find_element(*RegistrationPageIdentifiers.REGISTER).click()

        return CanonizerRegisterPage(self.driver)

    def register_page_mandatory_fields_are_marked_with_asterisk(self):
        """
        This Function checks, if Mandatory fields on Register Page Marked with *
        First Name, Last Name, Email, Password, Confirm Password are Mandatory Fields

        :return: the element value
        """
        return \
            self.find_element(*RegistrationPageIdentifiers.FIRST_NAME_ASTRK) and \
            self.find_element(*RegistrationPageIdentifiers.LAST_NAME_ASTRK) and \
            self.find_element(*RegistrationPageIdentifiers.EMAIL_ASTRK) and \
            self.find_element(*RegistrationPageIdentifiers.PASSWORD_ASTRK) and \
            self.find_element(*RegistrationPageIdentifiers.CONFIRM_PASSWORD_ASTRK)

    def enter_first_name(self, firstname):
        self.find_element(*RegistrationPageIdentifiers.FIRST_NAME).send_keys(firstname)

    def enter_last_name(self, lastname, ):
        self.find_element(*RegistrationPageIdentifiers.LAST_NAME).send_keys(lastname)

    def enter_email(self, user):
        self.find_element(*RegistrationPageIdentifiers.EMAIL).send_keys(user)

    def enter_mobile_number(self, mobile_number):
        self.find_element(*RegistrationPageIdentifiers.MOBILE_NUMBER).send_keys(mobile_number)

    def enter_password(self, password):
        self.find_element(*RegistrationPageIdentifiers.PASSWORD).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.find_element(*RegistrationPageIdentifiers.CONFIRM_PASSWORD).send_keys(confirm_password)

    def click_register_now_button(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, 'ant-btn ant-btn-primary ant-btn-block login-form-button')))
        except TimeoutException:
            pass
        self.find_element(*RegistrationPageIdentifiers.REGISTER_NOW).click()

    def register(self, *args):
        self.enter_first_name(args[0])
        self.enter_last_name(args[1])
        self.enter_email(args[2])
        self.enter_mobile_number(args[3])
        self.enter_password(args[4])
        self.enter_confirm_password(args[5])
        self.click_register_now_button()

    def registration_with_valid_credential(self, reg_list_17):
        self.register(reg_list_17[0], reg_list_17[1], reg_list_17[2], reg_list_17[3], reg_list_17[4], reg_list_17[5])
        return CanonizerRegisterPage(self.driver)
    def registration_with_blank_first_name(self, reg_list_3):
        self.register(reg_list_3[0], reg_list_3[1], reg_list_3[2], reg_list_3[3], reg_list_3[4], reg_list_3[5])
        error = self.find_element(*RegistrationPageIdentifiers.ERROR_FIRST_NAME).text
        if error == message['Register_Page']['FIRST_NAME_ERROR']:
            return CanonizerRegisterPage(self.driver)
        else:
            print("Error message not found")

    def registration_with_blank_last_name(self, reg_list_4):
        self.register(reg_list_4[0], reg_list_4[1], reg_list_4[2], reg_list_4[3], reg_list_4[4], reg_list_4[5])
        error = self.find_element(*RegistrationPageIdentifiers.ERROR_LAST_NAME).text
        if error == message['Register_Page']['LAST_NAME_ERROR']:
            return CanonizerRegisterPage(self.driver)
        else:
            print("Error message not found")

    def registration_with_blank_email(self, reg_list_5):
        self.register(reg_list_5[0], reg_list_5[1], reg_list_5[2], reg_list_5[3], reg_list_5[4], reg_list_5[5])
        error = self.find_element(*RegistrationPageIdentifiers.ERROR_EMAIL).text
        if error == message['Register_Page']['BLANK_EMAIL_ERROR']:
            return CanonizerRegisterPage(self.driver)
        else:
            print("Error message not found")

    def registration_with_blank_password(self, reg_list_6):
        self.register(reg_list_6[0], reg_list_6[1], reg_list_6[2], reg_list_6[3], reg_list_6[4], reg_list_6[5])
        error = self.find_element(*RegistrationPageIdentifiers.ERROR_PASSWORD).text
        if error == message['Register_Page']['BLANK_PASSWORD_ERROR']:
            return CanonizerRegisterPage(self.driver)
        else:
            print("Error message not found")

    def registration_with_spaces_first_name(self, reg_list_18):
        self.register(reg_list_18[0], reg_list_18[1], reg_list_18[2], reg_list_18[3], reg_list_18[4], reg_list_18[5])
        return CanonizerRegisterPage(self.driver)


    def registration_with_invalid_password_length(self, reg_list_7):
        self.register(reg_list_7[0], reg_list_7[1], reg_list_7[2], reg_list_7[3], reg_list_7[4], reg_list_7[5])
        error = self.find_element(*RegistrationPageIdentifiers.ERROR_PASSWORD).text
        if error == message['Register_Page']['INVALID_PASSWORD_ERR0R']:
            return CanonizerRegisterPage(self.driver)
        else:
            print("Error message not found")

    def registration_with_invalid_email(self, reg_list_14):
        self.register(reg_list_14[0], reg_list_14[1], reg_list_14[2], reg_list_14[3], reg_list_14[4], reg_list_14[5])
        error = self.find_element(*RegistrationPageIdentifiers.ERROR_EMAIL).text
        if error == message['Register_Page']['INVALID_EMAIL_ERROR']:
            return CanonizerRegisterPage(self.driver)
        else:
            print("Error message not found")

    def verify_the_functionality_0f_registration_with_entering_data_in_mobile_number_field(self, reg_list_16):
        self.register(reg_list_16[0], reg_list_16[1], reg_list_16[2], reg_list_16[3], reg_list_16[4], reg_list_16[5])
        error = self.find_element(*RegistrationPageIdentifiers.ERROR_MOBILE_NUMBER).text
        if error == message['Register_Page']['MOBILE_NUMBER_ERROR']:
            return CanonizerRegisterPage(self.driver)
        else:
            print("Error message not found")

        return CanonizerRegisterPage(self.driver)

    def verify_the_functionality_of_registration_with_entering_data_in_mandatory_fields(self, reg_list_15):
        self.register(reg_list_15[0], reg_list_15[1], reg_list_15[2], reg_list_15[3], reg_list_15[4], reg_list_15[5])

        return CanonizerRegisterPage(self.driver)

    def click_on_register_button(self):
        self.hover(*RegistrationPageIdentifiers.REGISTER)
        self.find_element(*RegistrationPageIdentifiers.REGISTER).click()
        self.hover(*RegistrationPageIdentifiers.REGISTRATION_TITLE)
        return CanonizerRegisterPage(self.driver)

    def check_login_page_open_click_login_here_link(self):
        self.find_element(*RegistrationPageIdentifiers.REGISTER).click()
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'ant-typography Registration_ft_link__tyQ1C')))
        except TimeoutException:
            pass
        self.find_element(*RegistrationPageIdentifiers.LOGIN_HERE).click()
        self.hover(*RegistrationPageIdentifiers.LOGIN_TITLE)
        title = self.find_element(*RegistrationPageIdentifiers.LOGIN_TITLE).text
        if title == message['Create_Topic']['LOGIN_TITLE']:
            return CanonizerRegisterPage(self.driver)
        else:
            print("Title not found")
