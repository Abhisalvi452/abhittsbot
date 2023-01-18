import telegram
from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("Hello! I am a Telegram bot.")

def main():
    # Replace YOUR_TOKEN with the token of your bot
    updater = Updater("5444828269:AAHYJxZzgRNMVqTkwXaCeEReU2q8r5Hiazs", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
