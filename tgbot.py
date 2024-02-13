import telebot


TOKEN = '6988974701:AAGyEpNKRfn4_tkk55p4wduJbMEtBODUWII'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я бот для отправки сообщений.")


def send_notification(order_number,sum):
    target_user_ids = [6335014694] # вітя - 6335014694 nekit - 747341930 moy - 5260769677
    for user_id in target_user_ids:
        bot.send_message(user_id, f"Привет! Поступил новый заказ: №{order_number} \n На сумму {sum}")


if __name__ == "__main__":
    bot.polling(none_stop=True)
