#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


os.system("apt-get install figlet")
os.system("apt-get install ikea-scan")
os.system("clear")
os.system("figlet EKO YASO")

print("""               

VPN Kontrol Programına Hoş Geldiniz


""")

hedefip = raw_input("Hedef ip Girin: ")

os.system("ike-scan " + hedefip)

print("işlem başarıyla tamamlandı.")


