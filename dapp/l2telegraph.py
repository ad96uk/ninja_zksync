from helpers.console import *
from settings import GAS_VALUE
from helpers.mm import mm_connect, mm_submit_thx, mm_unclock_token
from decimal import Decimal, getcontext
from helpers.mm import get_thx


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://l2telegraph.xyz/gas/"

    def open_website(self):
        self.driver.get(self.url)

    def find_element(self, locator):
            try:
                element = WebDriverWait(self.driver, timeout=10).until(
                    EC.visibility_of_element_located(locator)
                )
                return element
            except Exception as e:
                logger.error(f"Не удалось найти элемент: {e}\n{locator}")
                return None

    def find_unlock(self, locator):
        try:
            element = WebDriverWait(self.driver, timeout=10).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except Exception:
            return None

    def find_elements(self, locator):
        try:
            elements = WebDriverWait(self.driver, timeout=10).until(
                EC.visibility_of_all_elements_located(locator)
            )
            return elements
        except Exception as e:
            logger.error(f"Не удалось найти элементы: {e}\n{locator}")
            return []


class SearchList:
    CONNECT_WALLET = (By.XPATH, "//button[contains(@class, 'l2telegraph__button') and contains(text(), 'Connect Metamask')]")
    GAS_AMOUNT = (By.XPATH, "//input[@type='text' and @id='amount']")
    DROP_GAS = (By.XPATH, "//button[@class='l2telegraph__button' and @id='bridge']")


class L2telegrapActions(BasePage):
    def connect_wallet(self):
        return self.find_element(SearchList.CONNECT_WALLET).click()

    def paste_gas_value(self):
        random_gas_value = random.uniform(GAS_VALUE[0], GAS_VALUE[1])
        formatted_amount = "{:.7f}".format(random_gas_value)
        element = self.find_element(SearchList.GAS_AMOUNT)
        element.clear()
        element.send_keys(formatted_amount)

    def drop_gas(self):
        return self.find_element(SearchList.DROP_GAS).click()


def l2telegraph(driver):
    try:
        logger.info(f"Начинаю работу с модулем {white}L2 TELEGRAPH")
        l23 = L2telegrapActions(driver)
        l23.open_website()
        l23.connect_wallet()
        mm_connect(driver)
        l23.paste_gas_value()
        sleep(2)
        l23.drop_gas()
        mm_submit_thx(driver)
    except Exception as e:
        logger.error(f"Ошибка в l2telegraph: {e}")