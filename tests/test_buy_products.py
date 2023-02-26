import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from base.base_class import Base
from pages.cart_page import Cart_page
from pages.checkout_page import Checkout_page
from pages.main_page import Main_page
from pages.smartphones_gadgets_page import Smartphones_gadgets_page
from pages.smartphones_page import Smartphones_page
from pages.smartphones_photo_page import Smartphones_photo_page


class Test_buy_iphone13():
    print('Start test')
    g = Service("C:\\Users\\marat\\PycharmProjects\\dns_shop\\chromedriver.exe")
    driver = webdriver.Chrome(service=g)
    url = 'https://www.dns-shop.ru'
    driver.get(url)
    driver.maximize_window()
    mp = Main_page(driver)
    mp.choose_city_spb()
    time.sleep(1)
    mp.move_to_smartphones_photo()
    sm_ph = Smartphones_photo_page(driver)
    sm_ph.move_to_smartphones_gadgets()
    sm_gd = Smartphones_gadgets_page(driver)
    sm_gd.move_to_smartphones()
    smartphones = Smartphones_page(driver)
    smartphones.select_from_filter_iphone13(50000,100000)
    smartphones.move_to_cart()
    cart = Cart_page(driver)

    cart.move_to_checkout()
    check = Checkout_page(driver)
    check.input_checkout()
    # Base.assert_price(smartphones.select_price_1(),cart.select_price_2()) #не смог придумать как сравнить цену товара((
    print('Finish test')