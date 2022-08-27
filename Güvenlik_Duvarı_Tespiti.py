#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("apt-get install wafw00f")
os.system("clear")
os.system("figlet EKO YASO")

print("""       


Güvenlik Duvarı Tespit Programına Hoş geldiniz.


1)Güvenlik Duvarı Listesi
2)Güvenlik Duvarı Tespiti



""")

islemno = raw_input("İşlem No Girin: " )

if(islemno == "1"):
	os.system("wafw00f -l")

elif(islemno == "2"):
	site = raw_input("Site Adresi Girin ")
	os.system("wafw00f " + site)
	
	
else:
	
	print("Hatalı Giriş Yaptınız.")
	os.system("python Güvenlik_Duvarı_Tespiti.py")
	
	
	 
	 



