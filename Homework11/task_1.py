# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
url_sbis = 'https://sbis.ru'

try:
    print('Перейти на сайт https://sbis.ru/')
    driver.get(url_sbis)
    sleep(1)

    print('Перейти в раздел "Контакты"')
    contacts_btn = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item [href="/contacts"]')
    contacts_btn.click()
    sleep(1)

    print('Найти баннер Тензор, кликнуть по нему, перейти на https://tensor.ru')
    banner = driver.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor.mb-8')
    banner.click()
    driver.switch_to.window((driver.window_handles[1]))
    sleep(1)

    print('Проверить, что есть блок новости "Сила в людях"')
    news_banners = driver.find_elements(By.CLASS_NAME, 's-Grid-col')
    news = news_banners[7]

    print('Перейти в блоке "Сила в людях" по ссылке "Подробнее"')
    about_btn = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__card-text [href="/about"]')
    driver.execute_script("return arguments[0].scrollIntoView(true);", about_btn)
    sleep(1)

    about_btn.click()
    sleep(3)

    print('Проверить, что открылась страница "https://tensor.ru/about"')
    assert driver.current_url == 'https://tensor.ru/about'

finally:
    driver.quit()
