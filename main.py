from helpers.user_agent import random_user_agent
from helpers.console import *
from helpers.gas_cheker import gas_checker
from settings import (
    owlto_mode,
    eralend_mode,
    pancake_mode,
    dmail_mode,
    daily_activities_mode,
    random_send_mode,
    l2pass_mode)

from dapp.owlto import *
from dapp.send_to_okx import *
from dapp.merkly import *
from dapp.eralend import eralend
from dapp.self_send import self_send
from dapp.anti_detect import browser
from dapp.syncswap import syncswap
from dapp.pancake import panceswap
from dapp.dmail import dmail
from dapp.dailly_active import daily_activities
from dapp.random_send import random_send
from dapp.l2pass import l2pass_free_mint
from dapp.l2telegraph import l2telegraph
from dapp.jumper_exchange import jumper_exchange

logo()


def main(wallet_info, current_cycle=1, total_cycles_arg=None):
    mm_wallet_key = wallet_info
    print(f"{white}\n=================================================================================\nWallet {current_cycle}/{total_cycles_arg}.{reset}\n"
          f"{white}{wallet_info}\n{reset}"
          f"{white}================================================================================={reset}\n")
    time.sleep(0.5)

    # Настройка Chrome
    chrome_options = webdriver.ChromeOptions()
    if headless_mode:
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument(f"user-agent={random_user_agent}")
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.geolocation": 2})
    extension_dir = "MetaMask/11.7.5_0"
    chrome_options.add_argument(f'--load-extension={extension_dir}')
    driver = webdriver.Chrome(options=chrome_options)

    try:
        mm_setups(driver, mm_wallet_key)
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[0])
        if standart_rpc:
            era_mainet(driver)
        if custom_rpc:
            add_custom_rpc(driver)

        functions = []
        if owlto_mode:
            functions.append(owlto)
        if send_to_okx_mode:
            functions.append(lambda d=driver, c=current_cycle: send_to_okx(d, c))
        if merkly_mode:
            functions.append(merkly)
        if eralend_mode:
            functions.append(eralend)
        if self_send_mode:
            functions.append(self_send)
        if antidetect_mode:
            functions.append(browser)
        if syncswap_mode:
            functions.append(syncswap)
        if pancake_mode:
            functions.append(panceswap)
        if dmail_mode:
            functions.append(dmail)
        if daily_activities_mode:
            functions.append(daily_activities)
        if random_send_mode:
            functions.append(random_send)
        if l2pass_mode:
            functions.append(l2pass_free_mint)
        if l2telegraph_mode:
            functions.append(l2telegraph)

        random.shuffle(functions)
        time.sleep(0.5)

        # functions.append(jumper_exchange)

        for func in functions:
            try:
                #gas_checker(driver)
                func(driver)
            except Exception as e:
                logger.error(f"Error occurred in module: {e}")
                with open('results/error_wallets.txt', 'a') as error_file:
                    error_file.write(wallet_info + '\n')
                time.sleep(3)

    except Exception as e:
        logger.error(f"Retry for wallet:\n{wallet_info}\n"
                     f"Error occurred: {e}")
        with open('results/error_wallets.txt', 'a') as error_file:
            error_file.write(wallet_info + '\n')
        driver.quit()

    finally:
        driver.quit()
        

with open('data/wallets.txt', 'r') as file:
    wallet_data = file.read().splitlines()

total_cycles = len(wallet_data)
if random_mode:
    random.shuffle(wallet_data)
time.sleep(0.5)

try:
    for i, wallet_info in enumerate(wallet_data, start=1):
        main(wallet_info, current_cycle=i, total_cycles_arg=total_cycles)
        inter_wallet_delay_local = random.randint(INTER_DELAY[0], INTER_DELAY[1])
        logger.info(f"Сплю перед запуском следующего кошелька: {yellow}{inter_wallet_delay_local} секунд(ы).{l_blue}")
        time.sleep(inter_wallet_delay_local)
finally:
    logger.info("Работа завершена, сир 🫡!")
