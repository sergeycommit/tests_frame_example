import asyncio
import os
import ssl
import time

import aiohttp
import allure
import pytest
import pytest_asyncio

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
        if 'driver' in item.funcargs:
            driver = item.funcargs['driver']
            screen_name = f'{int(time.time())}.png'
            if not os.path.exists('screens'):
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


@pytest_asyncio.fixture(scope="session")
def event_loop():
    """
    Создаёт event loop для всей сессии тестирования.
    Необходимо для использования session-scoped async фикстур.
    """
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="session")
async def aiohttp_session():
    """
    Фикстура для создания aiohttp ClientSession с отключенной проверкой SSL.
    Создаётся один раз на всю сессию тестирования и переиспользуется во всех тестах.
    
    Преимущества:
    - Переиспользование TCP соединений (connection pooling)
    - Keep-alive соединения
    - Меньше overhead на создание/закрытие соединений
    - Быстрее выполнение тестов
    """
    # Создаем SSL context без проверки сертификатов (для тестовых целей)
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    
    connector = aiohttp.TCPConnector(ssl=ssl_context, limit=100, limit_per_host=30)
    async with aiohttp.ClientSession(connector=connector) as session:
        yield session
