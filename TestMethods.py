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

'''
def open_settings(driver):
    print "Let's open Settings"
    m_o = find_life_or_dead(tv.more_options, driver)
    m_o.click()
    print "     More Options was tapped"
    sleep(4)
    settings = find_life_or_dead(tv.More_Options.settings, driver)
    settings.click()
    print "     Settings was tapped"
    sleep(4)
    get_header(driver)
    scroll_view = find_life_or_dead(tv.Settings.settings_scroll_view_container, driver)
    print "ScrollView is on screen"

    account_data = [tv.Settings.account_data, tv.Settings.account_name, tv.Settings.account_email,
                    tv.Settings.account_phone]
    for element in account_data:
        on_screen = find_life_or_dead(element, driver)
        print "Element ", element, " with text ", on_screen.text, " is on screen"

def tap_on_settings_items(item,driver,path):
    # item - is key from TV.Settings.MenuItems
    all_settings_elements = give_all_path(path)
    element = driver.find_element_by_xpath(all_settings_elements[item])
    print "Element ", all_settings_elements[item], " with text ", element.text, " is on screen"
    element.click()
    print "Element was clicked"

def get_header(driver):
    header = find_life_or_dead(tv.Settings.header, driver)
    print "header: ", header.text, " is on screen"

def tap_tone(tones, driver):
    print "Let's tap tone!"
    tones_list = give_all_path(tones, 'RadioButton')
    print tones_list
    for tone in tones_list:
        print tone
        driver.find_element_by_xpath(tones_list[tone]).click()
        sleep(0.5)
    driver.find_element_by_xpath(tones_list[tones[1]]).click()

def give_all_path(menu_items, item_type ='TextView'):
    all = {}
    for all_element in menu_items:
        all[all_element] = '//android.widget.'+item_type+'[@text="' + all_element + '"]'
    return all

def parse_all_elevents(driver,type):
    pathes = []
    xml = str(driver.page_source).format(unicode)
    tree = etree.parse(StringIO(xml))
    elements = tree.xpath(
        '//android.widget.' + type)


    print elements
    for element in elements:
        pathes.append(tree.getpath(element))
    return pathes
'''

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