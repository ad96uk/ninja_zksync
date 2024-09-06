from helpers.console import *
from helpers.mm import get_thx
from settings import INTRA_DELAY


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.mm_url = "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html"

    def open_wallet_page(self):
        try:
            self.driver.get(self.mm_url)
        except Exception as e:
            logger.error(f"Ошибка открытия кошелька: {e}")
        return

    def find_element(self, locator):
            try:
                element = WebDriverWait(self.driver, timeout=10).until(
                    EC.visibility_of_element_located(locator)
                )
                return element
            except Exception as e:
                logger.error(f"Не удалось найти элемент: {e}\n{locator}")
                return None

    def swith_tab(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def swith_back_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def find_alert(self, locator):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located(locator)
        )
        return element

class SearhList:
    LOCATOR_SEND_BTN = (By.XPATH, "//button[@data-testid='eth-overview-send' and contains(p/text(), 'Send')]")
    LOCATOR_INPUT_ADRESS = (By.XPATH, "//input[@placeholder='Enter public address (0x) or ENS name' and @class='ens-input__wrapper__input']")
    LOCATOR_INPUT_AMOUNT = (By.XPATH, "//input[@data-testid='currency-input']")
    LOCATOR_NEXT = (By.XPATH, "//button[@data-testid='page-container-footer-next' and contains(text(), 'Next')]")
    LOCATOR_CONFIRM = (By.XPATH, "//button[@data-testid='page-container-footer-next' and contains(text(), 'Confirm')]")
    LOCATOR_SPAM = (By.XPATH, "/html/body/div[2]/div/div/section/div[1]/div/button/span")
    LOCATOR_MAX = (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[3]/div/div[2]/div[1]/button')

class RandonSendActions(BasePage):
    def max_btn(self):
        return  self.find_element(SearhList.LOCATOR_MAX).click()

    def send_btn(self):
        return self.find_element(SearhList.LOCATOR_SEND_BTN).click()

    def input_adress(self):
        try:
            with open('data/random_send.txt', 'r') as file:
                addresses = file.read().splitlines()
                if addresses:
                    random_address = random.choice(addresses)
                    self.find_element(SearhList.LOCATOR_INPUT_ADRESS).send_keys(random_address)

                with open('data/random_send.txt', 'w') as file:
                    for address in addresses:
                        if address != random_address:
                            file.write(address + '\n')
        except Exception as e:
            logger.error(f"Ошибка в input_address: {e}")

    def input_amount(self):




        try:
            random_amount = random.uniform(RANDOM_SEND_AMOUNT[0], RANDOM_SEND_AMOUNT[1])
            formatted_amount = "{:.7f}".format(random_amount)
            self.find_element(SearhList.LOCATOR_INPUT_AMOUNT).send_keys(formatted_amount)
        except Exception as e:
            logger.error(f"Ошибка в input_amount: {e}")

    def next_btn(self):
        return self.find_element(SearhList.LOCATOR_NEXT).click()

    def confirm_btn(self):
        return self.find_element(SearhList.LOCATOR_CONFIRM).click()

    def spam_btn(self):
        return self.find_alert(SearhList.LOCATOR_SPAM).click()


def repear_send(driver):
    try:
        rrs = RandonSendActions(driver)
        try:
            rrs.spam_btn()
        except:
            pass
        rrs.send_btn()
        rrs.input_adress()
        sleep(3)
        rrs.max_btn()
        rrs.next_btn()
        sleep(2)
        rrs.confirm_btn()
        get_thx(driver)
    except Exception as e:
        logger.error(f"Ошибка в repear_send: {e}")


def random_send(driver):
    try:
        number_of_repeats = random.randint(RANDOM_SEND_REPEATS[0], RANDOM_SEND_REPEATS[1])
        logger.info(f"Начинаю работу с {white}RANDOM SEND")
        rs = RandonSendActions(driver)
        rs.open_wallet_page()
        try:
            rs.spam_btn()
        except:
            pass
        for repetition in range(number_of_repeats):
            try:
                repear_send(driver)
            except:
                break
            delay_between_repeats = random.randint(INTRA_DELAY[0], INTRA_DELAY[1])
            logger.info(f"Повтор {yellow}{repetition + 1}/{number_of_repeats}{reset}{purple}. Следующий запуск через: "f"{yellow}{delay_between_repeats}{reset}{purple} секунд.")
            sleep(delay_between_repeats)
    except Exception as e:
        logger.error(f"Ошибка в random_send{e}")
