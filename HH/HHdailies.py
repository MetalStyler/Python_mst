from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
import traceback
import time

# настройки драйвера
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images":2}
chromeOptions.add_experimental_option("prefs",prefs)
# driver = webdriver.Chrome('C:\\Users\MetalStyler\\PycharmProjects\\my_own\\HH\\chromedriver.exe')
driver = webdriver.Chrome('C:\\Users\MetalStyler\\PycharmProjects\\my_own\\HH\\chromedriver.exe',
                          chrome_options=chromeOptions, desired_capabilities=capa)
# driver.set_window_size(1280, 1024)
# driver.set_window_size(450, 250)
wait = WebDriverWait(driver, 30)

# переходим на сайт, пытаемся отловить и закрыть алерт
driver.get("http://hentaiheroes.com")
try:
    element = wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    print("Алерт пойман и закрыт")
except TimeoutException:
    print("Алерта не было")

# логинимся
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="hh_game"]')))
driver.switch_to.frame(driver.find_element_by_css_selector('#hh_game'))
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="contains_all"]/header/div/a[1]')))
driver.find_element_by_xpath('//*[@id="contains_all"]/header/div/a[1]').click()
driver.find_element_by_xpath('//*[@id="popup_login_form"]/form/div/input[1]').send_keys('metalstyler@gmail.com')
driver.find_element_by_xpath('//*[@id="popup_login_form"]/form/div/input[2]').send_keys('A217427h')
driver.find_element_by_css_selector('#popup_login_form > form > div > div:nth-child(14) > button').click()

# ставим счетчик выполненных дейликов на 0
dailies_count = 0

# переходим к дейликам
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="homepage"]/a[7]/div/span')))
driver.find_element_by_xpath('//*[@id="homepage"]/a[7]/div/span').click()

# проверяем количество денег и монеток
money_amount = driver.find_element_by_xpath('//*[@id="contains_all"]/header/div[6]/div/span').text
coins_amount = driver.find_element_by_xpath('//*[@id="contains_all"]/header/div[7]/div/span').text

# получаем количество дейликов
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="missions"]/div/div[7]')))
quests = driver.find_elements_by_xpath('//*[@id="missions"]/div/div[7]/div[contains(@class, "mission_object")]')
quests = int(len(quests))

try:
    # пытаемся выполнить первый в списке дейлик
    if quests > 0:
        for i in range(0, quests):
            # считаем время на выполнение
            element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="missions"]/div/div[7]/'
                                                                       'div[1]/div[4]/button[1]')))

            m1 = driver.find_element_by_xpath('//*[@id="missions"]/div/div[7]/div[1]/div[4]/button[1]/'
                                              'span/monospace/m[1]')
            m1 = m1.text
            m2 = driver.find_element_by_xpath('//*[@id="missions"]/div/div[7]/div[1]/div[4]/button[1]/'
                                              'span/monospace/m[2]')
            m2 = m2.text
            s1 = driver.find_element_by_xpath('//*[@id="missions"]/div/div[7]/div[1]/div[4]/button[1]/'
                                              'span/monospace/m[3]')
            s1 = s1.text
            s2 = driver.find_element_by_xpath('//*[@id="missions"]/div/div[7]/div[1]/div[4]/button[1]/'
                                              'span/monospace/m[4]')
            s2 = s2.text
            m = int(m1 + m2)
            s = int(s1 + s2)
            print(m, s)
            daily_time = (m * 60) + s
            print(daily_time)
            # стартуем, ждем, завершаем
            driver.find_element_by_xpath('//*[@id="missions"]/div/div[7]/div[1]/div[4]/button[1]').click()
            time.sleep(daily_time+10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="missions"]/div/div[7]/'
                                                                       'div[1]/div[4]/button[3]')))
            driver.find_element_by_xpath('//*[@id="missions"]/div/div[7]/div[1]/div[4]/button[3]').click()
            element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="missions_rewards"]/button')))
            element = wait.until(EC.element_located_to_be_selected((By.XPATH, '//*[@id="missions_rewards"]/button')))
            driver.find_element_by_xpath('//*[@id="missions_rewards"]/button').click()
            # прибавляем 1 к количеству выполненных дейликов
            dailies_count = dailies_count + 1
    else:
        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="missions"]/div/div[6]/button')))
        driver.find_element_by_xpath('//*[@id="missions"]/div/div[6]/button').click()

except Exception as e:
    print('Ошибка:\n', traceback.format_exc())

# # считаем количество полученных денег и монеток
# money_amount2 = driver.find_element_by_xpath('//*[@id="contains_all"]/header/div[6]/div/span').text
# money_got = int(money_amount2) - int(money_amount)
# coins_amount2 = driver.find_element_by_xpath('//*[@id="contains_all"]/header/div[7]/div/span').text
# coins_got = int(coins_amount2) - int(coins_amount)

# # выводим количество выполненных дейликов и полученных денег, монеток
# dailies_count = str(dailies_count)
# print("Выполнено дейликов: " + dailies_count)
# print(money_got)
# print(coins_got)
