

class Base():
    def __init__(self,driver):
        self.driver = driver
    """Метод получения текущей url"""
    def get_current_url(self):
        current_url = self.driver.current_url
        print('Текущая страница - ' + current_url)

    """Метод проверки сверки цены"""
    def assert_price(self, price_1, price_2):
        assert price_1.text == price_2.text
        print('Значения совпадает')