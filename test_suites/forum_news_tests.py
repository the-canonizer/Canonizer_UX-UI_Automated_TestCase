from .shared import *

class ForumNewsTests:

    
    # Documentation: Click create thread button.
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
    # Documentation: Create thread with valid data.
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
    # Documentation: Create thread with blank title.
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
    # Documentation: Create thread with special chars.
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
    # Documentation: Create thread with blank mandatory fields.
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
    # Documentation: Create thread with duplicate title.
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
    # Documentation: Create thread with valid data with enter key.
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
    # Documentation: Create thread with trailing spaces.
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

    # Documentation: Load edit thread page.
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


    # Documentation: Edit thread.
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

   
    # Documentation: Create post.
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


    # Documentation: Edit post.
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


    # Documentation: Delete post.
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
    # Documentation: Load my threads page.
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


    # Documentation: Load top 10 threads page.
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
    # Documentation: Load add news page.
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
    # Documentation: Add news page mandatory fields are marked with asterisk.
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
    # Documentation: Create news with valid data.
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
    # Documentation: Create news with blank display text.
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
    # Documentation: Create news with blank link.
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


    # TC_CLICK_ADD_NEWS_CANCEL_BUTTON
    # Documentation: Click add news cancel button.
    def test_click_add_news_cancel_button(self):
        """Test case: Click add news cancel button."""
        print("\n" + str(test_cases('TC_CLICK_ADD_NEWS_CANCEL_BUTTON')))
        self.login_to_canonizer_app()
        CanonizerAddNewsPage(self.driver).load_add_news_page(DEFAULT_TOPIC).click_add_news_cancel_button()
        result = self.driver.find_element(*AddNewsIdentifiers.TOPIC).text
        assert "Topic :" in result


    # TC_CREATE_NEWS_WITH_INVALID_LINK_FORMAT
    # Documentation: Create news with invalid link format.
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
    # Documentation: Create news using enter key.
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
    # Documentation: Create news with duplicate data.
    def test_create_news_with_duplicate_data(self):
        """Test case: Create news with duplicate data."""
        print("\n" + str(test_cases('TC_CREATE_NEWS_WITH_DUPLICATE_DATA')))
        self.login_to_canonizer_app()
        CanonizerAddNewsPage(self.driver).load_add_news_page(DEFAULT_TOPIC).create_news_with_duplicate_data("Test automated news", "https://www.google.com/")
        result = self.driver.find_element(*CampStatementIdentifiers.ADD_STATEMENT_BUTTON).text
        assert "Manage/Edit Camp Statement" not in result


    # TC_CREATE_NEWS_WITH_TRAILING_SPACES
    # Documentation: Create news with trailing spaces.
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
    # Documentation: Load edit news page.
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


    # Documentation: Click edit news cancel button.
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


    # Documentation: Update news with blank display text.
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


    # Documentation: Update news with blank link.
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


    # Documentation: Edit news with valid data.
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


    # Documentation: Edit news with invalid link.
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


    # Documentation: Edit news with trailing spaces.
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


    # Documentation: Authentication add news.
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
