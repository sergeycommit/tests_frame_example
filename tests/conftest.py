import os
import time

import allure
import pytest

from source.core.drivers import get_driver

def pytest_addoption(parser):
    parser.addoption('--host', action='store', default='local')
    parser.addoption('--browser', action='store', default='chrome')

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    # выполняем все остальные хуки, чтобы получить report object
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.outcome == 'failed':
        key_driver = [i for i in item.funcargs if 'driver' in i][0]
        screen_name = f'{int(time.time())}.png'
        driver = item.funcargs[key_driver]
        if os.path.exists('screens') is False:
            os.mkdir('screens')
        driver.save_screenshot(f'screens/{screen_name}')
        allure.attach.file(f'screens/{screen_name}', "Screenshot", attachment_type=allure.attachment_type.PNG)

    return rep


@pytest.fixture(scope="function")
def driver(request):
    host = request.config.getoption('--host')

    driver = get_driver(host, browser=getattr(request, 'param', 'chrome'))

    if getattr(request, 'param', False) is not False:
        allure.dynamic.feature(driver.capabilities['browserName'].title() + " " + driver.capabilities['browserVersion'])

    yield driver
    driver.quit()
