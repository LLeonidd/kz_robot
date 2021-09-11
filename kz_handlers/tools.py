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