import allure
from selenium.webdriver import ActionChains

import source.data.strings
from source.data.locators import BuyPolis
from source.pages.base_page import BasePage


class IndexPageSkin(BasePage):
    locator = BuyPolis()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.action = ActionChains(self.driver)


    @allure.step("Клик на чекбокс отсутсвие совместнопроживающего больного коронавирусом")
    def click_checkbox_virus_contact(self):
        self.is_element_visible_and_clickable(self.locator.CHECKBOX_VIRUS_CONTACT).click()

        return self

    @allure.step("Клик на чекбокс Профсфера связана с мед.деятельностью")
    def click_checkbox_profsfera(self):
        elem = self.is_element_presence_in_dom(self.locator.MEDICINE_INFO)
        assert self.get_attr_(elem, 'hidden') == 'true', f"{self.get_attr_(elem, 'hidden')} is not true"
        self.is_element_visible_and_clickable(self.locator.CHECKBOX_PROFSFERA).click()
        assert self.get_attr_(elem, 'hidden') != 'true', f"{self.get_attr_(elem, 'hidden')} is true"

        return self

    @allure.step("Клик на чекбокс согласие на обработку ПД")
    def click_checkbox_agree(self):
        self.is_element_visible_and_clickable(self.locator.CHECKBOX_AGREE).click()

        return self

    @allure.step("Клик на кнопку Продолжить на этапе Расчет")
    def click_calculate(self):
        self.is_element_visible_and_clickable(self.locator.CONTINUE_BUTTON).click()

        return self

    @allure.step("Ввод ФИО")
    def enter_fio(self, name):
        self.is_element_visible_and_clickable(self.locator.NAME_FIELD).send_keys(name)

        return self

    @allure.step("Ввод birthdate")
    def enter_birthdate(self, birthdate):
        self.is_element_visible_and_clickable(self.locator.DATEBIRTH_FIELD).send_keys(birthdate)

        return self

    @allure.step("Ввод серии и номера паспорта")
    def enter_passport_number(self, passport_number):
        self.is_element_visible_and_clickable(self.locator.PASSPORT_FIELD).send_keys(passport_number)

        return self

    @allure.step("Ввод даты выдачи паспорта")
    def enter_passport_date(self, date):
        self.is_element_visible_and_clickable(self.locator.DATE_FIELD).send_keys(date)

        return self

    @allure.step("Ввод адреса")
    def enter_address(self, address):
        self.is_element_visible_and_clickable(self.locator.ADDRESS_FIELD).send_keys(address)

        return self

    @allure.step("Ввод телефона")
    def enter_phone(self, phone):
        self.is_element_visible_and_clickable(self.locator.PHONE_FIELD).send_keys(phone)

        return self

    @allure.step("Ввод email")
    def enter_email(self, email):
        self.is_element_visible_and_clickable(self.locator.EMAIL_FIELD).send_keys(email)

        return self

    @allure.step("Клик по чекбоксу Страхователь является застрахованным")
    def checkbox_strah(self):
        self.is_element_visible_and_clickable(self.locator.CHECKBOX_STRAH).click()

        return self

    @allure.step("Клик Перейти к оплате")
    def click_to_buy(self):
        self.is_element_visible_and_clickable(self.locator.TO_BUY_BUTTON).click()

        return self

    @allure.step("Проверим свитчер")
    def check_switcher(self):
        elems = self.driver.find_elements(self.locator.HOSPITALIZATION.by, self.locator.HOSPITALIZATION.value)
        result = []
        for elem in elems:
            result.append(self.get_attr_(elem, 'hidden'))

        assert result == [None, 'true'], f'{result} != [None, "true"]'

        self.is_element_visible_and_clickable(self.locator.SWITCHER).click()

        elems = self.driver.find_elements(self.locator.HOSPITALIZATION.by, self.locator.HOSPITALIZATION.value)
        result = []
        for elem in elems:
            result.append(self.get_attr_(elem, 'hidden'))

        assert result == ['true', None], f'{result} != ["true", None]'

    @allure.step("Проверим текст ошибки")
    def check_error(self, loc):
        elem = self.is_element_visible(self.locator.ERROR).text
        if loc == 'fio':
            assert elem == source.data.strings.FIO_ERROR, f"{elem} != {source.data.strings.FIO_ERROR}"
        elif loc == 'birthday':
            assert elem == source.data.strings.BIRTHDAY_ERROR, f"{elem} != {source.data.strings.BIRTHDAY_ERROR}"
        elif loc == 'passport_number':
            assert elem == source.data.strings.PASSPORT_NUMBER_ERROR, f"{elem} != {source.data.strings.PASSPORT_NUMBER_ERROR}"
        elif loc == 'passport_date':
            assert elem == source.data.strings.PASSPORT_DATE_ERROR, f"{elem} != {source.data.strings.PASSPORT_DATE_ERROR}"
        elif loc == 'address':
            assert elem == source.data.strings.ADDRESS_ERROR, f"{elem} != {source.data.strings.ADDRESS_ERROR}"
        elif loc == 'phone':
            assert elem == source.data.strings.PHONE_ERROR, f"{elem} != {source.data.strings.PHONE_ERROR}"
        elif loc == 'email':
            assert elem == source.data.strings.EMAIL_ERROR, f"{elem} != {source.data.strings.EMAIL_ERROR}"
