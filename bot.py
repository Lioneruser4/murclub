from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Telegram bot token'ınızı buraya ekleyin
TOKEN = "5741055163:AAGgnte1NoULR4ERoeX43aCGiF6VDOOds4o"

def start(update: Update, context: CallbackContext) -> None:
    # WebView bağlantısını gönder
    webview_url = "https://lioneruser4.github.io/roulette-game/"
    update.message.reply_text(f" giriş yapmak için [buraya tıklayın]({webview_url}).", parse_mode="Markdown")

def main() -> None:
    # Bot'u başlat
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # /start komutunu ekleyin
    dispatcher.add_handler(CommandHandler("start", start))

    # Bot'u çalıştır
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
