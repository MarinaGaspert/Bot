__total = 150
__user_total = 0
__is_new_game = False
__bot_mode = 0

def get_total() -> int:
    global __total
    return __total


def set_total(total: int):
    global __total
    __total = total

def get_user_total() -> int:
    global __user_total
    return __user_total


def set_user_total(total: int):
    global __user_total
    __user_total = total

def set_bot_mode(value: int):
    global __bot_mode
    __bot_mode = value
def set_default_bot_mode():
    global __bot_mode
    __bot_mode = 0

def get_bot_mode():
    global __bot_mode
    return __bot_mode

def take_candies(take: int):
    global __total
    __total -= take

def game() -> bool:
    global __is_new_game
    return __is_new_game


def new_game():
    global __is_new_game

    if __is_new_game:
        __is_new_game = False
    else:
        if get_user_total() == 0:
            set_total(150)
        else:
            set_total(get_user_total())
        __is_new_game = True


def finish_game():
    global __is_new_game
    __is_new_game = False

def log_data(data: str):
    with open('log.txt', 'a', encoding='UTF-8') as file:
        file.write(data)
