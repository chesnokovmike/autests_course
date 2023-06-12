# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory': 'D:\\autotest_course\Homework11'}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)

try:
    print('Перейти на  https://sbis.ru/')
    driver.get('https://sbis.ru/')
    sleep(1)
    print('В Footer e найти "Скачать СБИС"')
    footer_links = driver.find_elements(By.CLASS_NAME, 'sbisru-Footer__link')
    download_sbis = footer_links[39]
    print('Перейти по ней')
    driver.execute_script("return arguments[0].scrollIntoView(true);", download_sbis)

    download_sbis.click()
    sleep(1)
    sbis_plugin = driver.find_element(By.CSS_SELECTOR, '[data-id="plugin"]')
    sbis_plugin.click()
    sleep(1)
    download_link = driver.find_element(By.CSS_SELECTOR,
                                        '[href="https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]')
    download_link.click()


finally:
    driver.quit()