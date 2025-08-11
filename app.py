import os
import colorama
from colorama import Fore, Style
import pyfiglet
import base64

colorama.init()

# Neon ko'k rangda "GOLDEN" yozuvi
text = "GOLDEN"
ascii_art = pyfiglet.figlet_format(text, font="block")  # Qalin shrift
print(f"{Fore.CYAN}{ascii_art}{Style.RESET_ALL}")

olam = True
while olam:
    print("\n\033[1;36m  ###############################################################")
    print("\n\033[1;35m scriptni sotib olish uchun tg: @Golden_PML | tell: +998773776665 ")
    print(
        f"""
            \033[1;32m_______________________________________
           |\033[1;32m  [ 0 ] \033[1;32m KODNI YANGILASH 
           |\033[1;32m  [ 1 ] \033[1;32m RAQAMLARNI TEKSHIRISH 
           |\033[1;32m  [ 2 ] \033[1;32m YANGI NOMER ULASH
           |\033[1;32m  [ 3 ] \033[1;32m YOPIQ/OCHIQ KANAL/GURUH LARGA QOʻSHILISH
           |\033[1;32m  [ 4 ] \033[1;32m KANALGA QOʻSHILISH
           |\033[1;32m  [ 5 ] \033[1;32m BARCHA KANALLARDAN CHIQISH 
           |\033[1;32m  [ 6 ] \033[1;32m BARCHA GURUHLARDAN CHIQISH 
           |\033[1;32m  [ 7 ] \033[1;32m SESSIYADAN KOD OLISH RAQAMGA  QAYTA KIRISH 
           |\033[1;32m  [ 8 ] \033[1;32m BAN BOʻLGAN RAQAMLARNI OʻCHIRISH 
           |\033[1;32m  [ 9 ] \033[1;32m PREMIUM/STARS YUTGANINI TEKSHIRISH 
           |\033[1;32m  [ 10 ] \033[1;32mAYTILGAN KANALDAN CHIQISH 
           |\033[1;32m  [ 11 ] \033[1;32mLICKAGA YOZISH ( hamma akkdan )
           |\033[1;32m  [ 12 ] \033[1;32mLICKAGA YOZISH ( aytilgan akkdan )
           |\033[1;32m  [ 13 ] \033[1;32mPOSTALRGA LIKE BOSISH 
           |\033[1;32m  [ 14 ] \033[1;32mBOTLARGA START BOSISH ( ref ID bilan )
           |\033[1;32m  [ 15 ] \033[1;32mSPAM TEKSHIRISH
           |\033[1;32m  [ 16 ]\033[1;32m ROSMOTR URISH ( oxirgi 10 post )
           |\033[1;32m  [ 17 ]\033[1;32m 2 BOSQICHLI PAROL OʻRNATISH
           |\033[1;32m  [ 18 ]\033[1;32m 2 BOSQICHLI PAROL OʻZGARTIRISH 
           |\033[1;32m  [ 19 ]\033[1;32m 2 BOSQICHLI PAROL OʻCHIRISH
           |\033[1;32m  [ 20 ]\033[1;32m RANDOM ISM QOʻYISH
           |\033[1;32m  [ 21 ]\033[1;32m RANDOM BIO QOʻYISH
           |\033[1;32m  [ 22 ]\033[1;32m AKKDAN DEVICE TOZALASH
           |\033[1;32m  [ 23 ]\033[1;32m KANAL/GURUH ZAYAFKA YUBORISH 
           |\033[1;32m  [ 24 ]\033[1;32m YANGI SEANS ULASH ( DEVICE )
           |\033[1;32m  [ 25 ]\033[1;32m YANGI SEANSDAN BOSHQA ESKILARINI CHIQARISH
           |\033[1;32m  [ 26 ]\033[1;32m LIMITIGA YETGAN AKK TOZALASH ( NEW )
           |\033[1;32m  [ 27 ]\033[1;32m RANDOM FAMILIYA QOʻYISH
           |\033[1;32m  [ 28 ]\033[1;32m PHONE.CSV BOʻSH JOYNI TOZALASH
           |\033[1;32m  [ 29 ]\033[1;32m 24/7 ONLINE QILISH
           |\033[1;32m  [ 30 ]\033[1;32m RAQAMLARNI DAVLATINI ANIQLASH
           |\033[1;32m  [ 31 ]\033[1;32m OXIRGI POST ORQALI KANALLARGA QOʻSHILISH ( @Giveaways_List )
           |\033[1;32m  [ 32 ]\033[1;32m BESTRANDOM KONKURS BOSISH ( NEW )
           |\033[1;32m  [ 33 ]\033[1;32m KOʻP KANALGA AZO ( UNIVERSAL )
           |\033[1;32m  [ 34 ]\033[1;32m RANDOM USERNAME QOʻYISH
           |\033[1;32m  [ 35 ]\033[1;32m SESSION DB TOZALASH ( ZARARI YOʻQ )
           |\033[1;32m  [ 36 ]\033[1;32m POSTGA REAKSIYA BOSISH 
           |\033[1;32m  [ 37 ]\033[1;32m TERMUX SESSIYA LOG OUT QILISH ( sessiyadan chiqish )
           |\033[1;32m  [ 38 ]\033[1;32m STORY KOʻRISH VA REAKSIYA BOSISH 
           |\033[1;32m  [ 39 ]\033[1;32m SOʻROVNOMAGA OVOZ BERISH
           |\033[1;32m  [ 40 ]\033[1;32m PHONE.CSV IKKI MARTA YOZILGAN RAQAM OʻCHIRISH 
           |\033[1;32m  [ 41 ]\033[1;32m SESSION PAPKASIDAN RAQAM YOZISH ( phone.csv ga )
           |\033[1;32m  [ 42 ]\033[1;32m RAQAMLAR PROFILI MALUMOTINI BILISH 
           |\033[1;32m  [ 43 ]\033[1;32m PREMIUM REAKSIYA BOSISH ( batllarga )
           |\033[1;32m  [ 44 ]\033[1;32m BOT START ( link va vaqt bilan )
           |\033[1;32m  [ 45 ]\033[1;32m IKKI BOSQICHLI PAROL TIKLASH ( 7kun kutib | malumot yoʻqolmaydi )
           |\033[1;32m  [ 46 ]\033[1;32m spam SPAM AKKLARDAN SPAMDAN CHIQISH UCHUN ARIZA YUBORISH
           |\033[1;32m  [ 47 ]\033[1;32m HIKOYA ( Story ) QOʻYISH 
           |\033[1;32m  [ 48 ]\033[1;32m PHONE.CSV DAGI RAQAMLAR SESSIYALARI AJRATISH 
           |\033[1;32m  [ 49 ]\033[1;32m USERNAME QOʻYISH ( New )
           |\033[1;32m  [ 50 ]\033[1;32m AVTO GURUH YARATIB ICHIGA POST YOZISH 
           |\033[1;32m  [ 51 ]\033[1;32m POSTLARGA REAKSIYA BOSISH ( UNIVERSAL )
           |\033[1;32m  [ 52 ]\033[1;32m PROFILDAGI STARS/GIFTLARNI TEKSHIRISH
           |\033[1;32m______________________________________\033"""
    )

    bf = (f'''\033[1;33m\n   Buyruq kiriting! :''')
    print("\n\033[1;36m  ###############################################################")
    jm = input(bf)

    if jm == "0":
        os.system("python3 update.py")
    elif jm == "1":
        os.system("python3 1_device.py")
    elif jm == "2":
        os.system("python3 2_device.py")
    elif jm == "3":
        os.system("python3 3_device.py")
    elif jm == "4":
        os.system("python3 9_device.py")
        olam = False
    elif jm == "5":
        os.system("python3 5_device.py")
    elif jm == "6":
        os.system("python3 6_device.py")
    elif jm == "7":
        os.system("python3 7_device.py")
    elif jm == "8":
        os.system("python3 8_device.py")
    elif jm == "9":
        os.system("python3 4_device.py")
    elif jm == "10":
        os.system("python3 10_device.py")
    elif jm == "11":
        os.system("python3 11_device_deobf.py")
    elif jm == "12":
        os.system("python3 202_device.py")
    elif jm == "13":
        os.system("python3 13_device.py")
    elif jm == "14":
        os.system("python3 14_device.py")
    elif jm == "15":
        os.system("python3 15_device.py")
    elif jm == "16":
        os.system("python3 16_device.py")
    elif jm == "17":
        os.system("python3 17_device.py")
    elif jm == "18":
        os.system("python3 18_device.py")
    elif jm == "19":
        os.system("python3 19_device.py")
    elif jm == "20":
        os.system("python3 20_device.py")
    elif jm == "21":
        os.system("python3 21_device.py")
    elif jm == "22":
        os.system("python3 22_device.py")
    elif jm == "23":
        os.system("python3 zayafka_device.py")
    elif jm == "24":
        os.system("python3 48_device.py")
    elif jm == "25":
        os.system("python3 25_device.py")
    elif jm == "26":
        os.system("python3 26_device.py")
    elif jm == "27":
        os.system("python3 27_device.py")
    elif jm == "28":
        os.system("python3 28_device.py")
    elif jm == "29":
        os.system("python3 29_device.py")
    elif jm == "30":
        os.system("python3 30_device.py")
    elif jm == "31":
        os.system("python3 31_device.py")
    elif jm == "32":
        os.system("python3 Golden_2_device.py")
    elif jm == "33":
        os.system("python3 35_device.py")
    elif jm == "34":
        os.system("python3 32_device.py")
    elif jm == "35":
        os.system("python3 33_device.py")
    elif jm == "36":
        os.system("python3 36_device.py")
    elif jm == "37":
        os.system("python3 37_device.py")
    elif jm == "38":
        os.system("python3 38_device.py")
    elif jm == "39":
        os.system("python3 39_device.py")
    elif jm == "40":
        os.system("python3 40_device.py")
    elif jm == "41":
        os.system("python3 41_device.py")
    elif jm == "42":
        os.system("python3 42_device.py")
    elif jm == "43":
        os.system("python3 43_device.py")
    elif jm == "44":
        os.system("python3 44_device.py")
    elif jm == "45":
        os.system("python3 45_device.py")
    elif jm == "46":
        os.system("python3 46_device.py")
    elif jm == "47":
        os.system("python3 47_device.py")
    elif jm == "48":
        os.system("python3 24_device.py")
    elif jm == "49":
        os.system("python3 56_device.py")
    elif jm == "50":
        os.system("python3 gruh_ochish_encoded_device.py")
    elif jm == "51":
        os.system("python3 Maxfiy_encoded_device.py")
    elif jm == "52":
        os.system("python3 Stars.py")
