from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, WebAppInfo, \
    InlineKeyboardMarkup, InlineKeyboardButton

HOME_BUTTONS = ReplyKeyboardMarkup([
    [KeyboardButton("🤖 Asosiy sahifa", web_app=WebAppInfo(url="https://xiuedu.uz"))],
    [KeyboardButton("✍️ Xabar yo'llash"), KeyboardButton("✅ Rasmiy sahifalarimiz")]
], resize_keyboard=True)

CANSEL_BUTTON = ReplyKeyboardMarkup([
    [KeyboardButton("❌ Bekor qilish")]
], resize_keyboard=True)

def ADMIN_BUTTONS(messgae_id):
    ADMIN_BUTTONS = InlineKeyboardMarkup([
        [InlineKeyboardButton(text="✅ Javob berish", callback_data=f"javob_berish_{messgae_id}")]
    ])
    return ADMIN_BUTTONS

INLINE_CANSEL_BUTTON = InlineKeyboardMarkup([
    [InlineKeyboardButton(text="❌ Bekor qilish", callback_data="bekor_qilish")]
])
