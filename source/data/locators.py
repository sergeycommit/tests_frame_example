from collections import namedtuple

from selenium.webdriver.common.by import By


class BuyPolis(object):
    """Класс для локаторов страницы buy_polis"""

    WebElement = namedtuple('WebElement', ['by', 'value'])
    WebElements = namedtuple('WebElements', ['by', 'value'])

    CHECKBOX_PROFSFERA = WebElements(By.CSS_SELECTOR, ".checkbox-container .checkmark:nth-child(2)")
    MEDICINE_INFO = WebElements(By.CLASS_NAME, "medicine-info")
    CHECKBOX_VIRUS_CONTACT = WebElements(By.CSS_SELECTOR, ".checkbox-container .checkmark:nth-child(3)")
    CHECKBOX_AGREE = WebElements(By.CSS_SELECTOR, ".checkbox-container .checkmark:nth-child(4)")
    CONTINUE_BUTTON = WebElements(By.NAME, "calculate")
    NAME_FIELD = WebElements(By.ID, "name")
    DATEBIRTH_FIELD = WebElements(By.ID, "dateBirth")
    PASSPORT_FIELD = WebElements(By.ID, "id")
    DATE_FIELD = WebElements(By.ID, "idDate")
    ADDRESS_FIELD = WebElements(By.ID, "address")
    PHONE_FIELD = WebElements(By.ID, "phone")
    EMAIL_FIELD = WebElements(By.ID, "email")
    TO_BUY_BUTTON = WebElements(By.XPATH, '//button[text()="Перейти к оплате"]')
    PHONE_FIELD = WebElements(By.ID, "phone")
    EMAIL_FIELD = WebElements(By.ID, "email")
    TO_BUY_BUTTON = WebElements(By.XPATH, '//button[text()="Перейти к оплате"]')
    PHONE_FIELD = WebElements(By.ID, "phone")
    EMAIL_FIELD = WebElements(By.ID, "email")
    CHECKBOX_STRAH = WebElement(By.NAME, "addPerson")
    TO_BUY_BUTTON = WebElements(By.XPATH, '//button[text()="Перейти к оплате"]')

    SWITCHER = WebElements(By.CSS_SELECTOR, '.slider.round')
    HOSPITALIZATION = WebElements(By.CLASS_NAME, 'hospitalization')
    ERROR = WebElements(By.CSS_SELECTOR, ".error")




