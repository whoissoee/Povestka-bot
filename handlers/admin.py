from aiogram import F, Router
from aiogram.types import CallbackQuery, Message

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from signature import user
import keyboards.inline_kb as kb

admin = Router()


class Addreviews(StatesGroup):
    reviews = State()


@admin.callback_query(F.data == 'add_reviews')
async def cmd_add_reviews(call: CallbackQuery, state: FSMContext):
    await state.set_state(Addreviews.reviews)
    await call.message.answer("Отправьте фото отзыва вместе с описанием")


@admin.message(Addreviews.reviews)
async def load_reviews(msg: Message,state: FSMContext):

    command_args = msg.caption
    photo = msg.photo[-1].file_id

    if photo or command_args:
        await user.add_reviews(photo=photo, caption=command_args)
        await msg.answer("Добавлено!")
        await state.clear()
    else:
        await msg.answer("Один с параметров неверно передан!")
        