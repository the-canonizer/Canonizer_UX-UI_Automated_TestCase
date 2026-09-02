import pytest

from .shared import *


class BaseFlow:
    """Browser lifecycle and shared helpers for every test module.

    The browser itself is built by the `driver` fixture in conftest.py. This
    class only attaches it to the test instance, so all existing tests keep
    using `self.driver` unchanged.
    """

    @pytest.fixture(autouse=True)
    def _browser_session(self, request):
        """Attach a browser to the test instance, unless it does not need one."""
        if request.node.get_closest_marker("no_browser"):
            self.driver = None
            return
        self.driver = request.getfixturevalue("driver")

    def login_to_canonizer_app(self):
        """Log in with the configured credentials, for tests that need a session."""
        require_credentials()
        self.driver.implicitly_wait(30)
        CanonizerLoginPage(self.driver).click_on_login_page_button().verify_the_login_functionality_by_entering_the_registered_credential(DEFAULT_USER, DEFAULT_PASS)
        self.driver.maximize_window()
