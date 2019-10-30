from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import sys
import os
import HtmlTestRunner

# sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from ddt import ddt, data, unpack
from PageObjects.Pages.Yahoo.yahoosendemail import YahooSendEmail
from PageObjects.Pages.Gmail.gmailrecieveemail import GmailRecieveEmail
from PageObjects.PageVariables.variabledata import get_csv_data

dirpath = os.getcwd()
csv_path = dirpath + '/../TestData/test_data.csv'
driver_path = dirpath + '/../Dependencies/'
screenshot_dir = dirpath + '/../Screenshots/'
reports_dir = dirpath + '/../Reports/'



@ddt
class MailTransferTest(unittest.TestCase):

    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path= driver_path+'/chromedriver') #for chrome driver
        # cls.driver = webdriver.Firefox(executable_path=driver_path + "/geckodriver")  # for firefox driver
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @data(*get_csv_data(csv_path))
    @unpack
    def test_mail_transfer(self, yahoo_id, yahoo_password, gmail_id, gmail_password, subject_to, mail_template):
        self.driver.get("https://mail.yahoo.com")
        time.sleep(2)
        self.driver.get_screenshot_as_file(screenshot_dir + str(round(time.time())) + '.png')
        yahoo =YahooSendEmail(self.driver)
        yahoo.yahoo_login(yahoo_id, yahoo_password)

        yahoo.send_email(gmail_id,subject_to, mail_template)

        gmail = GmailRecieveEmail(self.driver)
        gmail.open_gmail()
        gmail.login_to_gmail(gmail_id, gmail_password)
        gmail.search_for_mails(yahoo_id+'@yahoo.com')

        total_number_of_mails_recieved = gmail.finding_total_number_of_mails()
        # print(total_number_of_mails_recieved)

        gmail.access_first_email()
        from_email_id = gmail.get_from_email_id()
        subject = gmail.get_subject()

        if yahoo_id in from_email_id and subject == subject_to :
            print("Test Passed and Total number of mails recieved = "+str(total_number_of_mails_recieved))
            assert 1==1
        else:
            print("Test Failed")
            assert 1==2

    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=os.getcwd()+'/../Reports/'))
