import random
import time

from helpers.console import *
from helpers.mm import mm_connect, mm_submit_thx
from decimal import Decimal, getcontext


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://jumper.exchange/"

    def open_website(self):
        self.driver.get(self.url)
        time.sleep(2)

    def find_element(self, locator):
            try:
                element = WebDriverWait(self.driver, timeout=10).until(
                    EC.visibility_of_element_located(locator)
                )
                return element
            except Exception as e:
                logger.error(f"Не удалось найти элемент: {e}\n{locator}")
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


class SearhList:
    CONNECT_WALLET = (By.XPATH, "//button[@id='connect-wallet-button']")
    #mm icon number 4
    MM_ICON = (By.XPATH, "//li[contains(@class, '-root') and contains(@class, 'MuiMenuItem-gutters') and contains(@class, 'mui-5zn61u')]")
    #fist element
    CHAIN_FROM_MENU = (By.CSS_SELECTOR, '#widget-scrollable-container-\:r0\: > div > div.MuiContainer-root.MuiContainer-maxWidthLg.MuiContainer-disableGutters.mui-121yh4u > div > div.MuiBox-root.mui-guqkjl > button:nth-child(1) > div > div')
    ZK_SYNC = (By.XPATH, "//button[@aria-label='zkSync Era']")
    #first element
    ZK_ETH = (By.XPATH, "//div[@class='MuiButtonBase-root MuiListItemButton-root MuiListItemButton-dense MuiListItemButton-gutters MuiListItemButton-root MuiListItemButton-dense MuiListItemButton-gutters mui-1kn3mtx']")
    #second element
    CHAIN_TO = (By.CSS_SELECTOR, "#widget-scrollable-container-\:r0\: > div > div.MuiContainer-root.MuiContainer-maxWidthLg.MuiContainer-disableGutters.mui-121yh4u > div > div.MuiBox-root.mui-guqkjl > button:nth-child(3) > div > div")
    ARB = (By.XPATH, "//button[@aria-label='Arbitrum']")
    ETH_ARB = (By.XPATH, "//img[@alt='ETH']/ancestor::li")
    BTN_MAX = (By.XPATH, "//button[text()='max']")
    #first element
    FROM_AMOUNT = (By.CSS_SELECTOR, "#widget-scrollable-container-\:r0\: > div > div.MuiContainer-root.MuiContainer-maxWidthLg.MuiContainer-disableGutters.mui-121yh4u > div > div.MuiPaper-root.MuiPaper-outlined.MuiPaper-rounded.MuiCard-root.mui-9x7hh6 > div > div > div.MuiInputBase-root.MuiInputBase-colorPrimary.MuiInputBase-formControl.MuiInputBase-sizeSmall.MuiInputBase-adornedEnd.mui-50zsmj > input")
    REVIEW_BRIDGE = (By.XPATH, '/html/body/div[3]/div/div/div[1]/div/div/div[2]/div/div[3]/button[1]')
    START_BRIDGE = (By.XPATH, '//*[@id=":re:"]')
    TEST = (By.XPATH, "")


class JumperActions(BasePage):
    def connect_wallet(self):
        element = self.find_element(SearhList.CONNECT_WALLET)
        self.driver.execute_script("arguments[0].click();", element)

    def select_mm(self):
        element = self.find_elements(SearhList.MM_ICON)
        return element[3].click()

    def chain_from(self):
        return self.find_element(SearhList.CHAIN_FROM_MENU).click()

    def select_zk(self):
        return self.find_element(SearhList.ZK_SYNC).click()

    def chose_eth_from_zk(self):
        e = self.find_elements(SearhList.ZK_ETH)
        return e[0].click()

    def chain_to(self):
        return self.find_element(SearhList.CHAIN_TO).click()

    def select_arb(self):
        return self.find_element(SearhList.ARB).click()

    def select_eth_from_arb(self):
        return self.find_element(SearhList.ETH_ARB).click()

    def click_max(self):
        return self.find_element(SearhList.BTN_MAX).click()

    # def input_amount(self, value):
    #     return self.find_element(SearhList.FROM_AMOUNT).send_keys(value)

    def review_bridge(self):
        e = self.find_element(SearhList.REVIEW_BRIDGE)
        self.driver.execute_script("arguments[0].click();", e)


    def start_bridge(self):
        e = self.find_element(SearhList.START_BRIDGE)
        self.driver.execute_script("arguments[0].click();", e)


    getcontext().prec = 28

    def calc_eth_to_leave(self, eth_leave_from, eth_leave_to, e_round):
        balance_str = self.find_element(SearhList.FROM_AMOUNT).get_attribute("value")
        balance_num = float(balance_str)
        random_percentage = random.uniform(eth_leave_from, eth_leave_to)
        eth_to_leave = Decimal(balance_num - random_percentage).quantize(Decimal('1.' + ('0' * e_round)))
        logger.info(
             f"Баланс: {yellow}{balance_str} ETH{purple}; Бриджу {yellow}{eth_to_leave} ETH{reset}")

        return eth_to_leave

    def input_amount(self, value):
        e = self.find_element(SearhList.FROM_AMOUNT)
        e.clear()
        return e.send_keys(str(value))


def jumper_exchange(driver):
    try:
        logger.info(f"Начинаю работу с модулем: {white}Jumper Excange")
        jump = JumperActions(driver)
        jump.open_website()
        try:
            jump.connect_wallet()
        except:
            jump.connect_wallet()
        jump.select_mm()

        mm_connect(driver)
        sleep(1)

        jump.chain_from()
        sleep(1)
        jump.select_zk()
        sleep(2)
        jump.chose_eth_from_zk()
        sleep(1)
        jump.chain_to()
        sleep(1)
        jump.select_arb()
        sleep(2)
        jump.select_eth_from_arb()
        jump.click_max()
        x = jump.calc_eth_to_leave(eth_leave_from, eth_leave_to, e_round)
        jump.input_amount(x)
        time.sleep(3)
        jump.review_bridge()
        jump.start_bridge()

    except Exception as e:
        logger.error(f"Ошибка в модуле: Jumper Exchange {e}")
