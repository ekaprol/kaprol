#!/usr/bin/env python
# *-* coding: utf-8 *-*

import os

os.system("apt-get install nikto")
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet EKO YASO")


print("""      

Zafiyet Analiz Programına Hoşgeldiniz

""")

hedefip = raw_input ("Hedef ip Giriniz: ")

os.system("nikto -h " + hedefip)





