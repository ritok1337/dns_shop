from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Smartphones_gadgets_page(Base):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    button_select_smartphones = "/html/body/div[2]/div[1]/div/a[1]/div[1]/span"

    #Getters
    def get_button_select_smartphones(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_select_smartphones)))

    #Actions
    def click_button_select_smartphones(self):
        self.get_button_select_smartphones().click()

    #Methods
    """Переход на страницу со смартфонами"""
    def move_to_smartphones(self):
        self.get_current_url()
        self.click_button_select_smartphones()