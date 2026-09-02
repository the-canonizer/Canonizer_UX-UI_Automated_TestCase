from .shared import *

class AuthRegistrationTests:



    # Authentication and registration flow tests.
    # Documentation: Login to canonizer.
    def test_login_to_canonizer(self):
        """Test case: Login to canonizer."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        result = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/div[2]/section/div/button/span[1]").text
        assert "Browse More" in result


    # TC_REGISTER_PAGE_MANDATORY_FIELDS_MARKED_WITH_ASTERISK
    # Documentation: Register page mandatory fields are marked with asterisk.
    def test_register_page_mandatory_fields_are_marked_with_asterisk(self):
        """Test case: Register page mandatory fields are marked with asterisk."""
        assert CanonizerRegisterPage(
            self.driver).click_register_button().register_page_mandatory_fields_are_marked_with_asterisk()


    # TC_CHECK_LOGIN_PAGE_OPEN_CLICK_ON_LOGIN_HERE_LINK
    # Documentation: Check login page open click login here link.
    def test_check_login_page_open_click_login_here_link(self):
        """Test case: Check login page open click login here link."""
        print("\n" + str(test_cases('TC_CHECK_LOGIN_PAGE_OPEN_CLICK_ON_LOGIN_HERE_LINK')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button()
        CanonizerRegisterPage(self.driver).check_login_page_open_click_login_here_link()
        result = self.driver.current_url
        assert "login" in result


    # Documentation: Click on login button.
    def test_click_on_login_button(self):
        """Test case: Click on login button."""
        print("\n" + str(test_cases('TC_CLICK_ON_LOGIN_BUTTON')))
        self.driver.implicitly_wait(30)
        CanonizerLoginPage(self.driver).click_on_login_page_button()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "login-submit-btn")))
        result = self.driver.current_url
        assert "login" in result



    # TC_LOGIN_WITH_REGISTERED_CREDENTIALS
    # Documentation: Login with registered credentials.
    def test_login_with_registered_credentials(self):
        """Test case: Login with registered credentials."""
        print("\n" + str(test_cases('TC_LOGIN_WITH_REGISTERED_CREDENTIALS')))
        self.driver.implicitly_wait(30)
        CanonizerLoginPage(self.driver).click_on_login_page_button().verify_the_login_functionality_by_entering_the_registered_credential(DEFAULT_USER, DEFAULT_PASS)
        result = self.driver.find_element(*LoginPageIdentifiers.START_TOPIC_BUTTON).text
        assert "Start a Topic" in result


    # TC_VERIFY_THE_LOGIN_WITH_BLANK_EMAIL
    # Documentation: Verify the login with blank email.
    def test_verify_the_login_with_blank_email(self):
        """Test case: Verify the login with blank email."""
        print("\n" + str(test_cases('TC_LOGIN_WITH_REGISTERED_CREDENTIALS')))
        self.driver.implicitly_wait(30)
        CanonizerLoginPage(self.driver).click_on_login_page_button().verify_the_login_with_blank_email("", DEFAULT_PASS)
        result = self.driver.find_element(*LoginPageIdentifiers.EMAIL_VALIDATION).text
        assert "Please input your Email!" in result


    # TC_VERIFY_THE_LOGIN_WITH_BLANK_PASSWORD
    # Documentation: Verify the login with blank password.
    def test_verify_the_login_with_blank_password(self):
        """Test case: Verify the login with blank password."""
        print("\n" + str(test_cases('TC_VERIFY_THE_LOGIN_WITH_BLANK_PASSWORD')))
        self.driver.implicitly_wait(30)
        CanonizerLoginPage(self.driver).click_on_login_page_button().verify_the_login_with_blank_password(DEFAULT_USER, "")
        result = self.driver.find_element(*LoginPageIdentifiers.PASSWORD_VALIDATION).text
        assert "Please input your Password!" in result


    # TC_LOGIN_WITH_INVALID_EMAIL
    # Documentation: Login with invalid email.
    def test_login_with_invalid_email(self):
        """Test case: Login with invalid email."""
        self.driver.implicitly_wait(30)
        CanonizerLoginPage(self.driver).click_on_login_page_button().verify_the_login_with_invalid_email_format(DEFAULT_INVALID_USER, DEFAULT_PASS)
        result = self.driver.find_element(*LoginPageIdentifiers.VALID_EMAIL).text
        assert "Input is not valid!" in result


    # Documentation: Login page mandatory fields are marked with asterisk.
    def test_login_page_mandatory_fields_are_marked_with_asterisk(self):
        """Test case: Login page mandatory fields are marked with asterisk."""
        login_page = CanonizerLoginPage(self.driver).click_on_login_page_button()
        assert login_page.mandatory_fields_are_marked()


    # Documentation: Login remember me is selected by default.
    def test_login_remember_me_is_selected_by_default(self):
        """Test case: Login remember me is selected by default."""
        login_page = CanonizerLoginPage(self.driver).click_on_login_page_button()
        assert login_page.remember_me_is_selected()


    # Documentation: Login register now link.
    def test_login_register_now_link(self):
        """Test case: Login register now link."""
        CanonizerLoginPage(self.driver).click_on_login_page_button().open_registration_from_login()
        assert "/registration" in self.driver.current_url
        assert self.driver.find_element(
            *RegistrationPageIdentifiers.REGISTRATION_TITLE
        ).is_displayed()


    # Documentation: Forgot password link.
    def test_forgot_password_link(self):
        """Test case: Forgot password link."""
        CanonizerLoginPage(self.driver).click_on_login_page_button().open_forgot_password()
        assert "/forgot-password" in self.driver.current_url
        assert self.driver.find_element(
            *AuthenticationFlowIdentifiers.FORGOT_TITLE
        ).is_displayed()

    # Documentation: Login social provider is available.
    def test_login_social_provider_is_available(self, provider):
        """Test case: Login social provider is available."""
        login_page = CanonizerLoginPage(self.driver).click_on_login_page_button()
        social_button = login_page.social_login_providers()[provider]
        assert social_button.is_displayed()
        assert social_button.is_enabled()


    # Documentation: Logout.
    def test_logout(self):
        """Test case: Logout."""
        self.login_to_canonizer_app()
        CanonizerLoginPage(self.driver).logout()
        assert self.driver.find_element(
            *LoginPageIdentifiers.LOGGED_OUT_LOGIN_LINK
        ).is_displayed()


    # Documentation: Forgot password with blank email.
    def test_forgot_password_with_blank_email(self):
        """Test case: Forgot password with blank email."""
        CanonizerLoginPage(self.driver).click_on_login_page_button().open_forgot_password()
        auth_page = CanonizerAuthenticationPage(self.driver)
        auth_page.submit_forgot_password_email("")
        assert auth_page.forgot_password_error() == "Please input your E-mail!"


    # Documentation: Forgot password with invalid email.
    def test_forgot_password_with_invalid_email(self):
        """Test case: Forgot password with invalid email."""
        CanonizerLoginPage(self.driver).click_on_login_page_button().open_forgot_password()
        auth_page = CanonizerAuthenticationPage(self.driver)
        auth_page.submit_forgot_password_email("not-an-email")
        assert auth_page.forgot_password_error() == "Please enter a valid email address."


    # Documentation: Forgot password with unregistered email.
    def test_forgot_password_with_unregistered_email(self):
        """Test case: Forgot password with unregistered email."""
        CanonizerLoginPage(self.driver).click_on_login_page_button().open_forgot_password()
        auth_page = CanonizerAuthenticationPage(self.driver)
        auth_page.submit_forgot_password_email(UNREGISTERED_EMAIL)
        error = auth_page.forgot_password_error()
        assert error != ""


    # Documentation: Close login modal.
    def test_close_login_modal(self):
        """Test case: Close login modal."""
        CanonizerLoginPage(self.driver).click_on_login_page_button().click_on_close_icon_button()
        assert self.driver.find_element(*LoginPageIdentifiers.LOGIN_BUTTON).is_displayed()


    # Documentation: Forgot password otp with invalid code.
    def test_forgot_password_otp_with_invalid_code(self):
        """Test case: Forgot password otp with invalid code."""
        CanonizerLoginPage(self.driver).click_on_login_page_button().open_forgot_password()
        auth_page = CanonizerAuthenticationPage(self.driver)
        auth_page.submit_forgot_password_email(DEFAULT_USER).wait_for_otp_page()
        auth_page.enter_otp("111111").submit_otp()
        error = self.driver.find_element(*AuthenticationFlowIdentifiers.OTP_ERROR).text
        assert error != ""


    # Documentation: Forgot password otp with blank code.
    def test_forgot_password_otp_with_blank_code(self):
        """Test case: Forgot password otp with blank code."""
        CanonizerLoginPage(self.driver).click_on_login_page_button().open_forgot_password()
        auth_page = CanonizerAuthenticationPage(self.driver)
        auth_page.submit_forgot_password_email(DEFAULT_USER).wait_for_otp_page()
        auth_page.submit_otp()
        error = self.driver.find_element(*AuthenticationFlowIdentifiers.OTP_ERROR).text
        assert error != ""


    # Documentation: Resend forgot password otp.
    def test_resend_forgot_password_otp(self):
        """Test case: Resend forgot password otp."""
        CanonizerLoginPage(self.driver).click_on_login_page_button().open_forgot_password()
        auth_page = CanonizerAuthenticationPage(self.driver)
        auth_page.submit_forgot_password_email(DEFAULT_USER).wait_for_otp_page()
        auth_page.resend_otp()
        assert self.driver.find_element(*AuthenticationFlowIdentifiers.OTP_TITLE).is_displayed()


    # Documentation: Reset password with mismatched passwords.
    def test_reset_password_with_mismatched_passwords(self):
        """Test case: Reset password with mismatched passwords."""
        CanonizerLoginPage(self.driver).click_on_login_page_button().open_forgot_password()
        auth_page = CanonizerAuthenticationPage(self.driver)
        auth_page.submit_forgot_password_email(DEFAULT_USER).wait_for_otp_page()
        auth_page.enter_otp("111111").submit_otp()
        auth_page.fill_reset_password("Test@12345", "Different@12345")
        self.driver.find_element(*AuthenticationFlowIdentifiers.RESET_SUBMIT).click()
        assert auth_page.reset_confirmation_error() == "Confirm Password does not match!"


    # TC_CLICK_CREATE_TOPIC_WITHOUT_USER_LOGIN
    # Documentation: Click create topic without user login.
    def test_click_create_topic_without_user_login(self):
        """Test case: Click create topic without user login."""
        print("\n" + str(test_cases('TC_CLICK_CREATE_TOPIC_WITHOUT_USER_LOGIN')))
        self.driver.implicitly_wait(30)
        CanonizerCreateNewTopic(self.driver).click_create_topic_button_without_login()
        result = self.driver.current_url
        assert "/login?returnUrl=%2Fcreate%2Ftopic" in result


    # Documentation: Upload file without userlogin.
    def test_upload_file_without_userlogin(self):
        """Test case: Upload file without userlogin."""
        self.driver.implicitly_wait(30)
        CanonizerUploadFile(self.driver).upload_file_without_userlogin()
        result = self.driver.current_url
        assert "login" in result
