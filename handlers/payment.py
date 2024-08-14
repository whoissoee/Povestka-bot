from aiogram import F
from aiogram.types import Message, CallbackQuery

from handlers.user import router
import keyboards.inline_kb as kb
from config import price_services


@router.callback_query(F.data.startswith("bay_"))
async def cmd_bay(call: CallbackQuery):

    service_info = price_services.get(call.data.split("_")[1], {})
    price = service_info.get("price", "")
    support = service_info.get("text", "")
    
    await call.message.edit_text(
        f"""📄Оплата производится на <b>наш криптокошелёк USDT TRC20</b>. (<b>анонимно и безопасно</b>)\n
<b>Стоимость услуги "{support}": {price}</b>\n
Кошелек для оплаты USDT TRC20 (копируется при нажатии):\n
<code>code</code>\n
По ссылке site предоставлена информация о том, как приобрести криптовалюту, если у вас её нет.\n
<b>После оплаты, нажмите кнопку “Оплатил USDT TRC20”, мы свяжемся с вами для записи на консультацию.</b>\n
<u>Если у вас есть вопросы или возникли проблемы с оплатой, нажмите кнопку “Менеджер”</u>""", reply_markup=kb.menu_sucs_payment()
    )
        