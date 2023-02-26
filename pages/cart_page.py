from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Cart_page(Base):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    button_buy = "//button[@id='buy-btn-main']"
    select_price_2 = "/html/body/div/div[1]/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[1]/div[3]/div/div[1]/div[1]/span[2]"

    #Getters
    def get_button_buy(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.button_buy)))
    def get_select_price_2(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.select_price_2)))

    #Actions
    def click_button_buy(self):
        self.get_button_buy().click()
        print('Кнопка Перейти к оформлению нажата')

    #Methods
    def move_to_checkout(self):
        self.get_current_url()
        self.click_button_buy()

    def select_text_price_2(self):
        price_2 = self.get_select_price_2().text
        return price_2
