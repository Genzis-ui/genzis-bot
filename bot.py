from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8996256208:AAE2vOg_NH7Q-f_99TOfOwvR6buaCFdtCas"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """👋 Welcome to <b>Genzis Official Support Bot</b> 🇺🇬

We are building sovereign AI, cloud infrastructure, and digital talent for Africa.

Your support helps us create Africa's technological future.

Choose how you want to donate:"""

    keyboard = [
        [InlineKeyboardButton("💰 PayPal / International", callback_data="paypal")],
        [InlineKeyboardButton("📱 Mobile Money (MTN / Airtel)", callback_data="mobile")],
        [InlineKeyboardButton("🌍 Our Mission", callback_data="impact")]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text, reply_markup=reply_markup, parse_mode='HTML')

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "paypal":
        text = """💰 <b>PayPal Donations</b>

Send your donation to:
<b>obidonald763@gmail.com</b>

Please include your name and "Genzis Donation" in the note.

After sending, forward the receipt here."""

    elif query.data == "mobile":
        text = """📱 <b>Mobile Money Donations</b>

Send to: <b>+256 782 422 223</b>

Networks: MTN or Airtel

After sending, forward the receipt/screenshot here."""

    elif query.data == "impact":
        text = """🌍 <b>Genzis Mission</b>

We are building African-led AI and sovereign digital infrastructure for the continent.

Thank you for supporting us!"""

    await query.edit_message_text(text, parse_mode='HTML')

# Start the bot
app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

print("✅ Genzis Donation Bot is running...")
app.run_polling()