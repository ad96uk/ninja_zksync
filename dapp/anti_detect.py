import time

from helpers.console import *


def open_new_window(driver):
    driver.execute_script("window.open('about:blank', '_blank');")
    driver.switch_to.window(driver.window_handles[-1])


def browser(driver):
    open_new_window(driver)
    driver.get("https://explorer.zksync.io/")
    time.sleep(0.5)
    logger.info("Скрипт перешел в режим ожидания...\n")
    input(f"🤖: {purple}Нажми 'Enter' чтобы перейти к следующему кошельку...")