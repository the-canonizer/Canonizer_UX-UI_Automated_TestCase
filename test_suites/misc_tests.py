from .shared import *

class MiscTests:

    # Documentation: Click on join now.
    def test_click_on_join_now(self):
        """Test case: Click on join now."""
        print("\n" + str(test_cases('TC_CLICK_ON_REGISTER_BUTTON')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).join_now()

        result = self.driver.find_element(*RegistrationPageIdentifiers.REGISTRATION_TITLE).text
        assert "Create your account" in result



    # Documentation: Registration with valid credential.
    def test_registration_with_valid_credential(self):
        """Test case: Registration with valid credential."""
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_17)
        result = self.driver.find_element(*RegistrationPageIdentifiers.OTP_SENT).text
        assert "Note : Registration code has been sent to your registered email address." in result


    # Documentation: Registration first name with spaces.
    def test_registration_first_name_with_spaces(self):
        """Test case: Registration first name with spaces."""
        print("\n" + str(test_cases('TC_REGISTER_WITH_BLANK_SPACES_FIRST_NAME')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_18)
        result = self.driver.find_element(*RegistrationPageIdentifiers.OTP_SENT).text
        assert "Note : Registration code has been sent to your registered email address." in result


    # TC_REGISTER_WITH_BLANK_FIRST_NAME
    # Documentation: Registration with blank first name.
    def test_registration_with_blank_first_name(self, ):
        """Test case: Registration with blank first name."""
        print("\n" + str(test_cases('TC_REGISTER_WITH_BLANK_FIRST_NAME')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_3)
        result = self.driver.find_element(*RegistrationPageIdentifiers.FIRST_NAME_VALIDATION).text
        assert "Please input your first name!" in result


    # TC_REGISTRATION_WITH_BLANK_EMAIL
    # Documentation: Registration with blank email.
    def test_registration_with_blank_email(self):
        """Test case: Registration with blank email."""
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_BLANK_EMAIL')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_5)
        result = self.driver.find_element(*RegistrationPageIdentifiers.EMAIL_VALIDATION).text
        assert "Please input your E-mail!" in result


    # TC_REGISTER_WITH_BLANK_LAST_NAME
    # Documentation: Registration with blank last name.
    def test_registration_with_blank_last_name(self):
        """Test case: Registration with blank last name."""
        print("\n" + str(test_cases('TC_REGISTER_WITH_BLANK_LAST_NAME')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_4)
        result = self.driver.find_element(*RegistrationPageIdentifiers.LAST_NAME_VALIDATION).text
        assert "Please input your last name!" in result


    # TC_REGISTRATION_WITH_BLANK_PASSWORD
    # Documentation: Registration with blank password.
    def test_registration_with_blank_password(self):
        """Test case: Registration with blank password."""
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_BLANK_PASSWORD')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_6)
        result = self.driver.find_element(*RegistrationPageIdentifiers.PASSWORD_VALIDATION).text
        assert "Please input your password!" in result


    # TC_REGISTRATION_WITH_INVALID_PASSWORD_LENGTH
    # Documentation: Registration with invalid password length.
    def test_registration_with_invalid_password_length(self):
        """Test case: Registration with invalid password length."""
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_INVALID_PASSWORD_LENGTH')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_7)
        result = self.driver.find_element(*RegistrationPageIdentifiers.PASSWORD_TYPE_VALIDATION).text
        assert "Password must contain small, capital letter, number and special character like Abc@1234." in result


    # TC_REGISTER_WITH_BLANK_SPACES_FIRST_NAME

    # TC_REGISTRATION_WITH_INVALID_EMAIL
    # Documentation: Registration with invalid email.
    def test_registration_with_invalid_email(self):
        """Test case: Registration with invalid email."""
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_INVALID_EMAIL')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_14)
        result = self.driver.find_element(*RegistrationPageIdentifiers.VALID_EMAIL).text
        assert "Please enter a valid email address." in result


    # TC_VERIFY_THE_FUNCTIONALITY_OF_REGISTRATION_WITH_MANDATORY_FIELDS
    # Documentation: Verify the functionality of registration with entering data in mandatory fields.
    def test_verify_the_functionality_of_registration_with_entering_data_in_mandatory_fields(self):
        """Test case: Verify the functionality of registration with entering data in mandatory fields."""
        print("\n" + str(test_cases('TC_VERIFY_THE_FUNCTIONALITY_OF_REGISTRATION_WITH_MANDATORY_FIELDS')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_15)
        result = self.driver.find_element(*RegistrationPageIdentifiers.OTP_SENT).text
        assert "Note : Registration code has been sent to your registered email address." in result


    # TC_VERIFY_THE_FUNCTIONALITY_OF_REGISTRATION_WITH_MOBILE_NUMBER_FIELDS
    # Documentation: Verify the functionality 0f registration with entering data in mobile number field.
    def test_verify_the_functionality_0f_registration_with_entering_data_in_mobile_number_field(self):
        """Test case: Verify the functionality 0f registration with entering data in mobile number field."""
        print("\n" + str(test_cases('TC_VERIFY_THE_FUNCTIONALITY_OF_REGISTRATION_WITH_MOBILE_NUMBER_FIELDS')))
        self.driver.implicitly_wait(30)
        CanonizerRegisterPage(self.driver).click_on_register_button().registration_with_valid_credential(reg_list_16)
        result = self.driver.find_element(*RegistrationPageIdentifiers.VALID_PHONE_NUMBER).text
        assert "Please input valid phone number!" in result


    # TC_VERIFY_ONE_TIME_REQUEST_CODE_WITH_VALID_CREDENTIALS
    # Documentation: Verify one time request code with valid credentials.
    def test_verify_one_time_request_code_with_valid_credentials(self):
        """Test case: Verify one time request code with valid credentials."""
        print("\n" + str(test_cases('TC_VERIFY_ONE_TIME_REQUEST_CODE_WITH_VALID_CREDENTIALS')))
        self.driver.implicitly_wait(30)
        CanonizerLoginPage(self.driver).click_on_login_page_button().verify_one_time_request_code(DEFAULT_USER)
        result = self.driver.find_element(*LoginPageIdentifiers.RESEND_OTP).text
        assert "Resend OTP" in result


    # Documentation: Registration with blank confirm password.
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


    # Documentation: Registration with mismatched passwords.
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


    # Documentation: Registration with invalid mobile number.
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


    # Documentation: Registration social providers are available.
    def test_registration_social_providers_are_available(self):
        """Test case: Registration social providers are available."""
        register_page = CanonizerRegisterPage(self.driver).click_on_register_button()
        providers = register_page.social_signup_providers()
        assert set(providers) == {"facebook", "google", "linkedin", "github"}
        assert all(button.is_displayed() and button.is_enabled() for button in providers.values())


    # Documentation: Load my participation page.
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

    # TC_NEW_FEED_WITH_BLANK_FIELDS
    # Documentation: Create new with blank fields.
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


    # Documentation: Cafe text in address bar.
    def test_cafe_text_in_address_bar(self):
        """Test case: Cafe text in address bar."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.get(PROFILE_PAGE)
        self.driver.find_element(*ProfileInfoIdentifiersPage.ADDRESS_LINE).send_keys("Café,")
        self.driver.find_element(*ProfileInfoIdentifiersPage.SAVE_PROFILE_CHANGES).click()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.PROFILE_UPDATED_POP_UP).text

        assert "Profile updated successfully." in result


    # Documentation: Update first name.
    def test_update_first_name(self):
        """Test case: Update first name."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerPofileUpdatePage(self.driver).enter_first_name()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.PROFILE_UPDATED_POP_UP).text

        assert "Profile updated successfully." in result



    # Documentation: Update last name.
    def test_update_last_name(self):
        """Test case: Update last name."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerPofileUpdatePage(self.driver).enter_last_name()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.PROFILE_UPDATED_POP_UP).text

        assert "Profile updated successfully." in result


    # Documentation: Update date of birth.
    def test_update_date_of_birth(self):
        """Test case: Update date of birth."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerPofileUpdatePage(self.driver).select_date_of_birth()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.PROFILE_UPDATED_POP_UP).text

        assert "Profile updated successfully." in result


    # Documentation: Update gender.
    def test_update_gender(self):
        """Test case: Update gender."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerPofileUpdatePage(self.driver).select_gender()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.PROFILE_UPDATED_POP_UP).text

        assert "Profile updated successfully." in result


    # Documentation: Update phone number.
    def test_update_phone_number(self):
        """Test case: Update phone number."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerPofileUpdatePage(self.driver).enter_phone_number()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.PROFILE_UPDATED_POP_UP).text

        assert "Profile updated successfully." in result


    # Documentation: Update address 1.
    def test_update_address_1(self):
        """Test case: Update address 1."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerPofileUpdatePage(self.driver).enter_address_1()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.PROFILE_UPDATED_POP_UP).text
        assert "Profile updated successfully." in result
