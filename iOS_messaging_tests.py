import unittest
from appium import webdriver
import argparse
import sys
import xmlrunner
import os
from time import sleep
import TestVariables as tv
import TestMethods as tm
import adb_info
import subprocess


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--device_name',
                        default='84B7N16804000866')
    parser.add_argument('-pl', '--platform', default='Android')
    parser.add_argument('-l', '--link', default='localhost')
    parser.add_argument('-p', '--port', default='4723')
    parser.add_argument('-f', '--folder', default='Android')
    parser.add_argument('-app_path', '--app_path', default=tv.app_path)
    parser.add_argument('-plV', '--platform_version', default='7.1.2')
    return parser



parser = create_parser()
namespace = parser.parse_args()
device_name = namespace.device_name
platform = namespace.platform
port = namespace.port
folder = namespace.folder
link = namespace.link
platform_version = namespace.platform_version
app_path = namespace.app_path
phone_number = tv.account_data['number']


class TestAuto(unittest.TestCase):
    def setUp(self):
        "Setup for the test"
        desired_caps = {"udid": "ec21a45af61f2d7c54658008724b590017d2413f",
                        "platformName": "iOS",
                        "bundleId": "im.talkme.talkmeim",
                        "deviceName": "Anton's iPhone",
                        "automationName": "XCUITest",
                        "autoAcceptAlerts": 'true'}

        self.driver = webdriver.Remote(
            'http://' + str(link) + ':' + str(port) + '/wd/hub', desired_caps)
        print "\n.*....*.*****.*....*....*...*******.*****..****..*******."
        print ".**...*.*......*...*...*.......*....*.....*.........*...."
        print ".*.*..*.*****...*.*.*.*........*....*****..***......*...."
        print ".*..*.*.*.......*.*.*.*........*....*.........*.....*...."
        print ".*...**.*****....*...*.........*....*****.****......*...."

        print "Set up - OK!"
        print self.driver.session_id
        # TM.preLogin(self.driver)

        sleep(5)

    def tearDown(self):
        """Tear down the test"""
        print "##########################################################"
        self.driver.quit()
        print"\n"



    def test_Keypad_Send_a_10000_Messages(self):
        test_name = 'Keyapad > Send 50 message'
        print "Test: ", test_name
        sleep(10)
        self.driver.find_element_by_xpath(tv.keypad['xpath']).click()
        sleep(5)
        phone = '3656516221'

        tm.send_a_message_from_keypad(self.driver, phone)
        tm.chat_screen_analizer(self.driver, tm.phone_format(phone))
        message_text = 'This is the message '
        for count in range(50):
            sent_message = message_text + str(count)
            tm.send_message(self.driver, )
            sent_msg = self.driver.find_element_by_xpath('//XCUIElementTypeTextView[@value="' + sent_message + '"]')
            print "Sent messages: ", sent_msg.get_attribute('value')
            answer = sent_message + ' answer'
            waiting_for_answer = True
            error_counter = 0
            while waiting_for_answer == True:
                try:
                    received_msg = self.driver.find_element_by_xpath('//XCUIElementTypeTextView[@value="' + answer + '"]')
                    print 'Received message: ', received_msg.get_attribute('value')
                    waiting_for_answer = False
                except:
                    sleep(10)
                    error_counter += 1
                    print 'Error counter was increased. Error counter = ', error_counter
                    if error_counter > 5:
                        waiting_for_answer = False
                        print 'Error counter  was maximum increased.'
                        break
            if error_counter > 5:
                print 'Aswer was not comming...'
                break
            sent_msg = self.driver.find_element_by_xpath('//XCUIElementTypeTextView[@value="' + sent_message + '"]')
            sent_msg_xy = sent_msg.location
            self.driver.swipe(sent_msg_xy['x'], sent_msg_xy['y'], 0 , sent_msg_xy['y'])
            sleep(2)
            self.driver.find_element_by_id('Delete')
            sleep(5)
            received_msg = self.driver.find_element_by_xpath('//XCUIElementTypeTextView[@value="' + answer + '"]')
            received_msg_xy = received_msg.location
            self.driver.swipe(received_msg_xy['x'], received_msg_xy['y'], 0, received_msg_xy['y'])
            sleep(2)
            self.driver.find_element_by_id('Delete')
        sleep(3)





if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAuto)
    print "SUITE"
    unittest.TextTestRunner().run(suite)

    # unittest.main(testRunner=xmlrunner.XMLTestRunner(output='/Users/galaninaa/test-reports/' ))
    # os.path.dirname(__file__)+'/'+str(folder) + '/' + 'report' +
    # str(datetime.datetime.now().date()))

    # for running with report
    #       runner = xmlrunner.XMLTestRunner()
    #       runner. run(suite)
