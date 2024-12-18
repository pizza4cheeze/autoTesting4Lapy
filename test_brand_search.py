from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestBrandSearch:
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

            # Нажимаем на кнопку "Каталог"
            catalog_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(@class, 'HeaderToggleCatalogBtn_catalogButton__ZVW49')]"))
            )
            catalog_button.click()

            # Находим и кликаем на изображение бренда (Grandin)
            brand_image = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//img[@src='https://storage.yandexcloud.net/pim-core/dbpim-prod_122204.png']"))
            )
            brand_image.click()

            # Ждем, пока элементы товаров загрузятся, и проверяем название товара
            product_elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.CardProduct_productNameInner__Jc_on"))
            )

            # Проверяем, что в каждом элементе содержится текст "Grandin"
            for product in product_elements:
                product_name = product.text
                assert "Grandin" in product_name, f"Товар '{product_name}' не содержит 'Grandin'."

            print("Тест поиска товара по бренду 'Grandin' пройден: Все товары содержат 'Grandin'.")
        except Exception as e:
            print(f"Ошибка в тесте поиска товара по бренду: {e}")
            raise
