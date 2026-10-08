# brozen AI — Railway-ready Telegram bot

ربات تلگرام فارسی برای چت AI، فروش پلن، پرداخت دستی با رسید و تأیید ادمین.

## فایل‌ها

همه فایل‌های اصلی باید مستقیماً در ریشه‌ی مخزن GitHub باشند؛ نه داخل یک پوشه‌ی تودرتو:

- `bot.py`
- `requirements.txt`
- `Procfile`
- `railway.toml`
- `.python-version`

## دیپلوی صحیح در Railway

> Railway معمولاً فایل ZIP را مستقیماً به‌عنوان سورس پروژه Deploy نمی‌کند. ZIP را روی دستگاه خود Extract کن و فایل‌های داخل آن را به یک مخزن GitHub بفرست؛ سپس در Railway گزینه‌ی **New Project → Deploy from GitHub Repo** را انتخاب کن.

1. در GitHub یک repository جدید بساز.
2. محتویات ZIP را Extract کن و فایل‌ها را مستقیماً در ریشه‌ی repository قرار بده.
3. Commit/Push کن.
4. در Railway یک پروژه از همان GitHub repository بساز.
5. در **Variables** متغیرهای زیر را اضافه کن.
6. Deploy Logs را بررسی کن. Start Command از `railway.toml` برابر `python bot.py` است. در `Procfile` نام process برابر `worker` است تا ربات به‌عنوان worker شناخته شود، نه web service.

## Railway Variables

اجباری:

- `BOT_TOKEN` — توکن BotFather
- `ADMIN_IDS` — آیدی عددی تلگرام ادمین؛ اگر چند ادمین داری با کاما جدا کن، مثل `123456789,987654321`

برای فعال شدن AI:

- `OPENAI_API_KEY` — کلید API معتبر
- `AI_MODEL` — اختیاری، پیش‌فرض `gpt-5-mini`

اختیاری:

- `BRAND_NAME=brozen AI`
- `SUPPORT_USERNAME=IBrOzen`
- `CURRENCY=تومان`
- `DB_PATH=/data/brozen_ai.db` (اگر Railway Volume به `/data` وصل کردی؛ بدون Volume از `data/brozen_ai.db` استفاده می‌شود.)

اگر `OPENAI_API_KEY` هنوز تنظیم نشده باشد، خود ربات و فروشگاه می‌توانند بالا بیایند، اما پاسخ‌گویی AI تا افزودن کلید کار نمی‌کند.

## قابلیت‌ها

- منوی فارسی و پیام خوش‌آمد قابل تنظیم
- ساخت پلن از پنل/دستور ادمین `/newplan`
- قیمت، مدت و اعتبار پلن
- پرداخت دستی، ارسال رسید و تأیید/رد ادمین
- فعال‌سازی اشتراک پس از تأیید پرداخت
- کد تخفیف با `/addcoupon CODE PERCENT [MAX_USES]`
- تنظیم کارت با `/setcard شماره|نام`
- تنظیم خوش‌آمد با `/setwelcome متن`
- تنظیم پشتیبانی با `/setsupport username`
- تنظیم مدل با `/setmodel gpt-5-mini`
- Health endpoint در `/health`
- SQLite

## نکته‌های مهم

- این نسخه پرداخت دستی است؛ درگاه بانکی آنلاین به اتصال رسمی درگاه نیاز دارد.
- برای حفظ دیتابیس پس از redeploy، یک Railway Volume بساز و آن را به `/data` متصل کن، سپس `DB_PATH=/data/brozen_ai.db` قرار بده.
- Deploy صددرصدی را نمی‌توان بدون دسترسی به پروژه و Variables واقعی Railway تضمین کرد. این بسته از نظر ساختار فایل، پیکربندی و syntax بررسی شده؛ خطاهای وابسته به توکن، کلید API، GitHub یا تنظیمات حساب باید در Deploy Logs دیده شوند.

## گزارش بررسی
فایل `AUDIT_REPORT.md` اصلاحات و تست‌های آفلاین انجام‌شده را توضیح می‌دهد. فایل `check_deploy.py` را می‌توان محلی با `python check_deploy.py` اجرا کرد. این بررسی جایگزین تست واقعی در Railway نیست.
