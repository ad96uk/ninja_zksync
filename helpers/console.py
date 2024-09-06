from helpers.general import *
from settings import *
import logging
from datetime import datetime
from time import sleep


class CustomFormatter(logging.Formatter):
    grey = "\033[0;35m"
    yellow = "\033[93m"
    red = "\033[91m"
    bold_red = "\033[91m"
    reset = "\033[0m"
    format = '%(asctime)s - %(levelname)s - %(message)s'

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, "%H:%M:%S")
        return formatter.format(record)


# Настройка логгера
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# Создание обработчика, который будет выводить сообщения в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
# Установка кастомного форматтера
console_handler.setFormatter(CustomFormatter())
# Добавление обработчика к логгеру
logger.addHandler(console_handler)


def logo():
    print(f"""# Запомните, бляди! Снэпшота не было!\n""")
    print(f"{bold}{purple}Список модулей:{reset}")
    if owlto_mode:
        print(f"Owlto:{reset} {green}True{reset}")
    else:
        print(f"Owlto:{reset} {red}False{reset}")
    if eralend_mode:
        print(f"EraLend:{reset} {green}True{reset}")
    else:
        print(f"EraLend:{reset} {red}False{reset}")
    if send_to_okx_mode:
        print(f"Send to OKX:{reset} {green}True{reset}")
    else:
        print(f"Send to OKX:{reset} {red}False{reset}")
    if merkly_mode:
        print(f"Merkly:{reset} {green}True{reset}")
    else:
        print(f"Merkly:{reset} {red}False{reset}")
    if self_send_mode:
        print(f"Self Send:{reset} {green}True{reset}")
    else:
        print(f"Self Send:{reset} {red}False{reset}")
    if random_send_mode:
        print(f"Random Send:{reset} {green}True{reset}")
    else:
        print(f"Random Send:{reset} {red}False{reset}")
    if syncswap_mode:
        print(f"SyncSwap:{reset} {green}True{reset}")
    else:
        print(f"SyncSwap:{reset} {red}False{reset}")
    if pancake_mode:
        print(f"Pancake Swap:{reset} {green}True{reset}")
    else:
        print(f"Pancake Swap:{reset} {red}False{reset}")
    if dmail_mode:
        print(f"Dmail:{reset} {green}True{reset}")
    else:
        print(f"Dmail:{reset} {red}False{reset}")
    if l2pass_mode:
        print(f"L2Pass free mint:{reset} {green}True{reset}")
    else:
        print(f"L2Pass free mint:{reset} {red}False{reset}")
    if l2telegraph_mode:
        print(f"L2 Telegraph:{reset} {green}True{reset}")
    else:
        print(f"L2Telegraph:{reset} {red}False{reset}")
    if daily_activities_mode:
        print(f"Daily activities:{reset} {green}True{reset}")
    else:
        print(f"Daily activities:{reset} {red}False{reset}")
    if antidetect_mode:
        print(f"Ati-Detect Browser:{reset} {green}True{reset}")
    else:
        print(f"Ati-Detect Browser:{reset} {red}False{reset}")
    print(f"\n{purple}Дополнительные настройки:{reset}")
    if headless_mode:
        print(f"Headless mode:{reset} {green}True{reset}")
    else:
        print(f"Headless mode:{reset} {red}False{reset}")
    if random_mode:
        print(f"Random wallet's:{reset} {green}True{reset}")
    else:
        print(f"Random wallet's:{reset} {red}False{reset}")
    if standart_rpc:
        print(f"Standart RPC:{reset} {green}True{reset}")
    else:
        print(f"Standart RPC:{reset} {red}False{reset}")
    if custom_rpc:
        print(f"Custom RPC:{reset} {green}True{reset}")
    else:
        print(f"Custom RPC:{reset} {red}False{reset}")

    # time.sleep(0.6)
    # input(f"\n{bold}{purple_2}Нажмите Enter, чтобы начать трахать zkSync >>> [] {reset}")
    # print(f"\n{bold}{purple_2}LFG 🫡{reset}\n")
    # time.sleep(0.5)


# Цвета текста
purple = "\033[0;35m"
purple_2 = "\033[1;35m"
white = '\033[97m'
yellow = "\033[93m"
green = "\033[92m"
red = "\033[91m"
mint = "\033[96m"
blue = "\033[34m"
bold = "\033[1m"
black = "\033[30m"
reset = '\033[0m'
orange = "\033[38;5;208m"
l_blue = '\x1b[36m'
curv = "\033[3m"


# Время | Вызывать перед каждым запросом "timex = clock()"
def clock():
    default_time = datetime.now().time()
    formatted_time = default_time.strftime("%H:%M:%S")
    time_now = "\033[38;5;208m" + formatted_time + f"{red} |{reset}"
    return time_now


timex = clock()
# Аннотации
module = f"{purple_2} MODULE  {reset}" + f"{red}|{reset}"
info = f"{white} INFO    {reset}" + f"{red}|{reset}"
error = f"{red} ERROR   {reset}" + f"{red}|{reset}"
warning = f"{yellow} WARNING {reset}" + f"{red}|{reset}"
success = f"{green} SUCCESS {reset}" + f"{red}|{reset}"

