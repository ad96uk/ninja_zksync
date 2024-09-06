from time import sleep
from helpers.console import *
from helpers.mm import mm_connect, mm_submit_thx
from selenium.webdriver.common.action_chains import ActionChains
from dapp.eralend_random_thx_beetwen_the_loop import separate_loop


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://app.eralend.com/"

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


class SearhList:
    LOCATOR_ERA_1_CNT_WLT = (By.XPATH, "//button[contains(text(), 'Connect wallet')]")
    LOCATOR_ERA_2_SHADOW_HOST = (By.TAG_NAME, "onboard-v2")
    LOCATOR_ERA_3_TICK_BOX = (By.CSS_SELECTOR, "input.svelte-tz7ru1")
    LOCATOR_ERA_4_MANAGE_BTN = (By.XPATH, "//button[contains(@class, 'MuiButton-root') and contains(@class, 'MuiButton-contained') and contains(@class, 'MuiButton-containedPrimary') and contains(@class, 'MuiButton-sizeLarge') and contains(@class, 'MuiButton-containedSizeLarge') and contains(@class, 'MuiButton-fullWidth') and contains(@class, 'MuiButtonBase-root') and contains(@class, 'css-12nczmx') and @tabindex='0' and @type='button' and text()='Manage']")
    LOCATOR_ERA_5_WITHDRAW_MENU_BTN = (By.XPATH, "//span[contains(@class, 'mm-tab-content') and text()='WITHDRAW']")
    LOCATOR_ERA_6_WITHDRAW_MAX_BTN = (By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 css-10yuwrp' and @aria-label='Max Withdrawl' and text()='MAX']")
    LOCATOR_ERA_7_WITHDRAW_BTN = (By.XPATH, "//button[contains(@class, 'MuiButton-root') and contains(@class, 'MuiButton-contained') and contains(@class, 'MuiButton-containedPrimary') and contains(@class, 'MuiButton-sizeLarge') and contains(@class, 'MuiButton-containedSizeLarge') and contains(@class, 'MuiButton-fullWidth') and contains(@class, 'MuiButtonBase-root') and contains(@class, 'css-10qb2nd') and @tabindex='0' and @type='submit' and text()='Withdraw']")
    LOCATOR_ERA_8_TOOGLE = (By.XPATH, "//span[contains(@class, 'MuiSwitch-thumb') and not(@aria-hidden='true')]")
    LOCATOR_ERA_9_75_IN = (By.XPATH, "//p[text()='75%']")
    LOCATOR_ERA_8_SUPPLY = (By.XPATH, "//button[contains(@class, 'MuiButton-root') and contains(@class, 'MuiButton-contained') and contains(@class, 'MuiButton-containedPrimary') and contains(@class, 'MuiButton-sizeLarge') and contains(@class, 'MuiButton-containedSizeLarge') and contains(@class, 'MuiButton-fullWidth') and contains(@class, 'MuiButtonBase-root') and contains(@class, 'css-10qb2nd') and @tabindex='0' and @type='submit' and contains(text(), 'Supply')]")
    LOCATOR_ERA_10_MAX_IN = (By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 css-1s0953s' and text()='MAX']")
    LOCATOR_ERA_11_BALANCE = (By.XPATH, "//input[@type='number' and @placeholder='0.00' and @class='css-13k9r7c']")


class EraActions(BasePage):
    def connect_wallet_click(self):
        return self.find_element(SearhList.LOCATOR_ERA_1_CNT_WLT).click()

    def calucate_percent_to_dep(self):
        self.find_element(SearhList.LOCATOR_ERA_10_MAX_IN).click()
        input_element = self.find_element(SearhList.LOCATOR_ERA_11_BALANCE)
        input_value = float(input_element.get_attribute('value'))

        random_percentage = random.randint(DEP[0], DEP[1])
        random_value = (random_percentage / 100) * input_value

        random_value_rounded = round(random_value, e_round)
        logger.info(f"Делаю депозит: {yellow}{random_percentage}%{purple} = {yellow}{random_value_rounded}eth")
        return random_value_rounded

    def paste_balance_to_deposit(self, random_value_rounded):
        element = self.find_element(SearhList.LOCATOR_ERA_11_BALANCE)
        element.clear()
        sleep(2)
        element.send_keys(random_value_rounded)

    def click_titck_box(self):
        try:
            shadow_host_locator = SearhList.LOCATOR_ERA_2_SHADOW_HOST
            shadow_host = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(shadow_host_locator)
            )
            script = """
            var shadowHost = arguments[0];
            var shadowRoot = shadowHost.shadowRoot;
            var targetElement = shadowRoot.querySelector('input.svelte-tz7ru1');
            if (targetElement) {
                targetElement.click();
            } else {
                return 'Элемент не найден';
            }
            """
            result = self.driver.execute_script(script, shadow_host)
            if result:
                print(result)
        except Exception as e:
            logger.error(f"Ошибка click_titck_box: {e}")

    def click_mm_icon(self):
        try:
            shadow_host_locator = SearhList.LOCATOR_ERA_2_SHADOW_HOST
            shadow_host = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(shadow_host_locator)
            )
            # Используем execute_script для выполнения клика на элемент внутри shadowRoot
            script = """
            var shadowHost = arguments[0];
            var shadowRoot = shadowHost.shadowRoot;
            var targetElement = shadowRoot.querySelector('.name.svelte-1vlog3j'); // Исправленный селектор для поиска элемента
            if (targetElement) {
                targetElement.click();
                return;
            } else {
                return 'Элемент не найден';
            }
            """
            result = self.driver.execute_script(script, shadow_host)
            if result:
                print(result)
        except Exception as e:
            logger.error(f"Ошибка click_mm_icon: {e}")

    def click_manage_btn(self):
        try:
            element = self.find_element(SearhList.LOCATOR_ERA_4_MANAGE_BTN)
            element.click()  # Используем элемент напрямую, без индексации
        except Exception as e:
            logger.error(f"Ошибка click_manage_btn: {e}")

    def click_withdraw_menu(self):
        element = self.find_element(SearhList.LOCATOR_ERA_5_WITHDRAW_MENU_BTN)
        action = ActionChains(self.driver)
        action.move_to_element(element).click().perform()

    def click_withdraw_max(self):
        element = self.find_element(SearhList.LOCATOR_ERA_6_WITHDRAW_MAX_BTN)
        self.driver.execute_script("arguments[0].click();", element)

    def click_withdraw_btn(self):
        try:
            element = self.driver.find_element(
                *SearhList.LOCATOR_ERA_7_WITHDRAW_BTN)
            action = ActionChains(self.driver)
            action.move_to_element(element).click().perform()
        except Exception as e:
            print(f"Ошибка при попытке кликнуть на кнопку Withdraw: {e}")

    def click_75_per(self):
        elements = self.find_element(SearhList.LOCATOR_ERA_9_75_IN)
        self.driver.execute_script("arguments[0].click();", elements)

    def click_supply_btn(self):
        element = self.find_element(SearhList.LOCATOR_ERA_8_SUPPLY)
        action = ActionChains(self.driver)
        action.move_to_element(element).click().perform()

    def click_toogle_btn(self):
        try:
            element = self.driver.find_element(
                *SearhList.LOCATOR_ERA_8_TOOGLE)
            self.driver.execute_script("arguments[0].click();", element)
            mm_submit_thx(self.driver)
        except Exception as e:
            logger.error(f"Ошибка в click_toogle_btn: {e}")


def era_withdraw(driver):
    logger.info("Начинаю withdraw")
    try:
        w = EraActions(driver)
        w.open_website()
        time.sleep(5)
        w.click_manage_btn()
        sleep(3)
        w.click_withdraw_menu()
        w.click_withdraw_max()
        w.click_withdraw_btn()
        sleep(4)
        mm_submit_thx(driver)
    except Exception as e:
        logger.error(f"Ошибка в withdraw: {e}")


def era_deposit(driver):
    logger.info("Начинаю deposit")
    try:
        d = EraActions(driver)
        d.open_website()
        time.sleep(6)
        d.click_manage_btn()
        sleep(5)
        random_value_rounded = d.calucate_percent_to_dep()
        d.paste_balance_to_deposit(random_value_rounded)
        d.click_supply_btn()
        sleep(8)
        mm_submit_thx(driver)
        sleep(9)
    except Exception as e:
        logger.error(f"Ошибка в deposit: {e}")


def era_deposit_1(driver):
    logger.info("Начинаю deposit first time")
    try:
        d = EraActions(driver)
        d.open_website()
        time.sleep(6)
        d.click_manage_btn()
        sleep(5)
        random_value_rounded = d.calucate_percent_to_dep()
        d.paste_balance_to_deposit(random_value_rounded)
        sleep(1)
        d.click_supply_btn()
        sleep(9)
        mm_submit_thx(driver)
        sleep(9)
    except Exception as e:
        logger.error(f"Ошибка в deposit: {e}")


def era_loop(driver):
    era_deposit(driver)
    y_time = random.randint(INTRA_DELAY[0], INTRA_DELAY[1])
    logger.info(f"Сплю: {y_time} секунд")
    sleep(y_time)
    separate_loop(driver)
    era_withdraw(driver)


def era_connect_wallet(driver):
    try:
        m = EraActions(driver)
        m.connect_wallet_click()
        m.click_titck_box()
        m.click_mm_icon()
        mm_connect(driver)
    except:
        logger.error("Ошибка подключения кошелька eralend")


locator = (By.CLASS_NAME, "MuiButton-containedPrimary")


def wait_for_element(driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//script[@src="/_next/static/chunks/pages/account-36e4fd144e6da1cf.js"]'))
        )
        sleep(0.5)
    except TimeoutException:
        print("Элемент не был найден в течение 10 секунд")


def eralend(driver):
    try:
        number_of_repeats = random.randint(ERA_REPEATS[0], ERA_REPEATS[1])
        logger.info(f"Начинаю работу с модулем:{white} EraLend")
        m = EraActions(driver)
        m.open_website()

        wait_for_element(driver)        # time.sleep(9)

        era_connect_wallet(driver)
        sleep(3)
        era_deposit_1(driver)

        separate_loop(driver)

        x_time = random.randint(INTRA_DELAY[0], INTRA_DELAY[1])
        logger.info(f"Сплю: {x_time} секунд")
        sleep(x_time)
        era_withdraw(driver)
        xy_time = random.randint(INTRA_DELAY[0], INTRA_DELAY[1])
        logger.info(f"Сплю: {xy_time} секунд")
        sleep(xy_time)

        separate_loop(driver)

        for repetition in range(number_of_repeats):
            try:
                era_loop(driver)
            except:
                break
            delay_between_repeats = random.randint(INTRA_DELAY[0], INTRA_DELAY[1])
            logger.info(f"Повтор {yellow}{repetition + 1}/{number_of_repeats}{reset}{purple}. Следующий запуск через: "f"{yellow}{delay_between_repeats}{reset}{purple} секунд.")
            time.sleep(delay_between_repeats)
    except Exception as e:
        logger.error(f"Ошибка в работе модуля EraLend:\n{e}")
