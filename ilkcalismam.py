import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = int(input("Parolanızın uzunluğunu giriniz"))
parola = ""
for i in range(int(uzunluk)):
    parola += random.choice(karakterler)
print(parola)    
