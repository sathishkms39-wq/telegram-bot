import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram

TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    update.message.reply_text("Vanakkam! File to Link bot ready ✅")

def echo(update, context):
    if update.message.document:
        file = update.message.document.get_file()
        link = file.file_path
        update.message.reply_text(f"Download link: {link}")
    else:
        update.message.reply_text("Please send me a file 📂")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.all, echo))

updater.start_polling()
updater.idle()
