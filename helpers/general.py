import time
import datetime
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from decimal import Decimal, ROUND_DOWN



delay_05_to_2 = random.uniform(0.5,2)
d_1_2 = random.uniform(1,3)
d_2_3 = random.uniform(2,4)
d_3_4 = random.uniform(3,5)
d_4_5 = random.uniform(4,6)
d_5_6 = random.uniform(5,7)
d_6_7 = random.uniform(6,8)
d_7_8 = random.uniform(7,9)