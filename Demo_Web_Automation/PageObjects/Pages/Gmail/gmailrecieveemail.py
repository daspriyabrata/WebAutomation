import time
from selenium.webdriver.common.keys import Keys

from PageObjects.Locators.Locators import Locators


class GmailRecieveEmail():

    def __init__(self, driver):
        self.driver = driver

        self.gmail_username_field_id = Locators.gmail_usedname_field_id
        self.gmail_password_field_id = Locators.gmail_password_id
        self.gmail_searchbox_xpath = Locators.gmail_search_box_xpath
        self.gmail_mail_number_xpath = Locators.gmail_mail_number_xpath
        self.gmail_first_mail_xpath = Locators.gmail_first_mail_xpath
        self.gmail_from_email_xpath = Locators.gmail_from_email_xpath
        self.gmail_subject_xpath = Locators.gmail_subject_xpath

    def open_gmail(self):
        self.driver.execute_script("window.open('https://gmail.com')")
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def login_to_gmail(self, username, password):
        self.driver.find_element_by_id(self.gmail_username_field_id).send_keys(username + Keys.ENTER)
        self.driver.find_element_by_name(self.gmail_password_field_id).send_keys(password + Keys.ENTER)

    def search_for_mails(self, from_email_id):
        self.driver.find_element_by_xpath(self.gmail_searchbox_xpath).send_keys(from_email_id + Keys.ENTER)

    def finding_total_number_of_mails(self):
        time.sleep(5)
        number = self.driver.find_element_by_xpath(self.gmail_mail_number_xpath).text
        return number

    def access_first_email(self):
        self.driver.find_element_by_xpath(self.gmail_first_mail_xpath).click()

    def get_from_email_id(self):
        from_mail_id = self.driver.find_element_by_xpath(self.gmail_from_email_xpath).text
        return from_mail_id

    def get_subject(self):
        subject = self.driver.find_element_by_xpath(self.gmail_subject_xpath).text
        return subject