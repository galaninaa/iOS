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
  "autoAcceptAlerts" : 'true'}

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

    def test_Keypad(self):
        test_name = 'Keyapad > Tap all keys'
        print "Test: ", test_name
        sleep(10)
        self.driver.find_element_by_xpath(tv.keypad['xpath']).click()
        sleep(5)
        for element in tv.kpd.keypad_elements:
            self.driver.find_element_by_accessibility_id(element).click()
            print element
            self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@value="' + str(element) + '"]')
            self.driver.find_element_by_accessibility_id(tv.kpd.add)
            self.driver.find_element_by_accessibility_id(tv.kpd.delete).click()

    def test_Keypad_Send_Message(self):
        test_name = 'Keyapad > Send message'
        print "Test: ", test_name
        sleep(10)
        self.driver.find_element_by_xpath(tv.keypad['xpath']).click()
        sleep(5)
        phone = '4154960838'
        tm.phone_format(phone)
        tm.send_a_message_from_keypad(self.driver, phone)
        tm.chat_screen_analizer(self.driver, tm.phone_format(phone))
        sleep(3)

    def test_Keypad_Make_a_Call(self):
        test_name = 'Keyapad > Make a call'
        print "Test: ", test_name
        sleep(10)
        self.driver.find_element_by_xpath(tv.keypad['xpath']).click()
        sleep(5)
        phone =  '4154960838'

        tm.make_a_call(self.driver, phone)
        tm.call_screen_analizer(self.driver, tm.phone_format(phone))
        self.driver.find_element_by_accessibility_id(tv.acs.decline).click()

'''
    def test_tmp(self):
        test_name = 'Calls > More Options Validation'
        print "Test: ", test_name

        sleep(2)
        self.driver.find_element_by_xpath(tv.keypad['xpath']).click()
        sleep(1)
        self.driver.find_element_by_xpath(tv.calls['xpath']).click()
        sleep(1)
        self.driver.find_element_by_xpath(tv.contacts['xpath']).click()
        sleep(1)
        self.driver.find_element_by_xpath(tv.settings['xpath']).click()
        sleep(1)
        self.driver.find_element_by_xpath(tv.messages['xpath']).click()
        sleep(10)
        

'''




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
