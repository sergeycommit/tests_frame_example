import allure
import pytest

from settings import URL, TSM_LINK, PAYMENT_URL
from source.pages.page_buy_polis import IndexPageSkin
from source.data.params import FIELD_DATA


@allure.testcase(TSM_LINK + (case_num := '1'), "Позитивная проверка сценария покупки полиса")
@allure.story('Покупка полиса от коронавируса')
@allure.title(f"{case_num} " + "Позитивная проверка сценария покупки полиса")
def test_positiv_buy_with_min_req(driver):
    page = IndexPageSkin(driver)
    driver.get(URL)

    (page.click_checkbox_virus_contact().
     click_checkbox_agree().
     click_calculate().
     enter_fio('Иванов Иван Иванович').
     enter_birthdate(12121988).
     enter_passport_number(2233546755).
     enter_passport_date(12122008).
     enter_address('Москва ул. Ленина 1').
     enter_phone(89222323322).
     enter_email('test@mail.com').
     click_to_buy().
     check_current_url(PAYMENT_URL)
     )


allure.testcase(TSM_LINK + (case_num := '2'), "Позитивная проверка сценария покупки полиса")
@allure.story('Покупка полиса от коронавируса')
@allure.title(f"{case_num} " + "Проверка свитчера и изменения цены")
def test_switcher(driver):
    page = IndexPageSkin(driver)
    driver.get(URL)

    page.check_switcher()


allure.testcase(TSM_LINK + (case_num := '3'), "Позитивная проверка сценария покупки полиса")
@allure.story('Покупка полиса от коронавируса')
@allure.title(f"{case_num} " + "Проверка чекбокса Профсфера связана с мед.деятельностью")
def test_checkbox_profsfera(driver):
    page = IndexPageSkin(driver)
    driver.get(URL)

    page.click_checkbox_profsfera()

allure.testcase(TSM_LINK + (case_num := '3'), "Позитивная проверка сценария покупки полиса")
@allure.story('Покупка полиса от коронавируса')
@allure.title(f"{case_num} " + "Проверка чекбокса Профсфера связана с мед.деятельностью")
@pytest.mark.parametrize("loc", FIELD_DATA)
def test_check_errors_with_empty_field(driver, loc):
    page = IndexPageSkin(driver)
    driver.get(URL)

    (page.click_checkbox_virus_contact().
     click_checkbox_agree().
     click_calculate().
     enter_fio('Иванов Иван Иванович' if loc != 'fio' else '').
     enter_birthdate('12121988' if loc != 'birthday' else '').
     enter_passport_number(2233546755 if loc != 'passport_number' else '').
     enter_passport_date(12122008 if loc != 'passport_date' else '').
     enter_address('Москва ул. Ленина 1' if loc != 'address' else '').
     enter_phone(89222323322 if loc != 'phone' else '').
     enter_email('test@mail.com' if loc != 'email' else '').
     click_to_buy().
     check_error(loc)
     )


allure.testcase(TSM_LINK + (case_num := '3'), "Позитивная проверка сценария покупки полиса")
@allure.story('Покупка полиса от коронавируса')
@allure.title(f"{case_num} " + "Проверка чекбокса Профсфера связана с мед.деятельностью")
@pytest.mark.parametrize("name", [' ', 'asdasd', 'Иванов_Иван_Иванович'])
def test_not_valid_name(driver, name):
    page = IndexPageSkin(driver)
    driver.get(URL)

    (page.click_checkbox_virus_contact().
     click_checkbox_agree().
     click_calculate().
     enter_fio(name).
     enter_birthdate('12121988').
     enter_passport_number(2233546755).
     enter_passport_date(12122008).
     enter_address('Москва ул. Ленина 1').
     enter_phone(89222323322).
     enter_email('test@mail.com').
     click_to_buy().
     check_error('fio')
     )