from yandex_results_analyzer import main as Y
from selenium.webdriver.common.action_chains import ActionChains
import time

import time

def get_yandex_link(results, root_url):
    result = results['ads']
    result = results['results']
    return [{'link': link['link'], 'item': link['item_link']} for link in result if link['root_url'] == root_url][0]

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


if __name__ == '__main__':
    yandex_results = Y.get_search_results('Вертикальные жалюзи Краснодар')
    driver = yandex_results['driver']
    results = yandex_results['search_results']
    print(get_yandex_link(results, 'kubanzhalyuzi.ru'))
    item_result = get_yandex_link(yandex_results['search_results'], 'kubanzhalyuzi.ru')['item']

    scroll_shim(driver, item_result)
    ActionChains(driver).move_to_element(item_result).click().perform()

    time.sleep(10)

    # Переключаемся на новую вкладку, т.к. яндекс открывает результаты запроса в новой вкладке
    windows = driver.window_handles #0 - страница от куда перешли ( яндекс ), 1 - страница куда перешли
    driver.switch_to.window(windows[1])


    """
    from selenium import webdriver
    driver = webdriver.Firefox()
    driver.get('http://kubanzhalyuzi.ru')
    scroll_shim(driver, driver.find_element_by_css_selector('.main-nav-list'))
    time.sleep(10)
    ActionChains(driver).move_to_element(driver.find_element_by_css_selector('#menu-item-25')).click().perform()
    time.sleep(10)
    driver.close()
    """






