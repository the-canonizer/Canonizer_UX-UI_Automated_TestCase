from .shared import *

class CampTests:


    # Documentation: Topic comparison create camp button.
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

    # TC_LOAD_CREATE_CAMP_PAGE
    # Camp creation and camp management tests.
    # Documentation: Load create camp page.
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
    # Documentation: Create camp with valid data.
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
    # Documentation: Create camp with blank camp name.
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
    # Documentation: Create camp with duplicate camp name.
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
    # Documentation: Create camp with invalid camp about url.
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
    # Documentation: Create camp without entering data in mandatory fields.
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


    # Documentation: Create camp mandatory fields are marked with asterisk.
    def test_create_camp_mandatory_fields_are_marked_with_asterisk(self):
        """Test case: Create camp mandatory fields are marked with asterisk."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        page = CanonizerCreateCampPage(self.driver).load_create_camp_page()
        assert page.new_camp_mandatory_fields_are_marked_with_asterisk()


    # Documentation: Cancel create camp.
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


    # Documentation: Create camp with only mandatory fields.
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


    # Documentation: Update camp with valid data.
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


    # Documentation: Verify submit camp update button.
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


    # Documentation: Camp preview fields.
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


    # Documentation: Camp preview cancel.
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


    # Documentation: Camp preview submitter nickname.
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


    # Documentation: Compare camp versions.
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


    # Documentation: Camp comparison displays both versions.
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


    # Documentation: Load camp manage edit page.
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



    # TC_UPDATE_CAMP_WITH_INVALID_URL
    # Documentation: Submit camp update with invalid url.
    def test_submit_camp_update_with_invalid_url(self):
        """Test case: Submit camp update with invalid url."""
        self.login_to_canonizer_app()
        result = CanonizerEditCampPage(self.driver).load_topic_detail_page(DEFAULT_TOPIC)\
            .submit_camp_update_with_invalid_url(INVALID_CAMP_ABOUT_URL)
        assert "/manage/camp/" in result.get_url()


    # TC_UPDATE_CAMP_WITH_DUPLICATE_CAMP_NAME
    # Documentation: Update camp with duplicate camp name.
    def test_update_camp_with_duplicate_camp_name(self):
        """Test case: Update camp with duplicate camp name."""
        self.login_to_canonizer_app()
        result = CanonizerEditCampPage(self.driver).load_topic_detail_page(DEFAULT_TOPIC)\
            .update_camp_with_duplicate_camp_name(DUPLICATE_CAMP_NAME)
        assert "/manage/camp/" in result.get_url()



    # TC_VERIFY_CANCEL_BUTTON_FUNCTIONALITY_ON_CAMP_UPDATE_PAGE
    # Documentation: Verify cancel button functionality on camp update page.
    def test_verify_cancel_button_functionality_on_camp_update_page(self):
        """Test case: Verify cancel button functionality on camp update page."""
        self.login_to_canonizer_app()
        result = CanonizerEditCampPage(self.driver).load_topic_detail_page(DEFAULT_TOPIC)\
            .verify_cancel_button_functionality_on_camp_update_page()
        assert "/camp/history/" in result.get_url()


    # TC_VERIFY_PREVIEW_BUTTON_FUNCTIONALITY_ON_CAMP_UPDATE_PAGE
    # Documentation: Verify preview button functionality on camp update page.
    def test_verify_preview_button_functionality_on_camp_update_page(self):
        """Test case: Verify preview button functionality on camp update page."""
        self.login_to_canonizer_app()
        result = CanonizerEditCampPage(self.driver).load_topic_detail_page(DEFAULT_TOPIC) \
            .verify_preview_button_functionality_on_camp_update_page()
        assert "/manage/camp/" in result.get_url()


    # Documentation: Create news available for child camps.
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


    # Documentation: Advanced search camp tab navigation.
    def test_advanced_search_camp_tab_navigation(self):
        """Test case: Advanced search camp tab navigation."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerSearchPage(self.driver).open_all_results("tree").click_sidebar_tab("/search/camp")
        result = self.driver.find_element(*SearchPageIdentifiers.CAMP_HEADING).text
        assert "Camp" in result


    # Documentation: Advanced search camp bydate filter route.
    def test_advanced_search_camp_bydate_filter_route(self):
        """Test case: Advanced search camp bydate filter route."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerSearchPage(self.driver).open_camp_results("tree", "asof=bydate")
        result = self.driver.current_url
        assert "asof=bydate" in result and "/search/camp" in result


    # Documentation: Browse profile setting supported camps.
    def test_browse_profile_setting_supported_camps(self):
        """Test case: Browse profile setting supported camps."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*BrowsePageIdentifiers.PROFILE_LINK).click()
        self.driver.find_element(*BrowsePageIdentifiers.SUPPORTED_CAMP).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/settings?tab=direct_supported_camps" in result


    # Documentation: Authentication expiry for create camp.
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



    # Documentation: Authentication expiry for supported camp.
    def test_authentication_expiry_for_supported_camp(self):
        """Test case: Authentication expiry for supported camp."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        CanonizerPofilePage(self.driver).profile_page_direct_supported_camp_tab()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result


    # Documentation: Authentication expiry for direct supported camp.
    def test_authentication_expiry_for_direct_supported_camp(self):
        """Test case: Authentication expiry for direct supported camp."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        CanonizerPofilePage(self.driver).profile_page_direct_supported_camp_tab()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result


    # Documentation: Authentication expiry for delegate supported camp.
    def test_authentication_expiry_for_delegate_supported_camp(self):
        """Test case: Authentication expiry for delegate supported camp."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerPofilePage(self.driver).profile_page_delegate_supported_camp_tab()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result


    # Documentation: Support camp error first time.
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


    # Documentation: Profile page direct supported camp tab.
    def test_profile_page_direct_supported_camp_tab(self):
        """Test case: Profile page direct supported camp tab."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerPofilePage(self.driver).profile_page_direct_supported_camp_tab()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.DIRECT_SUPPORTED).text
        assert "DIRECT SUPPORTED CAMPS" in result


    # Documentation: Profile page delegate supported camp tab.
    def test_profile_page_delegate_supported_camp_tab(self):
        """Test case: Profile page delegate supported camp tab."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerPofilePage(self.driver).profile_page_delegate_supported_camp_tab()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.DELEGATE_SUPPORT).text
        assert "DELEGATED SUPPORTED CAMPS" in result


    # Documentation: Asp old urls for camps.
    def test_asp_old_urls_for_camps(self):
        """Test case: Asp old urls for camps."""
        self.driver.implicitly_wait(30)
        self.driver.get(OLD_ASP_CAMP_URL)
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/topic/6669-Test-dlkskndlksndl/1-Agreement?is_tree_open=0" in result
