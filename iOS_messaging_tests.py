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
        test_name = 'Keyapad > Send 50 message'
        print "Test: ", test_name
        sleep(10)

        sleep(5)
        phone = '3656516221'
        print'We will send messages to ', phone
        print'But in first: Let\'s clear messages history'
        self.driver.find_element_by_xpath(tv.settings['xpath']).click()
        print'Settings was tapped'
        sleep(10)
        #--Clear messages history-
        action = TouchAction(self.driver)
        start_scroll = self.driver.find_element_by_accessibility_id('Off')
        end_scroll = self.driver.find_element_by_accessibility_id('Get a New Number')
        show_delete = action.press(start_scroll).wait(300).move_to(end_scroll).release()
        show_delete.perform()
        print' Settings screen was scrolled'
        sleep(2)
        self.driver.find_element_by_accessibility_id('History').click()
        print'History was tapped'
        sleep(2)
        self.driver.find_element_by_accessibility_id('Clear Messages History').click()
        print'Clear Messages History was tapped'
        sleep(2)
        self.driver.find_element_by_accessibility_id('Delete').click()
        print'Clear was accepted'
        sleep(2)
        self.driver.find_element_by_accessibility_id('Settings').click()
        print'Back to Settings was tapped'
        sleep(2)
        # ----------------------
        self.driver.find_element_by_xpath(tv.keypad['xpath']).click()
        print'Keypad was tapped'
        tm.send_a_message_from_keypad(self.driver, phone)
        print'Message Scree was opened from Keypad'
        print'Let\'s analize chat screen...'
        tm.chat_screen_analizer(self.driver, tm.phone_format(phone))
        message_text = 'This is the message '
        for count in range(50):
            sent_message = message_text + str(count)
            tm.send_message(self.driver, sent_message)
            print'Message '+sent_message+' was sent'
            sleep(10)
            sent_msg = self.driver.find_element_by_xpath('//XCUIElementTypeTextView[@value="' + sent_message + '"]')
            print "Sent messages: ", sent_msg.get_attribute('value')
            answer = sent_message + ' answer'
            waiting_for_answer = True
            error_counter = 0
            while waiting_for_answer == True:
                try:
                    print 'I\'ll wait incoming message with text: ',answer
                    sleep(5)
                    received_msg = self.driver.find_element_by_xpath('//XCUIElementTypeTextView[@value="' + answer + '"]')
                    print 'Received message: ', received_msg.get_attribute('value')
                    action = TouchAction(self.driver)
                    print 'Let\'s scroll chat!'
                    end_scroll = self.driver.find_element_by_accessibility_id(tv.cs.back)
                    print 'Back button was found'
                    xy = end_scroll.location
                    print 'Back button location', xy
                    show_delete = action.press(x=xy['x'],y=204).wait(300).move_to(end_scroll).release()
                    show_delete.perform()
                    #self.driver.drag_and_drop(start_scroll,end_scroll)
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
                self.driver.find_element_by_accessibility_id('Keypad').click()
                sleep(2)
                self.driver.find_element_by_accessibility_id(tv.settings['xpath']).click()
                sleep(2)
                action = TouchAction(self.driver)
                start_scroll = self.driver.find_element_by_accessibility_id('Off')
                end_scroll = self.driver.find_element_by_accessibility_id('Get a New Number')
                show_delete = action.press(start_scroll).wait(300).move_to(end_scroll).release()
                show_delete.perform()
                sys.exit(1)
        sleep(3)

if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='/Users/builder/PycharmProjects/iOS_tests/test-reports/'))
