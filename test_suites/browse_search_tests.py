from .shared import *

class BrowseSearchTests:


    # Browse, discovery, and event timeline tests.
    # Documentation: Eventline.
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


    # Documentation: Browse namespace filter.
    def test_browse_namespace_filter(self):
        """Test case: Browse namespace filter."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerBrowsePage(self.driver).select_dropdown_value()
        result = self.driver.find_element(*BrowsePageIdentifiers.NAMESPACE).text
        assert result != ""


    # Documentation: Browse algorithm filter.
    def test_browse_algorithm_filter(self):
        """Test case: Browse algorithm filter."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerBrowsePage(self.driver).click_browse_page_button().algo_dropdown_filter()
        result = self.driver.current_url
        assert "browse" in result


    # Documentation: Advanced search nickname tab navigation.
    def test_advanced_search_nickname_tab_navigation(self):
        """Test case: Advanced search nickname tab navigation."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerSearchPage(self.driver).open_all_results("tree").click_sidebar_tab("/search/nickname")
        result = self.driver.find_element(*SearchPageIdentifiers.NICKNAME_HEADING).text
        assert "Nickname" in result


    # Documentation: Browse videos.
    def test_browse_videos(self):
        """Test case: Browse videos."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*BrowsePageIdentifiers.VIDEOS).click()
        result = self.driver.current_url
        assert "/videos" in result


    # Documentation: Browse help.
    def test_browse_help(self):
        """Test case: Browse help."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*BrowsePageIdentifiers.HELP).click()
        result = self.driver.current_url
        assert "/topic/132-Help/1-Agreement?is_tree_open=1" in result


    # Documentation: Browse notification.
    def test_browse_notification(self):
        """Test case: Browse notification."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*BrowsePageIdentifiers.NOTIFICATION_BELL).click()
        result = self.driver.find_element(*BrowsePageIdentifiers.NOTIFICATIONS).text
        assert "notifications" in result


    # Documentation: Browse profile setting.
    def test_browse_profile_setting(self):
        """Test case: Browse profile setting."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*BrowsePageIdentifiers.PROFILE_LINK).click()
        result = self.driver.find_element(*BrowsePageIdentifiers.PROFILE_SETTING).text
        assert "Account Settings" in result


    # Documentation: Browse profile setting account setting.
    def test_browse_profile_setting_account_setting(self):
        """Test case: Browse profile setting account setting."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*BrowsePageIdentifiers.PROFILE_LINK).click()
        self.driver.find_element(*BrowsePageIdentifiers.PROFILE_LINK_INFO).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/settings?tab=profile_info" in result


    # Footer and public navigation tests.
    # Documentation: Footer browse button.
    def test_footer_browse_button(self):
        """Test case: Footer browse button."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*HomePageIdentifiers.FOOTER_BROWSE).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/browse" in result


    # Documentation: Footer upload file button.
    def test_footer_upload_file_button(self):
        """Test case: Footer upload file button."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*HomePageIdentifiers.FOOTER_UPLOAD).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/uploadFile" in result


    # Documentation: Footer sitemap button.
    def test_footer_sitemap_button(self):
        """Test case: Footer sitemap button."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*HomePageIdentifiers.FOOTER_SITE_MAP).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/sitemap" in result


    # Documentation: Footer videos button.
    def test_footer_videos_button(self):
        """Test case: Footer videos button."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*HomePageIdentifiers.FOOTER_VIDEOS).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/videos" in result


    # Documentation: Footer help button.
    def test_footer_help_button(self):
        """Test case: Footer help button."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*HomePageIdentifiers.FOOTER_HELP).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/topic/132-Help/1-Agreement?is_tree_open=1" in result


    # Documentation: Footer white paper button.
    def test_footer_white_paper_button(self):
        """Test case: Footer white paper button."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*HomePageIdentifiers.FOOTER_WHITE_PAPER).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/files/2012_amplifying_final.pdf" in result


    # Documentation: Footer jobs button.
    def test_footer_jobs_button(self):
        """Test case: Footer jobs button."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*HomePageIdentifiers.FOOTER_JOBS).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/topic/6-Canonizer-Jobs/1-Agreement?is_tree_open=1" in result


    # Documentation: Footer privacy policy button.
    def test_footer_privacy_policy_button(self):
        """Test case: Footer privacy policy button."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*HomePageIdentifiers.FOOTER_PRIVACY).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/privacy-policy" in result


    # Documentation: Footer term and services button.
    def test_footer_term_and_services_button(self):
        """Test case: Footer term and services button."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*HomePageIdentifiers.FOOTER_TERM_CONDITION).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/terms-and-services" in result

   
    # Documentation: Footer upload file button repeat navigation.
    def test_footer_upload_file_button_repeat_navigation(self):
        """Test case: Footer upload file button repeat navigation."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.find_element(*HomePageIdentifiers.FOOTER_UPLOAD).click()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/uploadFile" in result 



    # Documentation: Authentication header browse pge.
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


    # Documentation: Authentication header videos.
    def test_authentication_header_videos(self):
        """Test case: Authentication header videos."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.get("https://ux-dev.canonizer.com/videos")
        self.driver.refresh()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result


    # Documentation: Authentication header help.
    def test_authentication_header_help(self):
        """Test case: Authentication header help."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.get(HELP_URL)
        self.driver.refresh()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result


    # Documentation: Authentication footer browse.
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


    # Documentation: Authentication footer upload file.
    def test_authentication_footer_upload_file(self):
        """Test case: Authentication footer upload file."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.find_element(*HomePageIdentifiers.FOOTER_UPLOAD).click()
        self.driver.refresh()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result


    # Documentation: Authentication footer videos.
    def test_authentication_footer_videos(self):
        """Test case: Authentication footer videos."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.find_element(*HomePageIdentifiers.FOOTER_VIDEOS).click()
        self.driver.refresh()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/videos" in result


    # Documentation: Authentication footer help.
    def test_authentication_footer_help(self):
        """Test case: Authentication footer help."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.find_element(*HomePageIdentifiers.FOOTER_HELP).click()
        self.driver.refresh()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/topic/132-Help/1-Agreement?is_tree_open=1" in result


    # Documentation: Authentication footer white paper.
    def test_authentication_footer_white_paper(self):
        """Test case: Authentication footer white paper."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.find_element(*HomePageIdentifiers.FOOTER_WHITE_PAPER).click()
        self.driver.refresh()
        old_window = self.driver.current_window_handle

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/files/2012_amplifying_final.pdf" in result


    # Documentation: Authentication footer policy.
    def test_authentication_footer_policy(self):
        """Test case: Authentication footer policy."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.find_element(*HomePageIdentifiers.FOOTER_PRIVACY).click()
        self.driver.refresh()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/privacy-policy" in result


    # Documentation: Authentication footer terms and services.
    def test_authentication_footer_terms_and_services(self):
        """Test case: Authentication footer terms and services."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()

        self.driver.find_element(*HomePageIdentifiers.FOOTER_TERM_CONDITION).click()
        self.driver.refresh()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/terms-and-services" in result


    # Documentation: Upload file manager search and reset.
    def test_upload_file_manager_search_and_reset(self):
        """Test case: Upload file manager search and reset."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        page = CanonizerUploadFile(self.driver).open_upload_file_manager()
        page.search_uploaded_files("test")
        page.reset_upload_filters()
        result = self.driver.find_element(*UploadFileIdentifiers.SEARCH_INPUT).get_attribute("value")
        assert result == ""


    # Documentation: Categories page.
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


    # Documentation: Elastic search count.
    def test_elastic_search_count(self):
        """Test case: Elastic search count."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.get(TOPIC_SEARCH_URL)
        result = self.driver.find_element(*BrowsePageIdentifiers.TOPIC_SEARCH_COUNT).text
        assert "1121" in result


    # Documentation: Videos thumbnail.
    def test_videos_thumbnail(self):
        """Test case: Videos thumbnail."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.get("https://ux-dev.canonizer.com/videos")
        result = self.driver.find_element(*BrowsePageIdentifiers.VIDEOS_THUMBNAIL).get_attribute("src")
        thumnail_link = "https://ux-dev.canonizer.com/_next/image?url=https%3A%2F%2Fux-dev.canonizer.com%2Ffiles%2Fvideos%2Fconsciousness%2Fintroduction_thumb.png&w=3840&q=75"
        assert thumnail_link in result


    # Documentation: Tree search crash.
    def test_tree_search_crash(self):
        """Test case: Tree search crash."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.get(TREE_SEARCH_URL)
        result = self.driver.find_element(*BrowsePageIdentifiers.ELASTIC_SEARCH_URL).text
        assert "Search Results for " in result


    # Documentation: Agree search crash.
    def test_agree_search_crash(self):
        """Test case: Agree search crash."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.get(AGREE_SEARCH_URL)
        result = self.driver.find_element(*BrowsePageIdentifiers.ELASTIC_SEARCH_URL).text
        assert "Search Results for " in result


    # Documentation: Direct supported search.
    def test_direct_supported_search(self):
        """Test case: Direct supported search."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerAdvancedSettingsPage(self.driver).open_direct_supported().search_direct_supported("test")
        result = self.driver.find_element(*AdvancedSettingsIdentifiers.DIRECT_TABLE).is_displayed()
        assert result


    # Documentation: Delegated supported search.
    def test_delegated_supported_search(self):
        """Test case: Delegated supported search."""
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerAdvancedSettingsPage(self.driver).open_delegated_supported().search_delegated_supported("test")
        result = self.driver.find_element(*AdvancedSettingsIdentifiers.DELEGATED_TABLE).is_displayed()
        assert result
