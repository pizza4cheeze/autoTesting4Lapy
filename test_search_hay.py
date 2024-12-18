from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestSearchHay:
    def __init__(self):
        self.driver_path = 'C:\\Users\\pizza4cheeze\\chromedriver-win64\\chromedriver.exe'
        self.driver = None

    def setup(self):
        service = Service(self.driver_path)
        self.driver = webdriver.Chrome(service=service)

    def teardown(self):
        if self.driver:
            self.driver.quit()

    def test(self):
        try:
            self.driver.get("https://4lapy.ru/")

            # Находим поле поиска
            search_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input.js-searchTrigger.HeaderSearch_input__Zug7g"))
            )
            search_input.click()
            search_input.send_keys("сено с календулой")

            # Нажимаем кнопку поиска
            search_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.HeaderSearch_button__wh1pL"))
            )
            search_button.click()

            # Проверяем наличие товара с нужным названием
            product_name = "Сено луговое с календулой"
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{product_name}')]"))
            )
            print("Тест поиска сена с календулой пройден: Товар найден.")
        except Exception as e:
            print(f"Ошибка в тесте поиска сена с календулой: {e}")
            raise
