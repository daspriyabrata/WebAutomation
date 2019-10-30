import time
from PageObjects.Locators.Locators import Locators


class YahooSendEmail():

    def __init__(self, driver):
        self.driver = driver

        self.yahoo_username = Locators.yahoo_username_xpath
        self.yahoo_password = Locators.yahoo_password_xpath
        self.yahoo_next_button = Locators.yahoo_next_button_xpath
        self.yahoo_signin_button = Locators.yahoo_sign_in_button_xpath
        self.yahoo_compose_button = Locators.yahoo_compose_button_xpath
        self.yahoo_to_email_field = Locators.yahoo_to_email_id_field_xpath
        self.yahoo_subject_field = Locators.yahoo_subject_field_xpath
        self.yahoo_message_body = Locators.yahoo_message_body_xpath
        self.yahoo_send_button = Locators.yahoo_send_button_xpath

    def yahoo_login(self, username, password):
        self.driver.find_element_by_xpath(self.yahoo_username).send_keys(username)
        self.driver.find_element_by_xpath(self.yahoo_next_button).click()
        self.driver.find_element_by_xpath(self.yahoo_password).send_keys(password)
        self.driver.find_element_by_xpath(self.yahoo_signin_button).click()

    def send_email(self, to_email_id, subject_to, mail_template):

        self.driver.find_element_by_xpath(self.yahoo_compose_button).click()
        self.driver.find_element_by_xpath(self.yahoo_to_email_field).send_keys(to_email_id)
        self.driver.find_element_by_xpath(self.yahoo_subject_field).send_keys(subject_to)
        self.driver.find_element_by_xpath(self.yahoo_message_body).send_keys(mail_template)
        self.driver.find_element_by_xpath(self.yahoo_send_button).click()