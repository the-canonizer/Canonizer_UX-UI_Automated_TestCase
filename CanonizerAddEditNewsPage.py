import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from CanonizerValidationCheckMessages import message
from CanonizerBase import Page
from Identifiers import CampForumIdentifiers, AddNewsIdentifiers, CampHistoryIdentifiers, BrowsePageIdentifiers
from selenium.webdriver.common.keys import Keys
import string
import random
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import *
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC



class CanonizerAddNewsPage(Page):

    def driver(self):
        self.driver = webdriver.Chrome()
    def load_add_news_page(self):
        self.driver.implicitly_wait(30)
        action = ActionChains(self.driver)
        '''self.driver.find_element(By.XPATH, "/html/body/div[1]/section/section/main/div/div/div/div[1]/div[2]/div[2]/a/span/img").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "threedot_dropdown_add_news_menu_item").click()'''
        news = self.driver.current_url
        news = news.replace("topic", "addnews")
        self.driver.get(news)
        time.sleep(5)

        return CanonizerAddNewsPage(self.driver)

    def enter_display_text(self, display_text):
        self.find_element(*AddNewsIdentifiers.DISPLAY_TEXT).send_keys(display_text)

    def enter_link(self, link):

        self.find_element(*AddNewsIdentifiers.LINK).send_keys(link)

    def click_create_news_button(self):

        self.find_element(*AddNewsIdentifiers.CREATE_NEWS_BUTTON).click()

    def check_available_for_child_camps(self):
        self.find_element(*AddNewsIdentifiers.AVAILABLE_FOR_CHILD_CAMP).click()

    def create_news(self, link, display_text):
        self.driver.implicitly_wait(10)
        self.enter_link(link)
        self.enter_display_text(display_text)
        self.click_create_news_button()

    def create_news_with_valid_data(self, display_text, link):
        self.create_news(display_text, link)
        return CanonizerAddNewsPage(self.driver)

    def add_news_page_mandatory_fields_are_marked_with_asterisk(self):
        try:
            WebDriverWait(self.driver, 8).until(
                EC.visibility_of_element_located((By.XPATH, '//div[text()="Add News"]')))
        except TimeoutException:
            pass

        return \
            self.find_element(*AddNewsIdentifiers.DISPLAY_TEXT_ASTERISK) and \
            self.find_element(*AddNewsIdentifiers.LINK_ASTERISK) and \
            self.find_element(*AddNewsIdentifiers.NICKNAME_ASTERISK)

    def create_news_with_blank_display_text(self, link):
        self.create_news('', link)
        return CanonizerAddNewsPage(self.driver)

    def create_news_with_blank_link(self, display_text):
        self.create_news(display_text, '')
        return CanonizerAddNewsPage(self.driver)

    def create_new_with_blank_fields(self, link, display_text):
        self.create_news(link, display_text)
        return CanonizerAddNewsPage(self.driver)

    def click_add_news_cancel_button(self):
        self.hover(*AddNewsIdentifiers.CANCEL_BUTTON)
        self.find_element(*AddNewsIdentifiers.CANCEL_BUTTON).click()
        return CanonizerAddNewsPage(self.driver)

    def create_news_with_invalid_link_format(self, display_text, link):
        self.create_news(display_text, link)
        self.hover(*AddNewsIdentifiers.INVALID_LINK)
        return CanonizerAddNewsPage(self.driver)

    def create_news_with_enter_key(self, display_text, link):
        self.enter_display_text(display_text)
        self.enter_link(link)
        self.check_available_for_child_camps()
        self.find_element(*AddNewsIdentifiers.CREATE_NEWS_BUTTON).send_keys(Keys.ENTER)
        return CanonizerAddNewsPage(self.driver)

    def create_news_with_duplicate_data(self, display_text, link):
        self.create_news(display_text, link)
        return CanonizerAddNewsPage(self.driver)

    def create_news_with_trailing_spaces(self, display_text, link):
        self.create_news(display_text, link)
        return CanonizerAddNewsPage(self.driver)


class CanonizerEditNewsPage(Page):
    window_scroll = "window.scrollTo(0, document.body.scrollHeight);"

    def load_edit_news_page(self, topic_name):
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.XPATH, "/html/body/div/div/header/div[2]/nav/ul/li[2]/a").click()

        # Click on Search Topic
        self.hover(*CampForumIdentifiers.SEARCH_TOPIC)
        self.find_element(*CampForumIdentifiers.SEARCH_TOPIC).send_keys(topic_name)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/div/div/div[2]/div[1]/div[1]/div/ul/li[1]/a/span[1]").click()

        self.hover(*CampForumIdentifiers.SEARCH_ICON)
        self.find_element(*CampForumIdentifiers.SEARCH_ICON).click()
        self.hover(*CampForumIdentifiers.TOPIC_CLICK)
        self.find_element(*CampForumIdentifiers.TOPIC_CLICK).click()
        # Click on Edit News
        self.hover(*AddNewsIdentifiers.EDIT_NEWS)
        self.find_element(*AddNewsIdentifiers.EDIT_NEWS).click()
        self.driver.execute_script(self.window_scroll)
        self.find_element(*AddNewsIdentifiers.EDIT_ICON).click()
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/ul/li[1]/span/a").click()

        return CanonizerEditNewsPage(self.driver)



    def update_display_text(self, display_text):
        self.find_element(*AddNewsIdentifiers.DISPLAY_TEXT).send_keys(display_text)

    def update_link(self, link):
        self.find_element(*AddNewsIdentifiers.LINK).send_keys(link)

    def click_create_news_button(self):
        self.find_element(*AddNewsIdentifiers.CREATE_NEWS_BUTTON).click()

    def update_available_for_child_camps(self):
        self.find_element(*AddNewsIdentifiers.AVAILABLE_FOR_CHILD_CAMP).click()

    def update_news(self, display_text, link):
        self.update_display_text(display_text)
        self.update_link(link)
        self.update_available_for_child_camps()
        self.click_create_news_button()

    def update_news_with_blank_display_text(self, link,):
        self.find_element(*AddNewsIdentifiers.DISPLAY_TEXT).clear()
        self.update_news('', link)
        self.hover(*AddNewsIdentifiers.BLANK_DISPLAY_TEXT_ERROR)
        return CanonizerEditNewsPage(self.driver)

    def update_news_with_blank_link(self, display_text):
        self.find_element(*AddNewsIdentifiers.LINK).clear()
        self.update_news(display_text, '')
        self.hover(*AddNewsIdentifiers.BLANK_LINK_ERROR)
        return CanonizerEditNewsPage(self.driver)

    def click_edit_news_cancel_button(self):
        self.hover(*AddNewsIdentifiers.EDIT_CANCEL_BUTTON)
        self.find_element(*AddNewsIdentifiers.EDIT_CANCEL_BUTTON).click()
        return CanonizerEditNewsPage(self.driver)


