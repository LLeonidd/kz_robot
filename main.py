from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import random
from random import randint
from yandex_results_analyzer import selenium as Y
target_prefix = 'kubanzhalyuzi.ru'
target_url = f'http://{target_prefix}'


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

    def __init__(self, driver=None, url=target_url):
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
        """
        Define main menu
        :param selector:
        :return:
        """
        self.main_menu = {'items':[], 'links':[], 'links_text':[]}
        for item in self.driver.find_elements_by_css_selector(selector):
            if item.is_displayed():
                self.main_menu['items'].append(item)
                self.main_menu['links'].append(item.get_attribute('href'))
                self.main_menu['links_text'].append(item.text)
        return self.main_menu

    def quit(self):
        self.driver.quit()

def main_test():
    WS = WebSpider()
    menu_links = WS.set_main_menu('#site-navigation ul li a')
    try:
        for item in menu_links:
            print(WS.driver, item, item.text)
            #scroll_shim(WS.driver, item)
            #print(item.text)
            ActionChains(WS.driver).move_to_element(item).click().perform()
            sleep(10)
        WS.quit()
    except:
        WS.quit()


if __name__ == '__main__':
    """
    
    #Search site in Yandex
    yandex_results = Y.get_search_results('Вертикальные жалюзи Краснодар')
    driver = yandex_results['driver']
    search_results = yandex_results['search_results']
    #Select site in Yandex search
    item_result = Y.get_yandex_link(search_results, target_prefix)['item']
    # Move and click on site link in Yandex
    ActionChains(driver).move_to_element(item_result).click().perform()
    # switch on tab
    windows = driver.window_handles  # 0 - страница от куда перешли ( яндекс ), 1 - страница куда перешли
    driver.switch_to.window(windows[1])
    WS = WebSpider(driver=driver)
    """
    #Work spider in site
    WS = WebSpider()

    main_menu_items = WS.set_main_menu('.main-nav-list li a')['items']
    main_menu_links = WS.set_main_menu('.main-nav-list li a')['links']
    random.shuffle(main_menu_links)
    main_menu_item = random.choice(main_menu_items)

    for main_menu_link in main_menu_links:
        current_menu_item = WS.driver.find_element_by_xpath(f'//ul[@class="nav navbar-nav navbar-right responsive-nav main-nav-list"]/li/a[@href="{main_menu_link}"]')

        print('Select item menu: ', current_menu_item.text)

        ActionChains(WS.driver).move_to_element(current_menu_item).click().perform()

        #Прокрутка страницы вниз
        step=10
        for timer in range(0,50):
            #WS.driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight);")
            WS.driver.execute_script(f"window.scrollTo(0, {step});")
            step+=step*random.choice(range(8, 15))/10
            sleep(random.choice(range(1, 5))/10)

        sleep(random.choice(range(1, 6)))

    WS.quit()



