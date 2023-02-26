from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Smartphones_photo_page(Base):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    button_smartphones_photo = "/html/body/div[2]/div[1]/div/a[1]/div[1]/span"

    #Getters

    def get_button_smartphones_photo(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.button_smartphones_photo)))

    #Actions

    def click_button_smartphones_photo(self):
        self.get_button_smartphones_photo().click()

    #Methods
    """Переход на страницу Смартфоны и Гаджеты"""
    def move_to_smartphones_gadgets(self):
        self.get_current_url()
        self.click_button_smartphones_photo()
