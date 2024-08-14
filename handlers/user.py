from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from aiogram.fsm.context import FSMContext

from signature import user, bot
import keyboards.inline_kb as kb
from config import price_services, admin_list
from handlers.text import user_start, service_text, questions

router = Router()


@router.message(CommandStart())
async def cmd_start(msg: Message):
    if msg.from_user.id in admin_list:
        await msg.answer("Вы в админ панели", reply_markup=kb.menu_admin)
    else:
        await msg.answer(user_start, reply_markup=kb.menu_user())
        if not await user.check_user(user_id=msg.from_user.id):
            await user.add_user(user_id=msg.from_user.id,  username=msg.from_user.username)


@router.callback_query(F.data  == 'services')
async def cmd_services(call: CallbackQuery):
    await call.message.edit_text(service_text, reply_markup=kb.menu_services())


@router.callback_query(F.data == 'support')
async def cmd_support(call: CallbackQuery):

    service_info = price_services.get(call.data, {})
    price = service_info.get("price", "")
    support = service_info.get("text", "")

    await call.message.edit_text(
        f"""🎓<b><u>{support}</u></b>\n
ℹ️Эта услуга идеально подходит для тех, кто столкнулся с <b>непризывным заболеванием</b> или другим <b>основанием</b> для освобождения от военной службы и <b>имеет соответствующие документы.</b>\n
<b>В рамках данной услуги вас ожидает:</b>\n
📌<b>Неограниченное количество консультаций, связанных с получением военного билета или отсрочки;\n
📌Анализ медицинских документов для подтверждения диагноза и сопровождение до необходимого уровня для негодности истории болезни;\n
📌Подготовка заявлений в медицинские учреждения и военкоматы, при необходимости;\n
📌Написание жалоб в вышестоящий РВК или суд первой и вышестоящих инстанций.</b>\n
🔖<u>Стоимость услуги составляет</u> <s>600</s> <b>{price}.</b>""", reply_markup=kb.menu_support(services=call.data)
    )


@router.callback_query(F.data == 'ind_cons')
async def cmd_ind_cons(call: CallbackQuery):

    service_info = price_services.get(call.data, {})
    price = service_info.get("price", "")
    support = service_info.get("text", "")

    await call.message.edit_text(
        f"""<b><u>{support}</u></b>\n
Включает в себя:
📌 ответы на вопросы в рамках мероприятий призыва на срочную военную службу, переосвидетельствования, в том числе вопросы медицинского характера;\n
📌 оценка медицинских документов врачами на предмет непризывных патологий, предварительное определение категории годности\n
📌 разъяснение доступным языком действующего законодательства (как оно действует на практике и где оно не действует вовсе) со ссылками на нормативно правовые акты и примерами из практики\n
📌 инструктаж перед явкой в военкомат\n
📌 презентация пакетов услуг «Военный билет» и «Поддержка»\n
<b>Длительность</b>
40 минут\n
<b>Формат</b>
📞 Аудиозвонок в телеграм
🤝 Диалог без формализма\n
<b>Как начать</b>
После оплаты консультации в рабочее время с вами свяжется менеджер для согласования даты и времени консультации\n
<b>🔖<u>Стоимость услуги</u></b>
{price} (1 usdt ~ 1 usd)\n
🚨<b>UPD 06.04.24: по всем изменениям законодательства тоже консультируем и отправляем сжатую письменную информацию</b>""", reply_markup=kb.menu_support(services=call.data)
    )


@router.callback_query(F.data == 'military_ticket')
async def cmd_military_ticket(call: CallbackQuery):

    service_info = price_services.get(call.data, {})
    price = service_info.get("price", "")
    support = service_info.get("text", "")
    
    await call.message.delete()
    await call.message.answer(
        f"""<b><u>{support}</u></b>\n
<i>Услуга включает в себя полное сопровождение профессионального юриста на пути к получению отсрочки или военного билета.</i>\n
<b>В данную услугу входит:</b>\n
📌 неограниченное количество консультаций, связанных с получением военного билета или отсрочки;\n
📌 изучение первичной документации, для составления углубленного плана обследований;\n
📌 помощь в формировании пакета документов в РВК по медицинскому или юридическому основанию;\n
📌 информационная поддержка специалистом по РВК во время прохождения мед. комиссии в военкомате;\n
📌 помощь при составлении жалоб в вышестоящий РВК или суд первой и вышестоящих инстанций.\n
<u><b>Стоимость услуги</b></u> <s>1500</s> <b>{price}</b>.""", reply_markup=kb.menu_support(services=call.data)
    )


@router.callback_query(F.data == 'faq')
async def cmd_faq(call: CallbackQuery):
    await call.message.edit_text("<b>Популярные вопросы:</b>")
    for question in questions:
        await call.message.answer(question)

    await call.message.answer("О чем Вам рассказать?", reply_markup=kb.menu_user())


@router.callback_query(F.data.casefold().in_(['back_services', 'back_support']))
async def cmd_back_all(call: CallbackQuery):
    if call.data == 'back_services':
        await call.message.edit_text(user_start, reply_markup=kb.menu_user())

    if call.data == 'back_support':
        await call.message.edit_text(service_text, reply_markup=kb.menu_services())


@router.callback_query(F.data.casefold().in_(['meneger', 'change_cripto']))
async def cmd_send_meneger(call: CallbackQuery):
    await call.message.edit_text("🗞Нажмите на кнопку ниже и укажите, какой криптовалютой желаете оплатить.", reply_markup=kb.menu)


@router.callback_query(F.data == 'reviews')
async def cmd_reviews(call: CallbackQuery, state: FSMContext):
    info = await user.get_reviews()
    await state.update_data(info=info)
    await call.message.delete()
    await call.message.answer_photo(photo=info[0][0], caption=info[0][1], reply_markup=kb.pagination(page=0))


@router.callback_query(F.data.startswith(('next_', 'prev_')))
async def cmd_pagination(call: CallbackQuery, state: FSMContext):
    action, page = call.data.split("_")
    page = int(page)

    data = await state.get_data()
    info = data['info']

    if action == 'next':
        page = page + 1 if page < (len(info) - 1) else page
    if action  == 'prev':
        page = page - 1 if page > 0 else 0

    await call.message.delete()
    await bot.send_photo(call.from_user.id, photo=info[page][0], caption=info[page][1], reply_markup=kb.pagination(page=page))
