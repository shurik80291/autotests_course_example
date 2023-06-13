# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By


sbis_site = 'https://sbis.ru/'
tensor_site = 'https://tensor.ru/'
tensor_about = 'https://tensor.ru/about'
driver = webdriver.Chrome()
try:
    driver.get(sbis_site)
    assert driver.current_url == sbis_site, 'Не верно открыт сайт'

    contact_btn = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item-1')
    contact_btn_txt = 'Контакты'
    assert contact_btn.text == contact_btn_txt, 'Неверный текст у кнопки "Контакты"'
    assert contact_btn.is_displayed(), 'Кнопка не отображается на странице'
    contact_btn.click()

    banner = driver.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor')
    banner.click()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == tensor_site, 'Открыт неверный сайт'

    news = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content .tensor_ru-Index__card-title')
    assert news.text == 'Сила в людях', 'Нет блока новости "Сила в людях"'

    link = driver.find_element(By.CSS_SELECTOR, '[href="/about"].tensor_ru-link')
    assert link.text == 'Подробнее', 'Неверный текст у кнопки "Подробнее"'
    link.location_once_scrolled_into_view
    link.click()
    assert driver.current_url == tensor_about, 'Открыт неверный адрес сайта'
finally:
    driver.quit()
