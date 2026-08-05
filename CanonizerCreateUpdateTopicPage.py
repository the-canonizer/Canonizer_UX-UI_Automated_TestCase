import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from CanonizerValidationCheckMessages import message
from CanonizerBase import Page
from Identifiers import CreateTopicIdentifiers, CampForumIdentifiers, UpdateTopicIdentifiers, CreateCampIdentifiers, \
    BrowsePageIdentifiers, CampStatementIdentifiers
from selenium.webdriver.chrome.service import Service
from selenium import webdriver




class CanonizerCreateNewTopic(Page):

    def driver(self):
        self.driver = webdriver.Chrome()
        self.action = ActionChains(self.driver)

    def click_create_topic_button_without_login(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.ID, "create-topic-link").click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "login-submit-btn")))
        return CanonizerCreateNewTopic(self.driver)

    def click_create_topic_button(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.ID, "create-topic-link").click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "cancel-btn")))
        return CanonizerCreateNewTopic(self.driver)

    def create_topic_button(self):
        self.driver.implicitly_wait(30)
        self.find_element(*CreateTopicIdentifiers.CREATE_TOPIC_BUTTON).click()

    def enter_topic_name(self, topic_name):
        self.driver.implicitly_wait(30)
        WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'create_new_topic_topic_name')))
        self.find_element(*CreateTopicIdentifiers.TOPIC_NAME).send_keys(topic_name)

    def entering_data_fields(self, topic_name):
        self.driver.implicitly_wait(30)
        self.enter_topic_name(topic_name)

    def scroll_down(self):
        self.driver.implicitly_wait(10)
        action = ActionChains(self.driver)

        self.i = 100
        self.current_name_list = []

        while self.i >= 1:
            action.key_down(Keys.DOWN).perform()
            action.key_down(Keys.DOWN).perform()
            action.key_down(Keys.ENTER).perform()
            self.i = self.i - 1
            time.sleep(0.4)
            self.current_name = self.driver.find_element(By.XPATH,
                                                         "/html/body/div[1]/section/section/main/div/div/div/div[1]/div/div/form/div[1]/div[4]/div/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div/div/div/span[2]").text
            if self.current_name == "sandbox testing":
                time.sleep(10)
                break
            self.driver.find_element(By.XPATH,
                                     "/html/body/div[1]/section/section/main/div/div/div/div[1]/div/div/form/div[1]/div[4]/div/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div/div/div/span[2]").click()

    def scroll_down_edit(self):
        self.driver.implicitly_wait(20)
        action = ActionChains(self.driver)

        self.i = 100
        self.current_name_list = []

        while self.i >= 1:
            action.key_down(Keys.DOWN).perform()
            action.key_down(Keys.DOWN).perform()
            action.key_down(Keys.ENTER).perform()
            self.i = self.i - 1
            time.sleep(0.4)
            self.current_name = self.driver.find_element(By.XPATH,
                                                         "/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div[2]/form/div/div[3]/div/div/div[2]/div/div/div/div/span[2]").text
            if self.current_name == "sandbox testing":
                time.sleep(10)
                break
            if self.current_name == "Testingcanon1":
                return CanonizerCreateNewTopic(self.driver)

    def scroll_to_sandbox(self):
        self.driver.implicitly_wait(20)
        action = ActionChains(self.driver)

        self.i = 100
        self.current_name_list = []

        while self.i >= 1:
            action.key_down(Keys.DOWN).perform()
            action.key_down(Keys.DOWN).perform()
            action.key_down(Keys.ENTER).perform()
            self.i = self.i - 1
            time.sleep(0.4)
            self.current_name = self.driver.find_element(By.XPATH,
                                                         "/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/form/div[1]/div[1]/div[4]/div/div[2]/div/div/div/div/span[2]/text()").text
            time.sleep(10)
            if self.current_name == "sandbox testing":
                time.sleep(10)
                break

    def create_topic(self, topic_name):
        self.driver.implicitly_wait(30)
        self.entering_data_fields(topic_name)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/section/section/main/div/div/div/div[1]/div/div/form/div[1]/div[4]/div/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div/div/div/span[2]").click()
        self.scroll_down()

        self.create_topic_button()

    def create_topic_with_valid_data(self, topic_name):
        self.driver.implicitly_wait(30)
        self.create_topic(topic_name)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/section/header/div/nav/ul/li[1]/a/span[1]")))
        return CanonizerCreateNewTopic(self.driver)

    def create_topic_with_blank_topic(self):
        self.driver.implicitly_wait(30)
        self.create_topic("     ")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "create_new_topic_topic_name_help")))

        return CanonizerCreateNewTopic(self.driver)

    def create_topic_with_same_topic(self, topic_name):
        self.driver.implicitly_wait(30)
        self.create_topic(topic_name)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(
            EC.invisibility_of_element((By.CLASS_NAME, "ant-typography text-canRed font-medium text-base !mb-2")))
        return CanonizerCreateNewTopic(self.driver)

    def create_topic_name_with_trailing_space(self, topic_name):
        self.driver.implicitly_wait(30)
        self.create_topic("     New Topic")

        return CanonizerCreateNewTopic(self.driver)

    def create_topic_name_with_enter_key(self, summary, topic_name, namespace):
        self.entering_data_fields(topic_name)
        self.hover(*CreateTopicIdentifiers.CREATE_TOPIC_BUTTON)
        self.find_element(*CreateTopicIdentifiers.CREATE_TOPIC_BUTTON).send_keys(Keys.ENTER)
        self.hover(*CreateTopicIdentifiers.TOPIC_PAGE)
        topic_page_confirmation = self.find_element(*CreateTopicIdentifiers.TOPIC_PAGE).text
        if topic_page_confirmation == message['Create_Topic']['CREATE_TOPIC_TITLE']:
            return CanonizerCreateNewTopic(self.driver)
        else:
            print("Page not found")

    def create_topic_with_special_chars(self, topic_name):
        self.driver.implicitly_wait(30)
        self.create_topic(topic_name)

        return CanonizerCreateNewTopic(self.driver)

    def create_topic_without_entering_mandatory_fields(self, topic_name):
        self.driver.implicitly_wait(30)
        self.create_topic('')
        return CanonizerCreateNewTopic(self.driver)

    def create_topic_with_entering_data_only_in_mandatory_fields(self, summary, topic_name, namespace):
        # Reuse the base create flow to submit only required fields for this scenario.
        self.create_topic(topic_name)
        return CanonizerCreateNewTopic(self.driver)

    def click_on_cancel_button(self):
        self.hover(*CreateTopicIdentifiers.CANCEL_BUTTON)
        self.find_element(*CreateTopicIdentifiers.CANCEL_BUTTON).click()
        self.hover(*CreateTopicIdentifiers.MAIN_PAGE)
        topic_page_confirmation = self.find_element(*CreateTopicIdentifiers.MAIN_PAGE).text
        if topic_page_confirmation == message['Create_Topic']['TOPIC_LABEL']:
            return CanonizerCreateNewTopic(self.driver)
        else:
            print("Page not found")

    def topic_page_mandatory_fields_are_marked_with_asterisk(self):
        """
        This Function checks, if Mandatory fields on Create topic Page Marked with *
        """
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'ant-form-item-extra')))
        except TimeoutException:
            pass

        return \
            self.find_element(*CreateTopicIdentifiers.NICK_NAME_ASTERISK) and \
            self.find_element(*CreateTopicIdentifiers.TOPIC_NAME_ASTERISK) and \
            self.find_element(*CreateTopicIdentifiers.NAMESPACE_ASTERISK)


class CanonizerUpdateTopicPage(Page):
    def load_topic_history_page(self):

        self.driver.implicitly_wait(30)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/section/section/main/div/div/div/div[1]/div[1]/div[2]/div[2]/a/span").click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "threedot_dropdown_manage_topic_btn__menu_item_text")))
        self.driver.find_element(By.ID, "threedot_dropdown_manage_topic_btn__menu_item_text").click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "topic-history-container")))
        self.driver.find_element(By.XPATH, "/html/body/div[1]/section/section/main/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/button/span").click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "history-page-back-button")))

        return CanonizerUpdateTopicPage(self.driver)




    def verify_submit_topic_update_button(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/section/section/main/div/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button/span").click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "create-topic-btn")))

        return CanonizerUpdateTopicPage(self.driver)


    def update_topic_name(self):
        self.driver.implicitly_wait(30)

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "create-topic-btn")))
        self.driver.find_element(*UpdateTopicIdentifiers.UPDATE_TOPIC_NAME).send_keys("Test")
        self.driver.find_element(*UpdateTopicIdentifiers.SUBMIT_UPDATE_BUTTON).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/section/main/div/div/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/button[1]/span")))
        self.driver.find_element(By.XPATH, "/html/body/div[1]/section/section/main/div/div/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/button[1]/span").click()

        return CanonizerUpdateTopicPage(self.driver)

    def update_topic_name_and_verify_submit_update_button(self, topic_name):
        self.verify_submit_topic_update_button()
        self.find_element(*UpdateTopicIdentifiers.UPDATE_TOPIC_NAME).send_keys(topic_name)
        self.find_element(By.ID, "edit_summary").send_keys("new summary")
        self.find_element(*UpdateTopicIdentifiers.SUBMIT_UPDATE_BUTTON).click()

        return CanonizerUpdateTopicPage(self.driver)


    def verify_cancel_button_functionality_on_topic_update_page(self):
        self.verify_submit_topic_update_button()
        self.find_element(*UpdateTopicIdentifiers.CANCEL_BUTTON).click()
        return CanonizerUpdateTopicPage(self.driver)


    def verify_preview_button_functionality_on_topic_update_page(self):
        self.verify_submit_topic_update_button()
        self.find_element(*UpdateTopicIdentifiers.PREVIEW_BUTTON).click()
        return CanonizerUpdateTopicPage(self.driver)

    def verify_submitter_nick_name_on_preview_modal(self):
        self.verify_submit_topic_update_button()
        self.find_element(*UpdateTopicIdentifiers.PREVIEW_BUTTON).click()
        self.find_element(*UpdateTopicIdentifiers.SUBMITTER_NICK_NAME_LINK_ON_PREVIEW_MODAL).click()
        return CanonizerUpdateTopicPage(self.driver)


    def verify_cancel_button_on_preview_modal(self):
        self.verify_submit_topic_update_button()
        self.find_element(*UpdateTopicIdentifiers.PREVIEW_BUTTON).click()
        self.find_element(*UpdateTopicIdentifiers.CANCEL_BUTTON).click()
        return CanonizerUpdateTopicPage(self.driver)


    def verify_compare_topics_button_functionality(self):
        self.find_element(*UpdateTopicIdentifiers.COMPARE_CHECKBOX1).click()
        self.find_element(*UpdateTopicIdentifiers.COMPARE_CHECKBOX2).click()
        self.find_element(*UpdateTopicIdentifiers.COMPARE_TOPIC_BUTTON).click()
        return CanonizerUpdateTopicPage(self.driver)

    def verify_agreement_link_on_topic_comparison_page(self):
        self.find_element(*UpdateTopicIdentifiers.COMPARE_CHECKBOX1).click()
        self.find_element(*UpdateTopicIdentifiers.COMPARE_CHECKBOX2).click()
        self.find_element(*UpdateTopicIdentifiers.COMPARE_TOPIC_BUTTON).click()
        self.find_element(*UpdateTopicIdentifiers.AGREEMENT_LINK).click()

        return CanonizerUpdateTopicPage(self.driver)


    def verify_create_topic_button_functionality_on_topic_comparison_page(self):
        self.find_element(*UpdateTopicIdentifiers.COMPARE_CHECKBOX1).click()
        self.find_element(*UpdateTopicIdentifiers.COMPARE_CHECKBOX2).click()
        self.find_element(*UpdateTopicIdentifiers.COMPARE_TOPIC_BUTTON).click()
        self.find_element(*UpdateTopicIdentifiers.CREATE_TOPIC).click()

        return CanonizerUpdateTopicPage(self.driver)

    def verify_create_camp_button_functionality_on_topic_comparison_page(self):
        self.find_element(*UpdateTopicIdentifiers.COMPARE_CHECKBOX1).click()
        self.find_element(*UpdateTopicIdentifiers.COMPARE_CHECKBOX2).click()
        self.find_element(*UpdateTopicIdentifiers.COMPARE_TOPIC_BUTTON).click()
        self.find_element(*UpdateTopicIdentifiers.CREATE_CAMP).click()
        return CanonizerUpdateTopicPage(self.driver)

    def verify_back_arrow_icon_on_topic_comparison_page(self):
        self.hover(*UpdateTopicIdentifiers.COMPARE_CHECKBOX1)
        self.find_element(*UpdateTopicIdentifiers.COMPARE_CHECKBOX1).click()
        self.hover(*UpdateTopicIdentifiers.COMPARE_CHECKBOX2)
        self.find_element(*UpdateTopicIdentifiers.COMPARE_CHECKBOX2).click()
        self.hover(*UpdateTopicIdentifiers.COMPARE_TOPIC_BUTTON)
        self.find_element(*UpdateTopicIdentifiers.COMPARE_TOPIC_BUTTON).click()
        self.hover(*UpdateTopicIdentifiers.BACK_ARROW_ICON)
        self.find_element(*UpdateTopicIdentifiers.BACK_ARROW_ICON).click()
        self.hover(*UpdateTopicIdentifiers.TOPIC_HISTORY_TITLE)
        page_title = self.find_element(*UpdateTopicIdentifiers.TOPIC_HISTORY_TITLE).text
        if page_title == message['Update_Topic']['TOPIC_HISTORY_TITLE']:
            return CanonizerUpdateTopicPage(self.driver)
        else:
            print("Title not found or is not matching")

    def verify_view_this_version_button_functionality(self):
        self.hover(*UpdateTopicIdentifiers.VIEW_THIS_VERSION_BUTTON)
        self.find_element(*UpdateTopicIdentifiers.VIEW_THIS_VERSION_BUTTON).click()
        self.hover(*CreateTopicIdentifiers.TOPIC_PAGE)
        topic_page_confirmation = self.find_element(*CreateTopicIdentifiers.TOPIC_PAGE).text
        if topic_page_confirmation == message['Create_Topic']['CREATE_TOPIC_TITLE']:
            return CanonizerCreateNewTopic(self.driver)
        else:
            print("Page not found")
