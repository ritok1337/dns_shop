from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main_page(Base):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    button_smartphones = "//a[@href='/catalog/17a890dc16404e77/smartfony-i-fototexnika/']"
    button_choose_city = "//div[@data-city-select-label='city-select-label']"
    select_spb = "//a[@data-city-id='566ca284-5bea-11e2-aee1-00155d030b1f']"

    #Getters
    def get_button_smartphones(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.button_smartphones)))
    def get_button_choose_city(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.button_choose_city)))
    def get_select_spb(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.select_spb)))
    #Actions
    def click_button_smartphones(self):
        self.get_button_smartphones().click()
        print('Нажат раздел Смартфоны и фототехника')
    def click_button_choose_city(self):
        self.get_button_choose_city().click()
        print('Нажат выбор города')
    def click_select_spb(self):
        self.get_select_spb().click()
        print('Выбран Санкт-Петербург')
    #Methods
    """Переход на страницу Смартфоны и Фототехника"""
    def move_to_smartphones_photo(self):
        self.click_button_smartphones()

    """Выбор города Санкт-Петербург"""
    def choose_city_spb(self):
        self.click_button_choose_city()
        self.click_select_spb()