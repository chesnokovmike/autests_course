# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Задачи на вкладку "В работе"
# Убедиться, что выделена папка "Входящие" и стоит маркер.
# Убедиться, что папка не пустая (в реестре есть задачи)
# Перейти в другую папку, убедиться, что теперь она выделена, а со "Входящие" выделение снято
# Создать новую папку и перейти в неё
# Убедиться, что она пустая
# Удалить новую папку, проверить, что её нет в списке папок


from atf.ui import *
from atf import log
from selenium.webdriver.common.by import By
from time import sleep

task_page_utl = 'https://fix-online.sbis.ru/page/tasks-in-work'
user_login = 'мирчук'
user_password = 'мирчук123'
new_folder = 'название папки Михиной'
class Task_on_me(Region):
    current_folder = Element(By.CSS_SELECTOR, '.controls-Grid__row-cell_selected__first-master')
    tasks_list = Table(By.CSS_SELECTOR, '.edo3-Browser-view')
    folder_list = CustomList(By.CSS_SELECTOR, '.controls-Grid__cell_master')
    new_task_btn = Button(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    add_folder = Button(By.CSS_SELECTOR, '[key="list-render-folderItem"]')
    folder_name_input = Element(By.CSS_SELECTOR, '.controls-Popup [data-qa="controls-Render__field"]')
    # TextField(By.CSS_SELECTOR, ".controls-Popup input.controls-Field", 'Поле ввода названия')
    # create_folder.folder_input.type_in(user_login)
    save_folder_btn = Button(By.CSS_SELECTOR, '.controls-Popup .controls-BaseButton')

class AuthPage(Region):
    login = TextField(By.CSS_SELECTOR, '[name="Login"]')
    password = TextField(By.CSS_SELECTOR, '[name="Password"]')

class TestTask2(TestCaseUI):


    def test1(self):
        log('Авторизоваться на сайте https://fix-online.sbis.ru/')
        self.browser.open(task_page_utl)
        auth_page = AuthPage(self.driver)
        auth_page.login.type_in(user_login + Keys.ENTER).should_be(ExactText(user_login))
        auth_page.password.type_in(user_password + Keys.ENTER).should_be(Not(Visible))
        log('Перейти в реестр Задачи на вкладку "В работе"')
        task_page = Task_on_me(self.driver)
        log('Убедиться, что выделена папка "Входящие" и стоит маркер.')
        task_page.current_folder.should_be(ContainsText('Входящие'))
        log('Убедиться, что папка не пустая')
        task_page.tasks_list.should_not_be(RowsNumber(0))
        log('Перейти в другую папку')
        task_page.folder_list.item(2).click()
        log('Убедиться, что она выделена')
        task_page.current_folder.should_be(ContainsText('для тестирования'))
        # доделать "убедиться, что со входящих выделение снято
        log('Создать новую папку и перейти в нее')
        task_page.new_task_btn.click()
        task_page.add_folder.click()
        task_page.folder_name_input.send_keys(new_folder)
        sleep(5)
        task_page.save_folder_btn.click()
        print('чет получилось')
