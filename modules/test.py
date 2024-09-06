import time
from helpers.general import *
from helpers.console import *
from helpers.mm import *


def test(driver):
    print("Hello")
    driver.get("https://app.zerolend.xyz/dashboard/")
    time.sleep(1000)
