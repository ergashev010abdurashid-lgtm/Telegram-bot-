from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8981400107:AAG1ZKhhgeHdVzDI6OQVXcO8-Wu_tO_NBYI"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Bot ishlayapti ✅")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
