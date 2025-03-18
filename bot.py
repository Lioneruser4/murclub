from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler
from dotenv import load_dotenv
import os

# .env dosyasından ortam değişkenlerini yükle
load_dotenv()

# Telegram bot token'ını buradan al
TOKEN = "5741055163:AAGgnte1NoULR4ERoeX43aCGiF6VDOOds4o"

def start(update: Update, context: CallbackContext) -> None:
    # Inline Keyboard Butonu oluştur
    keyboard = [
        [InlineKeyboardButton("Oynamak için dokun 🎮", web_app={"url": "https://lioneruser4.github.io/slot-game/"})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Kullanıcıya mesaj gönder
    update.message.reply_text(
        "Slot oyununu oynamak için aşağıdaki butona dokunun:",
        reply_markup=reply_markup
    )

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
