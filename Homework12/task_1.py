# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста
import time

from atf.ui import *
from atf import log, info
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


url_sbis = 'https://fix-online.sbis.ru'
contact_page = 'https://fix-online.sbis.ru/page/dialogs'
user_login = 'мирчук'
user_password = 'мирчук123'
hello_message = 'Привет, Саша Шленский'


class AuthPage(Region):
    login = TextField(By.CSS_SELECTOR, '[name="Login"]')
    password = TextField(By.CSS_SELECTOR, '[name="Password"]')


class ContactsPage(Region):
    new_message_btn = Button(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    search_area = TextField(By.CSS_SELECTOR, '.controls-Field.js-controls-Field.controls-InputBase__nativeField.controls'
                                          '-Search__nativeField_caretEmpty.controls'
                                          '-Search__nativeField_caretEmpty_theme_default')
    employee = Button(By.CSS_SELECTOR, '[data-qa="msg-addressee-selector__plain-list-view"]')
    text_editor = TextField(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph')
    message_send_btn = Button(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
    messages_list = CustomList(By.CSS_SELECTOR, '.msg-dialogs-item p')


class Test(TestCaseUI):

    def test_task_1(self):
        self.browser.open(url_sbis)
        log('Авторизоваться на сайте https://fix-online.sbis.ru/')
        auth_page = AuthPage(self.driver)
        auth_page.login.type_in(user_login + Keys.ENTER).should_be(ExactText(user_login))
        auth_page.password.type_in(user_password + Keys.ENTER).should_be(Not(Visible))
        log('Перейти в реестр Контакты')
        self.browser.open(contact_page)
        contacts_page = ContactsPage(self.driver)
        log('Отправить сообщение самому себе')
        contacts_page.new_message_btn.click()
        time.sleep(1)
        # search_area = driver.find_element(By.CSS_SELECTOR,
        #                                   '.controls-Field.js-controls-Field.controls-InputBase__nativeField.controls'
        #                                   '-Search__nativeField_caretEmpty.controls'
        #                                   '-Search__nativeField_caretEmpty_theme_default ')
        #
        # search_area.send_keys('Мирчук Михаил')
        contacts_page.search_area.type_in('мирчук михаил' + Keys.ENTER)
        sleep(1)
        # employee = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-addressee-selector__plain-list-view"]')
        contacts_page.employee.click()
        sleep(1)
        # employee.click()
        # sleep(1)
        # text_editor = driver.find_element(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph')
        contacts_page.text_editor.type_in(hello_message)
        # text_editor.send_keys(hello_message)
        sleep(1)
        # message_send_btn = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
        # message_send_btn.click()
        contacts_page.message_send_btn.click()
        # sleep(1)
        # messages = driver.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item p')
        log('Убедиться, что сообщение появилось в реестре')
        contacts_page.messages_list[0].should_be(ContainsText(hello_message))
        sleep(1)
        # assert messages[0].text == hello_message
        # print('Удалить это сообщение')
        # action_chains = ActionChains(driver)
        # action_chains.move_to_element(messages[0])
        # action_chains.context_click(messages[0])
        # action_chains.perform()
        # sleep(1)
        # menu_btns = driver.find_elements(By.CLASS_NAME, 'controls-Menu__row')
        # delete_btn = menu_btns[5]
        # delete_btn.click()
        # sleep(1)
        # print('Убедиться, что сообщение удалилось')
        # messages = driver.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item p')
        # assert messages[0].text != hello_message
        # sleep(1)
        # print('Все ок')
