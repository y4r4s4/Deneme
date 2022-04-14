#!/usr/bin/env python3

import os

while True:
        os.system("pkg install figlet")
        os.system("clear")
        os.system("figlet -c  HASANLI.B")
        print("""
Qabaqcıl Skan Aləti

1) Sayt Haqqında Ümumi Məlumat
2) Çevik Port Axtarışı
3) Versiya Məlumatı
Q) Çıxış


""")

        islemno = input("Xidmət Nömrəsi Daxil Edin: ")

        if islemno=="1":
                hedefip= input("Hədəf İP girin: ")
                os.system("whois "+hedefip)
                input("Əsas Səhifə >>ENTER<<")

        elif islemno=="2":
                hedefip= input("Hədəf İP girin: ")
                os.system("nmap "+hedefip)
                input("Əsas Səhifə >>ENTER<<")

        elif islemno=="3":
                hedefip= input("Hədəf İP girin: ")
                os.system("nmap -sV "+hedefip)
                input("Əsas Səhifə >>ENTER<<")

        elif islemno=="q" or islemno=="Q":
                quit()

        else:
                input("Xəta...Press Enter")
