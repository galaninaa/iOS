import unittest
from appium import webdriver
from time import sleep
import TestVariables as tv
import TestMethods as tm

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
        # TM.preLogin(self.driver)

        sleep(5)

    def tearDown(self):
        """Tear down the test"""
        print "##########################################################"
        self.driver.quit()
        print"\n"

    def test_Keypad_Make_a_1000_calls(self):
        test_name = 'Keyapad > Make a 1000 calls'
        print "Test: ", test_name
        sleep(10)
        self.driver.find_element_by_xpath(tv.keypad['xpath']).click()
        sleep(5)
        phone = '3656516221'
        formated_phone = tm.phone_format(phone)
        tm.make_a_call(self.driver, phone)
        for count in range(1000):
            print count
            #tm.call_screen_analizer(self.driver, formated_phone)
            self.driver.find_element_by_accessibility_id(tv.acs.decline).click()
            sleep(2)
            try:
                self.driver.find_element_by_accessibility_id(tv.acs.redial).click()
                print 'True'
                sleep(5)
            except:
                tm.rating_call_screen(self.driver)
                tm.repeat_a_call(self.driver)
        self.driver.find_element_by_accessibility_id(tv.acs.decline).click()

    def test_Keypad_Send_a_1000_Messages(self):
        test_name = 'Keyapad > Send 1000 message'
        print "Test: ", test_name
        sleep(10)
        self.driver.find_element_by_xpath(tv.keypad['xpath']).click()
        sleep(5)
        phone = '3656516221'

        tm.send_a_message_from_keypad(self.driver, phone)
        tm.chat_screen_analizer(self.driver, tm.phone_format(phone))
        for count in range(1000):
            tm.send_message(self.driver, count)
            #sleep(5)
            #tm.find_sended_message(self.driver, count)
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
