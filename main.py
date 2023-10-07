from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, \
    ContextTypes, MessageHandler, filters, CallbackQueryHandler

from texts import *
from buttons import *
from states import *
from messages import messages

# dotenv
import os
from dotenv import load_dotenv
load_dotenv()

# Logs
import logging

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Set state
    context.user_data['state'] = STATE_HOME

    user = update.effective_user

    await update.message.reply_text(
        text=str(HELLO_TEXT).format(user.first_name),
        parse_mode="HTML",
        reply_markup=HOME_BUTTONS
    )

async def inline(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    user = update.callback_query.from_user

    await query.answer()

    data = query.data.split("_")
    user_id = data[2]
    context.user_data['user_id'] = user_id

    # Change state
    context.user_data['state'] = STATE_REPLY

    await query.message.reply_text(
        text=ADMIN_WRITE_MESSAGE,
        parse_mode="HTML"
    )


TOKEN = os.getenv("TOKEN")
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, messages))
app.add_handler(CallbackQueryHandler(inline))

if __name__ == "__main__":
    app.run_polling()