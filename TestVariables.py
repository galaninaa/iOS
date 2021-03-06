
import ActiveCallScreen as acs
import Keypad as kpd
import ChatScreen as cs

app_path = '/Users/galaninaa/Downloads/TalkMeIMBeta\ 5.7.0-9115.42.ipa'
#  'C:\\PyCharmProj\\talkatoneAndroid-5.6.4-rc4.apk'

account_data = {'email': 'anton+iOSAuto1@talkme.im', 'number': '7013692306', 'name': 'Anton iOSAuto1'}

calls = {'accessibility id': '', 'xpath': '//XCUIElementTypeButton[@name="Calls" and @x > 0]', 'text': ''}
messages = {'accessibility id': '', 'xpath': '//XCUIElementTypeButton[@name="Messages" and @x > 0]',
            'text': ''}
contacts = {'accessibility id': '', 'xpath': '//XCUIElementTypeButton[@name="Contacts" and @x > 0]',
            'text':'' }
keypad = {'accessibility id': '', 'xpath': '//XCUIElementTypeButton[@name="Keypad" and @x > 0]',
             'text': ''}


settings = {'accessibility id': '', 'xpath': '//XCUIElementTypeButton[@name="Settings" and @x > 0]',
             'text': ''}

make_call = 'make call'
text_message = 'text message'

desired_caps = {"udid":
                    #"cc1257db6dd070e229924b58a92bf51e12f93129",
                        'ec21a45af61f2d7c54658008724b590017d2413f',
                        "platformName": "iOS",
                        "bundleId": "im.talkme.talkmeim",
                        "deviceName": "Anton's iPhone",
                        "automationName": "XCUITest",
                        "autoAcceptAlerts": 'true'}