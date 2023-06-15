from atf.ui import *


user_login = 'мирчук'
user_password = 'мирчук123'
url_sbis = 'https://fix-online.sbis.ru'
contact_page_url = 'https://fix-online.sbis.ru/page/dialogs'
task_page_utl = 'https://fix-online.sbis.ru/page/tasks-in-work'
etalon_task_url = 'https://fix-online.sbis.ru/opendoc.html?guid=cd75e424-987a-449c-b8c4-0d446d4cdcfd&client=6255711'
task_number, task_date = '231', '15.06.23'
etalon_executor = 'Мирчук Михаил'


class AuthPage(Region):
    login = TextField(By.CSS_SELECTOR, '[name="Login"]')
    password = TextField(By.CSS_SELECTOR, '[name="Password"]')


class ContactsPage(Region):
    new_message_btn = Button(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    search_area = TextField(By.CSS_SELECTOR, '.controls-Field')
    employee = Button(By.CSS_SELECTOR, '[data-qa="msg-addressee-selector__plain-list-view"]')
    text_editor = TextField(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph')
    message_send_btn = Button(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
    messages_list = CustomList(By.CSS_SELECTOR, '.msg-dialogs-item p')
    menu_btns = CustomList(By.CLASS_NAME, 'controls-Menu__row')


class TaskOnMe(Region):

    current_folder = Element(By.CSS_SELECTOR, '.controls-Grid__row-cell_selected__first-master')
    marker = '.controls-ListView__itemV_marker'
    tasks_list = Table(By.CSS_SELECTOR, '.edo3-Browser-view')
    folder_list = CustomList(By.CSS_SELECTOR, '.controls-Grid__cell_master')
    new_task_btn = Button(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    add_folder = Button(By.CSS_SELECTOR, '[key="list-render-folderItem"]')
    folder_name_input = TextField(By.CSS_SELECTOR, '.controls-Popup input.controls-Field')
    save_folder_btn = Button(By.CSS_SELECTOR, '.controls-DialogTemplate__top-area-content .controls-BaseButton')
    folder_menu_list = CustomList(By.CSS_SELECTOR, '.controls-Menu__row')
    confirmation_button = CustomList(By.CSS_SELECTOR, '.controls-ConfirmationDialog__button-standard')


class TaskNewWindow(Region):
    executor = Element(By.CSS_SELECTOR, '.controls-SelectedCollection__item__caption-wrapper')
    date_number = Element(By.CSS_SELECTOR, '.edo3-DateNumber')
    task_text_editor = Element(By.CSS_SELECTOR, '.richEditor_richContentRender')
    sticker = Element(By.CSS_SELECTOR, '[data-qa="edo3-Sticker__mainInfo"]')
