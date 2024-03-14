import os
import requests
from telegram.ext import Updater, CommandHandler

# Binance API endpoint
API_ENDPOINT = "https://api.binance.com/api/v3/ticker/price"

# Telegram bot token
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")

# Function to handle the /price command
def price(update, context):
    # Fetch the symbol from the command argument
    symbol = context.args[0].upper()

    # Make a request to the Binance API
    response = requests.get(API_ENDPOINT, params={"symbol": symbol})

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        price = data.get("price")
        update.message.reply_text(f"The current price of {symbol} is {price}")
    else:
        update.message.reply_text("Failed to fetch price. Please try again later.")

def main():
    # Create the Updater and pass it your bot's token
    updater = Updater(TELEGRAM_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register the /price handler
    dp.add_handler(CommandHandler("price", price, pass_args=True))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == "__main__":
    main()
