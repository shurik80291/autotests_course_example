# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from time import sleep


sbis_ru = 'https://fix-online.sbis.ru/'
driver = webdriver.Chrome()
try:
    driver.maximize_window()
    driver.get(sbis_ru)
    sleep(1)

    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys('tosaka', Keys.ENTER)
    assert login.get_attribute('value') == 'tosaka', 'Введен неправильный логин'
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys('tosaka123', Keys.ENTER)
    sleep(7)

    contacts = driver.find_element(By.CSS_SELECTOR, '[name="item-contacts"]')
    contacts.click()
    sleep(1)

    contacts_menu = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle')
    contacts_menu.click()
    sleep(5)

    plus = driver.find_element(By.CSS_SELECTOR, '.icon-RoundPlus')
    plus.click()
    sleep(3)

    search = driver.find_element(By.CSS_SELECTOR, '.controls-StackTemplate__top-area-content input')
    search.send_keys('tosaka rin')
    sleep(3)
    person = driver.find_element(By.CSS_SELECTOR, '[data-qa="person-Information__fio"][title="Tosaka Rin"]')
    person.click()
    sleep(2)
    text = driver.find_element(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph')
    text.send_keys('Тест автотеста')
    send = driver.find_element(By.CSS_SELECTOR, '.icon-BtArrow')
    send.click()
    sleep(2)

    message = driver.find_element(By.CSS_SELECTOR, '.msg-dialogs-item p')
    assert message.text == 'Тест автотеста', 'Сообщение не появилось в реестре'

    action_chains = ActionChains(driver)
    action_chains.move_to_element(message)
    action_chains.perform()
    sleep(1)

    delete = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-itemActions__action deleteToArchive"]')
    delete.click()
    sleep(1)

    message = driver.find_element(By.CSS_SELECTOR, '.msg-dialogs-item p')
    assert message.text != 'Тест автотеста', 'Сообщение не удалилось'
finally:
    driver.quit()
