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
        sleep(5)
        self.driver.find_element_by_xpath(tv.keypad['xpath']).click()
        sleep(5)
        phone = '3656516221'
        formated_phone = tm.phone_format(phone)
        tm.make_a_call(self.driver, phone)
        for count in range(50):
            print 'This is the call number ', count+1, ' is in progress...'
            #SpeakerModul
            r = sr.Recognizer()
            with sr.Microphone(device_index=0) as source:
                audio = r.listen(source)

                try:
                    print("You said :" + r.recognize_google(audio))
                    #speaches.append(str(r.recognize_google(audio)))

                except:
                    pass

            self.driver.find_element_by_accessibility_id(tv.acs.decline).click()

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
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAuto)
    print "SUITE"
    unittest.TextTestRunner().run(suite)
