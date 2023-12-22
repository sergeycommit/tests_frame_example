from time import sleep

import allure
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def switch_to_frame(self, locator):
        """Переключить на iframe"""
        self.driver.switch_to.frame(self.is_element_visible(locator))

    def is_element_visible(self, web_element, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((web_element.by, web_element.value)))

    def is_element_visible_and_clickable(self, web_element, timeout=20):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((web_element.by, web_element.value)))
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((web_element.by, web_element.value)))

    def is_element_presence_in_dom(self, web_element, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((web_element.by, web_element.value)))

    @allure.step("Наводим мышку на элемент {web_element}")
    def hover(self, web_element):
        ActionChains(self.driver) \
            .move_to_element(self.is_element_presence_in_dom(web_element)) \
            .perform()

    @allure.step("Навели мышку на элемент {web_element} и кликнули")
    def hover_and_click(self, web_element):
        ActionChains(self.driver) \
            .move_to_element(self.is_element_presence_in_dom(web_element)) \
            .click(self.is_element_presence_in_dom(web_element)) \
            .perform()

    @allure.step("Проверим что мы на нужном урле {url}")
    def check_current_url(self, url, wait=10):
        for t in range(wait):
            try:
                assert url in self.driver.current_url, f"Current url does not {self.driver.current_url}"
                return
            except:
                sleep(1)
        raise TimeoutException(f"Ждали {wait} секунд нужная страница не загрузилась")

    @allure.step("Проверим атрибут элемента")
    def get_attr_(self, web_element, attr):
        return web_element.get_attribute(attr)
