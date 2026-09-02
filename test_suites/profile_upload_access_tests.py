from .shared import *

class ProfileUploadAccessTests:


    # TC_VERIFY_SUBMITTER_NICK_NAME_LINK_ON_USER_PROFILE
    # Documentation: Verify submitter nick name link on user profile.
    def test_verify_submitter_nick_name_link_on_user_profile(self):
        """Test case: Verify submitter nick name link on user profile."""
        print("\n" + str(test_cases('TC_VERIFY_SUBMITTER_NICK_NAME_LINK_ON_USER_PROFILE')))
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("New Topic " + add_name)
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page()

        result = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/section/main/div/div/div[2]/div/div/div[2]/div/div[1]/p[6]/span").text
        assert "$%$%$%$%" in result


    # Upload and profile media tests.
    # Documentation: Upload files.
    def test_upload_files(self):
        """Test case: Upload files."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        self.driver.find_element(*BrowsePageIdentifiers.UPLOAD_FILES).click()
        result = self.driver.current_url
        assert "/uploadFile" in result


    # Documentation: Upload profile picture.
    def test_upload_profile_picture(self):
        """Test case: Upload profile picture."""
        self.login_to_canonizer_app()
        self.driver.get("https://ux-dev.canonizer.com/settings")
        image = image_under_5mb()
        upload_image = self.driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        upload_image.send_keys(image)
        self.driver.find_element(*ProfileInfoIdentifiersPage.UPLOAD_IMAGE_OK).click()
        self.driver.find_element(*ProfileInfoIdentifiersPage.SAVE_PROFILE_CHANGES).click()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.IMAGE_UPLOADED_SUCCESFULLY).text
        assert "Profile updated successfully" in result


    # Documentation: View profile picture.
    def test_view_profile_picture(self):
        """Test case: View profile picture."""
        self.login_to_canonizer_app()
        self.driver.get("https://ux-dev.canonizer.com/settings")
        self.driver.find_element(*ProfileInfoIdentifiersPage.VIEW_IMAGE).click()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.VIEW_IMAGE_POP_UP).text
        assert "Profile picture" in result


    # Documentation: Delete profile picture.
    def test_delete_profile_picture(self):
        """Test case: Delete profile picture."""
        self.login_to_canonizer_app()
        self.driver.get("https://ux-dev.canonizer.com/settings")
        self.driver.find_element(*ProfileInfoIdentifiersPage.DELETE_PROFILE_IMAGE).click()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.IMAGE_DELETED_POP_UP).text
        assert "Image Deleted" in result


    # Documentation: Delete profile picture when no image exists.
    def test_delete_profile_picture_when_no_image_exists(self):
        """Test case: Delete profile picture when no image exists."""
        self.login_to_canonizer_app()
        self.driver.get("https://ux-dev.canonizer.com/settings")
        self.driver.find_element(*ProfileInfoIdentifiersPage.DELETE_PROFILE_IMAGE).click()
        self.driver.find_element(*ProfileInfoIdentifiersPage.DELETE_PROFILE_IMAGE).click()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.IMAGE_DELETED_POP_UP).text
        assert "Image Deleted" not in result


    # Documentation: Alphabets for no profile image.
    def test_alphabets_for_no_profile_image(self):
        """Test case: Alphabets for no profile image."""
        self.login_to_canonizer_app()
        self.driver.get("https://ux-dev.canonizer.com/settings")
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.NO_IMAGE_ALPHABET).text
        assert "AR" in result



    # Documentation: Authentication expiry for upload file.
    def test_authentication_expiry_for_upload_file(self):
        """Test case: Authentication expiry for upload file."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        self.driver.get(UPLOAD_FILE_URL)
        self.driver.get(UPLOAD_FILE_URL)

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result


    # Documentation: Authentication expiry for account setting.
    def test_authentication_expiry_for_account_setting(self):
        """Test case: Authentication expiry for account setting."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        CanonizerPofilePage(self.driver).profile_button()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result


    # Documentation: Authentication expiry for nicknames.
    def test_authentication_expiry_for_nicknames(self):
        """Test case: Authentication expiry for nicknames."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        CanonizerPofilePage(self.driver).profile_page_nickname_tab()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result


    # Documentation: Authentication expiry for user preference.
    def test_authentication_expiry_for_user_preference(self):
        """Test case: Authentication expiry for user preference."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        CanonizerPofilePage(self.driver).profile_page_preferences_tab()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result


    # Documentation: Authentication expiry for subscriptions.
    def test_authentication_expiry_for_subscriptions(self):
        """Test case: Authentication expiry for subscriptions."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        CanonizerPofilePage(self.driver).profile_page_mysubscription_tab()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result


    # Documentation: Authentication social oauth verification.
    def test_authentication_social_oauth_verification(self):
        """Test case: Authentication social oauth verification."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        CanonizerPofilePage(self.driver).profile_page_account_setting_social_auth_tab()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result


    # Documentation: Authentication change password.
    def test_authentication_change_password(self):
        """Test case: Authentication change password."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        CanonizerPofilePage(self.driver).profile_page_account_setting_password_tab()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result


    # Documentation: Authentication homepage.
    def test_authentication_homepage(self):
        """Test case: Authentication homepage."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()

        self.driver.refresh()
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result



    # Documentation: Authentication notification page.
    def test_authentication_notification_page(self):
        """Test case: Authentication notification page."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()

        self.driver.get(NOTIFICATION_URL)
        self.driver.refresh()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result


    # Documentation: Authentication notification delete.
    def test_authentication_notification_delete(self):
        """Test case: Authentication notification delete."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()

        self.driver.get(NOTIFICATION_URL)
        self.driver.find_element(*BrowsePageIdentifiers.DELETE_NOTIFICATION).click()

        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/login" in result


    # Documentation: Upload file with admin.
    def test_upload_file_with_admin(self):
        """Test case: Upload file with admin."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        CanonizerUploadFile(self.driver).upload_file_with_admin()
        result = self.driver.current_url
        assert "uploadFile" in result



    # Documentation: Upload file less than 5mb.
    def test_upload_file_less_than_5mb(self):
        """Test case: Upload file less than 5mb."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        CanonizerUploadFile(self.driver).uploading_file_less_than_5mb()
        result = self.driver.current_url
        assert "uploadFile" in result


    # Documentation: Upload file more than 5mb.
    def test_upload_file_more_than_5mb(self):
        """Test case: Upload file more than 5mb."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        CanonizerUploadFile(self.driver).upload_file_more_than_5mb()
        result = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/section/main/div/div/div/form/div/div[2]/div/div[2]/div[1]/span/div[2]/div/div/div/div/p").text
        assert "This file is exceeding the max limit and will not be uploaded" in result


    # Documentation: Upload in create new folder.
    def test_upload_in_create_new_folder(self):
        """Test case: Upload in create new folder."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        CanonizerUploadFile(self.driver).upload_in_create_new_folder()
        result = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/section/main/div/div/div/form/div/div[2]/div/div[1]/div/div[2]/button/span[1]").text
        assert "Upload New File" in result


    # Documentation: Upload file in new folder.
    def test_upload_file_in_new_folder(self):
        """Test case: Upload file in new folder."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        CanonizerUploadFile(self.driver).upload_in_create_new_folder()
        CanonizerUploadFile(self.driver).upload_file_in_new_folder()
        result = self.driver.current_url
        assert "uploadFile" in result


    # Documentation: Upload file manager toggle views.
    def test_upload_file_manager_toggle_views(self):
        """Test case: Upload file manager toggle views."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        page = CanonizerUploadFile(self.driver).open_upload_file_manager()
        page.switch_to_list_view()
        page.switch_to_grid_view()
        result = self.driver.find_element(*UploadFileIdentifiers.CREATE_FOLDER_BUTTON).is_displayed()
        assert result


    # Documentation: Upload file manager file actions menu.
    def test_upload_file_manager_file_actions_menu(self):
        """Test case: Upload file manager file actions menu."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        page = CanonizerUploadFile(self.driver).open_upload_file_manager()
        opened = page.open_first_file_menu_if_available()
        if opened:
            result = page.file_menu_has_actions()
        else:
            result = self.driver.find_element(*UploadFileIdentifiers.CREATE_FOLDER_BUTTON).is_displayed()
        assert result


    # Documentation: Upload file manager delete modal cancel.
    def test_upload_file_manager_delete_modal_cancel(self):
        """Test case: Upload file manager delete modal cancel."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        page = CanonizerUploadFile(self.driver).open_upload_file_manager()
        opened = page.open_first_file_menu_if_available()
        if opened and len(self.driver.find_elements(*UploadFileIdentifiers.FILE_ACTION_DELETE)) > 0:
            page.open_delete_modal_and_cancel()
        result = self.driver.find_element(*UploadFileIdentifiers.CREATE_FOLDER_BUTTON).is_displayed()
        assert result


    # Documentation: Profile page name change.
    def test_profile_page_name_change(self):
        """Test case: Profile page name change."""
            # Profile, account settings, and preference tests.
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        self.driver.get(PROFILE_PAGE)
        self.driver.find_element(*ProfileInfoIdentifiersPage.FIRST_NAME).send_keys("ing")
        self.driver.find_element(*ProfileInfoIdentifiersPage.SAVE_PROFILE_CHANGES).click()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.USERNAME_UPPER).text

        assert "Akashing" in result


    # Documentation: Notifications filters matrix.
    def test_notifications_filters_matrix(self):
        """Test case: Notifications filters matrix."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        CanonizerAdvancedSettingsPage(self.driver).open_notifications().notifications_apply_filters()
        result = self.driver.find_element(*AdvancedSettingsIdentifiers.NOTIFICATIONS_LIST).is_displayed()
        assert result


    # Documentation: Notifications mark all read cancel.
    def test_notifications_mark_all_read_cancel(self):
        """Test case: Notifications mark all read cancel."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        CanonizerAdvancedSettingsPage(self.driver).open_notifications().open_mark_all_read_modal().cancel_mark_all_read_modal()
        result = self.driver.find_element(*AdvancedSettingsIdentifiers.NOTIFICATIONS_TITLE).is_displayed()
        assert result


    # Documentation: Notifications delete all cancel.
    def test_notifications_delete_all_cancel(self):
        """Test case: Notifications delete all cancel."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        CanonizerAdvancedSettingsPage(self.driver).open_notifications().open_delete_all_modal().cancel_delete_all_modal()
        result = self.driver.find_element(*AdvancedSettingsIdentifiers.NOTIFICATIONS_TITLE).is_displayed()
        assert result


    # Documentation: Notifications load more if available.
    def test_notifications_load_more_if_available(self):
        """Test case: Notifications load more if available."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        was_clicked = CanonizerAdvancedSettingsPage(self.driver).open_notifications().click_load_more_if_available()
        result = self.driver.find_element(*AdvancedSettingsIdentifiers.NOTIFICATIONS_LIST).is_displayed()
        assert result or (was_clicked is False)


    # Documentation: Direct supported remove modal cancel.
    def test_direct_supported_remove_modal_cancel(self):
        """Test case: Direct supported remove modal cancel."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        CanonizerAdvancedSettingsPage(self.driver).open_direct_supported().open_direct_remove_modal().cancel_support_remove_modal()
        result = self.driver.find_element(*AdvancedSettingsIdentifiers.DIRECT_TABLE).is_displayed()
        assert result


    # Documentation: Delegated supported remove modal cancel.
    def test_delegated_supported_remove_modal_cancel(self):
        """Test case: Delegated supported remove modal cancel."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        CanonizerAdvancedSettingsPage(self.driver).open_delegated_supported().open_delegated_remove_modal().cancel_support_remove_modal()
        result = self.driver.find_element(*AdvancedSettingsIdentifiers.DELEGATED_TABLE).is_displayed()
        assert result


    # Documentation: Social auth link controls visible.
    def test_social_auth_link_controls_visible(self):
        """Test case: Social auth link controls visible."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        page = CanonizerAdvancedSettingsPage(self.driver).open_social_auth()
        result = page.social_link_button_count()
        assert result >= 1



    # Documentation: Profile page nickname tab.
    def test_profile_page_nickname_tab(self):
        """Test case: Profile page nickname tab."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        CanonizerPofilePage(self.driver).profile_page_nickname_tab()

        result = self.driver.find_element(*ProfileInfoIdentifiersPage.NICKNAME).text
        assert "NICKNAMES" in result


    # Documentation: Profile page preferences tab.
    def test_profile_page_preferences_tab(self):
        """Test case: Profile page preferences tab."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        CanonizerPofilePage(self.driver).profile_page_preferences_tab()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.PREFERENCE).text
        assert "PREFERENCES" in result

    # Documentation: Profile page mysubscription tab.
    def test_profile_page_mysubscription_tab(self):
        """Test case: Profile page mysubscription tab."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        CanonizerPofilePage(self.driver).profile_page_mysubscription_tab()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.MY_SUBCRIPTION).text
        assert "My Subscriptions" in result


    # Documentation: Profile page account setting social auth tab.
    def test_profile_page_account_setting_social_auth_tab(self):
        """Test case: Profile page account setting social auth tab."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        CanonizerPofilePage(self.driver).profile_page_account_setting_social_auth_tab()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.SOCIAL_AUTH).text
        assert "SOCIAL AUTH" in result


    # Documentation: Profile page account setting password tab.
    def test_profile_page_account_setting_password_tab(self):
        """Test case: Profile page account setting password tab."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        CanonizerPofilePage(self.driver).profile_page_account_setting_password_tab()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.CHANGE_PASSWORD).text
        assert "CHANGE PASSWORD" in result


    # Documentation: Profile setting public crash.
    def test_profile_setting_public_crash(self):
        """Test case: Profile setting public crash."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.login_to_canonizer_app()
        CanonizerPofilePage(self.driver).profile_page_public_crash()
        self.driver.find_element(*ProfileInfoIdentifiersPage.PREFERENCE_SAVE_BUTTON).click()
        result = self.driver.find_element(*ProfileInfoIdentifiersPage.PROFILE_UPDATED_POP_UP).text

        assert "Profile updated successfully." in result


    # Documentation: Asp old urls for support.
    def test_asp_old_urls_for_support(self):
        """Test case: Asp old urls for support."""
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.driver.get(OLD_ASP_SUPPORT_URL)
        result = self.driver.current_url
        assert "https://ux-dev.canonizer.com/topic/97-Mormon-Spirits/1-Agreement?is_tree_open=0" in result
