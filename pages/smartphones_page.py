import time

from selenium.webdriver import ActionChains, Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Smartphones_page(Base):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    button_submit_filter = "/html/body/div[2]/div/div[2]/div[1]/div/div[3]/div[2]/div/button[1]"
    select_min_price = "/html/body/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[4]/div/div/div[1]/input"
    select_max_price = "/html/body/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[4]/div/div/div[2]/input"
    checkbox_rating = "/html/body/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/label"
    select_internal_storage = "/html/body/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[8]/a/span"
    checkbox_512gb = "/html/body/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[8]/div/div/div[2]/label[7]/span[1]"
    select_year = "/html/body/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[9]/a/span"
    checkbox_2021y = "/html/body/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[9]/div/div/div/label[3]/span[2]"
    button_buy = "/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/div[4]/div[4]/button[2]"
    button_cart = "//a[@class='buttons__link ui-link cart-link-counter']"
    select_iphone13 = "/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/div[4]/a/span"
    select_price_1 = "/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/div[4]/div[4]/div/div[1]"

    #Getters

    def get_button_submit_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_submit_filter)))

    def get_select_min_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_min_price)))

    def get_select_max_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_max_price)))

    def get_checkbox_rating(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_rating)))

    def get_select_internal_storage(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_internal_storage)))

    def get_checkbox_512gb(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_512gb)))

    def get_select_year(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_year)))

    def get_checkbox_2021y(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_2021y)))

    def get_button_buy(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_buy)))

    def get_button_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_cart)))

    def get_select_iphone13(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_iphone13)))

    def get_select_price_1(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.select_price_1)))

    #Actions

    def click_button_submit_filter(self):
        self.get_button_submit_filter().click()
        print('Кнопка Применить нажата')

    def input_min_price(self,min):
        self.min = min
        self.get_select_min_price().send_keys(min)
        print('Введена минимальная цена')

    def input_max_price(self,max):
        self.max = max
        self.get_select_max_price().send_keys(max)
        print('Введена максимальная цена')

    def click_checkbox_rating(self):
        self.get_checkbox_rating().click()
        print('Чекбокс с Рейтингом от 4 активирован')

    def click_select_internal_storage(self):
        self.get_select_internal_storage().click()
        print('Раскрыты чекбоксы Внутренней памяти')

    def click_checkbox_512gb(self):
        self.get_checkbox_512gb().click()
        print('Чекбокс с 512 ГБ памяти активирован')

    def click_select_year(self):
        self.get_select_year().click()
        print('Раскрыты чекбоксы Года выпуска')

    def click_checkbox_2021y(self):
        self.get_checkbox_2021y().click()
        print('Чекбокс с 2021 года выпуска активирован')

    def click_button_buy(self):
        self.get_button_buy().click()
        print('Кнопка Купить нажата')

    def click_button_cart(self):
        self.get_button_cart().click()
        print('Кнопка Корзина нажата')

    def click_select_iphone13(self):
        self.get_select_iphone13().click()
        print('Переход на страницу с товаром')

    #Methods
    """Установка фильтра для выбора iphone13"""
    def select_from_filter_iphone13(self,min,max): # Назначение атрибутов min и max - минимальная цена и максимальная цена для ввода их в поля
        self.get_current_url()
        actions = ActionChains(self.driver)
        self.driver.execute_script("window.scrollBy(0, 200);") # Скролл страницы вниз, чтобы открылись нужные элементы
        actions.click_and_hold().move_by_offset(10,0).release().perform() # Движение мышкой, без нее метод иногда не срабатывал
        self.click_checkbox_rating()
        self.input_min_price(min)
        self.input_max_price(max)
        self.driver.execute_script("window.scrollBy(0, 1000);") # Скролл страницы вниз, чтобы открылись нужные элементы
        time.sleep(0.5) # небольшая задержка, без нее метод иногда срабатывал не как нужно
        self.click_select_internal_storage()
        time.sleep(0.5)
        self.click_checkbox_512gb()
        self.driver.execute_script("window.scrollBy(0, 500);") # Скролл страницы вниз, чтобы открылись нужные элементы
        self.click_select_year()
        self.click_checkbox_2021y()
        self.click_button_submit_filter()
        self.driver.execute_script("window.scrollTo(0, 750);") # Скролл страницы вверх, чтобы открылись нужные элементы
        time.sleep(3)
        self.click_button_buy()
        time.sleep(3)

    """Переход в корзину"""
    def move_to_cart(self):
        self.click_button_cart()

    def select_text_price(self):
        price_1 = self.get_select_price_1().text
        return price_1