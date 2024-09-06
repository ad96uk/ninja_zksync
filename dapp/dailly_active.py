from helpers.general import *
from helpers.console import *
from dapp.dmail import dmail
from dapp.owlto import owlto
from dapp.l2telegraph import l2telegraph
from dapp.merkly import merkly
from dapp.self_send import self_send
from dapp.syncswap import syncswap
from dapp.eralend import eralend
from dapp.random_send import random_send


def daily_activities(driver):
    activities = [dmail, self_send, owlto]
    random_activity = random.choice(activities)
    logger.info(f"Дневная активность для кошелька: {random_activity.__name__}")
    random_activity(driver)
