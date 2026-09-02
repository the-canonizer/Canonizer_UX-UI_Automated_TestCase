from .shared import *

class BaseFlow:

    def setup_method(self):
        """
            Initialize the Things
            :return:
        """
        driver_location = DEFAULT_CHROME_DRIVER_LOCATION
        options = webdriver.ChromeOptions()
        options.binary_location = DEFAULT_BINARY_LOCATION
        # will run all the test cases
        # options.add_argument('headless')

        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome()
        self.driver.get(DEFAULT_BASE_URL)
        self.driver.implicitly_wait(30)


    def driver(self):
        self.driver = webdriver.Chrome()
        self.action = ActionChains(self.driver)


    def login_to_canonizer_app(self):
        """
            This Application will allow you to login to canonizer App on need basis
        :param flag:
        :return:
        """
        self.driver.implicitly_wait(30)
        CanonizerLoginPage(self.driver).click_on_login_page_button().verify_the_login_functionality_by_entering_the_registered_credential(DEFAULT_USER, DEFAULT_PASS)
        self.driver.maximize_window()


    
    def teardown_method(self):

        self.driver.close()
