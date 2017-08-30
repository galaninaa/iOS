import unittest
from appium import webdriver
import argparse

from time import sleep
import TestVariables as tv
import TestMethods as tm





def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--device_name',
                        default='84B7N16804000866')
    parser.add_argument('-pl', '--platform', default='iOS')
    parser.add_argument('-l', '--link', default='192.168.82.87')
    parser.add_argument('-p', '--port', default='4728')
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
        desired_caps = {"udid": "cc1257db6dd070e229924b58a92bf51e12f93129",
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
        try:
            self.driver.find_element_by_id('Cancel')
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
        sleep(5)
        self.driver.find_element_by_xpath(tv.keypad['xpath']).click()
        sleep(5)
        phone = '3656516221'

        tm.send_a_message_from_keypad(self.driver, phone)
        #tm.chat_screen_analizer(self.driver, tm.phone_format(phone))
        message_text = 'This is the message 0'

        sent_message = message_text

        sleep(5)
        sent_msg = self.driver.find_element_by_xpath('//XCUIElementTypeTextView[@value="' + sent_message + '"]')
        sent_msg_xy = sent_msg.location
        print sent_msg_xy
        y = int(sent_msg_xy['y'])+1 # "y" coordinate of time stamp bubble
        end_scroll_xpath = '//XCUIElementTypeStaticText[@y="' + str(y) + '"]'



        #self.driver.swipe(  int(sent_msg_xy['x']), int(sent_msg_xy['y']),  ,  int(sent_msg_xy['y']) )
        #self.driver.swipe(start_x=100,start_y=100,end_x=1,end_y=100)
        #print ' r to l'
        #sleep(10)
        #self.driver.swipe(start_x=-100, start_y=1, end_x=1, end_y=1)
        #print ' l to r'

        #self.driver.swipe(start_x=100, start_y=1, end_x=100, end_y=100)
        #print ' u to d'
        #sleep(10)
        #self.driver.swipe(start_x=100, start_y=100, end_x=100, end_y=1)
        #print ' d to u'

        sleep(5)
        self.driver.find_element_by_id('Delete')





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
