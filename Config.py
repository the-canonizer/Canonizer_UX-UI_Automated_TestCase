import os
import platform
import string
import random

"""
Set All Basic Configuration required for testing Framework
"""

DEFAULT_BASE_URL = "https://ux-dev.canonizer.com/"

ARCHIVED_CAMP_URL = "https://development.canonizer.com/topic/861-can-1462-test/2-camp-1"
ARCHIVED_EDIT_CAMP_URL = "https://development.canonizer.com/camp/history/861-can-1462-test/2-camp-1"
UPLOAD_FILE_URL = "https://ux-dev.canonizer.com/uploadFile"
ACCOUNT_SETTING_URL = "https://ux-dev.canonizer.com/settings?tab=profile_info"
SUPPORTED_CAMP_URL = "https://ux-dev.canonizer.com/settings?tab=direct_supported_camps"
NICKNAME_URL = "https://ux-dev.canonizer.com/settings?tab=nick_name"
USER_PREFERENCE_URL = "https://ux-dev.canonizer.com/settings?tab=user_preferences"
DIRECT_SUPPORTED_CAMP_URL = "https://ux-dev.canonizer.com/settings?tab=direct_supported_camps"
DELEGATE_SUPPORT_URL = "https://ux-dev.canonizer.com/settings?tab=delegate_supported_camp"
SUBSCRIPTION_URL = "https://ux-dev.canonizer.com/settings?tab=subscriptions"
SOCIAL_AUTH = "https://ux-dev.canonizer.com/settings?tab=social_oauth_verification"
CHANGE_PASSWORD = "https://ux-dev.canonizer.com/settings?tab=change_password"
NOTIFICATION_URL = "https://ux-dev.canonizer.com/notifications"
BROWSE_PAGE_URL = "https://ux-dev.canonizer.com/browse"
VIDEOS_URL = "https://ux-dev.canonizer.com/videos"
HELP_URL = "https://ux-dev.canonizer.com/topic/132-Help/1-Agreement?is_tree_open=1"
UPLOAD_FILE_URL = "https://ux-dev.canonizer.com/uploadFile"
PROFILE_PAGE = "https://ux-dev.canonizer.com/settings?tab=profile_info"
TOPIC_TAG_URL = "https://ux-dev.canonizer.com/categories/9"
TOPIC_SEARCH_URL = "https://ux-dev.canonizer.com/search?q=test"
TREE_SEARCH_URL = "https://ux-dev.canonizer.com/search?q=tree"
AGREE_SEARCH_URL = "https://ux-dev.canonizer.com/search?q=tree"


"""
    Identify the Default Chrome Binary Location for different OS 
"""
DEFAULT_BINARY_LOCATION = ''

if platform.system() == 'Darwin':
    DEFAULT_BINARY_LOCATION = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    DEFAULT_CHROME_DRIVER_LOCATION = os.getcwd() + "/Webdrivers/chromedriver"
elif platform.system() == 'Windows':
    DEFAULT_BINARY_LOCATION = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    DEFAULT_CHROME_DRIVER_LOCATION = os.getcwd() + "/Webdrivers/chromedriver"
elif platform.system() == 'Linux':
    DEFAULT_BINARY_LOCATION = "/usr/bin/google-chrome"
    DEFAULT_CHROME_DRIVER_LOCATION = os.getcwd() + "/Webdrivers/chromedriver"
else:
    print("Unknown OS")
    exit(1)
import random
import string

def random_char(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

NEW_USER = random_char(7)+"@gmail.com"
DEFAULT_NAME = "Akash"
INVALID_NAME = "Akash   ksndmsnd,mas"
INVALID_PASSWORD = "sfagf@@3 sfg gdahg"

FIRST_NAME = "test"
FIRST_NAME_WITH_SPACES = ''.join(random.choices(string.ascii_uppercase + "        ", k=10))
MIDDLE_NAME = "testing"
LAST_NAME = "automation"

DEFAULT_FIRST_NAME = "kumar"
DEFAULT_LAST_NAME = "file"
DEFAULT_EMAIL = "akash.roshan@iffort.com"
DEFAULT_PASSWORD = "Test@123"
DEFAULT_CONFIRM_PASSWORD = "Test@123"
INVALID_MOBILE_NUMBER = "12345"
DEFAULT_MOBILE_NUMBER = ''.join(random.choices(string.digits, k=10))
DEFAULT_INVALID_EMAIL = "akash222222gmail"

reg_list_1 = [
    "      ",
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    INVALID_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
reg_list_2 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    INVALID_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
reg_list_3 = [
    '',
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
reg_list_4 = [
    DEFAULT_FIRST_NAME,
    '',
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASSWORD,
    DEFAULT_CONFIRM_PASSWORD,
    ''
]
reg_list_5 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    '',
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
reg_list_6 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    '',
    DEFAULT_PASS,
    ''
]
reg_list_7 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    'ab123',
    '1234567',
    ''
]
reg_list_8 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    'Test@123',
    ''

]
reg_list_9 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
reg_list_10 = [
    "first  @##$#$$$23",
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
reg_list_11 = [
    DEFAULT_FIRST_NAME,
    "akash@@@@###@@",
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
reg_list_12 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
reg_list_13 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    'INVALID'
]
reg_list_14 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_INVALID_EMAIL,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''

]
reg_list_15 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    NEW_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
reg_list_16 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    NEW_USER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
reg_list_17 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    NEW_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
reg_list_18 = [
    FIRST_NAME_WITH_SPACES,
    DEFAULT_LAST_NAME,
    NEW_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]

# Forgot Password  Page Configuration Parameters
UNREGISTERED_EMAIL = "can@gmail.com"
INVALID_LONG_OTP = "7272727722"
DEFAULT_EMAIL = "cano3@yopmail.com"
DEFAULT_USER_INVALID = "xcvxc"

DEFAULT_USER = "akash.roshan@iffort.com"
DEFAULT_PASS = "Test@123"
DEFAULT_INVALID_USER = 'invaliduse22rgmail.com'
DEFAULT_INVALID_PASSWORD = "invalid_password"

# Account Setting page Configuration Parameters
DEFAULT_NICK_NAME = "Ahasg"
DEFAULT_NEW_PASSWORD = "Test@1234"
DEFAULT_INVALID_NICK_NAME = "Akash Roshan"
DEFAULT_INVALID_CONFIRM_PASSWORD = "Akash@   12333333"
INVALID_NEW_PASSWORD = "Akash123333"
INVALID_CURRENT_PASSWORD = "Akash@    12333"
DEFAULT_CONFIRM_PASSWORD = "Akash@166666"
DEFAULT_FIRST_NAME = "  automation  testing"
DEFAULT_LAST_NAME = "  testing  cases"
DEFAULT_MIDDLE_NAME = "  test  case "

# support camps tab Configuration Parameters
DEFAULT_TOPIC_NAME = "Test"
DEFAULT_UNVERIFIED_PHONE_NUMBER = "1234567890"
DEFAULT_INVALID_PHONE_NUMBER = "1212121212"
DEFAULT_VALID_PHONE_NUMBER = ""
DEFAULT_INVALID_OTP = "123456789"
DEFAULT_INVALID_EMAIL_FORMAT = "test@test"


# Create New Topic Configuration Parameters

DEFAULT_NAMESPACE = ""
DEFAULT_SUMMARY = "Default note"
DUPLICATE_TOPIC_NAME = "Theories of Consciousness"
INVALID_TOPIC_NAME = "@#$%^&(!(!(!"
add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
DEFAULT_UPDATE_TOPIC_NAME = "Camp" + add_name,

# Camp Forum Configuration Parameters
DEFAULT_TOPIC = "Test"
DUPLICATE_THREAD_TITLE = "Automated thread"

# Create New Camp Configuration Parameters
DEFAULT_NICK_NAME = "Akash-New"
DEFAULT_PARENT_CAMP = ""
DEFAULT_NOTE = "Automated note"
DUPLICATE_CAMP_NAME = "New Camp"
DEFAULT_CAMP_ABOUT_URL = "https://canonizer3.canonizer.com/"
INVALID_CAMP_ABOUT_URL = "google@com"
add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
DEFAULT_CAMP_NAME = "Selenium Test Camp" + add_name,
DEFAULT_CAMP2_NAME = "Selenium Test Camp" + add_name + add_name,

CREATE_CAMP_LIST_1 = [
    DEFAULT_NICK_NAME,
    DEFAULT_PARENT_CAMP,
    DEFAULT_CAMP_NAME,
    "Keywords",
    "Test summary",
    DEFAULT_CAMP_ABOUT_URL,

]
CREATE_CAMP2_LIST_1 = [
    DEFAULT_NICK_NAME,
    DEFAULT_PARENT_CAMP,
    DEFAULT_CAMP2_NAME,
    "Keywords",
    "Test summary",
    DEFAULT_CAMP_ABOUT_URL,

]
CREATE_CAMP_LIST_2 = [
    DEFAULT_NICK_NAME,
    DEFAULT_PARENT_CAMP,
    "",
    "Keywords",
    "Test summary",
    DEFAULT_CAMP_ABOUT_URL,
]
CREATE_CAMP_LIST_3 = [
    "",
    "",
    DUPLICATE_CAMP_NAME,
    "",
    "",
    ""
]
CREATE_CAMP_LIST_4 = [
    DEFAULT_NICK_NAME,
    DEFAULT_PARENT_CAMP,
    DEFAULT_CAMP_NAME,
    "Keywords",
    "Test summary",
    INVALID_CAMP_ABOUT_URL,
]
CREATE_CAMP_LIST_5 = [
    DEFAULT_NICK_NAME,
    DEFAULT_PARENT_CAMP,
    DUPLICATE_CAMP_NAME,
    "Keywords",
    "Test summary",
    DEFAULT_CAMP_ABOUT_URL,
]
# Create News Configuration Parameters
DEFAULT_INVALID_LINK = "ww@format"

# History Pages Parameters
DEFAULT_HISTORY_TOPIC = "Software Testing"

# Supported Camp Parameters
DEFAULT_SUPPORTED_TOPIC_NAME = "Supported topic automation"






