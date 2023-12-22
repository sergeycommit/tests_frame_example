from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from settings import CHROME_SELENOID_REMOTE_URL, FIREFOX_SELENOID_REMOTE_URL, SELENOID_URL


def get_driver(host='local', browser='chrome'):
    browser = browser.lower()
    match browser:
        case 'firefox':
            options = webdriver.FirefoxOptions()
            Service = FirefoxService()
            options.set_preference("media.eme.enabled", True)
            options.set_preference("media.gmp-manager.updateEnabled", True)
            options.set_preference("security.fileuri.strict_origin_policy", False)
            options.set_preference("network.http.refere.XOriginPolicy", False)
            options.set_preference("content.cors.disable", False)
            options.set_preference("privacy.trackingprotection.enabled", False)
            options.add_argument("--width=1280")
            options.add_argument("--height=800")
            options.add_argument('--autoplay-policy=no-user-gesture-required')
            options.add_argument("--disable-web-security")
            options.add_argument("--disable-gpu")
            options.set_capability("selenoid:options", {
                "enableVNC": True,
                "enableVideo": False,
                "sessionTimeout": "2h"
            }
                                   )

        case 'chrome':
            options = webdriver.ChromeOptions()
            Service = ChromeService()
            options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--ignore-ssl-errors')
            options.add_argument("--window-size=1280,800")
            options.add_argument("--start-maximized")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_experimental_option('excludeSwitches', ['--enable-automation'])
            options.add_argument('--autoplay-policy=no-user-gesture-required')
            options.set_capability("selenoid:options", {
                    "enableVNC": True,
                    "enableVideo": False,
                    "sessionTimeout": "2h"
                }
                                   )

    match (host, browser):
        case ('local', browser):
            return webdriver.Chrome(service=Service, options=options)

        case ('remote', browser):
            return webdriver.Remote(command_executor=SELENOID_URL, options=options)

        case (_, browser) if browser == 'chrome':
            return webdriver.Remote(command_executor=CHROME_SELENOID_REMOTE_URL, options=options)

        case (_, browser) if browser == 'firefox':
            return webdriver.Remote(command_executor=FIREFOX_SELENOID_REMOTE_URL, options=options)
