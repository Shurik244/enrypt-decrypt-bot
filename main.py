import telebot # pip install telegrambotapi

bot= telebot.TeleBot('')

def encrypt(msg, shift):
    output=""
    for char in msg:
        if char == ' ':
            pass
        elif char.isupper():
            output = output + chr((ord(char) + shift - 1072) % 26 + 1072)
        else:
            output = output + chr((ord(char) + shift - 1040) % 26 + 1040)

    return output


def decrypt(msg, shift):
    res = ''
    for char in msg:
        if char == ' ':
            pass
        elif  char.isupper():
            res = res + chr((ord(char) - shift - 1072) % 26 + 1072)
        else:
            res = res + chr((ord(char) - shift - 1040) % 26 + 1040)
    return res


def get_arg(arg):
    try:
        arg = arg.split()[1:]
    except:
        arg = ''
    return arg


def ltstr(msg): 
    str1 = "" 
    for ele in msg: 
        str1 += ele + ' '
    return str1 


@bot.message_handler(commands = ['encrypt'])
def msg_encrypt(message):
    error = 'Вы не указали параметры шифрования!\nПример: `/encrypt {Ваше сверх секретное сообщение} {цифра смещения}`'
    arg = get_arg(message.text)
    if len(arg) >= 2:
        try:
            shift = int(arg[-1])
            bot.send_message(message.chat.id, f"{encrypt(ltstr(arg[0:-1]), shift)}")
        except ValueError:
            bot.send_message(message.chat.id, error, parse_mode = 'Markdown')
    else:
        bot.send_message(message.chat.id, error, parse_mode = 'Markdown')


@bot.message_handler(commands = ['decrypt'])
def msg_decrypt(message):
    error = 'Вы не указали параметры шифрования!\nПример: `/decrypt {Ваше зашифрованое сообщение} {цифра смещения}`'
    arg = get_arg(message.text)
    if len(arg) >= 2:
        try:
            shift = int(arg[-1])
            bot.send_message(message.chat.id, f"{decrypt(ltstr(arg[0:-1]), shift)}")
        except ValueError:
            bot.send_message(message.chat.id, error, parse_mode = 'Markdown')
    else:
        bot.send_message(message.chat.id, error, parse_mode = 'Markdown')


@bot.message_handler(commands = ['help'])
def help(message):
    bot.send_message(message.chat.id, '`/encrypt {Ваше сверх секретное сообщение} {цифра смещения}` - **Зашифрует ваше сообщение**\n`/decrypt {Ваше зашифрованое сообщение} {цифра смещения}` - **Расшифрует сообщение**\n`Бот создан:` [YOKA](tg://user?id=1941611154) & [Shurik24](tg://user?id=1386048883)', parse_mode = 'Markdown')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Этот бот создан для шифрации/дешифрации сообщений с использованием шифра Цезаря\nЧтобы узнать как использовать бота используй /help")


@bot.message_handler(func=lambda m:True ,content_types=['document','audio','sticker','photo'])
def echo_(message):
    bot.send_message(message.chat.id, 'Бот поддерживает только текст!')


bot.polling()
