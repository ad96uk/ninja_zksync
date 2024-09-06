from helpers.console import *
from helpers.mm import mm_connect, mm_submit_thx, mm_unclock_token, log_in
from settings import INTRA_DELAY, DMAIL_REPEAT


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://mail.dmail.ai/login?path=%2Finbox"

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

    def find_alert(self, locator):
            try:
                element = WebDriverWait(self.driver, timeout=3).until(
                    EC.visibility_of_element_located(locator)
                )
                return element
            except:
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
    LOCATOR_CHOOSE_MM = (By.XPATH, "//li[span[text()='MetaMask'] and p[@class='metamask']]")
    LOCATOR_WELCOM_ALERT = (By.XPATH, "//a[@class='red-btn']")
    LOCATOR_COMPOSE = (By.XPATH, "//div[@class='li']/span[@class='name'][text()='Compose']")
    LOCATOR_INPUT_TO = (By.XPATH, "//input[@type='text' and @placeholder='Default Address/NFT Domain/Email Address/DID' and @value='']")
    LOCATOR_5_INPUT_SUBJECT = (By.XPATH, "//input[@type='text' and @placeholder='Enter the subject' and @value='']")
    LOCATOR_6_INPUT_MSG = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[5]/div/div/div/div[2]/div[1]/p[1]')
    LOCATOR_7_SEND = (By.XPATH, "//a[@class='red-btn send']/span[text()='Send']")
    LOCATOR_8_AI = (By.XPATH, "//span[@class='quick-title' and @data-title='AI Assistant']")
    LOCATOR_9_SUBJECT_TO_AI = (By.XPATH, "//input[@type='text' and @placeholder='Briefly enter what do you want to write']")
    LOCATOR_10_GENERATE_RESPONSE = (By.XPATH, "//a[@class='btn ' and .//span[contains(@class, 'MuiCircularProgress')]]")
    LOCATOR_11_INSERT_RESPONSE = (By.XPATH, "//a[contains(@class, 'btn-reply') and .//*[name()='svg']]")


class DmailActions(BasePage):

    def close_alert(self):
        try:
            alert = self.driver.switch_to.alert
            alert.dismiss()
        except:
            pass

    def choose_mm(self):
        return self.find_element(SearchList.LOCATOR_CHOOSE_MM).click()

    def welcom_alert(self):
        for _ in range(4):
            try:
                self.find_alert(SearchList.LOCATOR_WELCOM_ALERT).click()
            except:
                pass

    def compose(self):
        return self.find_element(SearchList.LOCATOR_COMPOSE).click()

    def input_to(self):
        with open("data/dmail/1.txt", 'r') as file:
            recipient_adress = file.read().splitlines()
            random_recipient = random.choice(recipient_adress)
            self.find_element(SearchList.LOCATOR_INPUT_TO).send_keys(random_recipient)

        with open ("data/dmail/1.txt", 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if line.strip() !=random_recipient:
                    file.write(line)
            file.truncate()

    def input_subject(self):
        with open('data/dmail/2.txt', 'r') as file:
            theme = file.read().splitlines()
            random_theme = random.choice(theme)
            self.find_element(SearchList.LOCATOR_5_INPUT_SUBJECT).send_keys(random_theme)

        with open('data/dmail/2.txt', 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if line.strip != random_theme:
                    file.write(line)
            file.truncate()

    def input_msg(self):
        with open('data/dmail/3.txt', 'r') as file:
            msg = file.read().splitlines()
            random_msg = random.choice(msg)
            self.find_element(SearchList.LOCATOR_6_INPUT_MSG).send_keys(random_msg)

        with open('data/dmail/3.txt', 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if line.strip != random_msg:
                    file.write(line)
            file.truncate()

    def send(self):
        return self.find_element(SearchList.LOCATOR_7_SEND).click()

    def ai(self):
        return self.find_element(SearchList.LOCATOR_8_AI).click()

    def generate_response(self):
        return self.find_element(SearchList.LOCATOR_10_GENERATE_RESPONSE).click()

    def insert_response(self):
        return self.find_element(SearchList.LOCATOR_11_INSERT_RESPONSE).click()

    def input_ai(self):
        with open('data/dmail/3.txt', 'r') as file:
            msg = file.read().splitlines()
            random_msg = random.choice(msg)
            self.find_element(SearchList.LOCATOR_5_INPUT_SUBJECT).send_keys(random_msg)

        with open('data/dmail/3.txt', 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if line.strip != random_msg:
                    file.write(line)
            file.truncate()


def repeat_dmail(driver):
    try:
        rd = DmailActions(driver)
        rd.compose()
        rd.welcom_alert()
        rd.input_to()
        rd.input_subject()
        rd.input_msg()
        rd.send()
        mm_submit_thx(driver)
        rd.close_alert()
    except Exception as e:
        logger.error(f"Ошибка в repeat_dmail: {e}")


def dmail(driver):
    try:
        logger.info(f"Начинаю работу с модулем {white}DMAIL")
        number_of_repeats = random.randint(DMAIL_REPEAT[0], DMAIL_REPEAT[1])
        dm = DmailActions(driver)
        dm.open_website()
        dm.choose_mm()
        mm_connect(driver)
        try:
            log_in(driver)
        except:
            pass
        # mm_connect(driver)
        time.sleep(2)
        dm.welcom_alert()
        for repetition in range(number_of_repeats):
            try:
                repeat_dmail(driver)
            except:
                break
            delay_between_repeats = random.randint(INTRA_DELAY[0], INTRA_DELAY[1])
            logger.info(f"Повтор {yellow}{repetition + 1}/{number_of_repeats}{reset}{purple}. Следующий запуск через: "f"{yellow}{delay_between_repeats}{reset}{purple} секунд.")
            time.sleep(delay_between_repeats)
    except Exception as e:
        logger.error(f"Ошибка в dmail: {e}")
