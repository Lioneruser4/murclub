from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

# Telegram bot token'ınızı buraya ekleyin
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def start(update: Update, context: CallbackContext) -> None:
    # WebView bağlantısını gönder
    webview_url = "https://your-vercel-app.vercel.app"
    update.message.reply_text(f"MurClub'a giriş yapmak için [buraya tıklayın]({webview_url}).", parse_mode="Markdown")

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
