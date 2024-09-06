from helpers.console import *


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.eth_url = "https://etherscan.io"

    def open_etherscan(self):
        try:
            self.driver.get(self.eth_url)
        except Exception as e:
            logger.error("Ошибка перехода на etherscan")

    def find_element(self, locator):
        element = WebDriverWait(self.driver, timeout=10).until(
            EC.visibility_of_element_located(locator)
        )
        return element


class SearhList:
    LOCATOR_1 = (By.CLASS_NAME, "gasPricePlaceHolder")


class EtherscanActions(BasePage):

    @property
    def find_gas_element(self):
        return self.find_element(SearhList.LOCATOR_1)


def gas_checker(driver):
    try:
        check = EtherscanActions(driver)
        check.open_etherscan()
        while True:
            gas_element = check.find_gas_element
            if gas_element is not None:
                gas_price = float(gas_element.text)
                gas_price_integer = int(gas_price)
                if gas_price < eth_gas_price:
                    logger.info(f"Текущий газ {gas_price_integer} Gwei - OK, начинаю воркать!")
                    break
                else:
                    logger.info(f"Текущий газ {red}{gas_price_integer} Gwei{purple_2} > установленного ({eth_gas_price} Gwei). Жду {interval} секунд перед следующей проверкой...")
                    time.sleep(interval)
                    driver.refresh()
            else:
                logger.error("Gas element not found, retrying...")
                time.sleep(interval)
                driver.refresh()
    except Exception as e:
        logger.error(f"Ошибка проверки газа: {e}")

