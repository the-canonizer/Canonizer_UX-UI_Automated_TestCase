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
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        CanonizerLoginPage(self.driver).click_on_login_page_button().verify_the_login_functionality_by_entering_the_registered_credential(DEFAULT_USER, DEFAULT_PASS)
        self.driver.maximize_window()
        self._wait_until_logged_in()

    def _wait_until_logged_in(self, timeout=25):
        """Block until the post-login landing page has actually rendered.

        Many login-required tests do a bare ``self.driver.find_element(...)`` as
        their first step after login. With a low implicit wait they race the
        login redirect/render and fail with NoSuchElement. Gating here lets the
        global implicit wait stay small without every test needing its own wait.
        """
        # Auth succeeded once the login modal (its email field) is gone.
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located((By.ID, "login_form_username"))
            )
        except TimeoutException:
            pass
        # App shell finished loading.
        try:
            WebDriverWait(self.driver, 15).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
        except Exception:
            pass
        # A stable landmark from the authenticated landing page.
        try:
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    '//span[contains(normalize-space(.), "Browse More")]'
                    ' | //footer | //*[contains(@class, "footer")]',
                ))
            )
        except TimeoutException:
            pass
