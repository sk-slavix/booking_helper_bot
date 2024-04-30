import telebot
from telebot import types

bot = telebot.TeleBot('6878195444:AAE7poXCeC1qCleJ3QKGSpjs9G0i7njnZeE')

# Декоратор для обработки команл бота
@bot.message_handler(commands=['start'])
def main(message):
    # bot.send_message(message.chat.id, 'Hi there!')
    bot.send_message(message.chat.id, message)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    
    bt1 = types.KeyboardButton('Open web-sute')
    markup.row(bt1)
    bt2 = types.KeyboardButton('Delete photo')
    bt3 = types.KeyboardButton('Edit text')
    markup.row(bt2, bt3)
    
    # bot.send_message(message.chat.id, 'Hi friend', reply_markup=markup)
    bot.send_message(message.chat.id, 'Hi friend')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    # bot.send_message(message.chat.id, message)
    
    markup = types.InlineKeyboardMarkup()
    # markup.add(types.InlineKeyboardButton('Open web-sute', url='https://google.com'))
    # markup.add(types.InlineKeyboardButton('Delete photo', callback_data='Photo is deleted'))
    # markup.add(types.InlineKeyboardButton('Edit text', callback_data='Text is changed'))
    bt1 = types.InlineKeyboardButton('Open web-sute', url='https://google.com')
    markup.row(bt1)
    bt2 = types.InlineKeyboardButton('Delete photo', callback_data='delete')
    bt3 = types.InlineKeyboardButton('Edit text', callback_data='edit')
    markup.row(bt2, bt3)
        
    bot.reply_to(message, 'Beautiful photo', reply_markup=markup)

# для обробки колбек клавіш треба створити наступні функції
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)
        

# Щоб програма працювала постійно  
# bot.polling(none_stop=True)
# абсолютно теж саме
bot.infinity_polling() 