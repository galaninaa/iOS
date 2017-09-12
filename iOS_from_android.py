import unittest
from appium import webdriver
from time import sleep
import TestVariables as tv
import TestMethods as tm
import speech_recognition as sr

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
        print "I'll waiting incoming call."
        sleep(10)
        count = 0
        bad_counter = 0
        while count < 50:
            try:
                #sleep(10)
                self.driver.find_element_by_accessibility_id('accept').click()
                sleep(2)
                self.driver.find_element_by_xpath(tv.acs.speaker).click()
                print 'This is the call number ', count + 1
                count +=1
                sleep(25)
                self.driver.find_element_by_accessibility_id(tv.acs.call_screen_keypad).click()

                self.driver.find_element_by_accessibility_id(tv.acs.call_screen_keypad).click()
                print ' Call in progress, time of call is:  00:51'
                sleep(25)
                try:
                    self.driver.find_element_by_accessibility_id(tv.acs.decline).click()
                    print ' Call was stooped from outgoing side'
                except:
                    print ' Call was stopped from incoming side'
                bad_counter = 0
            except:
                print 'I\'ll wait the call a few seconds more...'
                sleep(10)
                bad_counter += 1
                if bad_counter > 15:
                    count = 50
                    print ' Bad counter is more that 15. Let\'s stop it!'

        self.driver.find_element_by_accessibility_id(tv.acs.decline).click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAuto)
    print "SUITE"
    unittest.TextTestRunner().run(suite)
