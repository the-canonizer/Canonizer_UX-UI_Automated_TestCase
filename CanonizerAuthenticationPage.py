from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from CanonizerBase import Page
from Identifiers import AuthenticationFlowIdentifiers


class CanonizerAuthenticationPage(Page):
    """Forgot-password, OTP, and reset-password route workflows."""

    def wait_for_forgot_password_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(AuthenticationFlowIdentifiers.FORGOT_TITLE)
        )
        return self

    def submit_forgot_password_email(self, email):
        self.wait_for_forgot_password_page()
        field = self.set_input_value(AuthenticationFlowIdentifiers.FORGOT_EMAIL, email)
        if email:
            pass
        else:
            field.send_keys(Keys.TAB)
        self.find_element(*AuthenticationFlowIdentifiers.FORGOT_SUBMIT).click()
        return self

    def forgot_password_error(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                AuthenticationFlowIdentifiers.FORGOT_EMAIL_ERROR
            )
        ).text

    def wait_for_otp_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(AuthenticationFlowIdentifiers.OTP_TITLE)
        )
        return self

    def enter_otp(self, otp):
        inputs = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(AuthenticationFlowIdentifiers.OTP_INPUTS)
        )
        for field, value in zip(inputs, otp):
            field.clear()
            field.send_keys(value)
        return self

    def submit_otp(self):
        self.find_element(*AuthenticationFlowIdentifiers.OTP_SUBMIT).click()
        return self

    def resend_otp(self):
        WebDriverWait(self.driver, 70).until(
            EC.element_to_be_clickable(AuthenticationFlowIdentifiers.OTP_RESEND)
        ).click()
        return self

    def fill_reset_password(self, password, confirmation):
        self.set_input_value(AuthenticationFlowIdentifiers.RESET_PASSWORD, password)
        confirmation_field = self.set_input_value(
            AuthenticationFlowIdentifiers.RESET_CONFIRM_PASSWORD, confirmation
        )
        confirmation_field.send_keys(Keys.TAB)
        return self

    def reset_confirmation_error(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                AuthenticationFlowIdentifiers.RESET_CONFIRM_ERROR
            )
        ).text
