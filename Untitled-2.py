import random

sayilar = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

uzunluk = int(input("Parolanizin Uzunluğunu Yazin: "))

parola = ""

for i in range(uzunluk):
    parola += random.choice(sayilar)

print(parola)