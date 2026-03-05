import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes

load_dotenv()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я эхо-бот — повторяю всё что ты пишешь.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

def main():
    app = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("Бот запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()
