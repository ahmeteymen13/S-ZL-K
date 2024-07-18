meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "MİNECRAFT": "oyun",
            "KYS": "intihar et"
    
                                }  
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if word in meme_dict.keys():
    print("tamamdır")
else:
    print("böyle bir kelime yok")
