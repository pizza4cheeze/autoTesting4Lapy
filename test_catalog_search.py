from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCatalogSearch:
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
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'HeaderToggleCatalogBtn_catalogButton__ZVW49')]"))
            )
            catalog_button.click()

            # Наводим курсор на "Ветаптека"
            vet_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'HeaderCatalog_categoryLink__Di_DW')]//span[contains(text(), 'Ветаптека')]"))
            )
            vet_button.click()

            # Кликаем по ссылке "Универсальные"
            universal_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/catalog/veterinarnaya-apteka/zashchita-ot-blokh-i-kleshchey/universalnyi/']"))
            )
            universal_link.click()

            # Проверяем наличие товара с нужным названием
            product_name = "Ошейник для кошек и собак мелких пород от блох и клещей, 40 см"
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{product_name}')]"))
            )

            print(f"Тест поиска через каталог пройден: Товар '{product_name}' найден.")
        except Exception as e:
            print(f"Ошибка в тесте поиска через каталог: {e}")
            raise
