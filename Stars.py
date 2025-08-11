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

print("\nAzaboi")
print("Mavjud raqamlar ✅")
index = 0

results = []

with open('phone.csv', 'r') as f:
    str_list = [row[0] for row in csv.reader(f)]

    for pphone in str_list:
        api_id = er
        api_hash = err
        phone = utils.parse_phone(pphone)
        index += 1

        client = TelegramClient(f"sessions/{phone}", api_id, api_hash)

        try:
            client.connect()
            if not client.is_user_authorized():
                print(f"Akk {index}: +{phone}")
                print("⚠️ Sessiya avtorizatsiya qilinmagan (kod/parol kerak). SKIP qilindi!\n")
                continue

            me = client.get_me()
            full = client(GetFullUserRequest(me.id))
            gifts_count = getattr(full.full_user, 'stargifts_count', None)
            is_premium = getattr(me, 'premium', False)
            result = client(functions.payments.GetStarsStatusRequest(peer=me.id))
            stars_balance = result.balance.amount if hasattr(result.balance, 'amount') else 0

            first_name = me.first_name or ""
            last_name = me.last_name or ""
            full_name = (first_name + " " + last_name).strip()
            username = f"@{me.username}" if me.username else ""

            print(f"Akk {index}: +{phone} | {full_name} | {username}")

            # Gift
            if gifts_count and gifts_count > 0:
                print(f"🎁 Gift bor! Gifts count: {gifts_count}")
            else:
                print("❌ Gift yo'q")

            # Premium
            if is_premium:
                print("✅ Premium foydalanuvchi!")
            else:
                print("❌ Premium emas")

            # Stars
            if stars_balance > 0:
                print(f"⭐ Stars bor! Balance: {stars_balance}")
            else:
                print("❌ Stars yo'q")

            print()  # Bo‘sh qator bilan ajratish

            if (gifts_count and gifts_count > 0) or is_premium or stars_balance > 0:
                results.append({
                    "index": index,
                    "phone": phone,
                    "full_name": full_name,
                    "username": username,
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
            print(f"Akk {index}: +{phone}")
            print(f"⚠️ Skipped: {e}\n")

        except Exception as e:
            print(f"Akk {index}: +{phone}")
            print(f"⚠️ Skipped unknown error: {e}\n")

        finally:
            client.disconnect()

print("\n=== Yakuniy ro'yxat: BOR bo‘lganlar ===\n")
if results:
    for r in results:
        print(f"{r['index']}) +{r['phone']} | {r['full_name']} | {r['username']} | 🎁 Gift: {r['gift']} | 🏆 Premium: {r['premium']} | ⭐ Stars: {r['stars']}")
else:
    print("Hech bir akkauntda gift/premium/stars topilmadi.")
