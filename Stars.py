from telethon.sync import TelegramClient
from telethon import utils, functions
from telethon.tl.functions.users import GetFullUserRequest
from telethon.errors import (
    SessionPasswordNeededError,
    PhoneNumberBannedError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    RPCError,
    AuthKeyError,
)
import csv
from data import er, err  # API_ID va API_HASH

print("")
print("Azaboi")
print("Mavjud raqamlar ✅")
index = 0

results = []  # Faqat BOR bo‘lganlar shu yerga tushadi

with open('phone.csv', 'r') as f:
    str_list = [row[0] for row in csv.reader(f)]

    for pphone in str_list:
        api_id = er
        api_hash = err
        phone = utils.parse_phone(pphone)
        index += 1
        print("")
        print(f"Akk {index}: +{phone}")

        client = TelegramClient(f"sessions/{phone}", api_id, api_hash)

        gifts_count = None
        is_premium = False
        stars_balance = 0

        try:
            client.connect()
            if not client.is_user_authorized():
                print("⚠️ Sessiya avtorizatsiya qilinmagan (kod/parol kerak). SKIP qilindi!")
                continue

            me = client.get_me()
            full = client(GetFullUserRequest(me.id))

            # 🎁 Gift holati
            gifts_count = getattr(full.full_user, 'stargifts_count', None)
            if gifts_count and gifts_count > 0:
                print(f"🎁 Gift bor! Gifts count: {gifts_count}")
            else:
                print("❌ Gift yo'q")

            # 🏆 Premium holati
            is_premium = getattr(full.users[0], 'premium', False)
            if is_premium:
                print("✅ Premium foydalanuvchi!")
            else:
                print("❌ Premium emas")

            # ⭐ Stars holati
            result = client(functions.payments.GetStarsStatusRequest(peer=me.id))
            stars_balance = result.balance.amount if hasattr(result.balance, 'amount') else 0
            if stars_balance > 0:
                print(f"⭐ Stars bor! Balance: {stars_balance}")
            else:
                print("❌ Stars yo'q")

            # 🔥 Faqat BOR bo‘lsa ro‘yxatga qo‘shamiz
            if (gifts_count and gifts_count > 0) or is_premium or stars_balance > 0:
                results.append({
                    "index": index,
                    "phone": phone,
                    "gift": gifts_count,
                    "premium": is_premium,
                    "stars": stars_balance
                })

        except (
            SessionPasswordNeededError,
            PhoneNumberBannedError,
            PhoneCodeInvalidError,
            PhoneCodeExpiredError,
            RPCError,
            AuthKeyError,
            ConnectionError,
            OSError
        ) as e:
            print(f"⚠️ Skipped: {e}")

        except Exception as e:
            print(f"⚠️ Skipped unknown error: {e}")

        finally:
            client.disconnect()
            print()

# 🟢 Oxirida faqat BOR bo‘lganlar ro‘yxati
print("\n=== Yakuniy ro'yxat: BOR bo‘lganlar ===\n")
if results:
    for r in results:
        print(f"{r['index']}) +{r['phone']} | 🎁 Gift: {r['gift']} | 🏆 Premium: {r['premium']} | ⭐ Stars: {r['stars']}")
else:
    print("Hech bir akkauntda gift/premium/stars topilmadi.")
