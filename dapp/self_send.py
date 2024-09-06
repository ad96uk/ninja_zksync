from helpers.general import *
from helpers.console import *
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from decimal import Decimal, getcontext
from helpers.mm import get_thx

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.mm_url = "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html"

    def open_wallet(self):
        try:
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
    LOCATOR_SS_SETINGS = (By.CSS_SELECTOR, "#app-content > div > div.mm-box.multichain-app-header.mm-box--margin-bottom-0.mm-box--display-flex.mm-box--align-items-center.mm-box--width-full.mm-box--background-color-background-alternative > div > div.mm-box.mm-box--display-flex.mm-box--justify-content-flex-end.mm-box--align-items-center > div > div > button > span")
    LOCATOR_SS_ACC = (By.XPATH, "/html/body/div[2]/div[2]/button[1]")
    LOCATOR_SS_ADRESS = (By.CSS_SELECTOR, "body > div.mm-modal > div:nth-child(3) > div > section > div.mm-box.mm-box--display-flex.mm-box--flex-direction-column.mm-box--align-items-center > div.qr-code > div.box.box--margin-bottom-6.box--flex-direction-row > div > div > button > span.mm-box.mm-text.mm-text--inherit.mm-box--color-primary-default > div")
    LOCATOR_SS_CLOSE_SETTINGS = (By.CSS_SELECTOR, "body > div.mm-modal > div:nth-child(3) > div > section > div.mm-box.mm-header-base.mm-modal-header.mm-box--display-flex.mm-box--justify-content-space-between > div.mm-box.mm-box--display-flex.mm-box--justify-content-flex-end > button")
    LOCATOR_SS_ACC_BALANCE = (By.XPATH, "//span[contains(@class, 'mm-box') and contains(@class, 'mm-text') and contains(@class, 'currency-display-component__text') and contains(@class, 'mm-text--inherit') and contains(@class, 'mm-text--ellipsis') and contains(@class, 'mm-box--color-text-default')]")
    LOCATOR_SS_SEND_BTN = (By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div[1]/div/div[2]/button[2]")
    LOCATOR_SS_INPUT_ADRESS = (By.CSS_SELECTOR, "#app-content > div > div.mm-box.main-container-wrapper > div > div.ens-input.send__to-row > div > input")
    LOCATOR_SS_INPUT_AMOUNT = (By.CSS_SELECTOR, "#app-content > div > div.mm-box.main-container-wrapper > div > div.page-container__content > div > div:nth-child(2) > div.send-v2__form-field-container > div.send-v2__form-field > div > div > div.unit-input__input-container > input")
    LOCATOR_SS_COUNTINUE_BTN = (By.XPATH, "/html/body/div[1]/div/div[3]/div/div[4]/footer/button[2]")
    LOCATOR_SS_SEND_BTN_FINAL = (By.XPATH, "/html/body/div[1]/div/div[3]/div/div[3]/div[3]/footer/button[2]")
    LOCATOR_SS_SPAM = (By.XPATH, "/html/body/div[2]/div/div/section/div[1]/div/button/span")
    LOCATOR_INPUT_ADRESS = (By.XPATH, "//input[@placeholder='Enter public address (0x) or ENS name' and @class='ens-input__wrapper__input']")


class SelfSendActions(BasePage):

    def click_settings(self):
        return self.find_element(SearchList.LOCATOR_SS_SETINGS).click()

    def click_acc(self):
        element = self.find_element(SearchList.LOCATOR_SS_ACC)
        self.driver.execute_script("arguments[0].click();", element)

    def click_adress(self):
        my_adress = self.find_element(SearchList.LOCATOR_SS_ADRESS).text
        logger.info(f"Мой адресс: {curv}{my_adress}")
        return my_adress

    def click_close_settings(self):
        return self.find_element(SearchList.LOCATOR_SS_CLOSE_SETTINGS).click()

    def check_balance(self):
        eth_balance_str = self.find_element(SearchList.LOCATOR_SS_ACC_BALANCE).text
        try:
            eth_balance = float(eth_balance_str)
        except ValueError:
            logger.error(f"Не смог конвертировать полученный баланс в число: {eth_balance_str}")
            return 0
        return eth_balance

    getcontext().prec = 28

    def calculate_percent(self, eth_balance, SEND_PERCENT, e_round, curv):
        random_percentage = random.randint(SEND_PERCENT[0], SEND_PERCENT[1])
        eth_balance_dec = Decimal(eth_balance)
        random_percentage_dec = Decimal(random_percentage) / Decimal(100)

        random_value = random_percentage_dec * eth_balance_dec

        random_value_rounded = random_value.quantize(Decimal('1.' + ('0' * e_round)))

        logger.info(f"Баланс: {yellow}{eth_balance} ETH{purple}.Случайный %: {yellow}{random_percentage}{purple}. Сумма к отправке: {yellow}{random_value_rounded} ETH.")
        return random_value_rounded

    def click_send_btn(self):
        return self.find_element(SearchList.LOCATOR_SS_SEND_BTN).click()

    def paste_my_adress(self, my_adress):
        return self.find_element(SearchList.LOCATOR_SS_INPUT_ADRESS).send_keys(my_adress)

    def paste_amount(self, random_value_rounded):
        random_value_rounded_str = str(random_value_rounded)
        return self.find_element(SearchList.LOCATOR_SS_INPUT_AMOUNT).send_keys(random_value_rounded_str)

    def click_countinue_btn(self):
        return self.find_element(SearchList.LOCATOR_SS_COUNTINUE_BTN).click()

    def click_send_final_btn(self):
        return self.find_element(SearchList.LOCATOR_SS_SEND_BTN_FINAL).click()

    def click_sclose_spam(self):
        return self.find_element(SearchList.LOCATOR_SS_SPAM).click()

    def input_adress(self):
        try:
            with open('data/random_send.txt', 'r') as file:
                addresses = file.read().splitlines()
                if addresses:
                    random_address = random.choice(addresses)
                    self.find_element(SearchList.LOCATOR_INPUT_ADRESS).send_keys(random_address)

                with open('data/random_send.txt', 'w') as file:
                    for address in addresses:
                        if address != random_address:
                            file.write(address + '\n')
        except Exception as e:
            logger.error(f"Ошибка в input_address: {e}")



def repeat_ss(driver):
    try:
        ss = SelfSendActions(driver)
        ss.open_wallet()
        try:
            ss.click_sclose_spam()
        except:
            pass
        ss.click_settings()
        ss.click_acc()
        # my_adress = ss.click_adress()
        ss.click_close_settings()
        eth_balance = ss.check_balance()
        random_value_rounded = ss.calculate_percent(eth_balance, SEND_PERCENT, e_round, curv)
        ss.click_send_btn()
        ss.input_adress()
        ss.paste_amount(random_value_rounded)
        sleep(1)
        ss.click_countinue_btn()
        sleep(2)
        try:
            ss.click_send_final_btn()
            get_thx(driver)
        except:
            logger.error("Недостаточный баланс")
    except Exception as e:
        logger.error(f"Ошибка в REPEAT SELF SEND:{e}")


def self_send(driver):
    try:
        number_of_repeats = random.randint(SS_REPEATS[0], SS_REPEATS[1])
        ss = SelfSendActions(driver)
        logger.info(f"Начинаю работу с модулем {white}SELF SEND")
        ss.open_wallet()
        try:
            ss.click_sclose_spam()
        except:
            pass
        for repetition in range(number_of_repeats):
            try:
                repeat_ss(driver)
            except:
                break
            delay_between_repeats = random.randint(INTRA_DELAY[0], INTRA_DELAY[1])
            logger.info(f"Повтор {yellow}{repetition + 1}/{number_of_repeats}{reset}{purple}. Следующий запуск через: "f"{yellow}{delay_between_repeats}{reset}{purple} секунд.")
            time.sleep(delay_between_repeats)
    except Exception as e:
        logger.error(f"Произошла ошибка в модуле SELF SEND {e}")
