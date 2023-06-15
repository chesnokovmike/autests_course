# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from atf import log
from time import sleep
from pages import *


hello_message = 'как дела'


class Test(TestCaseUI):

    def test_task_1(self):
        self.browser.open(url_sbis)
        log('Авторизоваться на сайте https://fix-online.sbis.ru/')
        auth_page = AuthPage(self.driver)
        auth_page.login.type_in(user_login + Keys.ENTER).should_be(ExactText(user_login))
        auth_page.password.type_in(user_password + Keys.ENTER).should_be(Not(Visible))
        log('Перейти в реестр Контакты')
        self.browser.open(contact_page_url)
        contacts_page = ContactsPage(self.driver)
        log('Отправить сообщение самому себе')
        contacts_page.new_message_btn.click()
        sleep(1)
        contacts_page.search_area.type_in('мирчук михаил' + Keys.ENTER)
        contacts_page.employee.click()
        contacts_page.text_editor.send_keys(hello_message)
        contacts_page.message_send_btn.click()
        log('Убедиться, что сообщение появилось в реестре')
        contacts_page.messages_list.item(1).should_be(ExactText(hello_message))
        log('Удалить это сообщение')
        contacts_page.messages_list.item(1).context_click()
        contacts_page.menu_btns.item(6).click()
        contacts_page.messages_list.item(1).should_not_be(ExactText(hello_message))
