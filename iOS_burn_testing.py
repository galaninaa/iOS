import unittest
from appium import webdriver
from time import sleep
import TestVariables as tv
import TestMethods as tm
from appium.webdriver.common.touch_action import TouchAction
import sys
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
        try:
            self.driver.find_element_by_id('Cancel').click()
        except:
            pass

    def tearDown(self):
        """Tear down the test"""
        print "##########################################################"
        self.driver.quit()
        print"\n"

    def test_Keypad_Send_a_50_Messages(self):
        test_name = 'Burn > Burn 50 times'
        print "Test: ", test_name
        sleep(10)
        for count in range(50):
            print 'STEP ', count+1
            settings = self.driver.find_element_by_xpath(tv.settings['xpath'])
            settings.click()
            print 'Settings was tapped'
            sleep(2)
            burn_screen = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="Button" and @x < 300]')
            burn_screen.click()
            print 'Burn button was tapped'
            sleep(10)
            try:
                burn_now = self.driver.find_element_by_accessibility_id('Burn now')
                burn_now.click()
                print 'Burn Now was tapped'
            except:
                buy = self.driver.find_element_by_accessibility_id('Buy')
                buy.click()
                print 'Burn Now was tapped'
            sleep(5)
            self.driver.switch_to.alert.accept()
            #burn_now_banner = self.driver.find_element_by_accessibility_id('Burn now')
            #burn_now_banner.click()
            print 'Burn Now on banner was tapped'
            sleep(15)
            #self.driver.switch_to.alert.send_keys('BuyStuff1')
            try:
                self.driver.find_element_by_xpath('//XCUIElementTypeAlert[@name="Sign-In Required"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeSecureTextField').send_keys('BuyStuff1')
                print 'Password was added'
                self.driver.switch_to.alert.accept()
                print 'Allert was accepted with password'
            except:
                self.driver.switch_to.alert.accept()
                print 'Allert was accepted without password'
            sleep(10)
            try:
                self.driver.switch_to.alert.accept()
                print 'Buy button was tapped'
            except:
                print 'Buy button wasn\'t shown'
            sleep(10)
            self.driver.find_element_by_accessibility_id('OK').click()
            print 'OK was tapped on banner "You\'re on set"'
            sleep(25)

            static_text = self.driver.find_elements_by_xpath('//XCUIElementTypeStaticText')
            for el in static_text:
                print el.get_attribute('name')
            get_number = self.driver.find_element_by_accessibility_id('Get Number')
            get_number.click()
            print 'Get number was tapped'
            sleep(10)
            self.driver.find_element_by_accessibility_id('OK').click()
            print '911 OK was tapped'
            sleep(25)



if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='/Users/builder/PycharmProjects/iOS_tests/test-reports/'))
