from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from random import randint

def scroll_shim(passed_in_driver, object):
    x = object.location['x']
    y = object.location['y']
    scroll_by_coord = 'window.scrollTo(%s,%s);' % (
        x,
        y
    )
    scroll_nav_out_of_way = 'window.scrollBy(0, -120);'
    passed_in_driver.execute_script(scroll_by_coord)
    passed_in_driver.execute_script(scroll_nav_out_of_way)


class WebSpider:
    """
    Класс робота по созданию активности на сайте.
    В экземпляр класса возможно передать драйвер селениум ( при необходимости) и url сайта.
    """

    def __init__(self, driver=None, url='http://kubanzhalyuzi.ru'):
        self.url = url
        if None == driver:
            self.set_driver()
        else:
            self.driver = driver
        self.driver.get(self.url)

    def set_driver(self, browser='chrome'):
        if browser == 'chrome':
            self.driver = webdriver.Chrome(executable_path='chromedriver')

    def set_main_menu(self, selector):
        self.main_menu = []
        for item in self.driver.find_elements_by_css_selector(selector):
            self.main_menu.append(item)
        return self.main_menu

    def close(self):
        self.driver.close()


WS = WebSpider()
menu_links = WS.set_main_menu('#site-navigation ul li a')
try:
    for item in menu_links:
        print(WS.driver, item, item.text)
        #scroll_shim(WS.driver, item)
        #print(item.text)
        ActionChains(WS.driver).move_to_element(item).click().perform()
        sleep(10)
    WS.quite()
except:
    WS.quite()