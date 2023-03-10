import game

greeting = ''', приветствую!\n
Я создан для игры в "Конфеты".
Для начала новой игры, введи команду: /new_game
Для отображения доступных конмад, введи команду: /help'''

toss = 'Твой ход'
user_total = 'Начальное количство конфет утановлено: '
bot_mode = 'Сложность бота установленна в значение '
player_turn = ', твой ход, сколько возьмешь конфет?'
finish = 'Текущая игра завершена. Для начала новой игры, введи команду: /new_game'

start_new_game = " начал новую игру"
set_total = " изменил начальное количество конфет. Теперь Начально количество конфет:  "
set_mode = "изменил сложность игры. Текущая сложность: "
log_finish = " завершил игру командой finish"
player_win = "Игра завершена. Победу одержал "
bot_win = "Игра завершена. Выиграл Бот"

error_candies = 'Нельзя взять больше конфет, чем их осталось (0_о)!'
error_few_candies = 'Столько конфет нельзя взять физически (0_о). Нужно брать от 1 до 28'
error_many_candies = 'Что то ты многовато взял. Нужно брать от 1 до 28'
error_input_value = 'Необходимо вводить число от 1 до 28!'
error_bot = 'Бот не запущен. Введите команду /start или /help'
error_set_mode = 'Для установки режима. Необходимо после команды /set_mode ввести цифру 0 или 1!'
error_set = 'Для установки начального колличества конфет. Необходимо после команды /set ввести колличество конфет!'
error_finish = 'Игра не запущена'
error_set_total_new_game = ", какой ты хитрый. Игра уже запущена! Установка начального количества конфет возможна только перед началом игры"
error_set_mode_new_game = ", какой ты хитрый. Игра уже запущена! Установка сложности бота возможна только перед началом игры"
error_set_total_value = ' не является числом. Введите команду заново!'
error_set_mode_value = ' не является числом. Введите команду заново!'
error_new_game = r'Сначала необходимо завершить текущую игру. Доиграйте или введите соманду /finish'

commands = ["Список доступных команд:",
            '1. /start - Старт Бота',
            '2. /new_game - Старт новой игры',
            '3. /set ЧИСЛО - Установка начального колличества конфет.(default = 150) Ввод возможен только перед началом игры!!! ',
            '4. /set_mode ЧИСЛО - Установка сложности игры 0 - слабый бот, 1 - Сильный бот.(default = 0)',
            '5. /description - Правила игры',
            '6. /finish - моментальное завершение текущей игры',
            '7. /help - Отображение списка доступных команд']



description = '''\tЭто игра Конфеты!\n
На столе лежит определенное колличество конфет (по умолчанию 150)
На основании рандомного выбора ходит либо игрок либо бот.
За один ход можно брать от 1 до 28 конфет.
Побеждает тот кто возьмет последнюю конфету.
'''

def user_take_candies(take: int):
    return f' взял {take} конфет{choice_ending(take)} и на столе осталось {game.get_total()} конфет{choice_ending(game.get_total())}. Ходит Бот...'

def bot_take_candies(take: int):
    return f'Бот взял {take} конфет{choice_ending(take)} и их осталось {game.get_total()}'

def user_win(take: int):
    return f' взял {take} конфет{choice_ending(take)}, и одержал победу над железякой!'

def bot_win(take: int):
    return f' не смог обыграть бота! Бот взял {take} конфет{choice_ending(take)} и одержал победу!'

def choice_ending(take: int):
    if take in range(5, 21):
        return ''
    elif take in range(1, 9999, 10):
        return 'у'
    else:
        return 'ы'