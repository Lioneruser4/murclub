from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from dotenv import load_dotenv
import os
import requests
import json

# .env dosyasından ortam değişkenlerini yükle
load_dotenv()

# Telegram bot token'ını buradan al
TOKEN = "5741055163:AAGgnte1NoULR4ERoeX43aCGiF6VDOOds4o"

def start(update: Update, context: CallbackContext) -> None:
    # WebView bağlantısını gönder
    webview_url = "https://ssyoutube.com"  # WebView sayfanızın URL'si
    update.message.reply_text(
        f"Video veya müzik indirmek için [buraya tıklayın]({webview_url}).",
        parse_mode="Markdown"
    )

def handle_webview_data(update: Update, context: CallbackContext) -> None:
    # WebView'den gelen veriyi al
    webview_data = update.message.web_app_data.data
    data = json.loads(webview_data)
    youtube_url = data.get("url")

    if youtube_url:
        try:
            # ssyoutube.com API'sine istek gönder
            api_url = f"https://ssyoutube.com/api/convert?url={youtube_url}"
            response = requests.get(api_url)
            if response.status_code == 200:
                # İndirme bağlantısını al
                download_link = response.json().get("download_url")
                if download_link:
                    # Dosyayı indir
                    file_response = requests.get(download_link)
                    if file_response.status_code == 200:
                        # Dosyayı Telegram üzerinden gönder
                        update.message.reply_document(document=file_response.content)
                    else:
                        update.message.reply_text("Dosya indirilemedi.")
                else:
                    update.message.reply_text("İndirme bağlantısı bulunamadı.")
            else:
                update.message.reply_text("ssyoutube.com API'si ile bağlantı kurulamadı.")
        except Exception as e:
            update.message.reply_text(f"Hata: {str(e)}")
    else:
        update.message.reply_text("Geçersiz YouTube linki.")

def main() -> None:
    # Bot'u başlat
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # /start komutunu ekleyin
    dispatcher.add_handler(CommandHandler("start", start))

    # WebView'den gelen verileri işle
    dispatcher.add_handler(MessageHandler(Filters.web_app_data, handle_webview_data))

    # Bot'u çalıştır
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
