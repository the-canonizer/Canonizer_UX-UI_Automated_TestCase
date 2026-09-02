from .shared import *

class StatementTests:


    # Documentation: Add statement for archived camp.
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

    # TC_LOAD_ADD_NEW_CAMP_STATEMENT_PAGE
    # Camp statement creation and editing tests.

    # Documentation: Camp statement button.
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

    # Documentation: Load camp statement page.
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


    # Documentation: Add camp statement with valid data.
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

    # Documentation: Add camp statement page with asterisk.
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


    # Documentation: Add camp statement without mandatory field.
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


    # Documentation: Add camp statement with trailing spaces.
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


    # Documentation: Add camp statement with blank data.
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


    # Documentation: Cancel create camp statement.
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


    # Documentation: Preview camp statement.
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

        
    # Documentation: Camp statement template.
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
    # Documentation: Load edit camp statement.
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


    # Documentation: Edit camp statement.
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

    # Documentation: Update camp statement with mandatory field.
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


    # Documentation: Edit camp statement with trailing spaces.
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


    # Documentation: Edit camp statement with blank data.
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


    # Documentation: Compare camp statement.
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


    # Documentation: Advanced search camp statement tab navigation.
    def test_advanced_search_camp_statement_tab_navigation(self):
        """Test case: Advanced search camp statement tab navigation."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerSearchPage(self.driver).open_all_results("tree").click_sidebar_tab("/search/camp_statement")
        result = self.driver.find_element(*SearchPageIdentifiers.CAMP_STATEMENT_HEADING).text
        assert "Camp Statement" in result


    # Documentation: Authentication expiry for create statement.
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


    # Documentation: Statement image more than 5mb.
    def test_statement_image_more_than_5mb(self):
        """Test case: Statement image more than 5mb."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.get("https://ux-dev.canonizer.com/manage/statement/8215-update")
        image_statement = image_over_5mb()
        upload_image = self.driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        upload_image.send_keys(image_statement)

        result = self.driver.find_element(*CampStatementIdentifiers.IMAGE_SIZE_EXCEEDED).text
        assert "Alert: Image size exceed" in result


    # Documentation: Statement image more than 5mb note.
    def test_statement_image_more_than_5mb_note(self):
        """Test case: Statement image more than 5mb note."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.get("https://ux-dev.canonizer.com/manage/statement/8215-update")
        result = self.driver.find_element(*CampStatementIdentifiers.IMAGE_SIZE_NOTE).text

        assert "Note: You can drag and drop image files into the editor. The maximum allowed file size is 5 MB." in result
