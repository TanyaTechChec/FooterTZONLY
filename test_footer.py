from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Список страниц для проверки
urls = [
    "https://only.digital/",
    "https://only.digital/projects",
    "https://only.digital/company"
]

# Создание драйвера
driver = webdriver.Chrome()

# Проверка футера на каждой странице
for url in urls:
    driver.get(url)
    try:
        # Ожидание футера
        footer = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'footer'))
        )

        print(footer.get_attribute('outerHTML'))

        # Попробуем найти элемент в футере
        email_element = footer.find_element(By.LINK_TEXT, "hello@only.com.ru")
        assert email_element.is_displayed(), "Email не отображается в футере."
        print(f"На странице {url} элемент 'hello@only.com.ru' найден в футере.")

    except Exception as e:
        print(f"На странице {url} не найден один из элементов футера: {str(e)}")

# Закрытие драйвера
driver.quit()




