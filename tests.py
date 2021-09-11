import yandex_results_analyzer.selenium as Y
import time


if __name__ == '__main__':
    browser = Y.get_search_results(key_request='Linux Forever', ads=True)
    driver = browser['driver']
    search_results = browser['search_results']
    print("Search results:\n\r", search_results)
    time.sleep(1)
    driver.quit()