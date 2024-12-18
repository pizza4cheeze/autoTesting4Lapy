from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCatsByHref:
    def __init__(self):
        self.driver_path = 'C:\\Users\\pizza4cheeze\\chromedriver-win64\\chromedriver.exe'
        self.driver = None

    def setup(self):
        service = Service(self.driver_path)
        self.driver = webdriver.Chrome(service=service)

    def test(self):
        try:
            self.driver.get("https://4lapy.ru/")

            # Переход к "Кошки" по href
            cats_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/catalog/koshki/']"))
            )
            cats_link.click()

            # Переход к "Влажный корм" по href
            wet_food_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/catalog/koshki/korm-koshki/konservy/']"))
            )
            wet_food_link.click()

            # Проверка наличия товара
            product_name = "ProPlan Sterilised Maintenance Влажный корм (пауч) для взрослых стерилизованных кошек и кастрированных котов, с индейкой в желе"
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{product_name}')]"))
            )
            print("Тест 'Кошки' по href пройден: Товар найден.")
        except Exception as e:
            print(f"Ошибка в тесте 'Кошки' по href: {e}")
        finally:
            self.driver.quit()
