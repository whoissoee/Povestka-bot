from aiogram.utils.keyboard import (
    InlineKeyboardBuilder, InlineKeyboardButton, InlineKeyboardMarkup
)

from config import price_services


def menu_user():
    buttons = [
        ("⚙️Услуги", "services"),
        ("👤Консультация", "ind_cons"),
        ("📂Отзывы", "reviews"),
        ("ℹ️FAQ", "faq")
    ]

    builder = InlineKeyboardBuilder()
    for text, callback_data in buttons:
        builder.add(InlineKeyboardButton(text=text, callback_data=callback_data))
    return builder.adjust(3, 1).as_markup()


def menu_services():
    builder = InlineKeyboardBuilder()
    for key, value in price_services.items():
        text = value["text"]
        callback_data = key
        builder.add(InlineKeyboardButton(text=text, callback_data=callback_data))
    builder.row(InlineKeyboardButton(text="🔙Назад", callback_data="back_services"))
    return builder.adjust(1).as_markup()


def menu_support(services):
    buttons = [
        ("💳Оплатить услугу", f"bay_{services}"),
        ("📂Отзывы", "reviews"),
        ("ℹ️FAQ", "faq"),
        ("👤Менеджер", "meneger"),
        ("🔙Назад", "back_support")
    ]

    builder = InlineKeyboardBuilder()
    for text, callback_data in buttons:
        builder.add(InlineKeyboardButton(text=text, callback_data=callback_data))
    return builder.adjust(1, 2, 1, 1).as_markup()


def menu_sucs_payment():
    buttons = [
        ("🔍Оплатить другой криптовалютой", "change_cripto"),
        ("👤Менеджер", "meneger"),
        ("📂Отзывы", "reviews"),
        ("ℹ️FAQ", "faq"),
        ("🔙Назад", "back_support")
    ]

    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="✅Оплатил USDT TRC20", url="https://t.me/whoissoee"))
    for text, callback_data in buttons:
        builder.add(InlineKeyboardButton(text=text, callback_data=callback_data))
    return builder.adjust(1, 3, 1).as_markup()


menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Написать нам", url='https://t.me/whoissoee')]
])


menu_admin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Добавить отзыв", callback_data="add_reviews")]
])


def pagination(page):
    buttons = [
        ("◀️Назад", f"prev_{page}"),
        ("▶️Вперед", f"next_{page}")
    ]

    builder = InlineKeyboardBuilder()
    for text, callback_data in buttons:
        builder.add(InlineKeyboardButton(text=text, callback_data=callback_data))
    return builder.adjust(2).as_markup()


