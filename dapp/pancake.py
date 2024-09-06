from helpers.console import *
from helpers.mm import mm_connect, mm_submit_thx, mm_unclock_token
from selenium.webdriver.common.action_chains import ActionChains
from decimal import Decimal, getcontext
from settings import INTRA_DELAY, PANCAKE_ETH_SWAP_AMOUNT, PANCAKE_REPEAT


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://pancakeswap.finance/swap?chain=zkSync"

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

    def find_element_no_message(self, locator):
            try:
                element = WebDriverWait(self.driver, timeout=10).until(
                    EC.visibility_of_element_located(locator)
                )
                return element
            except Exception as e:
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
    LOCATOR_0_CONNECT_WALLET = (By.XPATH, "//button[@scale='sm' and @variant='primary' and contains(@class, 'sc-bcPKhP') and contains(@class, 'iArAUI')]")
    LOCATOR_01_SELECT_MM = (By.XPATH, "//div[@class='sc-iBAaJG jYOsvJ' and text()='Metamask']")
    LOCATOR_1_TICK_BOX = (By.XPATH, "//input[@id='checkbox' and @scale='sm' and @type='checkbox' and contains(@class, 'sc-fwdjSP BCiKx')]")
    LOCATOR_2_START_NOW = (By.XPATH, "//button[@width='100%' and @variant='primary' and @scale='md' and contains(@class, 'sc-bcPKhP dAcAHr')]")
    LOCATOR_3_TOKEN_TO_SWAP = (By.XPATH, "//div[@class='sc-eDnVMP sc-gKHVLF gkVgsf jrKqNj']")
    LOCATOR_TOKEN_SEARCH_FIELD = (By.XPATH, "//input[@id='token-search-input']")
    LOCATOR_4_USDT = (By.XPATH, "//div[@class='_1a5xov70 _1qhetbf6 _1qhetbf16 _1qhetbf7c']")
    LOCATOR_5_USDC = (By.XPATH, "//div[@class='sc-eDnVMP sc-gaeLBU sc-jUdNGI sc-cnojMS gkVgsf fIgOwm dwOCAQ jDKqWC token-item-0x3355df6D4c9C3035724Fd0e3914dE96A5a83aaf4']/img")
    LOCATOR_6_WETH = (By.XPATH, "//div[@class='sc-eDnVMP sc-gaeLBU sc-jUdNGI sc-cnojMS gkVgsf fIgOwm dwOCAQ jDKqWC token-item-0x5AEa5775959fBC2557Cc8789bC1bf90A239D9a91']")
    LOCATOR_1_INPUT = (By.XPATH, "//input[@class='token-amount-input z84kgl0 z84kgl5']")
    LOCATOR_2_INPUT = (By.XPATH, "//input[@class='token-amount-input z84kgl0 z84kgl5']")
    LOCATOR_BALANCE_ETH = (By.XPATH, "//div[@data-dd-action-name='Token balance' and contains(@title, 'Balance:')]")
    LOCATOR_SWAP_BTN = (By.XPATH, "//button[@class='sc-bcPKhP dAcAHr' and @id='swap-button' and @data-dd-action-name='Swap commit button' and @scale='md']")
    LOCATOR_CONFIRM_SWAP = (By.XPATH, "//button[@variant='primary' and @mt='12px' and @id='confirm-swap-or-send' and @width='100%' and @scale='md' and @class='sc-bcPKhP ksKcmN']")
    LOCATOR_X_BTN = (By.XPATH, "//button[@class='sc-bcPKhP dCKrCZ sc-ftLKQv gdmfJZ' and @variant='text' and @aria-label='Close the dialog' and @scale='md']")
    LOCATOR_SWAP_INPUT_BTN = (By.XPATH, "//button[contains(@class, 'sc-bcPKhP') and contains(@class, 'lgmQVu') and contains(@class, 'sc-ftLKQv') and contains(@class, 'sc-bTwhag') and contains(@class, 'gdmfDE') and contains(@class, 'gOXJwL') and @variant='light' and @scale='sm']")
    LOCATOR_MAX_BTN = (By.XPATH, "//button[@data-dd-action-name='Balance percent max' and @scale='xs' and @variant='secondary' and @class='sc-bcPKhP ffEPtV' and @style='text-transform: uppercase;']")
    LOCATOR_SWAP_ALERT = (By.XPATH, "//button[contains(text(), 'Dismiss') and contains(@class, 'sc-bcPKhP') and contains(@class, 'xiIkU') and @variant='primary' and @scale='md']")


class PancakeActions(BasePage):
    def close_swap_alert(self):
        return self.find_element(SearchList.LOCATOR_SWAP_ALERT).click()

    def click_max_btn(self):
        return self.find_element(SearchList.LOCATOR_MAX_BTN).click()

    def searh_usdt(self):
        return self.find_element(SearchList.LOCATOR_TOKEN_SEARCH_FIELD).send_keys("USDT")

    def connect_wallet(self):
        return self.find_element(SearchList.LOCATOR_0_CONNECT_WALLET).click()

    def choose_mm(self):
        return self.find_element(SearchList.LOCATOR_01_SELECT_MM).click()

    def tick_box(self):
        return self.find_element_no_message(SearchList.LOCATOR_1_TICK_BOX).click()

    def start_now(self):
        return self.find_element_no_message(SearchList.LOCATOR_2_START_NOW).click()

    def token_to_swap(self):
        elements = self.find_elements(SearchList.LOCATOR_3_TOKEN_TO_SWAP)
        elements[1].click()

    def choose_usdt(self):
        elements = self.find_element(SearchList.LOCATOR_4_USDT)
        self.driver.execute_script("arguments[0].click();", elements)

    def choose_usdc(self):
        return self.find_element(SearchList.LOCATOR_5_USDC).click()

    def choose_weth(self):
        return self.find_element(SearchList.LOCATOR_6_WETH).click()

    def input_1(self):
        elements = self.find_elements(SearchList.LOCATOR_1_INPUT)
        elements[0].click()
        return True

    def input_2(self):
        elements = self.find_elements(SearchList.LOCATOR_1_INPUT)
        elements[1].click()
        return True

    def balance_eth(self):
        try:
            balance_eth_text = self.find_element(SearchList.LOCATOR_BALANCE_ETH).text
            if balance_eth_text.startswith("Balance"):
                balance_eth_clean = balance_eth_text.replace("Balance: ", "").strip()
                balance_eth = float(balance_eth_clean)
                return balance_eth
            else:
                print("Unexpected balance text format:", balance_eth_text)
                return None
        except Exception as e:
            print("Error retrieving balance:", str(e))
            return None

    def swap_btn(self):
        return self.find_element(SearchList.LOCATOR_SWAP_BTN).click()

    def confirm_swap(self):
        return self.find_element(SearchList.LOCATOR_CONFIRM_SWAP).click()

    def click_x(self):
        return self.find_element(SearchList.LOCATOR_X_BTN).click()

    def swap_input_btn(self):
        return self.find_element(SearchList.LOCATOR_SWAP_INPUT_BTN).click()

    getcontext().prec = 28

    def calculate_eth_to_swap(self, balance_eth, PANCAKE_ETH_SWAP_AMOUNT, e_round):
        random_percentage = random.randint(PANCAKE_ETH_SWAP_AMOUNT[0], PANCAKE_ETH_SWAP_AMOUNT[1])
        eth_balance_dec = Decimal(balance_eth)
        random_percentage_dec = Decimal(random_percentage) / Decimal(100)
        random_value = random_percentage_dec * eth_balance_dec
        random_value_rounded = random_value.quantize(Decimal('1.' + ('0' * e_round)))
        logger.info(f"Баланс: {yellow}{balance_eth} ETH{purple}; Свапаю: {yellow}{random_percentage}%{purple} = {yellow}{random_value_rounded} ETH{reset}")
        return random_value_rounded

    def paste_eth_value(self, random_value_rounded):
        random_value_rounded_str = str(random_value_rounded)
        return self.find_element(SearchList.LOCATOR_1_INPUT).send_keys(random_value_rounded_str)


def eth_to_usdt(driver):
    try:
        logger.info("Начинаю свап ETH to USDT")
        usdt = PancakeActions(driver)
        usdt.token_to_swap()
        usdt.searh_usdt()
        sleep(2)
        usdt.choose_usdt()
        balance_eth = usdt.balance_eth()
        random_value_rounded = usdt.calculate_eth_to_swap(balance_eth, PANCAKE_ETH_SWAP_AMOUNT, e_round)
        usdt.paste_eth_value(random_value_rounded)
        sleep(2)
        usdt.swap_btn()
        usdt.confirm_swap()
        mm_submit_thx(driver)
        usdt.click_x()
    except Exception as e:
        logger.error(f"Ошибка в ETH to USDT: {e}")


def usdt_to_eth(driver):
    try:
        logger.info("Начинаю свап USDT to ETH")
        usdte = PancakeActions(driver)
        usdte.swap_input_btn()
        sleep(2)
        usdte.click_max_btn()
        usdte.swap_btn()
        usdte.confirm_swap()
        try:
            usdte.close_swap_alert()
            usdte.swap_btn()
            usdte.confirm_swap()
        except:
            pass
        mm_unclock_token(driver)
        mm_submit_thx(driver)
    except Exception as e:
        logger.error(f"Ошибка в USDT to ETH: {e}")


def eth_to_usdc(driver):
    try:
        logger.info("Начинаю свап ETH to USDC")

    except Exception as e:
        logger.error(f"Ошибка в ETH to USDC: {e}")


def usdc_to_eth(driver):
    try:
        logger.info("Начинаю свап USDC to ETH")
    except Exception as e:
        logger.error(f"Ошибка в USDC to ETH: {e}")


def eth_to_weth(driver):
    try:
        logger.info("Начинаю свап ETH to WETH")
    except Exception as e:
        logger.error(f"Ошибка в ETH to WETH: {e}")


def weth_to_eth(driver):
    try:
        logger.info("Начинаю свап WETH to ETH")
    except Exception as e:
        logger.error(f"Ошибка в WETH to ETH: {e}")


def usdt_cycle(driver):
    eth_to_usdt(driver)
    x_time = random.randint(INTRA_DELAY[0], INTRA_DELAY[1])
    logger.info(f"Сплю: {x_time} секунд перед следующей транзакцией")
    sleep(x_time)
    usdt_to_eth(driver)


def usdc_cycle(driver):
    eth_to_usdc(driver)
    x_time = random.randint(INTRA_DELAY[0], INTRA_DELAY[1])
    logger.info(f"Сплю: {x_time} секунд перед следующей транзакцией")
    sleep(x_time)
    usdc_to_eth(driver)


def weth_cycle(driver):
    eth_to_weth(driver)
    x_time = random.randint(INTRA_DELAY[0], INTRA_DELAY[1])
    logger.info(f"Сплю: {x_time} секунд перед следующей транзакцией")
    sleep(x_time)
    weth_to_eth(driver)


def swap_func(driver):
    function = [usdc_cycle, usdt_cycle, weth_cycle]
    random_swap = random.choice(function)
    random_swap(driver)


def panceswap(driver):
    try:
        number_of_repeats = random.randint(PANCAKE_REPEAT[0], PANCAKE_REPEAT[1])
        logger.info(f"Начинаю работу с модулем {white}PANCAKE SWAP")
        ps = PancakeActions(driver)
        ps.open_website()
        try:
            ps.tick_box()
            ps.start_now()
        except:
            pass
        ps.connect_wallet()
        ps.choose_mm()
        mm_connect(driver)
        sleep(2)
        for repetition in range(number_of_repeats):
            usdt_cycle(driver)
            delay_between_repeats = random.randint(INTRA_DELAY[0], INTRA_DELAY[1])
            logger.info(f"Повтор {yellow}{repetition + 1}/{number_of_repeats}{reset}{purple}. Следующий запуск через: "f"{yellow}{delay_between_repeats}{reset}{purple} секунд.")
            time.sleep(delay_between_repeats)
    except Exception as e:
        logger.error(f"Ошибка в модуле PANCAKE SWAP: {e}")

