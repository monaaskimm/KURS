print("modern dil sözlüğü")

meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "bir şakaya karşılık cevap",
            "SHEESH": "onaylamamak",
            "CREPPY": "korkunç" ,
            "AGGRO": "agresifleşmek/sinirlenmek"
            "YİPPE": "saf mutluluk"
            }
while True:
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!) (çıkmak isterseniz büyük Xe basınız) ")
    
    if word == "X":
        print("kullandığınız için teşekkürler")
        break
    if word in meme_dict.keys():
        print("anlamı" , meme_dict[word])
    else:
        print("malesef sözlükte bu kelime yok")
