# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Задачи на вкладку "В работе"
# Убедиться, что выделена папка "Входящие" и стоит маркер.
# Убедиться, что папка не пустая (в реестре есть задачи)
# Перейти в другую папку, убедиться, что теперь она выделена, а со "Входящие" выделение снято
# Создать новую папку и перейти в неё
# Убедиться, что она пустая
# Удалить новую папку, проверить, что её нет в списке папок


from atf import *
from pages import *


new_folder = 'название папки Михиной'
test_folder = 'для тестирования'


class TestTask2(TestCaseUI):

    def test1(self):
        log('Авторизоваться на сайте https://fix-online.sbis.ru/')
        self.browser.open(task_page_utl)
        auth_page = AuthPage(self.driver)
        auth_page.login.type_in(user_login + Keys.ENTER).should_be(ExactText(user_login))
        auth_page.password.type_in(user_password + Keys.ENTER).should_be(Not(Visible))
        log('Перейти в реестр Задачи на вкладку "В работе"')
        task_page = TaskOnMe(self.driver)
        log('Убедиться, что выделена папка "Входящие" и стоит маркер.')
        task_page.current_folder.should_be(ContainsText('Входящие'))
        task_page.folder_list.item(1).element(task_page.marker).should_be(Visible)
        log('Убедиться, что папка не пустая')
        task_page.tasks_list.should_not_be(Empty, wait_time=3)
        log('Перейти в другую папку')
        task_page.folder_list.item(2).click()
        log('Убедиться, что она выделена')
        task_page.current_folder.should_be(ContainsText(test_folder))
        log("Убедиться, что со входящих выделение снято")
        task_page.folder_list.item(1).element(task_page.marker).should_not_be(Displayed)
        log('Создать новую папку и перейти в нее')
        task_page.new_task_btn.click()
        task_page.add_folder.click()
        task_page.folder_name_input.type_in(new_folder)
        task_page.save_folder_btn.click()
        task_page.folder_list.item(3).click()
        log('Убедиться, что она пустая')
        task_page.tasks_list.should_not_be(RowsNumber(0))
        log('Удалить папку')
        task_page.folder_list.item(3).context_click()
        task_page.folder_menu_list.item(2).click()
        task_page.confirmation_button.item(1).click()
        log('Убедиться, что она удалилась')
        task_page.folder_list.item(3).should_not_be(Present)
