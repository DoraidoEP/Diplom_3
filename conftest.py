import pytest
from data import DataUrl
from selenium import webdriver


@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def driver(request):
    if 'chrome' in request.param:
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)

    elif 'firefox' in request.param:
        options = webdriver.FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)

    driver.get(DataUrl.STELLAR_BURGERS)
    yield driver
    driver.quit()