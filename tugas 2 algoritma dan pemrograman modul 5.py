# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 18:11:03 2022

@author: iskyd
"""

umur = "0"
total = 0
while (umur != "") :
    umur = input("masukan umur : ")
    if umur != '':
        umur_angka = int(umur)
        if umur_angka <= 2:
            print("Gratis")
            price = 0
        elif umur_angka >= 3 and umur_angka <= 12:
            print("harga $14.00")
            price = 14
        elif umur_angka >= 65:
            print("harga $18.00")
            price = 18
        else :
            print("harga $23.00")
            price = 23
        total = total + price
        print("total: %0.2f" % total)
        
jumlah = int(input("masukan jumlah uang: "))
hasil = jumlah - total
print("kembalian: %0.2f" % hasil)