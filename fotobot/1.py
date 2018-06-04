from selenium import webdriver
import time
# from selenium.webdriver.common.keys import Keys
import random



# предварительные настройки
driver = webdriver.Chrome()
driver.set_window_size(1600, 900)

# логин
driver.get('https://fotostrana.ru')
time.sleep(2)
driver.find_element_by_css_selector('#header > a.link-text.fl-r.trebuchet.signup-link-login').click()
time.sleep(2)
driver.find_element_by_css_selector('#user_email').send_keys('metalstyler@gmail.com')
driver.find_element_by_css_selector('#user_password').send_keys('A217427h')
driver.find_element_by_css_selector('#loginPopupSubmitButton').click()
time.sleep(2)

# закрываем поп-апы
try:
    driver.find_element_by_css_selector('#iPopup > div > div > div.payable-dating-pack-close.tr-opacity-03 > i').click()
except:
    pass


# если вдруг опять вылезла сраная анкета:
try:
    # driver.find_element_by_css_selector('#steps-result-inputs > div.fs-row.fs-row_align-items-end > div > div > div > div:nth-child(1) > div').click()
    # time.sleep(1)
    # driver.find_element_by_css_selector('#steps-result-inputs > div.fs-row.fs-row_align-items-end > div > div > div > div:nth-child(1) > div').click()
    # time.sleep(1)
    # driver.find_element_by_css_selector('#steps-result-inputs > div.fs-row.fs-row_align-items-end > div > div > div > div:nth-child(5) > div').click()
    # time.sleep(1)
    # driver.find_element_by_css_selector('#steps-result-inputs > div.fs-row.fs-row_align-items-end > div > div > div > div:nth-child(2) > div').click()
    # time.sleep(1)
    # driver.find_element_by_css_selector('#steps-result-inputs > div.fs-row.fs-row_align-items-end > div > div > div > div:nth-child(4) > div').click()
    # time.sleep(1)
    # driver.find_element_by_css_selector('#steps-result-inputs > div.fs-row.fs-row_align-items-end > div > div > div > div:nth-child(5) > div').click()
    # time.sleep(1)
    # driver.find_element_by_css_selector('#steps-result-inputs > div.fs-row.fs-row_align-items-end > div > div > div > div:nth-child(3) > div').click()
    # time.sleep(2)
    driver.find_element_by_css_selector('#steps-result-inputs > div.user-info-form-box-footer > div > div > a').click()
    # driver.execute_script("""$('#steps-result-inputs > div.fs-row.fs-row_align-items-end > div > div > div > div:nth-child(2)').click();""")
    time.sleep(2)
except:
    pass

# открываем игру "кафе знакомств"
# driver.find_element_by_css_selector('#header > a:nth-child(4)').click()
driver.get('https://fotostrana.ru/play/')
time.sleep(1)
driver.find_element_by_css_selector('#fs-play-search > input').send_keys('Кафе')
time.sleep(2)
driver.find_element_by_css_selector('#fspc_search-result > div > div > ul > li > div.fspc_apps-item-content > div.fspc_apps-item-title > a').click()
time.sleep(2)

try:
    driver.find_element_by_css_selector('#iPopup > div > div > div > div.cafe-popup-cross').click()
except:
    pass

# кликаем по произвольной фотке:
time.sleep(2)
for i in range(1, 100000000):
    a = random.randint(1, 2)
    if a == 1:
        driver.find_element_by_css_selector('#cafe-content > div > div.cafe-main.js-pair >'
                                            ' div > div.cafe-users.js-pair-users > div:nth-child(3) > '
                                            'div.cafe-user-photo > div').click()
        try:
            driver.find_element_by_css_selector('#iPopup > div > div > div > div.cafe-popup-cross').click()
            time.sleep(2)
        except:
            pass
    else:
        driver.find_element_by_css_selector('#cafe-content > div > div.cafe-main.js-pair > '
                                            'div > div.cafe-users.js-pair-users > div:nth-child(2) > '
                                            'div.cafe-user-photo > div').click()
        try:
            driver.find_element_by_css_selector('#iPopup > div > div > div > div.cafe-popup-cross').click()
            time.sleep(2)
        except:
            pass
