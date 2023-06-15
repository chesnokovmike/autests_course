# Предварительные действия (Создайте эталонную задачу, заполнив обязательные поля)
# Авторизоваться на сайте https://fix-online.sbis.ru/
# Откройте эталонную задачу по прямой ссылке в новом окне
# Убедитесь, что в заголовке вкладки отображается "Задача №НОМЕР от ДАТА",где ДАТА и НОМЕР - это ваши эталонные значения
# Проверьте, что поля: Исполнитель, дата, номер, описание и автор отображаются с эталонными значениями


from atf import *
from pages import *


class TestTaskWithStar(TestCaseUI):

    def test1(self):
        log('Авторизоваться на сайте https://fix-online.sbis.ru/')
        self.browser.open(etalon_task_url)
        auth_page = AuthPage(self.driver)
        auth_page.login.type_in(user_login + Keys.ENTER).should_be(ExactText(user_login))
        auth_page.password.type_in(user_password + Keys.ENTER).should_be(Not(Visible))
        task_new_window = TaskNewWindow(self.driver)
        self.browser.should_be(TitleContains(f'Задача №{task_number} от {task_date}'))
        task_new_window.date_number.should_be(ContainsText('231'), ContainsText('15 июн, чт'))
        task_new_window.task_text_editor.should_be(ContainsText('Эталонная задача, не трогать!'))
        task_new_window.sticker.should_be(ContainsText('Мирчук Михаил'))
