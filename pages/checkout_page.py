import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Checkout_page(Base):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    select_phone_number = "/html/body/div/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div/div/input"
    button_choose_store = "//button[@class='base-ui-button_GWR base-ui-button_medium__Fr base-ui-button_brand_UhA base-ui-button_ico-none_Gf6 base-checkout-getting-pickup__shop-change-btn']"
    button_choose_first_store = "//button[@class='base-ui-button-v2_medium base-ui-button-v2_orange-border base-ui-button-v2_ico-none base-ui-button-v2 shop-choose-list__select-shop-btn']"
    button_confirm_order = "/html/body/div/div/div[1]/div/div[2]/div[2]/div[3]/div/div/button"

    #Getters
    def get_select_phone_number(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.select_phone_number)))

    def get_button_choose_store(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.button_choose_store)))

    def get_button_choose_first_store(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.button_choose_first_store)))

    def get_button_confirm_order(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.button_confirm_order)))

    #Actions
    def input_phone_number(self):
        self.get_select_phone_number().click()
        self.get_select_phone_number().send_keys('8005553535')
        print('Номер телефона введен')

    def click_button_choose_store(self):
        self.get_button_choose_store().click()
        print('Нажата кнопка выбора магазина')

    def click_button_choose_first_store(self):
        self.get_button_choose_first_store().click()
        print('Выбран первый магазин')

    def click_button_confirm_orded(self):
        self.get_button_confirm_order().click()
        print('Нажата кнопка Подтвердить заказ')

    #Methods
    """Заполнение данных для оформления заказа"""
    def input_checkout(self):
        self.get_current_url()
        self.input_phone_number()
        self.click_button_choose_store()
        time.sleep(1) #задержка для прогрузки окна с магазинами
        self.click_button_choose_first_store()
        self.click_button_confirm_orded()
