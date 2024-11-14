def test_cases(index):
    return testCases[index]


Critical = "Critical"
major = "Major"
moderate = "Moderate"
low = "Low"





testCases = {

    'TC_CLICK_ON_REGISTER_BUTTON': [Critical, 'In Home page,when user click "Register" button, user should see '
                                              'register page'],
    'TC_REGISTER_WITH_BLANK_FIRST_NAME': [moderate, 'In User Registration Page, When user doesn\'t put First Name, '
                                                    'user must see Error Message'],
    'TC_REGISTER_WITH_BLANK_LAST_NAME': [moderate, 'In User Registration Page, When user doesn\'t put Last Name, '
                                                   'user must see Error Message'],
    'TC_REGISTRATION_WITH_BLANK_EMAIL': [moderate, 'In User Registration Page, When user doesn\'t put Email, '
                                                   'user must see Error Message'],
    'TC_VERIFY_THE_FUNCTIONALITY_OF_REGISTRATION_WITH_MOBILE_NUMBER_FIELDS': [Critical, 'when user click on register '
                                                                                        'now button with invalid '
                                                                                        'mobile number , user should '
                                                                                        'see proper error message'],
    'TC_REGISTRATION_WITH_BLANK_PASSWORD': [moderate, 'In User Registration Page, When user puts blank password, '
                                                      'user must see Error Message'],
    'TC_REGISTRATION_WITH_INVALID_PASSWORD_LENGTH': [moderate, 'In User Registration Page, when user puts invalid '
                                                               'password,user must see Error Message'],
    'TC_REGISTRATION_WITH_DIFFERENT_CONFIRM_PASSWORD': [moderate,
                                                        'In User Registration Page, when user puts different password '
                                                        'for confirmation,user must see Error Message'],
    'TC_REGISTER_WITH_BLANK_SPACES_FIRST_NAME': [Critical, 'In User Registration Page, when user puts blank spaces to '
                                                           'first name ,user must see Error Message'],

    'TC_REGISTRATION_WITH_INVALID_FIRST_NAME': [moderate, 'In User Registration Page, When user invalid put First '
                                                          'Name user must see Error Message'],
    'TC_REGISTRATION_WITH_INVALID_LAST_NAME': [moderate, 'In User Registration Page, When user put invalid Last Name, '
                                                         'user must see Error Message'],
    'TC_REGISTRATION_WITH_INVALID_EMAIL': [moderate, 'In User Registration Page, When user put invalid email, '
                                                     'user must see Error Message'],
    'TC_VERIFY_THE_FUNCTIONALITY_OF_REGISTRATION_WITH_MANDATORY_FIELDS': [moderate,
                                                                          'when user click on register now,user fill all mandatary fields'],
    'TC_CHECK_LOGIN_PAGE_OPEN_CLICK_ON_LOGIN_HERE_LINK': [Critical, 'when user click on main page register but , '
                                                                    'user should see login link ,when user click on '
                                                                    'login link ,user should redirect to canonizer '
                                                                    'login page'],
    'TC_VERIFY_THE_FUNCTIONALITY_OF_REGISTERATION_WITH_MANDATORY_FIELDS': [Critical, 'when user fill all mandatary '
                                                                                     'fields on register page,'
                                                                                     'user able to create a accounton '
                                                                                     'canonizer'],

    'TC_VERIFYING_ACCOUNT_PROFILE': [Critical, 'When user should click on login dropdown button,user should see '
                                               'account setting page option'],
    'TC_CLICK_ON_LOGIN_BUTTON': [Critical, 'When user should click on login button with valid email and password,'
                                           'user should see main page'],
    'TC_VERIFY_LOGIN_PAGE': [Critical, 'When user should click on close on on login page, user should go to canonize '
                                       'main page'],
    'TC_CLICK_CLOSE_ICON_ON_LOGIN_PAGE': [Critical, 'When user click on cross icon, should see log in link'],
    'TC_LOGIN_WITH_REGISTERED_CREDENTIALS': [Critical, 'When user should try to login with registered credentials, '
                                                       'user should see main page'],
    'TC_VERIFY_THE_LOGIN_WITH_BLANK_EMAIL': [Critical, 'when user should try to login with blank email, '
                                                       'user should see proper error message'],
    'TC_VERIFY_THE_LOGIN_WITH_BLANK_PASSWORD': [Critical, 'when user should try to login with blank password, '
                                                          'user should see proper error message'],
    'TC_LOGIN_WITH_INVALID_EMAIL': [Critical, 'When user should try to login with invalid email, user should see '
                                              'proper error message'],
    'TC_VERIFYING_REMEMBER_CHECK_BOX': [Critical, 'When user should click on checkbox on login page, user should see '
                                                  'marked with blue mark'],
    'TC_VERIFYING_EMPTY_SPACE_FOR_EMAIL_FILED': [Critical, 'When user should click on login button with empty fields, '
                                                           'user should see proper error message'],
    'TC_VERIFY_FORGET_PASSWORD': [Critical, 'When user should verify title of "forget password, user should get '
                                            'proper title'],
    'TC_CLICK_ON_REGISTER_NOW_LINK': [Critical, 'When user should click register now link button on login page ,'
                                                'user should redirect canonize register page'],
    'TC_CLICK_REQUEST_ONE_TIME_CODE_BUTTON': [Critical, 'When user should click one time verification code without '
                                                        'entering email, user should see proper error message'],
    'TC_CLICK_REQUEST_ONE_TIME_CODE_BUTTON_WITH_INVALID-EMAIL': [Critical, 'When user should click one time '
                                                                           'verification code with invalid email,user '
                                                                           'should see proper error message'],
    'TC_VERIFY_ONE_TIME_REQUEST_CODE_WITH_VALID_CREDENTIALS': [Critical, 'when user click on one time request code '
                                                                         'with valid credentials, user should redirect'
                                                                         ' to one time verification page'],
    'Tc_verifying_facebook_link': [Critical, 'when user click on facebook link on login page ,user should see it '
                                             'redirect to facebook page'],
    'TC_VERIFYING_TWITTER_LINK': [Critical, 'when user click on twitter link on login page , user should see it '
                                            'redirect to twitter page'],
    'TC_VERIFYING_GOOGLE_LINK': [Critical, 'when user click on google link on login page, user should see it redirect '
                                           'to google chrome site'],
    'TC_VERIFYING_LINKEDIN_LINK': [Critical, 'when user click on linkedin link on login page, user should see it '
                                             'redirect to linkedin page'],
    'TC_VERIFYING_GITHUB_LINK': [Critical, 'when user should click on github link, user should see it redirect to '
                                           'github page'],
    'TC_VERIFYING_LOGIN_PLACEHOLDERS': [Critical, 'when  user used verify place holder on login page, suer should see '
                                                  'proper verfing place holders'],
    'TC_VERIFYING_ACCOUNT_PROFILE_PAGE': [Critical, 'When user should click on login drop down button ,user should '
                                                    'redirect to account setting page'],

    'TC_VERIFICATION_CHANGE_PASSWORD': [Critical, 'when user click on account setting page, user should see change '
                                                  'password button'],
    'TC-VERIFYING_SOCIAL_OAUTH_VERIFICATION': [Critical, 'when user click on account setting page, user should see '
                                                         'social oauth verification'],
    'TC_VERIFYING_NICK_NAME': [Critical, 'when user click on account setting page, user should see nick name button'],
    'TC_VERIFYING_SUPPORTED_CHANGES': [Critical, 'when user should click on account setting page , user should see '
                                                 'support camp changes'],
    'TC_VERIFYING_VALIDATION_FOR_PROFILE_INFO_PHONE_NUMBER': [Critical, 'when user try to give lessthan 10 digits '
                                                                        'profile info  phone number field,'
                                                                        'user should  see proper error message'],
    'TC_VERIFYING_VERIFY_BUTTON_WITH_BLANK_FIELDS': [Critical, 'when user click on verify button without entering any '
                                                               'data in mandatory fields, user should see proper '
                                                               'error message'],
    'TC_VERIFYING_CLICK_ON_MOBILE_CARRIER_DROP_DOWN': [Critical, 'when user click on mobile carrier , user should see '
                                                                 'droo down option'],
    'TC_VERIFYING_ALL_THE_FIELDS_ARE_PERSONAL_INFORMATION': [Critical, 'when user wants to verify the personal '
                                                                       'information fields  present are not, '
                                                                       'user click on profile info,then user can see '
                                                                       'personal information fields'],
    'TC_VERIFYING_FIRST_NAME_FIELD_WITHOUT_ENTERING_DATA': [Critical, 'when user click submit button without entering '
                                                                      'first name fields,user should see proper error'
                                                                      ' message'],
    'TC_UPDATE_THE_FIRST_NAME_AND_CHECK_IF_IT_IS_UPDATING_SAME_FOR_USERNAME': [Critical, 'when user updated first '
                                                                                         'name and user should see '
                                                                                         'it reflect to user name '
                                                                                         'also'],
    'TC_VERIFY_THE_FUNCTIONALITY_OF_RADIO_BUTTON_IN_SELECTING_THE_GENDER': [Critical, 'when user checks radio button '
                                                                                      'gender must be selected'],
    'TC_VERIFY_THE_FUNCTIONALITY_OF_SELECTING_THE_DOB': [Critical, 'DOB must be selected'],
    'TC_VERIFY_WHEN_USER_UPDATE_THE_PERSONAL_INFORMATION_AND_LOGS_OUT_AND_LOGIN_AGAIN': [Critical,
                                                                                         'when user Update all the '
                                                                                         'Personal Information layout '
                                                                                         'field and Click on Update '
                                                                                         'button and user Logout '
                                                                                         'Again login and navigate to '
                                                                                         'account setting '],
    'TC_VERIFY_THE_SPACES_ARE_TRIMMED_IN_THE_FIRSTNAME_LASTNAME_MIDDLENAME_fields': [Critical, 'when user try to the '
                                                                                               'spaces are trimmed '
                                                                                               'in the first name, '
                                                                                               'lastname,middlename '
                                                                                               'fields,user should '
                                                                                               'see the spaces '
                                                                                               'should be trimmed '
                                                                                               'while saving the '
                                                                                               'entered  data'],
    'TC VERIFY_WHEN_USER_CLICK_ON_CHANGE_PASSWORD': [Critical, 'when user click on change password , user can see '
                                                               'current and new and confirm password fields'],
    'TC VERIFYING_CURRENT_PASSWORD_NEW_PASSWORD_CONFIRM_PASSWORD': [Critical, 'when user click on change password '
                                                                              'button,user can verify all fields are '
                                                                              'present'],
    'TC VERIFY_KEEPING_ALL_THE_FIELDS_EMPTY_AND_CLICK_ON_SAVE': [Critical, 'when user try to click on save button '
                                                                           'without entering any data  , user should '
                                                                           'see proper error message'],
    'TC VERIFY_ENTERING_THE_INVALID_CURRENT_PASSWORD': [Critical, 'when user click on save button entering '
                                                                  'current password with invalid data , user should '
                                                                  'see proper error message'],
    'TC VERIFY_THE_CURRENT_PASSWORD_FIELDS_EMPTY_AND_CLICK_ON_SAVE': [Critical, 'when user click on save with empty '
                                                                             'current password field, user should '
                                                                             'see proper error message'],
    'TC_VERIFY_THE_NEW_PASSWORD_FIELD_EMPTY_AND_CLICK_ON_SAVE': [Critical, 'when user click on save with empty new '
                                                                           'password field, user should see proper '
                                                                           'error message'],
    'TC_VERIFY_THE_CONFIRM_PASSWORD_FIELD_EMPTY_AND_CLICK': [Critical, 'when user click on save with empty confirm '
                                                                       'password field,user should see proper error '
                                                                       'message'],
    'TC_VERIFY_ENTERING_THE_INVALID_NEW_PASSWORD': [Critical, 'when user click on save button with invalid new '
                                                              'password data user should see proper error message'],
    'TC VERIFY_ENTERING_THE_INVALID_CONFIRM_PASSWORD': [Critical, 'when user click on save button with invalid confirm '
                                                                  'password data,user should see proper error message'],
    'TC VERIFY_WHEN_BOTH_NEW_PASSWORD_AND_CONFIRM_PASSWORD_DOES_NOT_MATCH': [Critical, 'when user click on save '
                                                                                       'button when both new and '
                                                                                       'confirm password invalid,'
                                                                                       'user should see proper error '
                                                                                       'message'],
    'TC VERIFY_WHEN_USER_CLICK_ON_NICK_NAME_TAB': [Critical, 'when user click on nick name button , user should all '
                                                             'related fields for nick name'],
    'TC_VERIFY_WITH_ADD_NICKNAME_BUTTON_IS_PRESENT': [Critical,
                                                      'when user click on nick name button , user should see nick '
                                                      'name , nick name id'],
    'Tc_VERIFY_THE_FUNCTIONALITY_OF_ADD_NICKNAME_BUTTON': [Critical, 'when user click on add nick name button,user '
                                                                     'should see pop-up to fil the details of nick'
                                                                     '(or) create new nick name'],
    'TC_VERIFY_THE_FUNCTIONALITY_OF_DIRECT_SUPPORT_CAMP': [Critical, 'when user click on support camps in account '
                                                                     'setting '
                                                                     'page, User should be navigated to supported camp '
                                                                     'page'],
    'TC_VERIFY_DIRECT_SUPPORTED_CAMPS': [Critical, 'when user click on supported camps tab , user should see direct '
                                                   'supported and delegated supported camps tab it will be clickable'],
    'TC_VERIFY_THE_SEARCH_BAR_IS_NEXT_TO_DELEGATED_SUPPORT_CAMP_TAB': [Critical, 'when user should click on supported '
                                                                                 'camps tab, user should see search '
                                                                                 'bar is present are not beside '
                                                                                 'delegated supported camp tab'],
    'TC_VERIFY_THE_FUNCTIONALITY_OF_DELEGATE_SUPPORT_CAMP': [Critical, 'when user click on delegate support camp, '
                                                                       'User delegated '
                                                                       'support camps list should be displayed  under '
                                                                       'Delegate '
                                                                       'Supported camp tab'],
    'TC_VERIFY_USER_NAVIGATE_SUPPORT_CAMP_PAGE': [Critical, 'when user click on supported camp tab , user should see '
                                                            'supported camp page'],
    'TC_VERIFY_REMOVE_SUPPORT_BUTTON': [Critical, 'when user click on delegated support camp , user should '
                                                  'see remove support button'],
    'TC_TOPIC_NAME_AND_CAMP_NAME_CLICKABLE': [Critical, 'when user click on direct support camp button , user '
                                                        'should see topic name and it clickable'],
    'TC_VERIFY_CURRENT_SUPPORTED_CAMP_LINK': [Critical, 'when user click on delegated support camp , user should '
                                                        'see supported camp tree on click link'],
    'TC_VERIFY_TOPIC_NAME_AND_AGREEMENT_CAMP_NAME_IN DIRECT_SUPPORT_CAMP': [Critical, 'when user click on topic link '
                                                                                      'must see topic detail page'],
    'TC_VERIFY_THE_SEARCH_FUNCTIONALITY_IN_SUPPORTED_CAMPS_PAGE': [Critical, 'when user should click on supported '
                                                                             'camps , user should see search bar, '
                                                                             'user can search topic name in search '
                                                                             'bar'],
    'TC_VERIFY_TOPIC_LINK_ON_DIRECT_SUPPORTED_TAB': [Critical, 'When user click on direct supported topic link '
                                                               'it must redirect to the details page'],
    'TC_VERIFY_SUPPORT_DELEGATED_TO_USER_LINK': [Critical, 'when user click on delegated support tab ,user should see '
                                                           'user profile of the delegated user on click the link'],
    'TC_VERIFY_NICK_NAME_LINK_ON_DELEGATED_TAB': [Critical, 'User should redirect to nick name details page on click '
                                                                             'link'],
    'TC_VERIFY_THE_FACEBOOK_LINK': [Critical, 'when user click on facebook link in home, user should see the page '
                                              'redirect to facebook login page'],

    'TC_VERIFY_THE_INSTA_LINK': [Critical, 'when user click on insta_link, user should see after click on link it '
                                           'redirect to insta login page'],
    'TC_VERIFY_THE_TWITTER_LINK': [Critical, 'when user click on twitter link, user should redirect to twitter login '
                                             'page'],
    'TC_VERIFY_THE_YOUTUBE_LINK': [Critical, 'when user click on youtube link, user should redirect to youtube main '
                                             'page'],
    'Tc_verify_the_linkedin_link': [Critical, 'when user should click on linkedin link, user should redirect to '
                                              'linkedin page'],
    'TC_CLICK_FORGOT_PASSWORD_LINK': [Critical, 'User should see forgot password link'],
    'TC_SUBMIT_BUTTON_WITH_VALID_EMAIL_AND_CHECK_OTP_SCREEN': [Critical, 'User must see OTP screen on submit button'],
    'TC_SUBMIT_BUTTON_WITH_INVALID_EMAIL': [Critical, 'User must see error message with invalid email'],
    'TC_SUBMIT_BUTTON_WITH_EMPTY_EMAIL': [Critical, 'User must see error message when email is left empty'],
    'TC_SUBMIT_EMPTY_OTP': [Critical, 'User must see error message when OTP is left empty'],
    'TC_SUBMIT_INVALID_LENGTH_OTP': [Critical, 'User must see error message when submit invalid length OTP'],
    'TC_SUBMIT_BUTTON_WITH_UNREGISTERED_EMAIL': [Critical,
                                                 'User must see error message for email which is unregistered'],
    'TC_CROSS_ICON_ON_FORGOT_MODAL': [Critical, ' User must be able to click cross icon and modal should close'],
    'TC_CROSS_ICON_ON_OTP_MODAL': [Critical, 'User must be able to click cross icon and modal should close'],
    'TC_ENTER_VALID_OTP': [Critical, ' User must enter valid OTP and must see change password page'],
    'TC_CLICK_CREATE_TOPIC_WITH_USER_LOGIN': [Critical, 'User must be able to click Create topic button on login'],
    'TC_CLICK_CREATE_TOPIC_WITHOUT_USER_LOGIN': [Critical, 'User must see login page when click create topic button '
                                                           'when not logged in'],
    'TC_CREATE_TOPIC_WITH_BLANK_TOPIC_NAME': [Critical, ' User must not be able to create topic with blank name'],
    'TC_CREATE_TOPIC_WITH_VALID_DATA': [Critical, 'User must be able to create a new topic with valid data'],
    'TC_CREATE_TOPIC_WITH_BLANK_SPACES_TOPIC_NAME': [Critical, ' User must see error message when enter blank spaces'],
    'TC_CREATE_NEW_TOPIC_WITH_ENTER_KEY': [Critical, 'User must be able to create new topi when press EnterKey'],
    'TC_CREATE_NEW_TOPIC_WITH_TRAILING_SPACES': [Critical, 'Trailing spaces must be removed '
                                                           'and new topic is created'],
    'TC_CREATE_TOPIC_WITH_DUPLICATE_NAME': [Critical, 'Duplicate topic name must not be created'],
    'TC_CREATE_NEW_TOPIC_WITH_SPECIAL_CHARS': [Critical, 'Topic must be created when special char is entered'],
    'TC_CREATE_NEW_WITHOUT_MANDATORY_FIELDS_DATA': [Critical, 'User must not be able to create a topic '
                                                              'when mandatory fields are blank'],
    'TC_CREATE_NEW_TOPIC_ENTERING_DATA_ONLY_IN_MANDATORY_FIELDS': [Critical, ' User must be able to create a new '
                                                                             'topic when enter data only in mandatory fields'],
    'TC_CLICK_ON_CANCEL_BUTTON': [Critical, 'User must not be able to create a topic on click '
                                            'cancel button instead redirect to home page'],
    'TC_TOPIC_PAGE_MANDATORY_FIELDS_ARE_MARKED_WITH_ASTERISK': [Critical, 'User must see mandatory fields marked '
                                                                'with asterisk'],
    'TC_CHECK_NO_THREAD_AVAILABILITY': [Critical, 'User must see no data found message'],
    'TC_CLICK_CAMP_FORUM_BUTTON': [Critical, 'User must be able to click on camp forum button'],
    'TC_CLICK_CREATE_THREAD_BUTTON': [Critical, 'User must be able to click on create thread button'],
    'TC_LOAD_ALL_THREADS_PAGE': [Critical, 'User must see all threads under all threads section'],
    'TC_LOAD_MY_THREADS_PAGE': [Critical, 'User must see only their threads when click my threads button'],
    'TC_LOAD_MY_PARTICIPATION_PAGE': [Critical, 'User must see participation page on click the button'],
    'TC_LOAD_TOP_10_THREADS_PAGE': [Critical, 'User must see top 10 threads on this page'],
    'TC_CREATE_THREAD_WITH_VALID_DATA': [Critical, 'User must be able to create a thread'],
    'TC_CREATE_THREAD_WITH_BLANK_TITLE': [Critical, 'User must not be able to create thread and see error message'],
    'TC_CREATE_THREAD_WITH_SPECIAL_CHARS': [Critical, 'User must be able to create thread when enter special chars'],
    'TC_CREATE_THREAD_WITH_BLANK_MANDATORY_FIELDS': [Critical, 'User must not be able to create thread '
                                                               'and see error message'],
    'TC_CREATE_THREAD_WITH_DUPLICATE_TITLE': [Critical, 'User must not be able to create thread'],
    'TC_CREATE_THREAD_WITH_VALID_DATA_WITH_ENTER_KEY': [Critical, 'User must be able to create thread with enter key'],
    'TC_CREATE_THREAD_WITH_TRAILING_SPACES': [Critical, 'User must be able to create a top with trailing spaces'],
    'TC_THREAD_PAGE_MANDATORY_FIELDS_ARE_MARKED_WITH_ASTERISK': [Critical, 'User must see asterisk symbol '
                                                                 'for mandatory fields'],
    'TC_LOAD_EDIT_THREAD_PAGE': [Critical, 'User must be able to see edit thread page on click edit icon'],
    'TC_CLICK_ON_BACK_BUTTON': [Critical, 'User must redirect to camp forum page on click back button'],
    'TC_UPDATE_THREAD': [Critical, 'User must be able to edit and update thread on submit button'],
    'TC_EDIT_THREAD_WITH_SPECIAL_CHARS': [Critical, 'Thread title should be updated if entered special chars'],
    'TC_CLICK_ON_EDIT_BACK_BUTTON': [Critical, 'On click back button user must redirect to camp forum page'],
    'TC_LOAD_THREAD_POSTS_PAGE': [Critical, 'User must be redirected tp thread post page on click thread link'],
    'TC_THREAD_POST_WITH_VALID_DATA': [Critical, 'User must be able to reply to a thread with all valid data'],
    'TC_THREAD_POST_WITH_EMPTY_REPLY': [Critical, 'User must see error message if reply field is left blank'],
    'TC_CLICK_ON_POST_BACK_BUTTON': [Critical, 'User must be navigated to camp forum page on click back button'],
    'TC_VERIFY_NICK_NAME_LINK_ON_POST_PAGE': [Critical, 'User must be navigated to the profile on  '
                                              'click the nick name link'],
    'TC_VERIFY_EDIT_REPLY_TO_THREAD': [Critical, 'User must be able to edit reply on click edit icon'],
    'TC_VERIFY_DELETE_REPLY_TO_THREAD': [Critical, 'User must be able to delete the reply on click yes'],
    'TC_LOAD_CREATE_CAMP_PAGE': [Critical, 'User must be navigated to create camp page on click the button'],
    'TC_NEW_CAMP_FIELDS_ARE_MARKED_WITH_ASTERISK': [Critical, 'All mandatory fields must be marked with asterisk sign'],
    'TC_CREATE_CAMP_WITH_VALID_DATA': [Critical, 'User must be able to create camp when enter all valid data'],
    'TC_LOAD_ADD_NEWS_FEED_PAGE': [Critical, 'When user click on Add News ,user should see Add News page'],
    'TC_ADD_NEWS_PAGE_MANDATORY_FIELDS_ARE_MARKED_WITH_ASTERISK': [Critical, 'On Add News Page, All mandatory fields '
                                                                             'are marked with * sign'],
    'TC_CREATE_NEWS_WITH_VALID_DATA': [Critical, 'On Add News page, When user put valid data , news should get added'],
    'TC_CREATE_NEWS_WITH_BLANK_DISPLAY_TEXT': [Critical, 'On Add News page, When user does not put Display Text , '
                                                         'user must see error message'],
    'TC_CREATE_NEWS_WITH_BLANK_LINK': [Critical, 'On Add News page, When user does not enter link, must see Error '
                                                 'Message'],
    'TC_NEW_FEED_WITH_BLANK_FIELDS': [Critical, 'On Add News page, When user does not enter  display text and  link, '
                                                'user must see Error Message'],
    'TC_CLICK_ADD_NEWS_CANCEL_BUTTON': [Critical, 'On Add News Page, When user click on cancel button user should see '
                                                  'agreement page'],
    'TC_CREATE_NEWS_WITH_INVALID_LINK_FORMAT': [Critical, 'On Add News page, if user enters invalid Link , user must '
                                                          'see Error Message'],
    'TC_CREATE_NEWS_WITH_ENTER_KEY': [Critical, ' When user add valid data, and press enter key, news should get added.'],
    'TC_CREATE_NEWS_WITH_DUPLICATE_DATA': [Critical, 'When user adds duplicate data , news should get added'],
    'TC_CREATE_NEWS_WITH_TRAILING_SPACES': [Critical, 'When user adds data with trailing spaces, news should get added'],
    'TC_CLICK_EDIT_NEWS_CANCEL_BUTTON': [Critical, 'On Edit News Page, When user click on cancel button user should '
                                                   'see agreement page'],
    'TC_CLICK_LOGOUT_PAGE_BUTTON': [Critical, 'User must log out the application on click logout button'],
    'TC_LOAD_ADD_NEW_CAMP_STATEMENT_PAGE': [Critical, 'User must be able to see add statement page on click the button'],
    'TC_ADD_NEW_CAMP_STATEMENT_PAGE': [Critical, 'User must be able to add statement to the camp on click Submit'],
    'TC_ADD_CAMP_STATEMENT_PAGE_MANDATORY_FIELDS_WITH_ASTERISK': [Critical, 'On Add Camp Statement page, all mandatory '
                                                                            'fields are marked with * Sign'],
    'TC_ADD_CAMP_STATEMENT_WITHOUT_MANDATORY_FIELDS': [Critical, 'When user add the Camp Statement without mandatory '
                                                                 'fields, User must see error message'],
    'TC_ADD_CAMP_STATEMENT_WITH_VALID_DATA': [Critical, 'When user entered valid data to Add Camp Statement Page, '
                                                        'Use must see History Page'],
    'TC_ADD_CAMP_STATEMENT_PAGE_DATA_WITH_TRAILING_SPACES': [Critical, 'When user entered data with trailing spaces, '
                                                                       'data should get added and'],
    'TC_ADD_CAMP_STATEMENT_BLANK_STATEMENT': [Critical, 'When user does not add statement, user must see Error Message'],

    'TC_CLICK_ON_STATEMENT_CANCEL_BUTTON': [Critical, 'User must see canonizer sorted tree page on click cancel button'],
    'TC_CLICK_ON_STATEMENT_PREVIEW_BUTTON': [Critical, 'User must see preview modal on click the button'],
    'TC_LOAD_EDIT_CAMP_STATEMENT_PAGE': [Critical, 'User must see camp history page on edit camp statement button'],
    'TC_SUBMIT_STATEMENT_UPDATE_WITH_ONLY_MANDATORY_FIELDS': [Critical, 'User must be able to edit and update the statement'],
    'TC_EDIT_CAMP_STATEMENT_WITH_TRAILING_SPACES': [Critical, 'On Update Camp Statement page, when user edit statement '
                                                              'with trailing space, statement should get update'],
    'TC_EDIT_CAMP_STATEMENT_WITH_BLANK_STATEMENT': [Critical, 'On Update Camp Statement page, when user leave statement '
                                                              'blank, user must see Error Message'],
    'TC_VERIFY_EDITABLE_FIELDS_ON_EDIT_CAMP_STATEMENT_PAGE': [Critical, 'In Camp Statment Update Page, fields should be editable.'],
    'TC_VERIFY_HISTORY_ON_EDIT_CAMP_STATEMENT': [Critical, 'When user click on Manage/Edit Camp Statement, user should '
                                                           'see object, live, in-review, old data'],
    'TC_COMPARE_TWO_STATEMENTS': [Critical, 'When user checks 2 check boxes of different statement history, '
                                  'compare button should be enabled'],

    'TC_CREATE_CAMP_WITH_BLANK_CAMP_NAME': [low,
                                            'On Create New Camp page, When user doesn\'t put Camp Name , user must '
                                            'see Error Message'],
    'TC_CREATE_CAMP_WITH_DUPLICATE_CAMP_NAME': [Critical, 'On Create New Camp Page, if user enters duplicate data, '
                                                          'should see error message'],
    'TC_CREATE_CAMP_WITHOUT_ENTERING_DATA_IN_MANDATORY_FIELDS': [Critical, 'On Create New Camp page, if user doesn\'t '
                                                                           'enter data and submit the camp, '
                                                                           'user must see error messages'],
    'TC_CREATE_CAMP_WITH_INVALID_CAMP_ABOUT_URL': [Critical, 'User must see error message if enter invalid camp URL'],
    'TC_CAMP_CANCEL_BUTTON': [Critical, 'On click cancel button, user must see sorted camp tree'],
    'TC_VERIFY_SUBMITTER_NICK_NAME_ON_CAMP_HISTORY_PAGE': [Critical, ' Submitter nick name must be a clickable '
                                                           'should redirect to user profile on click'],
    'TC_VERIFY_SUBMIT_CAMP_UPDATE_BUTTON': [Critical, 'On click submit camp update user must redirect to camp edit page'],
    'TC_VERIFY_EDIT_AND_UPDATE_CAMP_FUNCTIONALITY': [Critical, 'User must see submit update btton enabled when '
                                                     'edit and field and on click must update the same'],
    'TC_LOAD_TOPIC_HISTORY_PAGE': [Critical, 'When user clicks on manage/edit this topic, history page must load'],
    'TC_VERIFY_TOPIC_NAME_ON_TOPIC_HISTORY_PAGE': [Critical, 'Topic name must be same on detail page and history page'],
    'TC_VERIFY_SUBMITTER_NICK_NAME_LINK_ON_USER_PROFILE': [Critical, 'Submitter nick name must be same on user profile'],
    'TC_VERIFY_SUBMIT_TOPIC_UPDATE_BUTTON': [Critical, 'User must see topic update page on click button submit update'],
    'TC_UPDATE_TOPIC_WITH_DUPLICATE_NAME': [Critical, 'User must see error message when edit and update duplicate topic'],
    'TC_VERIFY_CANCEL_BUTTON_FUNCTIONALITY_ON_TOPIC_UPDATE_PAGE': [Critical, 'On click cancel button user should not be'
                                                                             ' able to update and save'],
    'TC_VERIFY_PREVIEW_BUTTON_FUNCTIONALITY_ON_TOPIC_UPDATE_PAGE': [Critical, 'On click preview button,'
                                                                              ' user must see the preview modal'],
    'TC_VERIFY_SUBMITTER_NICK_NAME_ON_PREVIEW_MODAL': [Critical, 'On click submitter nick name, user must redirect to'
                                                                 ' user profile with same nickname'],
    'TC_VERIFY_CANCEL_BUTTON_ON_PREVIEW_MODAL': [Critical, 'On click cancel button user must redirect to topic update'],
    'TC_UPDATE_TOPIC_NAME_AND_VERIFY_SUBMIT_UPDATE_BUTTON': [Critical, 'On submit topic update user must '
                                                                       'redirect to history page'],
    'TC_VERIFY_AGREEMENT_LINK_ON_TOPIC_COMPARISON_PAGE': [Critical, 'On click agreement link, user must redirect'
                                                                    ' to canonizer sorted tree'],
    'TC_VERIFY_CREATE_TOPIC_BUTTON_FUNCTIONALITY_ON_TOPIC_COMPARISON_PAGE': [Critical, 'User must redirect'
                                                                                       ' to create topic page'],
    'TC_VERIFY_CREATE_CAMP_BUTTON_FUNCTIONALITY_ON_TOPIC_COMPARISON_PAGE': [Critical, 'User must redirect'
                                                                                       ' to create camp page'],
    'TC_VERIFY_POST_EDIT_ICON': [Critical, 'User must be able to edit post on click edit icon'],
    'TC_VERIFY_POST_DELETE_FUNCTIONALITY': [Critical, 'User must be able to delete post on click delete icon'],
    'TC_UPDATE_NEWS_WITH_BLANK_DISPLAY_TEXT': [Critical, 'On Edit News page, When user does not put Display Text , '
                                                         'user must see Error Message'],
    'TC_UPDATE_NEWS_WITH_BLANK_LINK': [Critical, 'On Edit News page, When user does not put Link , user must see '
                                                 'Error Message'],
    'TC_LOAD_EDIT_NEWS_PAGE': [],
    'TC_CLICK_LOG_OUT_PAGE_BUTTON':[],
    'TC_LOAD_CAMP_STATEMENT_PAGE':[],
    'TC_ADD_CAMP_STATEMENT_PAGE_WITH_ASTERISK':[],
    'TC_ADD_CAMP_STATEMENT_WITHOUT_MANDATORY_FIELD':[],
    'TC_ADD_CAMP_STATEMENT_WITH_TRAILING_SPACES':[],
    'TC_ADD_CAMP_STATEMENT_WITH_BLANK_DATA':[],
    'TC_LOAD_EDIT_CAMP_STATEMENT':[],
    'TC_UPDATE_CAMP_STATEMENT_WITH_MANDATORY_FIELD':[],
    'TC_EDIT_CAMP_STATEMENT_WITH_BLANK_DATA':[],
    'TC_COMPARE_CAMP_STATEMENT':[],
    'TC_ADD_CAMP_STATEMENT':[],
    'TC_EDIT_CAMP_STATEMENT':[],
    'TC_LOAD_CAMP_MANAGE_EDIT_PAGE':[],
    'TC_UPDATE_CAMP_WITH_DUPLICATE_CAMP_NAME':[],
    'TC_VERIFY_CANCEL_BUTTON_FUNCTIONALITY_ON_CAMP_UPDATE_PAGE':[],
    'TC_VERIFY_PREVIEW_BUTTON_FUNCTIONALITY_ON_CAMP_UPDATE_PAGE':[],
    'TC_VERIFY_CAMP_NAME_ON_PREVIEW_MODAL':[],
    'TC_SUBMITTER_NICK_NAME_ON_PREVIEW_MODAL':[],
    'TC_VERIFY_COMPARE_CAMPS_BUTTON_FUNCTIONALITY':[],
    'TC_VERIFY_CAMPS_NAME_ON_CAMP_HISTORY_COMPARISON_PAGE':[],
    'TC_SELECT_DROPDOWN_VALUE':[],
    'TC_SELECT_ALL_NAMESPACES':[],
    'TC_UPLOAD_FILE_WITHOUT_ADMIN_LOGIN':[],
    'TC_UPLOAD_FILE_WITH_ADMIN_LOGIN':[],
    'TC_UPLOAD_MORE_THAN_5MB_FILE_WITH_USER_LOGIN':[],
    'TC_UPLOAD_FILE_WITH_INVALID_FILE_NAME_FORMAT':[],
    'TC_CLICK_UPLOAD_BUTTON':[],
    'TC_SUPPORT_VALUE_NEW_TOPIC':[],
    'TC_URL_REDIRECTION':[],
    'TC_UNKNOWN_TOPIC':[],
    'TC_ASP_URL_REDIRECTION':[],
    'TC_VIDEO_URL':[],
    'TC_SUPPORT_LIST_ASP_URL_REDIRECTION':[],
    'TC_THREAD_ASP_URL_REDIRECTION':[],
    'TC_FORUM_ASP_URL_REDIRECTION':[],
    'TC_TOPOC_ASP_URL_REDIRECTION':[],
    'TC_MANAGE_ASP_URL_REDIRECTION':[],
    'TC_STATEMENT_ASP_URL_REDIRECTION':[],
    'TC_STMT_ASP_URL_REDIRECTION':[],
    'TC_SITEMAP_URL':[],
    'TC_UPDATE_NEWS':[],
    'TC_SUBMIT_CAMP_UPDATE':[],
    'TC_FOOTER_BROWSE':[],
    'TC_FOOTER_CREATE_NEW_TOPIC':[],
    'TC_FOOTER_UPLOAD':[],
    'TC_FOOTER_SITEMAP':[],
    'TC_FOOTER_HELP':[],
    'TC_FOOTER_WHITE_PAPER':[],
    'TC_FOOTER_BLOG':[],
    'TC_footer_jobs':[],


}
