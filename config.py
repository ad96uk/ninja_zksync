import time
from helpers.general import *
from helpers.console import *
from settings import okx_pass


def prepare_chrome(driver):
    driver.get("data:,")
    time.sleep(2)
    window_handles = driver.window_handles  # print(f"Количество окон: {window_handles}")
    driver.switch_to.window(window_handles[-1])
    time.sleep(0.25)  # print("Переключился на вкладку расширения, открую автоматом") # переключение на новую вкладку
    driver.close()
    time.sleep(0.25)  # print("Закрыл её")
    driver.switch_to.window(window_handles[0])
    time.sleep(0.25)
    driver.switch_to.new_window('tab')  # print("создал 2 вкладку и переключился на неё")
    time.sleep(1)


def okx_auth(driver, okx_field_xpath, okx_wallet_key):
    try:
        words = okx_wallet_key.split()
        if len(words) >= len(okx_field_xpath):
            for i, word in enumerate(words[:len(okx_field_xpath)]):
                input_field = driver.find_element(By.XPATH, okx_field_xpath[i])
                input_field.send_keys(word)
                input_field.send_keys(Keys.TAB)
        else:
            timex = clock()
            print(f"{timex}{error} Сид фраза вставлена не полностью. Перепроверь")
    except Exception as e:
        timex = clock()
        print(f"{timex}{error} Ошибка вставки слова в id поля:\n{str(e)}")
        time.sleep(3)


okx_field_xpath = [
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


def okx_setup(driver, okx_wallet_key):
    timex = clock()
    print(f"{timex}{info} Начинаю настройку MetaMask")
    time.sleep(1)
    try:
        try:
            driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#onboarding/welcome")
            time.sleep(1)

            driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/ul/li[1]/div/input').click()
            #print("1")
            time.sleep(0.5)

            driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/ul/li[3]/button').click()
            #print("2")
            time.sleep(0.5)

            driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/button[1]').click()
            #print("3")
            time.sleep(0.5)

            okx_auth(driver, okx_field_xpath, okx_wallet_key)
            time.sleep(1.5)

            driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/button').click()
            #print("4")
            time.sleep(0.5)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input').send_keys(okx_pass)
            #print("5")
            time.sleep(0.5)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input').send_keys(okx_pass)
            #print("6")
            time.sleep(0.5)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input').click()
            #print("7")
            time.sleep(0.5)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/button').click()
            #print("8")
            time.sleep(0.5)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button').click()
            #print("skip")
            time.sleep(0.5)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button').click()
            #print("skip2")
            time.sleep(0.5)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button').click()
            #print("skip3")
            time.sleep(1.5)
            driver.find_element(By.XPATH, '/html/body/div[2]/div/div/section/div[1]/div/button').click()
            #print("skip4")
            time.sleep(0.5)
            driver.close()
        except Exception as e:
            timex = clock()
            print(f"{timex}{error} Произошла ошибка в настройке кошелька: {e}")
    except Exception as e:
        timex = clock()
        print(f"{timex}{error} {e}")

