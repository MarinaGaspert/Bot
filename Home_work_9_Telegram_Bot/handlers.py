from random import randint as RI
from config import dp
from aiogram.types import Message
import text
import game


@dp.message_handler(commands=['start'])
async def mes_start(message: Message):
    await message.answer(f'{message.from_user.first_name}{text.greeting}')


@dp.message_handler(commands=['new_game'])
async def start_new_game(message: Message):
    print(message.from_user.first_name)
    print(message.date.date())
    game.new_game()
    if game.game():
        game.log_data(f"{message.from_user.first_name}{text.start_new_game}")
        toss = RI(0, 1)
        if toss:
            await message.answer(text.toss)
            await player_turn(message)
        else:
            await bot_turn(message)
    else:
        await message.answer(text.error_new_game)


async def player_turn(message: Message):
    await message.answer(f"{message.from_user.first_name}{text.player_turn}")


@dp.message_handler(commands=['set'])
async def set_total_candies(message: Message):
    try:
        count = message.text.split()[1]
    except:
        await message.answer(f'{text.error_set}')
    if count.isdigit():
        if game.game():
            await message.answer(f'{message.from_user.first_name}{text.error_set_total_new_game}')
        else:
            game.log_data(f"{message.from_user.first_name}{text.set_total}{count}")
            game.set_user_total(int(count))
            await message.answer(f"{text.user_total}{count}")
    else:
        await message.answer(f"{count}{text.error_set_total_value}")

@dp.message_handler(commands=['set_mode'])
async def set_complex_mode(message: Message):
    try:
        value = message.text.split()[1]
    except:
        await message.answer(f'{text.error_set_mode}')
    if value.isdigit():
        if game.game():
            await message.answer(f'{message.from_user.first_name}{text.error_set_mode_new_game}')
        else:
            game.log_data(f"{message.from_user.first_name}{text.set_mode}{value}")
            game.set_bot_mode(int(value))
            await message.answer(f"{text.bot_mode}'{value}'")
    else:
        await message.answer(f"{value}{text.error_set_mode_value}")

@dp.message_handler(commands=['help'])
async def mes_help(message: Message):
    mess = ''
    for mes in text.commands:
        mess += f'\n{mes}'

    await message.answer(mess)


@dp.message_handler(commands=['description'])
async def mes_description(message: Message):
    await message.answer(text.description)


@dp.message_handler(commands=['finish'])
async def finish_game(message: Message):
    if game.game():
        game.log_data(f"{message.from_user.first_name}{text.log_finish}")
        game.finish_game()
        await message.answer(text.finish)
    else:
        await message.answer(text.error_finish)


@dp.message_handler(commands=['my_id'])
async def mes_my_id(message: Message):
        await message.answer(message.from_user.id)

@dp.message_handler()
async def take(message: Message):
    user_name = message.from_user.first_name
    if game.game():
        if message.text.isdigit():
            user_take = int(message.text)
            if (0 < user_take < 29) and user_take <= game.get_total():
                game.take_candies(user_take)
                if await check_win(message, user_take, "player"):
                    return
                await message.answer(f'{user_name}{text.user_take_candies(user_take)}')
                await bot_turn(message)
            elif user_take > 28:
                await message.answer(text.error_many_candies)
            elif user_take < 1:
                await message.answer(text.error_few_candies)
            elif user_take > game.get_total():
                await message.answer(text.error_candies)
        else:
            await message.answer(text.error_input_value)
    else:
        await message.answer(text.error_bot)


async def bot_turn(message: Message):
    total = game.get_total()
    if game.get_bot_mode():
        if total <= 28:
            bot_take = total
        else:
            bot_take = total % 29
            if bot_take == 0:
                bot_take = RI(1, 28)
    else:
        if total <= 28:
            bot_take = RI(1, total)
        else:
            bot_take = RI(1, 28)
    game.take_candies(bot_take)
    await message.answer(text.bot_take_candies(bot_take))
    if await check_win(message, bot_take, "бот"):
        return
    await player_turn(message)


async def check_win(message: Message, take: int, player: str):
    if game.get_total() <= 0:
        if player == "player":
            game.log_data(f"{text.player_win}{message.from_user.first_name}")
            await message.answer(f"{message.from_user.first_name}{text.user_win(take)}")
        else:
            game.log_data(f"{text.bot_win}")
            await message.answer(f"{message.from_user.first_name}{text.bot_win(take)} ")
        game.new_game()
        game.set_default_bot_mode()
        return True
    else:
        return False
