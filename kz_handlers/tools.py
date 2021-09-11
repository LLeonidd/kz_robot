import random
from time import sleep



def scroll_shim(passed_in_driver, object):
    """
    Fix:move to element for FireFox
    :param passed_in_driver:
    :param object:
    :return:
    """
    x = object.location['x']
    y = object.location['y']
    scroll_by_coord = 'window.scrollTo(%s,%s);' % (
        x,
        y
    )
    scroll_nav_out_of_way = 'window.scrollBy(0, -120);'
    passed_in_driver.execute_script(scroll_by_coord)
    passed_in_driver.execute_script(scroll_nav_out_of_way)


def scroll_down(driver):
    """
    Sroll page to end
    :param driver:
    :return:
    """
    step = 10
    for timer in range(0, 50):
        driver.execute_script(f"window.scrollTo(0, {step});")
        step += step * random.choice(range(8, 15)) / 10
        sleep(random.choice(range(1, 5)) / 10)
