import os
import platform
import random
import string
import time

"""
Set All Basic Configuration required for testing Framework
"""


def env_or_default(name, default):
    value = os.getenv(name)
    if value:
        return value
    return default

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
PROFILE_PAGE = "https://ux-dev.canonizer.com/settings?tab=profile_info"
TOPIC_TAG_URL = "https://ux-dev.canonizer.com/categories/9"
TOPIC_SEARCH_URL = "https://ux-dev.canonizer.com/search?q=test"
TREE_SEARCH_URL = "https://ux-dev.canonizer.com/search?q=tree"
AGREE_SEARCH_URL = "https://ux-dev.canonizer.com/search?q=tree"
OLD_ASP_TOPIC_URL = "https://ux-dev.canonizer.com/topic.asp/105"
OLD_ASP_CAMP_URL = "https://ux-dev.canonizer.com/topic.asp/6669-Test-dlkskndlksndl/1-Agreement"
OLD_ASP_SUPPORT_URL = "https://ux-dev.canonizer.com/secure/support.asp?topic_num=97&camp_num=1"



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

def unique_email(prefix="auto"):
    """Return a fresh address so each registration test creates its own account."""
    return "{}{}{}@gmail.com".format(prefix, random_char(7), int(time.time() * 1000) % 1000000)


DEFAULT_USER = env_or_default("CANONIZER_DEFAULT_USER", "")


def require_credentials():
    """Fail fast with a clear message instead of silently submitting a blank login form."""
    if not DEFAULT_USER or not DEFAULT_PASS:
        raise RuntimeError(
            "CANONIZER_DEFAULT_USER / CANONIZER_DEFAULT_PASS are not set. "
            "Run ./setup.sh, or export them, before running login-required tests."
        )


NEW_USER = unique_email()

# Each registration happy path creates a real account, so the three lists that are
# expected to succeed must not share an address - the 2nd and 3rd would fail as
# duplicates. Anything expected to fail validation can keep reusing NEW_USER.
REG_EMAIL_VALID_CREDENTIAL = unique_email("reg")
REG_EMAIL_MANDATORY_FIELDS = unique_email("mand")
REG_EMAIL_FIRST_NAME_SPACES = unique_email("space")
DEFAULT_NAME = "Rupali"
INVALID_NAME = "Rupali   ksndmsnd,mas"
INVALID_PASSWORD = "sfagf@@3 sfg gdahg"

FIRST_NAME = "test"
FIRST_NAME_WITH_SPACES = ''.join(random.choices(string.ascii_uppercase + "        ", k=10))
MIDDLE_NAME = "testing"
LAST_NAME = "automation"

DEFAULT_PASS = env_or_default("CANONIZER_DEFAULT_PASS", "")

DEFAULT_PASSWORD = "Test@123"

# Data used only to build the reg_list_* fixtures below. These used to be named
# DEFAULT_FIRST_NAME / DEFAULT_LAST_NAME / DEFAULT_CONFIRM_PASSWORD and were
# silently reassigned further down the file, so the name never meant one value.
REG_FIRST_NAME = "kumar"
REG_LAST_NAME = "file"
REG_CONFIRM_PASSWORD = "Test@123"
INVALID_MOBILE_NUMBER = "12345"
DEFAULT_MOBILE_NUMBER = ''.join(random.choices(string.digits, k=10))
DEFAULT_INVALID_EMAIL = "invalidusergmail.com"

reg_list_1 = [
    "      ",
    REG_LAST_NAME,
    DEFAULT_USER,
    INVALID_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
reg_list_2 = [
    REG_FIRST_NAME,
    REG_LAST_NAME,
    DEFAULT_USER,
    INVALID_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
reg_list_3 = [
    '',
    REG_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
reg_list_4 = [
    REG_FIRST_NAME,
    '',
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASSWORD,
    REG_CONFIRM_PASSWORD,
    ''
]
reg_list_5 = [
    REG_FIRST_NAME,
    REG_LAST_NAME,
    '',
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
reg_list_6 = [
    REG_FIRST_NAME,
    REG_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    '',
    DEFAULT_PASS,
    ''
]
reg_list_7 = [
    REG_FIRST_NAME,
    REG_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    'ab123',
    '1234567',
    ''
]
reg_list_8 = [
    REG_FIRST_NAME,
    REG_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    'Test@123',
    ''

]
reg_list_9 = [
    REG_FIRST_NAME,
    REG_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
reg_list_10 = [
    "first  @##$#$$$23",
    REG_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
reg_list_11 = [
    REG_FIRST_NAME,
    "rupali@@@@###@@",
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
reg_list_12 = [
    REG_FIRST_NAME,
    REG_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
reg_list_13 = [
    REG_FIRST_NAME,
    REG_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    'INVALID'
]
reg_list_14 = [
    REG_FIRST_NAME,
    REG_LAST_NAME,
    DEFAULT_INVALID_EMAIL,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''

]
reg_list_15 = [
    REG_FIRST_NAME,
    REG_LAST_NAME,
    REG_EMAIL_MANDATORY_FIELDS,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
reg_list_16 = [
    REG_FIRST_NAME,
    REG_LAST_NAME,
    DEFAULT_USER,
    NEW_USER,  # deliberately non-numeric: exercises the phone-number validator
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
reg_list_17 = [
    REG_FIRST_NAME,
    REG_LAST_NAME,
    REG_EMAIL_VALID_CREDENTIAL,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
reg_list_18 = [
    FIRST_NAME_WITH_SPACES,
    REG_LAST_NAME,
    REG_EMAIL_FIRST_NAME_SPACES,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]

# Forgot Password  Page Configuration Parameters
UNREGISTERED_EMAIL = "can@gmail.com"
INVALID_LONG_OTP = "7272727722"
DEFAULT_EMAIL = env_or_default("CANONIZER_DEFAULT_EMAIL", "")
DEFAULT_USER_INVALID = "xcvxc"

DEFAULT_INVALID_USER = 'invaliduse22rgmail.com'
DEFAULT_INVALID_PASSWORD = "invalid_password"

# Account Setting page Configuration Parameters
DEFAULT_NEW_PASSWORD = "NewPass@1234"
DEFAULT_INVALID_NICK_NAME = "Invalid Nick"
DEFAULT_INVALID_CONFIRM_PASSWORD = "Invalid@12333333"
INVALID_NEW_PASSWORD = "Invalid123333"
INVALID_CURRENT_PASSWORD = "Invalid@12333"
# Whitespace-padded profile data. Currently unused by any test; kept for the
# profile trimming scenarios. Previously these shadowed the registration
# constants of the same name defined near the top of this file.
ACCOUNT_CONFIRM_PASSWORD = "Confirm@166666"
PROFILE_FIRST_NAME_WITH_SPACES = "  automation  testing"
PROFILE_LAST_NAME_WITH_SPACES = "  testing  cases"
PROFILE_MIDDLE_NAME_WITH_SPACES = "  test  case "

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
topic_suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
DEFAULT_UPDATE_TOPIC_NAME = "Camp" + topic_suffix

# Camp Forum Configuration Parameters
DEFAULT_TOPIC = "Test"
DUPLICATE_THREAD_TITLE = "Automated thread"

# Create New Camp Configuration Parameters
DEFAULT_NICK_NAME = "Rupali-New"
DEFAULT_PARENT_CAMP = ""
DEFAULT_NOTE = "Automated note"
DUPLICATE_CAMP_NAME = "New Camp"
DEFAULT_CAMP_ABOUT_URL = "https://canonizer3.canonizer.com/"
INVALID_CAMP_ABOUT_URL = "google@com"
camp_suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
DEFAULT_CAMP_NAME = "Selenium Test Camp" + camp_suffix
DEFAULT_CAMP2_NAME = "Selenium Test Camp" + camp_suffix + camp_suffix

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






