from helpers.console import *
from helpers.mm import mm_connect, mm_submit_thx, mm_unclock_token
from decimal import Decimal, getcontext
from helpers.mm import get_thx


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://l2pass.com/mint"

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
    CONNECT_WALLET = (By.XPATH, "//button[@data-testid='rk-connect-button' and text()='Сonnect Wallet']")
    CHOOSE_MM = (By.XPATH, "//button[@data-testid='rk-wallet-option-metaMask']")
    FREE_MINT = (By.XPATH, "//button[contains(@class, 'sc-8bb921a8-0') and contains(@class, 'eALfgG') and contains(@class, 'button') and contains(@class, 'mint_button')]")


class L2passActions(BasePage):

    def connect_wallet(self):
        return self.find_element(SearchList.CONNECT_WALLET).click()

    def choose_mm(self):
        return self.find_element(SearchList.CHOOSE_MM).click()

    def free_mint(self):
        return self.find_element(SearchList.FREE_MINT).click()


def l2pass_free_mint(driver):
    try:
        logger.info(f"Начинаю работу с модулем {white}L2PASS")
        l2 = L2passActions(driver)
        l2.open_website()
        sleep(5)
        l2.connect_wallet()
        l2.choose_mm()
        mm_connect(driver)
        l2.open_website()
        sleep(5)
        l2.free_mint()
        mm_submit_thx(driver)
    except Exception as e:
        logger.error(f"Ошибка в l2pass_free_mint: {e}")
