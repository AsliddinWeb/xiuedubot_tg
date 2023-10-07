from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from texts import *
from buttons import *
from states import *

# dotenv
import os
from dotenv import load_dotenv
load_dotenv()

async def messages(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    user = update.effective_user

    state = context.user_data.get('state', STATE_HOME)

    if state == STATE_HOME:
        if text == "✅ Rasmiy sahifalarimiz":
            await update.message.reply_photo(
                photo=open("./xiu.jpg", "rb"),
                caption=SOCIAL_NETWORKS,
                parse_mode="HTML"
            )
        elif text == "✍️ Xabar yo'llash":
            # Change state
            context.user_data['state'] = STATE_WRITE

            await update.message.reply_text(
                text=WRITE_WELCOME,
                parse_mode="HTML",
                reply_markup=CANSEL_BUTTON
            )
    elif state == STATE_WRITE:
        if text == "❌ Bekor qilish":
            # Set state
            context.user_data['state'] = STATE_HOME

            user = update.effective_user

            await update.message.reply_text(
                text=str(HELLO_TEXT).format(user.first_name),
                parse_mode="HTML",
                reply_markup=HOME_BUTTONS
            )
        else:
            admin_id = os.getenv("ADMIN")
            await context.bot.sendMessage(
                chat_id=admin_id,
                text=str(SEND_ADMIN).format(
                    user.full_name,
                    user.id,
                    text
                ),
                parse_mode="HTML",
                reply_markup=ADMIN_BUTTONS(user.id)
            )
    elif state == STATE_REPLY:
        # Change state
        context.user_data['state'] = STATE_HOME

        # Userga
        await context.bot.sendMessage(
            chat_id=context.user_data['user_id'],
            text=f"<b>🔖 Admindan javob keldi!</b>\n\n"
                 f"<b>👉 Javob:</b> {text}",
            parse_mode="HTML"
        )

        # Adminga

        await update.message.reply_text(
            text="✅<b>Xabar yuborildi!</b>",
            parse_mode="HTML",
            reply_markup=HOME_BUTTONS
        )