from .shared import *

class TopicTests:


                # ----- CREATE TOPIC Test Cases Start -----
    # Topic creation and topic lifecycle tests.

    # TC_CLICK_CREATE_TOPIC_WITH_USER_LOGIN
    # Documentation: Click create new topic page button.
    def test_click_create_new_topic_page_button(self):
        """Test case: Click create new topic page button."""
        print("\n" + str(test_cases('TC_CLICK_CREATE_TOPIC_WITH_USER_LOGIN')))
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        result = self.driver.current_url
        assert "/create/topic" in result


    # TC_CREATE_TOPIC_WITH_BLANK_TOPIC_NAME
    # Documentation: Create topic with blank topic name.
    def test_create_topic_with_blank_topic_name(self):
        """Test case: Create topic with blank topic name."""
        print("\n" + str(test_cases('TC_CREATE_TOPIC_WITH_BLANK_TOPIC_NAME')))
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_blank_topic()
        result = self.driver.find_element(*CreateTopicIdentifiers.VALID_TOPIC_NAME).text
        assert "Topic name cannot start with a space" in result


    # TC_CREATE_NEW_TOPIC_WITH_VALID_DATA
    # Documentation: Create topic name with valid data.
    def test_create_topic_name_with_valid_data(self):
        """Test case: Create topic name with valid data."""
        print("\n" + str(test_cases('TC_CREATE_TOPIC_WITH_VALID_DATA')))
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        result = self.driver.current_url
        assert "1-Agreement" in result


    # Documentation: Create same topic name with valid data.
    def test_create_same_topic_name_with_valid_data(self):
        """Test case: Create same topic name with valid data."""
        print("\n" + str(test_cases('TC_CREATE_TOPIC_WITH_VALID_DATA')))
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_same_topic("same topic")
        result = self.driver.find_element(*CreateTopicIdentifiers.SAME_TOPIC_NAME).text
        assert "A Topic with this exact name already exists!" in result


    # Documentation: Create same topic name error link.
    def test_create_same_topic_name_error_link(self):
        """Test case: Create same topic name error link."""
        print("\n" + str(test_cases('TC_CREATE_TOPIC_WITH_VALID_DATA')))
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("new summary", "same topic")
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[2]/form/div[1]/div[1]/a").click()
        result = self.driver.find_element(*CreateTopicIdentifiers.SAME_TOPIC_TITLE).text
        assert "same topic" in result

    # TC_CREATE_NEW_TOPIC_WITH_SPECIAL_CHARS
    # Documentation: Create topic with special chars.
    def test_create_topic_with_special_chars(self):
        """Test case: Create topic with special chars."""
        print("\n", str(test_cases('TC_CREATE_NEW_TOPIC_WITH_SPECIAL_CHARS')))
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_special_chars("New Topic&^&#$(# " + add_name)
        result = self.driver.current_url
        assert "topic" in result


    # TC_CREATE_NEW_WITHOUT_MANDATORY_FIELDS_DATA
    # Documentation: Create topic without entering mandatory fields.
    def test_create_topic_without_entering_mandatory_fields(self):
        """Test case: Create topic without entering mandatory fields."""
        print("\n", str(test_cases('TC_CREATE_NEW_WITHOUT_MANDATORY_FIELDS_DATA')))
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_without_entering_mandatory_fields(" ")
        result = self.driver.current_url        
        assert "create/topic" in result


    # Documentation: Create topic mandatory fields are marked with asterisk.
    def test_create_topic_mandatory_fields_are_marked_with_asterisk(self):
        """Test case: Create topic mandatory fields are marked with asterisk."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        page = CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        assert page.topic_page_mandatory_fields_are_marked_with_asterisk()


    # Documentation: Create topic with trailing spaces.
    def test_create_topic_with_trailing_spaces(self):
        """Test case: Create topic with trailing spaces."""
        print("\n" + str(test_cases('TC_CREATE_NEW_TOPIC_WITH_TRAILING_SPACES')))
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_name_with_trailing_space("New Topic")
        result = self.driver.current_url
        assert "topic" in result


    # Documentation: Create topic using enter key.
    def test_create_topic_using_enter_key(self):
        """Test case: Create topic using enter key."""
        print("\n" + str(test_cases('TC_CREATE_NEW_TOPIC_WITH_ENTER_KEY')))
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_name_with_enter_key("summary", "New Topic " + add_name, "sandbox testing")
        result = self.driver.current_url
        assert "topic" in result


    # Documentation: Create topic with only mandatory fields.
    def test_create_topic_with_only_mandatory_fields(self):
        """Test case: Create topic with only mandatory fields."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
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


    # Documentation: Cancel create topic.
    def test_cancel_create_topic(self):
        """Test case: Cancel create topic."""
        print("\n" + str(test_cases('TC_CLICK_ON_CANCEL_BUTTON')))
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).click_on_cancel_button()
        result = self.driver.find_element(*CreateTopicIdentifiers.MAIN_PAGE).text
        assert "Select Namespace" in result

    # ----- UPDATE TOPIC Test Cases Start -----
    # Topic update and topic history tests.

    # TC_LOAD_TOPIC_HISTORY_PAGE
    # Documentation: Load topic history page.
    def test_load_topic_history_page(self):
        """Test case: Load topic history page."""
        print("\n" + str(test_cases('TC_LOAD_TOPIC_HISTORY_PAGE')))
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()
        result = self.driver.find_element(*CreateTopicIdentifiers.UPDATE_TOPIC_TITLE).text
        assert "Update Topic" in result


    # TC_VERIFY_TOPIC_NAME_ON_TOPIC_HISTORY_PAGE
    # Documentation: Verify topic name on topic history page.
    def test_verify_topic_name_on_topic_history_page(self):
        """Test case: Verify topic name on topic history page."""
        print("\n" + str(test_cases('TC_VERIFY_TOPIC_NAME_ON_TOPIC_HISTORY_PAGE')))
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()

        result = self.driver.current_url
        assert add_name in result


    # TC_VERIFY_SUBMIT_TOPIC_UPDATE_BUTTON
    # Documentation: Verify submit topic update button.
    def test_verify_submit_topic_update_button(self):
        """Test case: Verify submit topic update button."""
        print("\n" + str(test_cases('TC_VERIFY_SUBMIT_TOPIC_UPDATE_BUTTON')))
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()
        CanonizerUpdateTopicPage(self.driver).verify_submit_topic_update_button()

        result = self.driver.find_element(By.ID, "create-topic-btn").text

        assert "Update Topic" in result



    # TC_VERIFY_CANCEL_BUTTON_FUNCTIONALITY_ON_TOPIC_UPDATE_PAGE
    # Documentation: Verify cancel button functionality on topic update page.
    def test_verify_cancel_button_functionality_on_topic_update_page(self):
        """Test case: Verify cancel button functionality on topic update page."""
        print("\n" + str(test_cases('TC_VERIFY_CANCEL_BUTTON_FUNCTIONALITY_ON_TOPIC_UPDATE_PAGE')))
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()
        CanonizerUpdateTopicPage(self.driver).verify_cancel_button_functionality_on_topic_update_page()

        result = self.driver.current_url

        assert "/topic/history/" in result



    # TC_UPDATE_TOPIC_NAME_AND_VERIFY_SUBMIT_UPDATE_BUTTON
    # Documentation: Update topic name.
    def test_update_topic_name(self):
        """Test case: Update topic name."""
        print("\n" + str(test_cases('TC_UPDATE_TOPIC_NAME_AND_VERIFY_SUBMIT_UPDATE_BUTTON')))
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()
        CanonizerUpdateTopicPage(self.driver).update_topic_name()

        result = self.driver.current_url

        assert "topic/history/" in result


    # Documentation: Topic update preview.
    def test_topic_update_preview(self):
        """Test case: Topic update preview."""
        print("\n" + str(test_cases('TC_VERIFY_PREVIEW_BUTTON_FUNCTIONALITY_ON_TOPIC_UPDATE_PAGE')))
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()
        CanonizerUpdateTopicPage(self.driver).verify_preview_button_functionality_on_topic_update_page()
        result = self.driver.find_element(*UpdateTopicIdentifiers.TOPIC_PREVIEW_TITLE).text
        assert "Topic Preview" in result


    # Documentation: Topic preview cancel.
    def test_topic_preview_cancel(self):
        """Test case: Topic preview cancel."""
        print("\n" + str(test_cases('TC_VERIFY_CANCEL_BUTTON_ON_PREVIEW_MODAL')))
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()
        CanonizerUpdateTopicPage(self.driver).verify_cancel_button_on_preview_modal()
        result = self.driver.current_url
        assert "topic/history" in result


    # Documentation: Topic preview submitter nickname.
    def test_topic_preview_submitter_nickname(self):
        """Test case: Topic preview submitter nickname."""
        print("\n" + str(test_cases('TC_VERIFY_SUBMITTER_NICK_NAME_ON_PREVIEW_MODAL')))
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()
        CanonizerUpdateTopicPage(self.driver).verify_submitter_nick_name_on_preview_modal()
        result = self.driver.current_url
        assert "/profile/" in result


    # Documentation: Compare topic versions.
    def test_compare_topic_versions(self):
        """Test case: Compare topic versions."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()
        CanonizerUpdateTopicPage(self.driver).verify_compare_topics_button_functionality()
        result = self.driver.current_url
        assert "compare" in result


    # Documentation: Topic comparison agreement link.
    def test_topic_comparison_agreement_link(self):
        """Test case: Topic comparison agreement link."""
        print("\n" + str(test_cases('TC_VERIFY_AGREEMENT_LINK_ON_TOPIC_COMPARISON_PAGE')))
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()
        CanonizerUpdateTopicPage(self.driver).verify_agreement_link_on_topic_comparison_page()
        result = self.driver.current_url
        assert "1-Agreement" in result


    # Documentation: Topic comparison create topic button.
    def test_topic_comparison_create_topic_button(self):
        """Test case: Topic comparison create topic button."""
        print("\n" + str(test_cases('TC_VERIFY_CREATE_TOPIC_BUTTON_FUNCTIONALITY_ON_TOPIC_COMPARISON_PAGE')))
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()
        CanonizerUpdateTopicPage(self.driver).verify_create_topic_button_functionality_on_topic_comparison_page()
        result = self.driver.current_url
        assert "/create/topic" in result


    # Documentation: Topic comparison back button.
    def test_topic_comparison_back_button(self):
        """Test case: Topic comparison back button."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()
        CanonizerUpdateTopicPage(self.driver).verify_back_arrow_icon_on_topic_comparison_page()
        result = self.driver.current_url
        assert "/topic/history/" in result


    # Documentation: Topic history view this version.
    def test_topic_history_view_this_version(self):
        """Test case: Topic history view this version."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()
        CanonizerUpdateTopicPage(self.driver).verify_view_this_version_button_functionality()
        result = self.driver.current_url
        assert "/topic/" in result

   

    # Documentation: Browse start topic.
    def test_browse_start_topic(self):
        """Test case: Browse start topic."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        self.driver.find_element(*BrowsePageIdentifiers.START_TOPIC).click()
        result = self.driver.current_url
        assert "/create/topic" in result


    # Documentation: Browse only my topics.
    def test_browse_only_my_topics(self):
        """Test case: Browse only my topics."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        CanonizerBrowsePage(self.driver).click_browse_page_button().click_only_my_topics_button()
        result = self.driver.current_url
        assert "browse" in result


    # Documentation: Browse search by topic tag.
    def test_browse_search_by_topic_tag(self):
        """Test case: Browse search by topic tag."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        CanonizerBrowsePage(self.driver).search_topic_tag()
        result = self.driver.current_url
        assert "browse" in result


    # Documentation: Advanced search topic tab navigation.
    def test_advanced_search_topic_tab_navigation(self):
        """Test case: Advanced search topic tab navigation."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        CanonizerSearchPage(self.driver).open_all_results("tree").click_sidebar_tab("/search/topic")
        result = self.driver.find_element(*SearchPageIdentifiers.TOPIC_HEADING).text
        assert "Topic" in result


    # Documentation: Advanced search topic review filter route.
    def test_advanced_search_topic_review_filter_route(self):
        """Test case: Advanced search topic review filter route."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        CanonizerSearchPage(self.driver).open_topic_results("tree", "asof=review")
        result = self.driver.current_url
        assert "asof=review" in result and "/search/topic" in result


    # Documentation: Advanced search topic pagination visibility.
    def test_advanced_search_topic_pagination_visibility(self):
        """Test case: Advanced search topic pagination visibility."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        page = CanonizerSearchPage(self.driver).open_topic_results("tree")
        result = page.is_pagination_visible()
        assert result



    # Documentation: Footer create topic button.
    def test_footer_create_topic_button(self):
        """Test case: Footer create topic button."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        self.driver.find_element(*HomePageIdentifiers.FOOTER_CREATE_TOPIC).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/create/topic" in result


    # Authentication expiry and protected-route checks.
    # Documentation: Authentication expiry for create topic.
    def test_authentication_expiry_for_create_topic(self):
        """Test case: Authentication expiry for create topic."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()

        self.driver.get("https://ux-dev.canonizer.com/create/topic")
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result


    # Documentation: Authentication footer create topic.
    def test_authentication_footer_create_topic(self):
        """Test case: Authentication footer create topic."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()

        self.driver.find_element(*HomePageIdentifiers.FOOTER_CREATE_TOPIC).click()
        self.driver.refresh()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result




    # Documentation: Authentication topic history.
    def test_authentication_topic_history(self):
        """Test case: Authentication topic history."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()

        self.driver.get("https://ux-dev.canonizer.com/topic/history/6669-Test-dlkskndlksndl")
        self.driver.refresh()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" not in result


    # Documentation: Topic name in recent activities.
    def test_topic_name_in_recent_activities(self):
        """Test case: Topic name in recent activities."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("Recent Topic" + add_name)
        self.driver.get(DEFAULT_BASE_URL)
        result = self.driver.find_element(*CreateTopicIdentifiers.RECENT_TOPIC_NAME).text
        assert "Recent Topic" in result


    # Documentation: Preferences topic tag search.
    def test_preferences_topic_tag_search(self):
        """Test case: Preferences topic tag search."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        CanonizerAdvancedSettingsPage(self.driver).open_preferences().search_preference_tags("test")
        result = self.driver.find_element(*AdvancedSettingsIdentifiers.PREFERENCE_TAGS_CONTAINER).is_displayed()
        assert result


    # Documentation: Create topic edit draft crash.
    def test_create_topic_edit_draft_crash(self):
        """Test case: Create topic edit draft crash."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
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


    # Documentation: Asp old urls for topics.
    def test_asp_old_urls_for_topics(self):
        """Test case: Asp old urls for topics."""
            # Legacy URL coverage for backward compatibility.
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.driver.get(OLD_ASP_TOPIC_URL)
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/topic/105-Consciousness-Consensus-Projct/1-Agreement?is_tree_open=0" in result
