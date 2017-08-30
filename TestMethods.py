from time import sleep
import TestVariables as tv


def find_life_or_dead(victim, driver):
    print victim.keys()
    element = None
    print 'Let\'s find: ', victim
    for keys in victim.keys():
        if keys == 'id':
            try:
                element = driver.find_element_by_id(victim[keys])
                print "     Find  by id"
                break
            except:
                print "     Could not find by id..."
        if keys == 'xpath':
            try:
                element = driver.find_element_by_xpath(victim[keys])
                print "     Find by xpath"
                break
            except:
                print "     Could not find by xpath..."
        if keys == 'accessibility id':
            try:
                element = driver.find_element_by_accessibility_id(victim[keys])
                print "     Find by accessibility id"
                break
            except:
                print "     Could not find by accessibility id..."
    return element


def phone_format(phone):
    phone = str(phone)
    result = '(' + phone[0:3] + ') ' + phone[3:6] + '-' + phone[6:]
    return result

def make_a_call(driver, number):
    # Number is a string
    number = str(number)
    for element in number:
        driver.find_element_by_accessibility_id(element).click()

    driver.find_element_by_accessibility_id(tv.make_call).click()
    sleep(5)

def repeat_a_call(driver):
    # Number is a string

    driver.find_element_by_accessibility_id(tv.make_call).click()
    sleep(1)
    driver.find_element_by_accessibility_id(tv.make_call).click()



def send_a_message_from_keypad(driver, number):
    # Send message from Keypad screen
    # This method is opened New Chat screen from Keypad to selected number

    for element in number:
        driver.find_element_by_accessibility_id(element).click()
    driver.find_element_by_accessibility_id(tv.text_message).click()
    sleep(5)

def call_screen_analizer(driver, phone):
    driver.find_element_by_accessibility_id(tv.acs.call_status)
    print tv.acs.call_status + " was found"
    driver.find_element_by_accessibility_id(tv.acs.conection_type)
    print tv.acs.conection_type + " was found"
    driver.find_element_by_accessibility_id(str(phone))
    print str(phone) + " was found"
    driver.find_element_by_accessibility_id(tv.acs.mute_off)
    print tv.acs.mute_off + " was found"
    driver.find_element_by_accessibility_id(tv.acs.dialpad)
    print tv.acs.dialpad + " was found"
    driver.find_element_by_xpath(tv.acs.speaker)
    print tv.acs.speaker + " was found"
    driver.find_element_by_xpath(tv.acs.hold)
    print tv.acs.hold + " was found"
    driver.find_element_by_accessibility_id(tv.acs.mute)
    print tv.acs.mute + " was found"
    driver.find_element_by_accessibility_id(tv.acs.call_screen_keypad)
    print tv.acs.call_screen_keypad + " was found"
    driver.find_element_by_xpath(tv.acs.speaker_text)
    print tv.acs.speaker_text + " was found"
    driver.find_element_by_xpath(tv.acs.hold_text)
    print tv.acs.hold_text + " was found"
    driver.find_element_by_accessibility_id(tv.acs.decline)
    print tv.acs.decline + " was found"

def chat_screen_analizer(driver, phone_number):
    driver.find_element_by_accessibility_id(tv.cs.keypad)
    print tv.cs.keypad + " was found"
    driver.find_element_by_accessibility_id(tv.cs.back)
    print tv.cs.back + " was found"
    driver.find_element_by_accessibility_id(tv.cs.more_info)
    print tv.cs.more_info + " was found"
    #driver.find_element_by_accessibility_id(phone_number)
    #print phone_number + " was found"
    driver.find_element_by_accessibility_id(tv.cs.camera)
    print tv.cs.camera + " was found"
    driver.find_element_by_accessibility_id(tv.cs.sticker)
    print tv.cs.sticker + " was found"
    driver.find_element_by_accessibility_id(tv.cs.send)
    print tv.cs.send + " was found"
    driver.find_element_by_xpath(tv.cs.send_message_text_field)
    print tv.cs.more_info + " was found"

def find_sended_message(driver, text):
    text_field = driver.find_element_by_xpath('//XCUIElementTypeTextView')
    #print text_field.get('value')
    driver.find_element_by_xpath('//XCUIElementTypeTextView[@value="' + str(text) + '"]')

def send_message(driver, text):
    field = driver.find_element_by_xpath(tv.cs.send_message_text_field).send_keys(text)
    #field.click()
    #field.set_value(str(text))
    driver.find_element_by_accessibility_id(tv.cs.send).click()

def rating_call_screen(driver):
    sleep(6)
    driver.find_element_by_accessibility_id('Close').click()