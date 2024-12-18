import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestPriceFilter:
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
            self.driver.get("https://4lapy.ru/")  # Замените на URL вашего сайта

            # Наводим курсор на каталог
            catalog_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'HeaderToggleCatalogBtn_catalogButton__ZVW49')]"))
            )
            catalog_button.click()

            # Наводим курсор на категорию "Рыбы"
            fish_category_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'HeaderCatalog_categoryLink__Di_DW')]//span[text()='Рыбы']"))
            )
            fish_category_button.click()

            # Кликаем на подкатегорию "Аквариумы"
            aquariums_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/catalog/ryby/akvariumy/komplekty-akvariumy/']"))
            )
            aquariums_link.click()

            # Вводим значения в фильтры по цене
            min_price_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "id_filter_range_min_price"))
            )
            min_price_input.clear()
            min_price_input.send_keys("1000")

            max_price_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "id_filter_range_max_price"))
            )
            max_price_input.clear()
            max_price_input.send_keys("3000")

            # Применяем фильтры
            time.sleep(5)

            # Проверяем, что все товары находятся в пределах указанного ценового диапазона
            product_prices = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.text-price-big"))
            )

            for price_element in product_prices:
                # Извлекаем цену и преобразуем её в число
                price_text = price_element.text.replace('₽', '').replace(' ', '').strip()
                price_value = int(price_text)

                assert 1000 <= price_value <= 3000, f"Цена товара {price_value} не входит в диапазон от 1000 до 3000."

            print("Тест с ценовым фильтром пройден: Все товары находятся в пределах заданного диапазона цен.")
        except Exception as e:
            print(f"Ошибка в тесте с ценовым фильтром: {e}")
            raise
