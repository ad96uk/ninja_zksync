from helpers.general import *
from helpers.console import *
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from helpers.mm import get_thx

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.mm_url = "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html"

    def open_wallet(self):
        try:
            logger.info(f"Начинаю работу с модулем {white}SEND TO OKX")
            self.driver.get(self.mm_url)
        except Exception as e:
            logger.error(f"Ошибка открытия Metamask: {e}")

    def find_element(self, locator):
        element = WebDriverWait(self.driver, timeout=10).until(
            EC.visibility_of_element_located(locator)
        )
        return element

    def swith_tab(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def swith_back_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[0])


class SearchList:
    LOCATOR_1_SEND_BTN = (By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div[1]/div/div[2]/button[2]")
    LOCATOR_2_INPUT_ADRESS = (By.CSS_SELECTOR, "#app-content > div > div.mm-box.main-container-wrapper > div > div.ens-input.send__to-row > div > input")
    LOCATOR_3_INPUT_AMOUNT = (By.CSS_SELECTOR, "#app-content > div > div.mm-box.main-container-wrapper > div > div.page-container__content > div > div:nth-child(2) > div.send-v2__form-field-container > div.send-v2__form-field > div > div > div.unit-input__input-container > input")
    LOCATOR_4_MAX_BTN = (By.XPATH, "/html/body/div[1]/div/div[3]/div/div[3]/div/div[2]/div[1]/button/div")
    LOCATOR_5_COUNTINUE_BTN = (By.XPATH, "/html/body/div[1]/div/div[3]/div/div[4]/footer/button[2]")
    LOCATOR_6_BALANCE = (By.XPATH, "//span[contains(@class, 'mm-box') and contains(@class, 'mm-text') and contains(@class, 'currency-display-component__text') and contains(@class, 'mm-text--inherit') and contains(@class, 'mm-text--ellipsis') and contains(@class, 'mm-box--color-text-default')]")
    LOCATOR_7_EDIT_GAS_BTN = (By.XPATH, "/html/body/div[1]/div/div[3]/div/div[3]/div[2]/div[2]/div/div/div[1]/div[1]/div/h6[1]/div/button")
    LOCATOR_8_LOW_GAS_BTN = (By.XPATH, "/html/body/div[2]/div/div/section/div[2]/div/div/div[1]/button[1]")
    LOCATOR_9_SEND_BTN = (By.XPATH, "/html/body/div[1]/div/div[3]/div/div[3]/div[3]/footer/button[2]")
    LOCATOR_10_SPAM = (By.XPATH, "/html/body/div[2]/div/div/section/div[1]/div/button/span")


class SendActions(BasePage):

    def find_current_balance(self):
        eth_balance_str = self.find_element(SearchList.LOCATOR_6_BALANCE).text
        try:
            eth_balance = float(eth_balance_str)
        except ValueError:
            logger.error(f"Не смог конвертировать полученный баланс в число: {eth_balance_str}")
            return 0
        return eth_balance

    def calculate_percent(self, eth_balance, e_round):
        eth_balance = Decimal(str(eth_balance))
        # Использование переменной из файла settings.py
        eth_to_leave_random = Decimal(
            str(round(random.uniform(float(ETH_TO_LEAVE[0]), float(ETH_TO_LEAVE[1])), e_round)))
        eth_to_leave_random = eth_to_leave_random.quantize(Decimal('1e-{0}'.format(e_round)), rounding=ROUND_DOWN)

        amount_to_send = eth_balance - eth_to_leave_random
        logger.info(f"Баланс: {yellow}{eth_balance}{purple} ETH; Сумма к отправке {yellow}{amount_to_send}{purple} ETH")
        return amount_to_send
    def click_send_btn(self):
        self.find_element(SearchList.LOCATOR_1_SEND_BTN).click()

    def send_to_okx_in(self, current_cycle):
        try:
            with open('data/wallets.txt', 'r') as wallets_file:
                wallets = wallets_file.read().splitlines()
            with open('data/okx_address.txt', 'r') as okx_address_file:
                okx_addresses = okx_address_file.read().splitlines()

            if len(wallets) != len(okx_addresses):
                logger.error("Количество кошельков и адресов OKX не совпадает")
                return

            okx_address = okx_addresses[current_cycle - 1]
            try:
                input_element = self.find_element(SearchList.LOCATOR_2_INPUT_ADRESS)
                if input_element:  # Проверка, что элемент найден
                    input_element.clear()
                    input_element.send_keys(okx_address)
                    logger.info(f"Адрес {okx_address} OKX для кошелька #{current_cycle}")
                else:
                    logger.error("Элемент для ввода адреса не был найден.")
            except NoSuchElementException:
                logger.error("Элемент для ввода адреса не найден.")

        except Exception as e:
            logger.error(f"Неизвестная ошибка: {e}")

    def paste_amount_to_send(self, amount_to_send):
        self.find_element(SearchList.LOCATOR_3_INPUT_AMOUNT).send_keys(str(amount_to_send))

    def click_continue_btn(self):
        self.find_element(SearchList.LOCATOR_5_COUNTINUE_BTN).click()

    def click_edit_gas(self):
        self.find_element(SearchList.LOCATOR_7_EDIT_GAS_BTN).click()

    def click_low_gas(self):
        self.find_element(SearchList.LOCATOR_8_LOW_GAS_BTN).click()

    def click_submit_send_btn(self):
        self.find_element(SearchList.LOCATOR_9_SEND_BTN).click()

    def close_mm_spam(self):
        try:
            self.find_element(SearchList.LOCATOR_10_SPAM).click()
        except:
            pass


def send_to_okx(driver, current_cycle):
    try:
        send = SendActions(driver)
        send.open_wallet()
        send.close_mm_spam()
        eth_balance = send.find_current_balance()
        if eth_balance <= 0:
            logger.error("Баланс равен нулю или не удалось получить баланс. Прекращение работы функции.")
            return

        amount_to_send = send.calculate_percent(eth_balance, e_round)
        sleep(1)
        send.click_send_btn()
        sleep(1)
        send.send_to_okx_in(current_cycle)
        sleep(1)
        send.paste_amount_to_send(amount_to_send)
        sleep(2)
        send.click_continue_btn()
        sleep(2)
        #input("Press Enter чтобы отправить")
        send.click_submit_send_btn()
        sleep(15)
        get_thx(driver)
    except Exception as e:
        logger.error(f"Произошла ошибка в работе модуля send_to_okx1: {e}")