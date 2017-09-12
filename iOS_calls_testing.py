import unittest
from appium import webdriver
from time import sleep
import TestVariables as tv
import TestMethods as tm
import xmlrunner

parser = tm.create_parser()
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
        desired_caps = tv.desired_caps

        self.driver = webdriver.Remote(
            'http://' + str(link) + ':' + str(port) + '/wd/hub', desired_caps)
        print "\n.*....*.*****.*....*....*...*******.*****..****..*******."
        print ".**...*.*......*...*...*.......*....*.....*.........*...."
        print ".*.*..*.*****...*.*.*.*........*....*****..***......*...."
        print ".*..*.*.*.......*.*.*.*........*....*.........*.....*...."
        print ".*...**.*****....*...*.........*....*****.****......*...."
        print self.driver.session_id
        sleep(5)

    def tearDown(self):
        """Tear down the test"""
        print "##########################################################"
        self.driver.quit()
        print"\n"

    def test_Keypad_Make_a_50_calls(self):
        test_name = 'Keyapad > Make a 50calls'
        print "Test: ", test_name
        print "I'll making outgoing call."
        sleep(5)
        self.driver.find_element_by_xpath(tv.keypad['xpath']).click()
        sleep(5)
        phone = '3656516221'
        formated_phone = tm.phone_format(phone)
        tm.make_a_call(self.driver, phone)
        for count in range(50):
            self.driver.find_element_by_xpath(tv.acs.speaker).click()
            print 'This is the call number ', count+1
            #SpeakerModul
            sleep(25)
            self.driver.find_element_by_accessibility_id(tv.acs.call_screen_keypad).click()
            print ' Call in progress, time of call is:  00:25'

            try:
                self.driver.find_element_by_accessibility_id(tv.acs.call_status)
                print ' Let\'s call Alexander!!!!'
            except:
                pass

            sleep(25)
            self.driver.find_element_by_accessibility_id(tv.acs.call_screen_keypad).click()
            print ' Call in progress, time of call is:  00:51'
            sleep(30)

            try:
                self.driver.find_element_by_accessibility_id(tv.acs.decline).click()
                print ' Call was stooped from outgoing side'
            except:
                print ' Call was stopped from incoming side'

            try:
                self.driver.find_element_by_accessibility_id(tv.acs.redial).click()
                print 'Redial is OK'
                sleep(5)
                self.driver.find_element_by_accessibility_id(tv.acs.call_status).click()
            except:
                tm.rating_call_screen(self.driver)
                tm.repeat_a_call(self.driver)
        self.driver.find_element_by_accessibility_id(tv.acs.decline).click()


if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='/Users/builder/PycharmProjects/iOS_tests/test-reports/'))
