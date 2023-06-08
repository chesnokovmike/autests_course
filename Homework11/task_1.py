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
    driver.get(url_sbis)
    sleep(1)
    contacts_btn = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item [href="/contacts"]')
    contacts_btn.click()
# .sbisru-Contacts__logo-tensor.mb-8
finally:
    driver.quit()
