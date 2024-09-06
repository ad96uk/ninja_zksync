from helpers.mm import *


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://minter.merkly.com/deploy/empty"
        self.gas_url = "https://minter.merkly.com/gas"

    def open_website(self):
        self.driver.get(self.url)

    def open_gas_website(self):
        self.driver.get(self.gas_url)

    def find_elements(self, locator):
        try:
            elements = WebDriverWait(self.driver, timeout=10).until(
                EC.visibility_of_all_elements_located(locator)
            )
            return elements
        except Exception as e:
            logger.error(f"Не удалось найти элементы: {e}\n{locator}")
            return []

    def find_element(self, locator):
            try:
                element = WebDriverWait(self.driver, timeout=10).until(
                    EC.visibility_of_element_located(locator)
                )
                return element
            except Exception as e:
                logger.error(f"Не удалось найти элемент: {e}\n{locator}")
                return None


class SearhList:
    LOCATOR_MER_0 = (By.XPATH, "//a[@class='bg-[#8473ff] text-white px-4 py-2 rounded-md w-full uppercase disabled:bg-gray-500 max-w-max' and @href='/deploy/empty']")
    LOCATOR_MER_1 = (By.XPATH, "//button[contains(., 'Scroll')]")
    LOCATOR_MER_2_ZK_ICON = (By.XPATH, "//img[@src='/zksync.svg' and contains(@class, 'w-[40px]')]")
    LOCATOR_MER_3_DEPLOY = (By.XPATH, "//button[contains(@class,'bg-[#8473ff]') and contains(@class,'text-white') and contains(text(), 'DEPLOY')]")
    LOCATOR_MER_4_COUNTER = (By.XPATH, "//button[text()='Increase Counter']")
    LOCATOR_MER_5_BACK = (By.XPATH, "//button[normalize-space(text())='< Back']")
    LOCATOR_MERKLEY_INCREASE_COUNTER = (By.XPATH, "//button[contains(@class, 'bg-[#8473ff]') and contains(@class, 'text-white') and contains(@class, 'px-4') and contains(@class, 'py-2') and contains(@class, 'rounded-md') and contains(@class, 'uppercase') and text()='Increase Counter']")
    LOCATOR_TIME_MARKER = (By.XPATH, "//div[contains(@class, 'flex flex-col gap-1 bg-[#2f3146]') and contains(@class, 'w-[192px]') and contains(@class, 'p-3') and contains(@class, 'rounded-md') and contains(@class, 'mb-4')]/p[text()='Counter']")
    PREVIEW_THX = (By.XPATH, "//button[contains(@class, 'bg-[#8473ff]') and contains(@class, 'text-white') and contains(@class, 'px-4') and contains(@class, 'py-2') and contains(@class, 'rounded-md') and contains(@class, 'w-full') and contains(@class, 'uppercase')]")
    REFUEL = (By.XPATH, "//button[contains(@class, 'bg-[#8473ff]') and contains(@class, 'text-white') and contains(@class, 'px-4') and contains(@class, 'py-2') and contains(@class, 'rounded-md') and contains(@class, 'w-full') and contains(@class, 'uppercase')]")
    CONNECT_WALLET = (By.XPATH, "//button[contains(@class, 'bg-[#8473ff]') and contains(@class, 'text-white') and (contains(@class, 'px-2') or contains(@class, 'md:px-4')) and contains(@class, 'py-2') and contains(@class, 'rounded-md') and contains(text(), 'Connect Wallet')]")

class MerklyActions(BasePage):

    def preview_thx(self):
        return self.find_element(SearhList.PREVIEW_THX).click()

    def refuel(self):
        return self.find_element(SearhList.REFUEL).click()

    def connect_wallet(self):
        return self.find_element(SearhList.CONNECT_WALLET).click()

    def time_marker(self):
        try:
            wait = WebDriverWait(self.driver, 25)
            element = wait.until(EC.presence_of_element_located((SearhList.LOCATOR_TIME_MARKER)))
            #print("Элемент появился")
        except:
            pass

    @property
    def click_0(self):
        return self.find_element(SearhList.LOCATOR_MER_0).click()

    @property
    def click_1(self):
        return self.find_element(SearhList.LOCATOR_MER_1).click()

    @property
    def click_2(self):
        return self.find_element(SearhList.LOCATOR_MER_2_ZK_ICON).click()

    @property
    def click_deploy(self):
        return self.find_element(SearhList.LOCATOR_MER_3_DEPLOY).click()

    @property
    def click_counter(self):
        return self.find_element(SearhList.LOCATOR_MER_4_COUNTER).click()

    @property
    def click_back(self):
        return self.find_element(SearhList.LOCATOR_MER_5_BACK).click()

    def increase_counter(self):
        try:
            self.find_element(SearhList.LOCATOR_MERKLEY_INCREASE_COUNTER).click()
        except Exception as e:
            logger.error(f"Ошибка increase_counter{e}")

def merkly_loop(driver):
    try:
        #logger.info("Начинаю работу с функций merkly_loop")
        m1 = MerklyActions(driver)
        m1.time_marker()
        m1.increase_counter()
        mm_submit_thx(driver)
    except Exception as e:
        logger.error(f"Ошибка в работе merkly_loop:\n{e}")
        time.sleep(1000)


def send_gas(driver):
    try:
        gas = MerklyActions(driver)
        gas.open_gas_website()
        gas.connect_wallet()
        mm_connect(driver)
        gas.preview_thx()
        gas.refuel()
        mm_submit_thx(driver)
    except Exception as e:
        logger.error(f"Ошибка в send_gas: {e}")


def deploy_first_time(driver):
    try:
        number_of_repeats = random.randint(MERKLEY_REPEAT[0], MERKLEY_REPEAT[1])
        m = MerklyActions(driver)
        m.open_website()
        m.click_1
        m.click_2
        m.click_deploy
        mm_connect_merkley(driver)
        mm_connect_merkley(driver)
        mm_sigh_thx_merkley_version(driver)
        logger.info(f"{blue}Контракт создан")
        for repetition in range(number_of_repeats):
            try:
                two_in_one(driver)
            except:
                break
            delay_between_repeats = random.randint(INTRA_DELAY[0], INTRA_DELAY[1])
            logger.info(f"Повтор {yellow}{repetition + 1}/{number_of_repeats}{reset}{purple}. Следующий запуск через: "f"{yellow}{delay_between_repeats}{reset}{purple} секунд.")
            time.sleep(delay_between_repeats)
    except Exception as e:
        logger.error(f"Ошибка в deploy_first_time: {e}")


def two_in_one(driver):
    if gas_mode:
        send_gas(driver)
    if deploy_mode:
        deploy_first_time(driver)

def merkly(driver):
    try:
        logger.info(f"Начинаю работу с модулем {white}Merkly")
        two_in_one(driver)
    except Exception as e:
        logger.error(f"Ошибка в работу модуя Merkly:\n{e}")
        time.sleep(1)


