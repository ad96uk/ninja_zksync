from decimal import Decimal

#Модули
jumper_exchange_mode = False
owlto_mode = False
dmail_mode = False
merkly_mode = False
eralend_mode = False
send_to_okx_mode = False  # Не забудь поставить random_mode = False
self_send_mode = True
random_send_mode = False
syncswap_mode = False
pancake_mode = False
l2pass_mode = False
l2telegraph_mode = False
daily_activities_mode = False
antidetect_mode = False

# Дополнительные настройки
headless_mode = True
random_mode = False
standart_rpc = True #Если True, то custom_rpc = False. И наоборот.
custom_rpc = False


eth_gas_price = 100 # Газ в эфире при котором скрипт будет делать транзации в ZKSYNC
interval      = 30 # Частота проверки газа в секундах

#Настройка времени (в секундах)
INTRA_DELAY = [5, 15] # Задержка между транзакциями на одном кошельке
INTER_DELAY = [50, 180] # Задерка между кошельками

e_round = 6 #До скольки знаков округлять ETH (применяется по всему скрипту)

#JUMPER exchange EXCHANGE
eth_leave_from = 0.0051
eth_leave_to = 0.0052

# КОЛ-ВО СЛУЧАЙНЫХ ТРАНЗ МЕЖДУ НАКРУТКОЙ ОБЬЕМА НА ERALEND
SEPARATE_LOOPS = [0, 1]

#OWLTO
OWLTO_REPEATS = [1, 1] #Не настраивается

#ERALEND
ERA_REPEATS = [1, 1] #Количечетво повторов (выполняется на 1 больше чем указано в настройках)
DEP = [20, 30] #Сумма депозита в %

#SEND TO OKX
#ETH_TO_LEAVE = [Decimal('0.0052'), Decimal('0.00574')] #от 15$ на акк
ETH_TO_LEAVE = [Decimal('0.0003'), Decimal('0.00045')] #от 15$ на акк

#RANDOM SEND
RANDOM_SEND_REPEATS = [1, 1] # Кол-во повторов
RANDOM_SEND_AMOUNT  = [0.000015, 0.000020] #Сумма к отправке

#SELF SEND
SS_REPEATS   = [1, 1] #Кол-во повторов
SEND_PERCENT = [99, 99] #% от баланса для отправки

#SYNCSWAP
usdc_mode = False #СВАП ТОЛЬКО ИЗ USDC в ETH /  при активации этой функции кол-во повторов поставить на 0
usdt_mode = False #СВАП ТОЛЬКО ИЗ USDT в ETH /  при активации этой функции кол-во повторов поставить на 0
#Кол-во свапов
SYNC_REPEATS = [1, 1]
# % от баланса для свапа
swap_eth_from = 0.1
swap_eth_to   = 0.5

shit_eth_from = 0.0000029
shit_eth_to = 0.000015


#PANCAKE
PANCAKE_REPEAT = [1, 1] #Кол-во свапов(выполняется на 1 больше чем указано в настройках)
PANCAKE_ETH_SWAP_AMOUNT = [5, 10] #Указывается в % от баланса

#DMAIL
DMAIL_REPEAT = [1, 2] #Кол-во сообщений

#MERKLY
gas_mode    = True   # Бриджит газ -  КОЛ-ВО ПОВТОРОВ НЕ НАСТРАИВАЕТСЯ
deploy_mode = False  # Деплоит контракт - НЕ РАБОТАЕТ!
MERKLEY_REPEAT = [1, 1]

#L2TELEGRAPH
GAS_VALUE = [0.0000029, 0.000015] #Бриджит только в  ARB NOVA

#НЕ ТРОГАТЬ ЕСЛИ ВСЕ РАБОТАЕТ
rpc            = "https://1rpc.io/zksync2-era"
#https://zksync.drpc.org
#https://1rpc.io/zksync2-era
#https://zksync.meowrpc.com
#https://zksync-era.blockpi.network/v1/rpc/public
chain_name     = 'zkSync Mainnet'
chain_id       = '324'
chain_simvol   = 'ETH'
chain_explorer = 'https://explorer.zksync.io'
mm_pass = "Qwerty1234*!@£"