# Canonizer UI Automation Test Inventory

This repository currently holds the Canonizer browser automation suite in one runnable place: [main.py](main.py).

The suite is organized as a page-object model with:

- feature flows in `main.py`
- shared test data in `Config.py`
- scenario IDs in `CanonizerTestCases.py`
- locators in `Identifiers.py`
- page objects in the `Canonizer*Page.py` files

## Coverage Areas

### Authentication and onboarding

- `test_login_to_canonizer`
- `test_click_on_join_now`
- `test_register_page_mandatory_fields_are_marked_with_asterisk`
- `test_registration_with_valid_credential`
- `test_registration_first_name_with_spaces`
- `test_registration_with_blank_first_name`
- `test_registration_with_blank_email`
- `test_registration_with_blank_last_name`
- `test_registration_with_blank_password`
- `test_registration_with_invalid_password_length`
- `test_registration_with_invalid_email`
- `test_check_login_page_open_click_login_here_link`
- `test_verify_the_functionality_of_registration_with_entering_data_in_mandatory_fields`
- `test_verify_the_functionality_0f_registration_with_entering_data_in_mobile_number_field`
- `test_click_on_login_button`
- `test_login_with_registered_credentials`
- `test_verify_the_login_with_blank_email`
- `test_verify_the_login_with_blank_password`
- `test_login_with_invalid_email`
- `test_verify_one_time_request_code_with_valid_credentials`
- `test_login_page_mandatory_fields_are_marked_with_asterisk`
- `test_login_remember_me_is_selected_by_default`
- `test_login_register_now_link`
- `test_forgot_password_link`
- `test_login_social_provider_is_available` (Facebook, Google, LinkedIn, GitHub)
- `test_logout`
- `test_forgot_password_with_blank_email`
- `test_forgot_password_with_invalid_email`
- `test_registration_with_blank_confirm_password`
- `test_registration_with_mismatched_passwords`
- `test_registration_with_invalid_mobile_number`
- `test_registration_social_providers_are_available`

### Topic creation and topic lifecycle

- `test_click_create_new_topic_page_button`
- `test_click_create_topic_without_user_login`
- `test_create_topic_with_blank_topic_name`
- `test_create_topic_name_with_valid_data`
- `test_create_same_topic_name_with_valid_data`
- `test_create_same_topic_name_error_link`
- `test_create_topic_with_special_chars`
- `test_create_topic_without_entering_mandatory_fields`
- `test_load_topic_history_page`
- `test_verify_topic_name_on_topic_history_page`
- `test_verify_submitter_nick_name_link_on_user_profile`
- `test_verify_submit_topic_update_button`
- `test_verify_cancel_button_functionality_on_topic_update_page`
- `test_update_topic_name`
- `test_compare_camp_statement`
- `test_create_topic_edit_draft_crash`

### Camp creation and camp management

- `test_load_create_camp_page`
- `test_create_camp_with_valid_data`
- `test_create_camp_with_blank_camp_name`
- `test_create_camp_with_duplicate_camp_name`
- `test_create_camp_with_invalid_camp_about_url`
- `test_create_camp_without_entering_data_in_mandatory_fields`
- `test_load_camp_manage_edit_page`
- `test_add_statement_for_archived_camp`
- `test_submit_camp_update_with_invalid_url`
- `test_update_camp_with_duplicate_camp_name`
- `test_verify_cancel_button_functionality_on_camp_update_page`
- `test_verify_preview_button_functionality_on_camp_update_page`

### Camp statements

- `test_camp_statement_button`
- `test_load_camp_statement_page`
- `test_add_camp_statement_with_valid_data`
- `test_add_camp_statement_page_with_asterisk`
- `test_add_camp_statement_without_mandatory_field`
- `test_add_camp_statement_with_trailing_spaces`
- `test_add_camp_statement_with_blank_data`
- `test_camp_statement_template`
- `test_load_edit_camp_statement`
- `test_edit_camp_statement`
- `test_update_camp_statement_with_mandatory_field`
- `test_edit_camp_statement_with_trailing_spaces`
- `test_edit_camp_statement_with_blank_data`

### Forum and post flows

- `test_click_create_thread_button`
- `test_create_thread_with_valid_data`
- `test_create_thread_with_blank_title`
- `test_create_thread_with_special_chars`
- `test_create_thread_with_blank_mandatory_fields`
- `test_create_thread_with_duplicate_title`
- `test_create_thread_with_valid_data_with_enter_key`
- `test_create_thread_with_trailing_spaces`
- `test_load_edit_thread_page`
- `test_edit_thread`
- `test_create_post`

### News feed

- `test_load_add_news_page`
- `test_add_news_page_mandatory_fields_are_marked_with_asterisk`
- `test_create_news_with_valid_data`
- `test_create_news_with_blank_display_text`
- `test_create_news_with_blank_link`
- `test_create_new_with_blank_fields`
- `test_click_add_news_cancel_button`
- `test_create_news_with_invalid_link_format`
- `test_create_news_with_duplicate_data`
- `test_create_news_with_trailing_spaces`

### Browse, discovery, and search

- `test_eventline`
- `test_browse_start_topic`
- `test_browse_videos`
- `test_browse_help`
- `test_browse_notification`
- `test_browse_profile_setting`
- `test_browse_profile_setting_account_setting`
- `test_browse_profile_setting_supported_camps`
- `test_categories_page`
- `test_elastic_search_count`
- `test_videos_thumbnail`
- `test_tree_search_crash`
- `test_agree_search_crash`
- `test_support_camp_error_first_time`

### Uploads and profile media

- `test_upload_files`
- `test_upload_profile_picture`
- `test_view_profile_picture`
- `test_delete_profile_picture`
- `test_alphabets_for_no_profile_image`
- `test_upload_file_without_userlogin`
- `test_upload_file_with_admin`
- `test_upload_file_less_than_5mb`
- `test_upload_file_more_than_5mb`
- `test_upload_in_create_new_folder`
- `test_upload_file_in_new_folder`
- `test_statement_image_more_than_5mb`
- `test_statement_image_more_than_5mb_note`

### Footer and page navigation

- `test_footer_browse_button`
- `test_footer_create_topic_button`
- `test_footer_upload_file_button`
- `test_footer_sitemap_button`
- `test_footer_videos_button`
- `test_footer_help_button`
- `test_footer_white_paper_button`
- `test_footer_jobs_button`
- `test_footer_privacy_policy_button`
- `test_footer_term_and_services_button`

### Authentication expiry and protected-route checks

- `test_authentication_expiry_for_create_topic`
- `test_authentication_expiry_for_create_camp`
- `test_authentication_expiry_for_create_statement`
- `test_authentication_expiry_for_upload_file`
- `test_authentication_expiry_for_account_setting`
- `test_authentication_expiry_for_supported_camp`
- `test_authentication_expiry_for_nicknames`
- `test_authentication_expiry_for_user_preference`
- `test_authentication_expiry_for_direct_supported_camp`
- `test_authentication_expiry_for_delegate_supported_camp`
- `test_authentication_expiry_for_subscriptions`
- `test_authentication_social_oauth_verification`
- `test_authentication_change_password`
- `test_authentication_add_news`
- `test_authentication_homepage`
- `test_authentication_notification_page`
- `test_authentication_notification_delete`
- `test_authentication_header_browse_pge`
- `test_authentication_header_videos`
- `test_authentication_header_help`
- `test_authentication_footer_browse`
- `test_authentication_footer_create_topic`
- `test_authentication_footer_upload_file`
- `test_authentication_footer_videos`
- `test_authentication_footer_help`
- `test_authentication_footer_white_paper`
- `test_authentication_footer_policy`
- `test_authentication_footer_terms_and_services`
- `test_authentication_topic_history`

### Account settings and profile preferences

- `test_profile_page_name_change`
- `test_cafe_text_in_address_bar`
- `test_topic_name_in_recent_activities`
- `test_profile_page_nickname_tab`
- `test_profile_page_preferences_tab`
- `test_profile_page_direct_supported_camp_tab`
- `test_profile_page_delegate_supported_camp_tab`
- `test_profile_page_mysubscription_tab`
- `test_profile_page_account_setting_social_auth_tab`
- `test_profile_page_account_setting_password_tab`
- `test_update_first_name`
- `test_update_last_name`
- `test_update_date_of_birth`
- `test_update_gender`
- `test_update_phone_number`
- `test_update_address_1`
- `test_profile_setting_public_crash`

### Legacy URL coverage

- `test_asp_old_urls_for_topics`
- `test_asp_old_urls_for_camps`
- `test_asp_old_urls_for_support`

## Supporting Files

- [README.md](README.md) for setup and run commands
- [Config.py](Config.py) for environment data and credentials
- [CanonizerTestCases.py](CanonizerTestCases.py) for scenario IDs and descriptions
- [Identifiers.py](Identifiers.py) for locators

## Notes

- The suite is currently centered in `main.py` and discovered by pytest.
- Some flows are intentionally high risk for flakiness: uploads, notifications, and drag-and-drop support management.
- The first automation slice should stay focused on login, registration, browse/search, topic creation, and profile update.
