TOKEN = ""

DB_USER = 'postgres'
DB_PASSWORD = ''
DB_HOST = 'localhost'
DB_NAME = ''
sqlalchemy_url = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'


price_services = {
    "support": {"price": "500 USDT", "text": "Поддержка"},
    "ind_cons": {"price": "40 USDT", "text":  "Индивидуальная консультация"},
    "military_ticket": {"price": "1260 USDT", "text": "📑Пакет решений 'Военный билет'"}
}


admin_list  = []