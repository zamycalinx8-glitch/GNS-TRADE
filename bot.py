
import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 BIENVENUE SUR XIRIS TRADING SIGNALS\n\n"
        "📊 Plateforme de signaux Pocket Option\n"
        "💹 Analyse technique en préparation.\n\n"
        "Commandes disponibles :\n"
        "/start - Accueil\n"
        "/signal - Demander une analyse\n"
        "/help - Aide\n\n"
        "⚠️ Aucun signal n'est garanti."
    )

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 XIRIS TRADING SIGNALS\n\n"
        "⏳ Analyse de marché non connectée.\n"
        "Aucun signal fiable disponible actuellement.\n"
        "Réessaie après configuration du flux de données."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Utilise /start pour commencer.\n"
        "Utilise /signal pour demander une analyse."
    )

def main():
    if not TOKEN:
        raise RuntimeError("Token Telegram manquant.")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))
    app.add_handler(CommandHandler("help", help_command))

    print("XIRIS TRADING SIGNALS est en démarrage...")
    app.run_polling()

if __name__ == "__main__":
    main()
