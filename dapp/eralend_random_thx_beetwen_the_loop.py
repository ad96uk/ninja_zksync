from helpers.console import *
from dapp.dmail import dmail
from dapp.self_send import self_send
from dapp.syncswap import syncswap_separate
from helpers.mm import swith_tab_separate_loop, swith_back_tab_separate_loop


def main_func(driver):
    swith_back_tab_separate_loop(driver)
    activities = [syncswap_separate]
    random_activity = random.choice(activities)
    random_activity(driver)
    swith_back_tab_separate_loop(driver)


def separate_loop(driver):
    logger.info("\033[96mГенерирую случайное кол-во разбивочных транзакций")
    number_of_repeats = random.randint(SEPARATE_LOOPS[0], SEPARATE_LOOPS[1])
    for repetition in range(number_of_repeats):
        main_func(driver)
        delay_between_repeats = random.randint(INTRA_DELAY[0], INTRA_DELAY[1])
        logger.info(
            f"\033[96mПовтор случайной активности{yellow}{repetition + 1}/{number_of_repeats}{reset}{purple}. Следующий запуск через: "f"{yellow}{delay_between_repeats}{reset}{purple} секунд.")
        time.sleep(delay_between_repeats)



