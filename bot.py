import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes

load_dotenv()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я эхо-бот — повторяю всё что ты пишешь.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

async def echo_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    caption = update.message.caption if update.message.caption else "Держи своё фото!"
    await update.message.reply_photo(photo.file_id, caption=caption)

async def echo_sticker(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sticker = update.message.sticker
    await update.message.reply_sticker(sticker.file_id)

async def echo_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    voice = update.message.voice
    await update.message.reply_voice(voice.file_id, caption="Держи своё аудио!")

def main():
    app = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.add_handler(MessageHandler(filters.PHOTO, echo_photo))
    app.add_handler(MessageHandler(filters.Sticker.ALL, echo_sticker))
    app.add_handler(MessageHandler(filters.VOICE, echo_voice))

    print("Бот запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()