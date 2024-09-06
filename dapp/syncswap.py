import random
import time

from helpers.console import *
from helpers.mm import mm_connect, mm_submit_thx, mm_unclock_token
from decimal import Decimal, getcontext
from helpers.mm import get_thx


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://syncswap.xyz/"

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


class SearhList:
    LOCATOR_1_CNT_WALT = (By.XPATH, "//button[contains(@class, 'MuiButtonBase-root') and contains(@class, 'MuiButton-root') and contains(@class, 'MuiButton-text') and contains(@class, 'MuiButton-textPrimary') and contains(@class, 'MuiButton-sizeMedium') and contains(@class, 'MuiButton-textSizeMedium') and contains(@class, 'flex-center') and contains(@class, 'align') and contains(@class, 'zoom')]")
    LOCATOR_2_MM = (By.XPATH, "//p[contains(@class, 'MuiTypography-root') and contains(@class, 'MuiTypography-body1') and contains(@class, 'css-2skr0u') and text()='Browser Wallet']")
    LOCATOR_INPUT_1 = (By.XPATH, "//input[contains(@class, 'swap-input') and @placeholder='0.0' and @style='font-size: 30px; color: rgb(6, 8, 40);']")
    LOCATOR_INPUT_2 = (By.XPATH, "//input[@class='swap-input' and @placeholder='0.0' and @value='' and @style='font-size: 30px; color: rgb(6, 8, 40);']")
    LOCATOR_3_CHOOSE_TOKEN_TO_SWAP = (By.XPATH, "//div[contains(@class, 'pointer') and contains(@class, 'flex-center') and contains(@class, 'swap-input-btn')]")
    LOCATOR_USDT = (By.XPATH, "//p[contains(@class, 'MuiTypography-root') and contains(@class, 'MuiTypography-body1') and contains(@class, 'css-35mrzs') and text()='USDT']")
    LOCATOR_USDC = (By.XPATH, "//p[contains(@class, 'MuiTypography-root') and contains(@class, 'MuiTypography-body1') and contains(@class, 'css-1v41v22') and text()='USDC']")
    LOCATOR_SWAP_FIELD_BTN = (By.XPATH, "//div[contains(@class, 'box-shadow-thin') and contains(@class, 'swap-exchange-icon') and contains(@class, 'br10') and contains(@class, 'pointer')]")
    LOCATOR_100_PERCENT = (By.XPATH, "//button[contains(@class, 'MuiButtonBase-root') and contains(@class, 'MuiButton-root') and contains(@class, 'MuiButton-outlined') and contains(@class, 'MuiButton-outlinedPrimary') and contains(@class, 'MuiButton-sizeSmall') and contains(@class, 'MuiButton-outlinedSizeSmall') and contains(@class, 'MuiButton-fullWidth') and contains(@class, 'css-1wgf3jc') and @tabindex='0' and @type='button' and text()='100%']")
    LOCATOR_SWAP_BTN = (By.XPATH, "//button[contains(@class, 'MuiButton-containedSecondary') and contains(@class, 'MuiButton-sizeLarge') and contains(@class, 'MuiButton-fullWidth') and contains(@class, 'swap-confirm') and contains(@class, 'css-1g14qne')]")
    LOCATOR_UNDERSTOOD_BTN = (By.XPATH, "//button[contains(@class, 'MuiButton-outlinedPrimary') and contains(@class, 'MuiButton-sizeMedium') and contains(@class, 'MuiButton-fullWidth') and contains(@class, 'css-p1wc8o')]")
    LOCATOR_BALANCE = (By.XPATH, "//p[contains(@class, 'MuiTypography-root') and contains(@class, 'MuiTypography-body1') and contains(@class, 'css-tqlmt3')]")
    LOCATOR_CLOSE_WELCOM = (By.XPATH, "//div[contains(@class, 'pointer')]/*[name()='svg'][@xmlns='http://www.w3.org/2000/svg' and @width='20' and @height='20' and @viewBox='0 0 24 24' and @fill='none' and @stroke='#6f7183' and @stroke-width='2' and @stroke-linecap='round' and @stroke-linejoin='round']")
    LOCATOR_UNLOCK_USDC = (By.XPATH, "//button[normalize-space(.)='Unlock USDC']")
    LOCATOR_UNLOCK_USDT = (By.XPATH, "//button[normalize-space(.)='Unlock USDT']")
    LOCATOR_CLOSE_UNLOCK_ALERT = (By.XPATH, "")
    LOCATOR_LIBERTAS = (By.XPATH, '//p[@class="MuiTypography-root MuiTypography-body1 css-1fzym8t" and text()="LIBERTAS"]'),
    LOCATOR_MEOW = (By.XPATH, '//p[@class="MuiTypography-root MuiTypography-body1 css-1fzym8t" and text()="MEOW"]'),
    LOCATOR_AAI = (By.XPATH, '//p[@class="MuiTypography-root MuiTypography-body1 css-1fzym8t" and text()="AAI"]'),
    LOCATOR_HOLD = (By.XPATH, '//p[@class="MuiTypography-root MuiTypography-body1 css-1fzym8t" and text()="HOLD"]'),
    LOCATOR_CHEEMS = (By.XPATH, '//p[@class="MuiTypography-root MuiTypography-body1 css-1fzym8t" and text()="Cheems"]'),
    LOCATOR_SIS = (By.XPATH, '//p[@class="MuiTypography-root MuiTypography-body1 css-1fzym8t" and text()="SIS"]'),
    LOCATOR_SOL = (By.XPATH, '//p[@class="MuiTypography-root MuiTypography-body1 css-1fzym8t" and text()="SOL"]'),
    LOCATOR_WLD = (By.XPATH, '//p[@class="MuiTypography-root MuiTypography-body1 css-1fzym8t" and text()="WLD"]'),
    LOCATOR_TON = (By.XPATH, '//p[@class="MuiTypography-root MuiTypography-body1 css-1fzym8t" and text()="TON"]'),
    LOCATOR_MAV = (By.XPATH, '//p[@class="MuiTypography-root MuiTypography-body1 css-1fzym8t" and text()="MAV"]'),
    LOCATOR_SHIB = (By.XPATH, '//p[@class="MuiTypography-root MuiTypography-body1 css-1fzym8t" and text()="SHIB"]'),
    LOCATOR_LMAO = (By.XPATH, '//p[@class="MuiTypography-root MuiTypography-body1 css-1fzym8t" and text()="LMAO"]'),
    INPUT_TOKEN_FROM = (By.XPATH, '//input[@class="w100 input" and @placeholder="Search name or paste address"]')











class Syncswapactions(BasePage):
    def close_welcome(self):
        return self.find_element(SearhList.LOCATOR_CLOSE_WELCOM).click()

    def connect_wallet(self):
        return self.find_element(SearhList.LOCATOR_1_CNT_WALT).click()

    def choose_mm(self):
        return self.find_element(SearhList.LOCATOR_2_MM).click()

    def click_input_1(self):
        elements = self.find_elements(SearhList.LOCATOR_INPUT_1)
        if len(elements) >= 2:
            elements[0].click()
        else:
            logger.warning("Недостаточно элементов найдено для клика.")

    def click_input_2(self):
        elements = self.find_elements(SearhList.LOCATOR_INPUT_1)
        if len(elements) >= 2:
            elements[1].click()
        else:
            logger.warning("Недостаточно элементов найдено для клика.")

    def choose_token_to_swap(self):
        elements = self.find_elements(SearhList.LOCATOR_3_CHOOSE_TOKEN_TO_SWAP)
        if len(elements) >= 2:
            elements[1].click()
        else:
            logger.warning("Недостаточно элементов найдено для клика.")

    def click_usdt(self):
        return self.find_element(SearhList.LOCATOR_USDT).click()

    def click_usdc(self):
        return self.find_element(SearhList.LOCATOR_USDC).click()

    def swap_field_btn(self):
        return self.find_element(SearhList.LOCATOR_SWAP_FIELD_BTN).click()

    def hungreed_percent_btn(self):
        return self.find_element(SearhList.LOCATOR_100_PERCENT).click()

    def swap_btn(self):
        return self.find_element(SearhList.LOCATOR_SWAP_BTN).click()

    def get_balance(self):
        balance_elements = self.find_elements(SearhList.LOCATOR_BALANCE)
        if len(balance_elements) >= 1:
            balance_text = balance_elements[0].text
            # Удалить " ETH" из текста баланса
            balance_text = balance_text.replace(" ETH", "")

            try:
                balance_eth = float(balance_text)
                return balance_eth
            except ValueError:
                logger.warning(f"Не удалось преобразовать текст баланса в число: {balance_text}")
                return None
        else:
            logger.warning("Недостаточно элементов найдено для получения баланса.")
            return None

    getcontext().prec = 28

    def calculate_eth_to_swap(self, balance_eth, swap_eth_from, swap_eth_to, e_round):
        random_percentage = random.randint(swap_eth_from, swap_eth_to)
        eth_balance_dec = Decimal(balance_eth)
        random_percentage_dec = Decimal(random_percentage) / Decimal(100)
        random_value = random_percentage_dec * eth_balance_dec
        random_value_rounded = random_value.quantize(Decimal('1.' + ('0' * e_round)))
        logger.info(f"Баланс: {yellow}{balance_eth} ETH{purple}; Свапаю: {yellow}{random_percentage}%{purple} = {yellow}{random_value_rounded} ETH{reset}")
        return random_value_rounded

    def shitcoin_value(self):
        random_gas_value = random.uniform(shit_eth_from, shit_eth_to)
        formatted_amount = "{:.7f}".format(random_gas_value)
        print(formatted_amount)
        element = self.find_element(SearhList.LOCATOR_INPUT_1)
        element.clear()
        for char in formatted_amount:
            element.send_keys(char)
            time.sleep(0.1)
        time.sleep(5)

    def paste_eth_value(self, random_value_rounded):
        random_value_rounded_str = str(random_value_rounded)
        return self.find_element(SearhList.LOCATOR_INPUT_1).send_keys(random_value_rounded_str)

    def unlock_usdc(self):
        return self.find_unlock(SearhList.LOCATOR_UNLOCK_USDC).click()

    def unlock_usdt(self):
        return self.find_unlock(SearhList.LOCATOR_UNLOCK_USDT).click()

    def click_random_coin(self):
        try:
            token_list = [
                (0, SearhList.LOCATOR_MEOW),
                (1, SearhList.LOCATOR_AAI),
                (2, SearhList.LOCATOR_HOLD),
                (3, SearhList.LOCATOR_CHEEMS),
                (4, SearhList.LOCATOR_SIS),
                (5, SearhList.LOCATOR_SOL),
                (6, SearhList.LOCATOR_WLD),
                (7, SearhList.LOCATOR_TON),
                (8, SearhList.LOCATOR_MAV),
                (9, SearhList.LOCATOR_SHIB),
                (10, SearhList.LOCATOR_LMAO),
            ]

            # Выбираем случайный локатор из списка
            random_token_index, random_token_locator = random.choice(token_list)

            # Отправляем текст выбранного токена в поле ввода
            random_token_element = self.find_element(*random_token_locator)
            random_token_element_text = random_token_element.text
            self.find_element(SearhList.INPUT_TOKEN_FROM).send_keys(random_token_element_text)

            # Задержка для дожидания загрузки элемента
            time.sleep(1)

            # Перезагружаем случайно выбранный элемент после задержки
            random_token_element = self.find_element(*random_token_locator)

            # Кликаем на перезагруженном элементе
            random_token_element.click()
        except ValueError as e:
            logger.info(f'Словил ошибку {e}')




def eth_to_random_coin(driver):
    try:
        logger.info(f"Начинаю свап ETH to RANDOM COIN")
        rnd = Syncswapactions(driver)
        rnd.open_website()
        rnd.choose_token_to_swap()
        rnd.click_random_coin()
        rnd.shitcoin_value()
        rnd.swap_btn()
        mm_submit_thx(driver)
    except Exception as e:
        logger.error(f"Ошибка в модуле: ETH to RANDOM COIN: {e}")


def eth_to_usdc(driver):
    try:
        logger.info(f"Начинаю свап ETH to USDC")
        usdc = Syncswapactions(driver)
        usdc.open_website()
        balance_eth = usdc.get_balance()
        random_value_rounded = usdc.calculate_eth_to_swap(balance_eth, swap_eth_from, swap_eth_to, e_round)
        usdc.paste_eth_value(random_value_rounded)
        usdc.swap_btn()
        mm_submit_thx(driver)
    except Exception as e:
        logger.error(f"Ошибка в модуле: ETH to USDC{e}")


def usdc_to_eth(driver):
    try:
        logger.info(f"Начинаю свап USDC to ETH")
        usdc2 = Syncswapactions(driver)
        usdc2.open_website()
        usdc2.swap_field_btn()
        sleep(2)
        usdc2.hungreed_percent_btn()
        try:
            usdc2.unlock_usdc()
            mm_unclock_token(driver)
            usdc2.open_website()
            usdc2.swap_field_btn()
            sleep(4)
            usdc2.hungreed_percent_btn()
            sleep(1)
        except:
            pass
        usdc2.swap_btn()
        mm_submit_thx(driver)
    except Exception as e:
        logger.error(f"Ошибка в модуле: USDC to ETH{e}")


def eth_to_usdt(driver):
    try:
        logger.info(f"Начинаю свап ETH to USDT")
        usdt = Syncswapactions(driver)
        usdt.open_website()
        usdt.choose_token_to_swap()
        usdt.click_usdt()
        balance_eth = usdt.get_balance()
        random_value_rounded = usdt.calculate_eth_to_swap(balance_eth, swap_eth_from, swap_eth_to, e_round)
        usdt.paste_eth_value(random_value_rounded)
        usdt.swap_btn()
        mm_submit_thx(driver)
    except Exception as e:
        logger.error(f"Ошибка в модуле: ETH to USDT{e}")


def usdt_to_eth(driver):
    try:
        logger.info(f"Начинаю свап USDT to ETH")
        usdt2 = Syncswapactions(driver)
        usdt2.open_website()
        usdt2.choose_token_to_swap()
        usdt2.click_usdt()
        usdt2.swap_field_btn()
        sleep(2)
        usdt2.hungreed_percent_btn()
        try:
            usdt2.unlock_usdt()
            mm_unclock_token(driver)
            usdt2.open_website()
            usdt2.choose_token_to_swap()
            usdt2.click_usdt()
            usdt2.swap_field_btn()
            sleep(4)
            usdt2.hungreed_percent_btn()
            sleep(1)
        except:
            pass
        usdt2.swap_btn()
        mm_submit_thx(driver)
    except Exception as e:
        logger.error(f"Ошибка в модуле: USDT to ETH{e}")


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


def swap_func(driver):
    function = [usdc_cycle, usdt_cycle]
    random_swap = random.choice(function)
    random_swap(driver)


def swap(driver, usdc_mode, usdt_mode):
    if usdt_mode:
        usdt_to_eth(driver)
    if usdc_mode:
        usdc_to_eth(driver)


def syncswap(driver):
    try:
        number_of_repeats = random.randint(SYNC_REPEATS[0], SYNC_REPEATS[1])
        logger.info(f"Начинаю работу с модулем: {white}SyncSwap")
        sync = Syncswapactions(driver)
        sync.open_website()
        sync.close_welcome()
        sync.connect_wallet()
        sync.choose_mm()
        mm_connect(driver)
        sleep(2)
        swap(driver, usdc_mode, usdt_mode)
        for repetition in range(number_of_repeats):
            try:
                swap_func(driver)
            except:
                break
            delay_between_repeats = random.randint(INTRA_DELAY[0], INTRA_DELAY[1])
            logger.info(f"Повтор {yellow}{repetition + 1}/{number_of_repeats}{reset}{purple}. Следующий запуск через: "f"{yellow}{delay_between_repeats}{reset}{purple} секунд.")
            time.sleep(delay_between_repeats)
    except Exception as e:
        logger.error(f"Ошибка в модуле: SyncSwap {e}")


def syncswap_separate(driver):
    try:
        logger.info(f"Начинаю работу с модулем: {white}SyncSwap")
        sync = Syncswapactions(driver)
        sync.open_website()
        sync.close_welcome()
        sync.connect_wallet()
        sync.choose_mm()
        mm_connect(driver)
        sleep(2)
        eth_to_random_coin(driver)
    except Exception as e:
        logger.error(f"Ошибка в модуле: SyncSwap {e}")