from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
# driver.set_window_size(1280, 1024)

# переходим на сайт, логинимся`
driver.get("http://hentaiheroes.com")
time.sleep(2)
driver.switch_to.alert.accept()
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//iframe[@id="hh_game"]')))
driver.switch_to.frame(driver.find_element_by_xpath('/iframe[@id="hh_game"]'))
driver.find_element_by_xpath('//*[@id="contains_all"]/header/div/a[1]').click()
driver.find_element_by_xpath('//*[@id="popup_login_form"]/form/div/input[1]').send_keys('metalstyler@gmail.com')
driver.find_element_by_xpath('//*[@id="popup_login_form"]/form/div/input[2]').send_keys('A217427h')
driver.find_element_by_css_selector('#popup_login_form > form > div > div:nth-child(14) > button').click()

# переходим к актуальному противнику через продолжение квеста
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="homepage"]/a[4]')))
driver.find_element_by_xpath('//*[@id="homepage"]/a[4]').click()
element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#breadcrumbs > a:nth-child(5)')))
driver.find_element_by_css_selector('#breadcrumbs > a:nth-child(5)').click()

# проводим файты
for i in range(1, 20):
    try:

        # стартуем файт и скипаем бой
        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="worldmap"]/a[8]')))
        driver.find_element_by_xpath('//*[@id="worldmap"]/a[8]').click()
        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="battle_middle"]/button[1]')))
        driver.find_element_by_xpath('//*[@id="battle_middle"]/button[1]').click()
        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="battle_middle"]/button[2]')))
        driver.find_element_by_xpath('//*[@id="battle_middle"]/button[2]').click()

        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[id="battle_win"]/'
                                                                   'button[@class="blue_text_button"][text()=" Ok "]')))
        driver.find_element_by_xpath('//div[id="battle_win"]/button[@class="blue_text_button"][text()=" Ok "]')

    except:
        print("Вся энергия потрачена или ошибка скрипта")
        driver.close()
