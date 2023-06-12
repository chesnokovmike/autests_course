# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from time import sleep

driver = webdriver.Chrome()
web_site = 'https://fix-online.sbis.ru/'
user_login, user_password = 'мирчук', 'мирчук123'
hello_message = 'Привет, Саша Шленский'

try:
    print('Авторизоваться на сайте https://fix-online.sbis.ru/')
    driver.get(web_site)
    sleep(1)
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys(user_login, Keys.ENTER)
    sleep(1)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(user_password, Keys.ENTER)
    sleep(3)
    print('Перейти в реестр Контакты')
    driver.get('https://fix-online.sbis.ru/page/dialogs')
    sleep(2)
    print('Отправить сообщение самому себе')
    new_message_btn = driver.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    new_message_btn.click()
    sleep(1)
    search_area = driver.find_element(By.CSS_SELECTOR,
                                      '.controls-Field.js-controls-Field.controls-InputBase__nativeField.controls'
                                      '-Search__nativeField_caretEmpty.controls'
                                      '-Search__nativeField_caretEmpty_theme_default ')

    search_area.send_keys('Мирчук Михаил')
    sleep(1)
    employee = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-addressee-selector__plain-list-view"]')
    employee.click()
    sleep(1)
    text_editor = driver.find_element(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph')
    text_editor.send_keys(hello_message)
    sleep(1)
    message_send_btn = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
    message_send_btn.click()
    sleep(1)
    messages = driver.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item p')
    print('Убедиться, что сообщение появилось в реестре')
    assert messages[0].text == hello_message
    print('Удалить это сообщение')
    action_chains = ActionChains(driver)
    action_chains.move_to_element(messages[0])
    action_chains.context_click(messages[0])
    action_chains.perform()
    sleep(1)
    menu_btns = driver.find_elements(By.CLASS_NAME, 'controls-Menu__row')
    delete_btn = menu_btns[5]
    delete_btn.click()
    sleep(1)
    print('Убедиться, что сообщение удалилось')
    messages = driver.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item p')
    assert messages[0].text != hello_message
    sleep(1)
    print('Все ок')
finally:
    driver.quit()
