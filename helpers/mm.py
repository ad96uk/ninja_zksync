import time

from helpers.console import *
from settings import mm_pass
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.mm_url = "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#onboarding/welcome"
        self.mm_url_2 = "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#settings/networks/add-network"
        self.chainlink_url = "https://chainlist.org/"
        self.era_url = "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#settings/networks/add-popular-custom-network"

    def era_mainet(self):
        try:
            logger.info("Добавляю кастомную RPC")
            self.driver.get(self.era_url)
        except Exception as e:
            logger.error(f"Ошибка добавления кастомной url: {e}")
        return

    def find_elements(self, locator):
        try:
            elements = WebDriverWait(self.driver, timeout=10).until(
                EC.visibility_of_all_elements_located(locator)
            )
            return elements
        except Exception as e:
            logger.error(f"Не удалось найти элементы: {e}\n{locator}")
            return []

    def open_wallet_page(self):
        try:
            #logger.info("Начинаю настройку кошелька")
            self.driver.get(self.mm_url)
        except Exception as e:
            logger.error(f"Ошибка открытия кошелька: {e}")
        return

    def open_wallet_page_2(self):
            try:
                logger.info("Добавляю кастомную RPC")
                self.driver.get(self.mm_url_2)
            except Exception as e:
                logger.error(f"Ошибка открытия страницы RPC: {e}")
            return

    def open_chainlist(self):
        self.driver.get(self.chainlink_url)

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

    def prepare_chrome(self):
        self.driver.get("data:,")
        time.sleep(2)
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[-1])
        time.sleep(0.25)
        self.driver.close()
        time.sleep(0.25)
        self.driver.switch_to.window(window_handles[0])
        time.sleep(0.25)
        #self.driver.switch_to.new_window('tab')
        #time.sleep(1)

class SearhList:
    # Настройка кошелька:
    LOCATOR_MM_1 = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/ul/li[1]/div/input")
    LOCATOR_MM_2 = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/ul/li[3]/button")
    LOCATOR_MM_3 = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/button[1]")
    LOCATOR_MM_4 = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/button")
    LOCATOR_MM_PASS_1 = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input")
    LOCATOR_MM_PASS_2 = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input")
    LOCATOR_MM_5 = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input")
    LOCATOR_MM_6 = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/button")
    LOCATOR_MM_7 = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/button")
    LOCATOR_MM_8 = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/button")
    LOCATOR_MM_9 = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/button")
    LOCATOR_MM_10 = (By.XPATH, "/html/body/div[2]/div/div/section/div[1]/div/button")

    # Добавление сети в кошельке
    LOCATOR_MM_ADD_CHAIN_1 = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/button[2]")
    LOCATOR_MM_ADD_CHAIN_2 = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/button[2]")

    # Подключение кошелька
    LOCATOR_MM_CONNECT_1 = (By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]")
    LOCATOR_MM_CONNECT_2 = (By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]")
    LOCATOR_MM_CONNECT_3 = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/button[2]")
    LOCATOR_MM_CONNECT_4 = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/button[2]")

    # Подписание транзакции
    LOCATOR_MM_SUBMIT_TXH_1 = (By.CSS_SELECTOR, "#app-content > div > div > div > div.confirm-page-container-content > div.page-container__footer > footer > button.button.btn--rounded.btn-primary.page-container__footer-button")

    # Получение хэша транзакции
    LOCATOR_MM_GET_THX_ALERT_1 = (By.CSS_SELECTOR, "#popover-content > div > div > section > div.box.popover-header.box--padding-4.box--sm\:padding-4.box--md\:padding-4.box--display-flex.box--flex-direction-column.box--background-color-background-default.box--rounded-xl > div > button")
    LOCATOR_MM_GET_THX_ALERT_2 = (By.CSS_SELECTOR, "#popover-content > div > div > section > div.box.popover-header.box--padding-4.box--sm\:padding-4.box--md\:padding-4.box--display-flex.box--flex-direction-column.box--background-color-background-default.box--rounded-xl > div > button")
    LOCATOR_MM_GET_THX_1 = (By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div[2]/div/ul/li[3]/button")
    LOCATOR_MM_GET_THX_2 = (By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div[2]/div/div/div/div/div/div/div")
    LOCATOR_MM_GET_THX_3 = (By.XPATH, "/html/body/div[2]/div/div/section/div[2]/div/div[2]/div[2]/div[1]/a")

    # Проверка баланса
    LOCATOR_MM_CHEK_WARNING_1 = (By.XPATH, '/html/body/div[1]/div/div[3]/div/div[3]/div[3]/div/p[1]/span')

    #Chainlist
    LOCATOR_CLIST_1 = (By.XPATH, '//button[contains(text(), "Connect Wallet")][1]')
    LOCATOR_CLIST_2_INPUT = (By.CSS_SELECTOR, 'input[placeholder="ETH, Fantom, ..."]')
    #LOCATOR_CLIST_3 = (By.XPATH, '//button[contains(text(), "Add to Metamask")]')
    LOCATOR_CLIST_3_1 = (By.XPATH, '/html/body/div/div/div[2]/div[2]/div/button[2]')
    LOCATOR_CLIST_4 = (By.XPATH, '//tr[contains(td, "https://mainnet.era.zksync.io")]')
    LOCATOR_CLIST_5 = (By.XPATH, './/button[contains(text(), "Add to Metamask")]')

    #mm_submit_thx_merkley_version
    LOCATOR_MERKLEY_1 = (By.XPATH, "//i[contains(@class, 'fa fa-arrow-down') and @aria-label='Прокрутить вниз']")
    LOCATOR_MERKLEY_2 = (By.XPATH, "//button[contains(@class, 'button') and contains(@class, 'btn--rounded') and contains(@class, 'btn-primary') and contains(@class, 'page-container__footer-button') and @data-testid='page-container-footer-next']")
    LOCATOR_MERKLEY_3 = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div[4]/div[2]")

    LOCATOR_MERKLEU_DOWN_ICON = (By.XPATH, "//div[@class='box signature-request-message__scroll-button box--display-flex box--flex-direction-row box--justify-content-center box--align-items-center box--color-icon-default box--background-color-background-default box--border-color-border-default box--border-style-solid box--border-width-1'][@data-testid='signature-request-scroll-button']")
    LOCATOR_MERKLEU_SIGHN_BTN = (By.XPATH, "//button[@class='button btn--rounded btn-primary page-container__footer-button'][@data-testid='page-container-footer-next']")

    #add_custom_rpc
    LOCATOR_RPC_1 = (By.CSS_SELECTOR, "#app-content > div > div.mm-box.multichain-app-header.mm-box--margin-bottom-0.mm-box--display-flex.mm-box--align-items-center.mm-box--width-full.mm-box--background-color-background-alternative > div > div.mm-box.mm-box--display-flex.mm-box--justify-content-flex-end.mm-box--align-items-center > div > div > button > span")
    LOCATOR_RPC_2 = (By.CSS_SELECTOR, "#popover-content > div.menu__container > button:nth-child(7) > div > div")
    LOCATOR_RPC_3 = (By.CSS_SELECTOR, "#app-content > div > div.mm-box.main-container-wrapper > div > div.settings-page__content > div.settings-page__content__tabs > div > button:nth-child(6)")
    LOCATOR_RPC_4_INPUT = (By.CSS_SELECTOR, "#app-content > div > div.mm-box.main-container-wrapper > div > div.settings-page__content > div.settings-page__content__modules > div > div.networks-tab__content > div.networks-tab__network-form > div.networks-tab__network-form-body > div:nth-child(2) > label > input")
    LOCATOR_RPC_5 = (By.CSS_SELECTOR, "#app-content > div > div.mm-box.main-container-wrapper > div > div.settings-page__content > div.settings-page__content__modules > div > div.networks-tab__content > div.networks-tab__network-form > div.networks-tab__network-form-footer > button.button.btn--rounded.btn-primary")


    #new prc
    LOCATOR_CHAIN_NAME = (By.CSS_SELECTOR, "#app-content > div > div.mm-box.main-container-wrapper > div > div.settings-page__content > div.settings-page__content__modules > div > div.networks-tab__content > div > div.networks-tab__add-network-form-body > div:nth-child(1) > label > input")
    LOCATOR_CHAIN_PRC = (By.CSS_SELECTOR, "#app-content > div > div.mm-box.main-container-wrapper > div > div.settings-page__content > div.settings-page__content__modules > div > div.networks-tab__content > div > div.networks-tab__add-network-form-body > div:nth-child(2) > label > input")
    LOCATOR_CHAIN_ID = (By.CSS_SELECTOR, "#app-content > div > div.mm-box.main-container-wrapper > div > div.settings-page__content > div.settings-page__content__modules > div > div.networks-tab__content > div > div.networks-tab__add-network-form-body > div:nth-child(3) > label > input")
    LOCATOR_CHAIN_SIMVOL = (By.CSS_SELECTOR, "#app-content > div > div.mm-box.main-container-wrapper > div > div.settings-page__content > div.settings-page__content__modules > div > div.networks-tab__content > div > div.networks-tab__add-network-form-body > div.box.mm-form-text-field.box--display-flex.box--flex-direction-column > div > input")
    LOCATOR_CHAIN_EXPLORER = (By.CSS_SELECTOR, "#app-content > div > div.mm-box.main-container-wrapper > div > div.settings-page__content > div.settings-page__content__modules > div > div.networks-tab__content > div > div.networks-tab__add-network-form-body > div:nth-child(5) > label > input")
    LOCATOR_CHAIN_SAVE = (By.CSS_SELECTOR, "#app-content > div > div.mm-box.main-container-wrapper > div > div.settings-page__content > div.settings-page__content__modules > div > div.networks-tab__content > div > div.networks-tab__add-network-form-footer > button.button.btn--rounded.btn-primary")
    LOCATOR_CHAIN_SWAITH = (By.CSS_SELECTOR, "#popover-content > div > div > section > div.box.popover-content.box--display-flex.box--flex-direction-column.box--justify-content-flex-start.box--align-items-stretch.box--rounded-xl > div > button.button.btn--rounded.btn-primary.home__new-network-added__switch-to-button > h6")

    #Unlock token
    LOCATOR_MM_UNLOCK_1 = (By.XPATH, "//button[@class='button btn--rounded btn-primary page-container__footer-button' and @data-testid='page-container-footer-next' and text()='Next']")
    LOCATOR_MM_UNLOCK_2 = (By.XPATH, "//button[@class='button btn--rounded btn-primary page-container__footer-button' and @data-testid='page-container-footer-next' and text()='Approve']")

    #Mainet rpc
    LOCATOR_ERA_1 = (By.XPATH, "//button[@class='button btn--inline add-network__add-button']")
    LOCATOR_ERA_2 = (By.XPATH, "//button[@class='button btn--rounded btn-primary']")
    LOCATOR_ERA_3 = (By.XPATH, "//button[contains(@class, 'button') and contains(@class, 'btn--rounded') and contains(@class, 'btn-primary') and contains(@class, 'home__new-network-added__switch-to-button')]")

    LOCATOR_SIGH_LOGIN = (By.XPATH, "//button[@class='button btn--rounded btn-primary page-container__footer-button' and @data-testid='page-container-footer-next' and text()='Sign']")

# Поля для ввода фразы
mm_field_xpath = [
    "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[1]/div[1]/div/input",
    "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[2]/div[1]/div/input",
    "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[3]/div[1]/div/input",
    "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[4]/div[1]/div/input",
    "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[5]/div[1]/div/input",
    "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[6]/div[1]/div/input",
    "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[7]/div[1]/div/input",
    "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[8]/div[1]/div/input",
    "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[9]/div[1]/div/input",
    "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[10]/div[1]/div/input",
    "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[11]/div[1]/div/input",
    "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[12]/div[1]/div/input"
]


class MetamaskActions(BasePage):

    def sign_login_in(self):
        return self.find_element(SearhList.LOCATOR_SIGH_LOGIN).click()

    def add_era_3(self):
        return self.find_element(SearhList.LOCATOR_ERA_3).click()

    def add_era_btn(self):
        elements = self.find_elements(SearhList.LOCATOR_ERA_1)
        elements[8].click()

    def add_era_2(self):
        return self.find_element(SearhList.LOCATOR_ERA_2).click()

    #merkley
    def click_sign_btn(self):
        return self.find_element(SearhList.LOCATOR_MERKLEU_SIGHN_BTN).click()

    def click_down_icon(self):
        actions = ActionChains(self.driver)
        element = self.find_element(SearhList.LOCATOR_MERKLEU_DOWN_ICON)
        actions.click(element).perform()

    def click_down_icon_2(self):
        print(1)

    def click_down_icon_3(self):
        print(1)

    def unlock_token_1(self):
        return self.find_element(SearhList.LOCATOR_MM_UNLOCK_1).click()

    def unlock_token_2(self):
        return self.find_element(SearhList.LOCATOR_MM_UNLOCK_2).click()

    # Настройка кошелька
    @property
    def setup_mm_click_1(self):
        return self.find_element(SearhList.LOCATOR_MM_1).click()
    @property
    def setup_mm_click_2(self):
        return self.find_element(SearhList.LOCATOR_MM_2).click()
    @property
    def setup_mm_click_3(self):
        return self.find_element(SearhList.LOCATOR_MM_3).click()
    @property
    def setup_mm_click_4(self):
        return self.find_element(SearhList.LOCATOR_MM_4).click()
    @property
    def fill_mm_pass_1(self):
        return self.find_element(SearhList.LOCATOR_MM_PASS_1).send_keys(mm_pass)
    @property
    def fill_mm_pass_2(self):
        return self.find_element(SearhList.LOCATOR_MM_PASS_2).send_keys(mm_pass)
    @property
    def setup_mm_click_5(self):
        return self.find_element(SearhList.LOCATOR_MM_5).click()
    @property
    def setup_mm_click_6(self):
        return self.find_element(SearhList.LOCATOR_MM_6).click()
    @property
    def setup_mm_click_7(self):
        return self.find_element(SearhList.LOCATOR_MM_7).click()
    @property
    def setup_mm_click_8(self):
        return self.find_element(SearhList.LOCATOR_MM_8).click()
    @property
    def setup_mm_click_9(self):
        return self.find_element(SearhList.LOCATOR_MM_9).click()
    @property
    def setup_mm_click_10(self):
        return self.find_element(SearhList.LOCATOR_MM_10).click()

    # Добавление сети
    @property
    def mm_add_chain_1(self):
        return self.find_element(SearhList.LOCATOR_MM_ADD_CHAIN_1).click()
    @property
    def mm_add_chain_2(self):
        return self.find_element(SearhList.LOCATOR_MM_ADD_CHAIN_2).click()

    # Подключение кошелька
    @property
    def mm_connect_1(self):
        return self.find_element(SearhList.LOCATOR_MM_CONNECT_1).click()
    @property
    def mm_connect_2(self):
        return self.find_element(SearhList.LOCATOR_MM_CONNECT_2).click()
    @property
    def mm_connect_3(self):
        return self.find_element(SearhList.LOCATOR_MM_CONNECT_3).click()
    @property
    def mm_connect_4(self):
        return self.find_element(SearhList.LOCATOR_MM_CONNECT_4).click()

    # Подписание транзакции
    @property
    def mm_send_thx(self):
        try:
            button_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="page-container-footer-next"]'))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", button_element)
            button_element.click()

            return True
        except Exception as e:
            print(f"Произошла ошибка при выполнении mm_send_thx: {e}")
            return False

    # Получение хэша транзакции
    @property
    def mm_get_thx_1(self):
        return self.find_element(SearhList.LOCATOR_MM_GET_THX_ALERT_1).click()
    @property
    def mm_get_thx_2(self):
        return self.find_element(SearhList.LOCATOR_MM_GET_THX_ALERT_2).click()
    @property
    def mm_get_thx_3(self):
        return self.find_element(SearhList.LOCATOR_MM_GET_THX_1).click()
    @property
    def mm_get_thx_4(self):
        return self.find_element(SearhList.LOCATOR_MM_GET_THX_2).click()
    @property
    def mm_get_thx_5(self):
        return self.find_element(SearhList.LOCATOR_MM_GET_THX_3).click()
    # Проверка баланса
    @property
    def check_warning(self):
        return self.find_element(SearhList.LOCATOR_MM_CHEK_WARNING_1)

    @property
    def chainlist_click_1(self):
        return self.find_element(SearhList.LOCATOR_CLIST_1).click()

    @property
    def chainlist_click_2(self):
        return self.find_element(SearhList.LOCATOR_CLIST_2_INPUT).send_keys("zksync")

    @property
    def chainlist_click_3_1(self):
        element = self.find_element(SearhList.LOCATOR_CLIST_3_1)
        self.driver.execute_script("arguments[0].click();", element)
        return True

    @property
    def chainlist_click_4(self):
        row_element = self.find_element(SearhList.LOCATOR_CLIST_4)
        try:
            button_inside_row = WebDriverWait(row_element, 10).until(
                EC.visibility_of_element_located(SearhList.LOCATOR_CLIST_5)
            )
            button_inside_row.click()
            return True
        except Exception as e:
            print(f"Элемент {SearhList.LOCATOR_CLIST_5} не был найден. Ошибка: {e}")
            return False

    # MERKLY SING THX
    def merkly_acions_1(self):
        try:
            element = self.find_element(SearhList.LOCATOR_MERKLEY_1)
            if element:
                print("Элемент найден. Выполняю клик.")
                self.driver.execute_script("arguments[0].click();", element)
            else:
                print("Элемент не найден.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    @property
    def merkly_acions_2(self):
        return self.find_element(SearhList.LOCATOR_MERKLEY_2).click()

    def merkly_acions_3(self):
        element = self.find_element(SearhList.LOCATOR_MERKLEY_3)
        self.driver.execute_script("arguments[0].click();", element)
    @property
    def add_rpc_1(self):
        return self.find_element(SearhList.LOCATOR_RPC_1).click()
    @property
    def add_rpc_2(self):
        return self.find_element(SearhList.LOCATOR_RPC_2).click()
    @property
    def add_rpc_3(self):
        return self.find_element(SearhList.LOCATOR_RPC_3).click()

    def add_rpc_4(self):
        element = self.find_element(SearhList.LOCATOR_RPC_4_INPUT)
        element.clear()
        element.send_keys(rpc)
    @property
    def add_rpc_5(self):
        return self.find_element(SearhList.LOCATOR_RPC_5).click()

    def new_prc_chain_name(self):
        return self.find_element(SearhList.LOCATOR_CHAIN_NAME).send_keys(chain_name)

    def new_prc_chain_rpc(self):
        return self.find_element(SearhList.LOCATOR_CHAIN_PRC).send_keys(rpc)

    def new_prc_chain_id(self):
        return self.find_element(SearhList.LOCATOR_CHAIN_ID).send_keys(chain_id)

    def new_prc_chain_simvol(self):
        return self.find_element(SearhList.LOCATOR_CHAIN_SIMVOL).send_keys(chain_simvol)

    def new_prc_chain_explorer(self):
        return self.find_element(SearhList.LOCATOR_CHAIN_EXPLORER).send_keys(chain_explorer)

    def mm_debil(self):
        return self.find_element(SearhList.LOCATOR_CHAIN_EXPLORER).send_keys(Keys.ENTER)

    def new_rpc_save_btn(self):
        return self.find_element(SearhList.LOCATOR_CHAIN_SAVE).click()

    def new_rpc_swith_chain(self):
        return self.find_element(SearhList.LOCATOR_CHAIN_SWAITH).click()


def log_in(driver):
    try:
        login = MetamaskActions(driver)
        login.swith_tab()
        sleep(5)
        login.sign_login_in()
        login.swith_back_tab()
    except Exception as e:
        login.swith_back_tab()
        logger.error(f"Ошибка входа: {e}")


def era_mainet(driver):
    try:
        era = MetamaskActions(driver)
        era.open_wallet_page()
        era.era_mainet()
        era.add_era_btn()
        era.add_era_2()
        era.add_era_3()
    except Exception as e:
        logger.error(f"Ошибка era_mainet:{e}")


def mm_auth(driver, mm_field_xpath, mm_wallet_key):
    try:
        words = mm_wallet_key.split()
        if len(words) >= len(mm_field_xpath):
            for i, word in enumerate(words[:len(mm_field_xpath)]):
                input_field = driver.find_element(By.XPATH, mm_field_xpath[i])
                input_field.send_keys(word)
                input_field.send_keys(Keys.TAB)
        else:
            logger.error("Сид фраза вставлена не полностью")
    except Exception as e:
        logger.error(f"Ошибка вставки слова в id поля:\n{str(e)}")


def mm_setups(driver, mm_wallet_key):
    try:
        logger.info("Начинаю настройку кошелька")
        mm_setup = MetamaskActions(driver)
        mm_setup.prepare_chrome()
        mm_setup.open_wallet_page()
        mm_setup.setup_mm_click_1
        mm_setup.setup_mm_click_2
        mm_setup.setup_mm_click_3
        mm_auth(driver, mm_field_xpath, mm_wallet_key)
        mm_setup.setup_mm_click_4
        mm_setup.fill_mm_pass_1
        mm_setup.fill_mm_pass_2
        mm_setup.setup_mm_click_5
        mm_setup.setup_mm_click_6
        mm_setup.setup_mm_click_7
        mm_setup.setup_mm_click_8
        mm_setup.setup_mm_click_9
        mm_setup.setup_mm_click_10
        #logger.info("Кошелек успешно настроен")

    except Exception as e:
        logger.error(f"Ошибка функции настройки кошелька: {e}")


def mm_connect(driver):
    try:
        #logger.info("Подключаю кошелек")
        mm_connects = MetamaskActions(driver)
        mm_connects.swith_tab()
        try:
            mm_connects.mm_connect_1
            mm_connects.mm_connect_2
            try:
                mm_connects.mm_connect_3
                mm_connects.mm_connect_4
            except:
                pass
        except:
            pass
        mm_connects.swith_back_tab()
        #logger.info("Кошелек успешно подключен")
    except Exception as e:
        logger.error(f"Произошла ошибка при подключении кошелька: {e}")
        mm_connects.swith_back_tab()


def chainlist_zk(driver):
    try:
        logger.info("Добавляю сеть ZKSync")
        zk_setup = MetamaskActions(driver)
        zk_setup.open_chainlist()
        zk_setup.chainlist_click_1
        mm_connect(driver)
        zk_setup.chainlist_click_2
        time.sleep(1)
        zk_setup.chainlist_click_3_1
        time.sleep(1)
        zk_setup.chainlist_click_4
        mm_aprove_chain(driver)
    except Exception as e:
        logger.error(f"Произошла ошибка при добавлении сети: {e}")


def mm_aprove_chain(driver):
    try:
        mm_aprove = MetamaskActions(driver)
        mm_aprove.swith_tab()
        try:
            mm_aprove.mm_add_chain_1
        except:
            pass
        try:
            mm_aprove.mm_add_chain_2
        except:
            pass
        logger.info("Сеть успешно добавлена")
        mm_aprove.swith_back_tab()
    except Exception as e:
        logger.error("Произошла ошибка при добавлении сети")
        mm_aprove.swith_back_tab()


def add_custom_rpc(driver):
    try:
        r = MetamaskActions(driver)
        r.open_wallet_page_2()
        r.new_prc_chain_name()
        r.new_prc_chain_rpc()
        r.new_prc_chain_id()
        sleep(3)
        r.new_prc_chain_simvol()
        r.new_prc_chain_explorer()
        sleep(2)
        try:
            r.new_rpc_save_btn()
        except:
            try:
                sleep(1)
                r.new_rpc_save_btn()
                print(1)
            except:
                try:
                    sleep(1)
                    r.new_rpc_save_btn()
                    print(2)
                except:
                    sleep(1)
                    r.new_rpc_save_btn()
                    print(3)
        r.new_rpc_swith_chain()
    except Exception as e:
        logger.error(f"Ошибка в add_custom_rpc: {e}")


def check_eth_warning(driver):
    check = MetamaskActions(driver)
    try:
        message_element = check.check_warning
        message_text = message_element.text
        if "You do not have enough ETH in your account to pay for transaction fees on zkSync Mainnet network.  or deposit from another account." in message_text:
            logger.error("Не хватает газа для оплаты комиссии")
            return True
    except TimeoutException:
        return False


def mm_submit_thx(driver):
    submit = MetamaskActions(driver)
    submit.swith_tab()
    if check_eth_warning(driver):
        submit.swith_back_tab()
        return
    try:
        submit.mm_send_thx
        sleep(3)
        submit.swith_back_tab()
        get_thx(driver)
    except Exception as e:
        logger.error(f"Произошла ошибка при подписании транзакции: {e}")
        submit.swith_back_tab()


def mm_unclock_token(driver):
    unlokc = MetamaskActions(driver)
    unlokc.swith_tab()
    if check_eth_warning(driver):
        unlokc.swith_back_tab()
        return
    try:
        unlokc.unlock_token_1()
        unlokc.unlock_token_2()
        sleep(3)
        unlokc.swith_back_tab()
        get_unlock_thx(driver)
    except Exception as e:
        logger.error(f"Произошла ошибка при подписании транзакции: {e}")
        unlokc.swith_back_tab()


def get_unlock_thx(driver):
    hash = MetamaskActions(driver)
    try:
        driver.execute_script("window.open('about:blank', '_blank');")
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(0.5)
        driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#")
        time.sleep(1)
        # Skip alert
        try:
            hash.mm_get_thx_1
        except:
            try:
                hash.mm_get_thx_2
            except:
                pass
        hash.mm_get_thx_3
        hash.mm_get_thx_4
        hash.mm_get_thx_5
        driver.switch_to.window(driver.window_handles[2])
        new_tab_url = driver.current_url
        logger.info(f"Апрув подписан! Хэш: {white}{new_tab_url}{reset}")
        time.sleep(1)
        driver.close()
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    except Exception as e:
        logger.error("Произошла ошибка в получении Hash транзации ")
        hash.swith_back_tab()

def get_thx(driver):
    hash = MetamaskActions(driver)
    try:
        driver.execute_script("window.open('about:blank', '_blank');")
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(0.5)
        driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#")
        time.sleep(1)
        #Skip alert
        try:
            hash.mm_get_thx_1
        except:
            try:
                hash.mm_get_thx_2
            except:
                pass
        hash.mm_get_thx_3
        hash.mm_get_thx_4
        hash.mm_get_thx_5
        driver.switch_to.window(driver.window_handles[2])
        new_tab_url = driver.current_url
        logger.info(f"Транзакция подписана! Хэш: {white}{new_tab_url}{reset}")
        time.sleep(1)
        driver.close()
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    except Exception as e:
        logger.error("Произошла ошибка в получении Hash транзации ")
        hash.swith_back_tab()


def mm_connect_merkley(driver):
    try:
        mm_connects = MetamaskActions(driver)
        mm_connects.swith_tab()
        mm_connects.mm_connect_1
        mm_connects.mm_connect_2
        mm_connects.swith_back_tab()
    except Exception as e:
        logger.error(f"Произошла ошибка при подключении кошелька: {e}")
        mm_connects.swith_back_tab()


def mm_sigh_thx_merkley_version(driver):
    try:
        sm = MetamaskActions(driver)
        sm.swith_tab()
        sm.click_down_icon()
        sm.click_sign_btn()
        sm.swith_back_tab()
    except Exception as e:
        logger.error(f"Ошибка в подписании транзакции{e}")


def swith_tab_separate_loop(driver):
    driver.execute_script("window.open('about:blank', '_blank');")
    driver.switch_to.window(driver.window_handles[1])


def swith_back_tab_separate_loop(driver):
    driver.switch_to.window(driver.window_handles[0])