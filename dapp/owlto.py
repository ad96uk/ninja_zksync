import time
from helpers.general import *
from helpers.console import *
from helpers.mm import *


def owlto_old(driver):
    try:
        timex = clock()
        print(f"{timex}{module} Начинаю работу с модулем 'OWLTO'")
        driver.get("https://owlto.finance/rewards")
        time.sleep(1000000)

        driver.find_element(By.CSS_SELECTOR, "#app > div > div.top_bar > div.top_bar_right > div.wallet > div > button").click()
        #print(1)
        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, "#app > div > div.top_bar > div:nth-child(3) > div.wallet > div > div:nth-child(2) > div.wallet-group > div:nth-child(1)").click()
        #print(2)
        time.sleep(1)

        mm_connect(driver)

        driver.find_element(By.CSS_SELECTOR, "#app > div > div.top_bar > div.top_bar_right > div.signIn.new").click()
        #print(3)
        time.sleep(2)

        wait = WebDriverWait(driver, 10)
        checkin_element = wait.until(EC.presence_of_element_located((By.XPATH, '//img[@alt="checkin"]')))
        checkin_element.click()

        mm_aprove_chain(driver)

        driver.get("https://owlto.finance/rewards")
        time.sleep(2)

        driver.find_element(By.CSS_SELECTOR, "#app > div > div.top_bar > div.top_bar_right > div.signIn.new").click()
        # print(3)
        time.sleep(2)

        wait = WebDriverWait(driver, 10)
        checkin_element = wait.until(EC.presence_of_element_located((By.XPATH, '//img[@alt="checkin"]')))
        checkin_element.click()

        mm_submit_thx(driver)

        time.sleep(20000)

    except Exception as e:
        timex = clock()
        print(f"{timex}{error} Ошибка в работе модуля 'OWLTO' {e}")


#ООП
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://owlto.finance/rewards"

    def open_website(self):
        self.driver.get(self.url)

    def find_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except TimeoutException:
            logger.error(f"Не удалось найти элемент: {e}")
            return None

class SearhList:
    # Действия на помойке
    LOCATOR_OW_1 = (By.XPATH, "//*[text()='Connect Wallet']")
    LOCATOR_OW_2 = (By.XPATH, "//*[text()='MetaMask']")
    LOCATOR_OW_3 = (By.XPATH, '//div[@class="signIn new"]')
    LOCATOR_OW_4 = (By.XPATH, '//img[@alt="checkin"]')


class OwltoActions(BasePage):
    @property
    def click_1(self):
        return self.find_element(SearhList.LOCATOR_OW_1).click()

    @property
    def click_2(self):
        return self.find_element(SearhList.LOCATOR_OW_2).click()

    @property
    def click_3(self):
        try:
            self.find_element(SearhList.LOCATOR_OW_3).click()
        except:
            logger.info("Активность на сегодня уже выполнена")

    @property
    def click_4(self):
        return self.find_element(SearhList.LOCATOR_OW_4).click()


def owlto_repeat(driver):
    try:
        owlto_y = OwltoActions(driver)
        owlto_y.click_3
        owlto_y.click_4
        mm_submit_thx(driver)
    except:
        logger.info("Активность на сегодня уже выполнена")
def owlto(driver):
    try:
        number_of_repeats = random.randint(OWLTO_REPEATS[0], OWLTO_REPEATS[1])
        logger.info(f"Начинаю работу с модулем {white}owlto{reset}")
        owlto_x = OwltoActions(driver)
        owlto_x.open_website()
        owlto_x.click_1
        owlto_x.click_2
        mm_connect(driver)
        for repetition in range(number_of_repeats):
            owlto_repeat(driver)
            delay_between_repeats = random.randint(INTRA_DELAY[0], INTRA_DELAY[1])
            logger.info(f"Повтор {yellow}{repetition + 1}/{number_of_repeats}{reset}{purple}. Следующий запуск через: "f"{yellow}{delay_between_repeats}{reset}{purple} секунд.")
            time.sleep(delay_between_repeats)
    except Exception as e:
        logger.error(f"Произошла ошибка в работе модуля owlto: {e}")