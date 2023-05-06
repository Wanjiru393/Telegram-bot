from telegram import *
from telegram.ext import *
from requests import *

updater = Updater(token="")
#add your token
dispatcher = updater.dispatcher

randomPictureText = "Random Picture"
randomPersonText = "Static Image"

randomPictureUrl = "https://picsum.photos/1200"
randomPersonUrl = "https://picsum.photos/seed/picsum/200/300"


def start(update: Update, context:CallbackContext):
    buttons = [[KeyboardButton(randomPictureText)], [KeyboardButton(randomPersonText)]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to LaFliq Gallery!",
    reply_markup=ReplyKeyboardMarkup(buttons))

def messageHandler(update: Update, context: CallbackContext):
    if randomPersonText in update.message.text:
        image = get(randomPersonUrl).content
    if randomPictureText in update.message.text:
        image = get(randomPictureUrl).content
    
    if image:
        context.bot.sendMediaGroup(chat_id=update.effective_chat.id, media=[InputMediaPhoto
        (image, caption="")])

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))


updater.start_polling()
updater.idle()
