class Locators:

    yahoo_username_xpath = "//input[@id='login-username']"
    yahoo_password_xpath = "//input[@id='login-passwd']"
    yahoo_next_button_xpath = "//input[@id='login-signin']"
    yahoo_sign_in_button_xpath = "//button[@id='login-signin']"
    yahoo_compose_button_xpath =  "//a[@data-test-id='compose-button']"
    yahoo_to_email_id_field_xpath = "//input[@id='message-to-field']"
    yahoo_subject_field_xpath =  "//input[@placeholder='Subject']"
    yahoo_message_body_xpath = "//div[@aria-label='Message body']"
    yahoo_send_button_xpath = "//span[contains(text(),'Send')]"

    gmail_usedname_field_id = 'identifierId'
    gmail_password_id = 'password'
    gmail_search_box_xpath = "//input[@placeholder='Search mail']"
    gmail_mail_number_xpath = "//body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/span/div/span[contains(text(),'of')]/span[2]"
    gmail_first_mail_xpath = "//div[@class='ae4 UI UJ']//tr[1]"
    gmail_from_email_xpath = "//span[@class='go']"
    gmail_subject_xpath = "//h2[@class='hP']"