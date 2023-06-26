import telebot                                      # библиотека pyTelegramBotAPI
import private


bot = telebot.TeleBot(private.TELEGRAM_TOKEN)


@bot.message_handler(commands=['start'])            # декоратор для приема команд из бота.
#                                                   # Можно указать сколько угодно, или ничего
def start(current_chat):
    bot.send_message(current_chat.chat.id, f'Привет, {current_chat.from_user.first_name}!')


@bot.message_handler(commands=['help'])
def bot_help(current_chat):
    help_text = 'Прямо сейчас <b>активно</b> помогаем'
    bot.send_message(current_chat.chat.id, help_text, parse_mode='html')    # parse_mode - обработка  простых html-тэгов


bot.polling(none_stop=True)                         # для того чтобы программа не завершалась
# bot.infinity_polling()                            # тоже самое

