ilginckelime = {
                "CRINGE":"Garip ya da utandırıcı şey",
                "LOL":"Komik bir şeye verilen cevap",
                }


kelime = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if kelime in ilginckelime.keys():
    a = ilginckelime[kelime]
    print(a)
else:
    print("Bu kelimenin anlamını bende bilmiyom")
