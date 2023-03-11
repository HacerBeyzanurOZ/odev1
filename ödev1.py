#soru1: veri türleri nelerdir?
#metin tipi için => str 
#sayısal veriler için => float, int, complex 
#dizi veerilerimiz için =>list, tuple, range
#adresleme => dict
#küme veri => set, frozenset 
#mantıksal veri türü => bool 
#binary => bytes, bytearray, memoryview


print("kodlamaio")
#11. satırda "" ile kullandığımız bu ifade mmetin tipi olarak çıkıyor
print(20)
#13. satırda "" kullanmadan yazdığımız bu sayısal ifade int veri türünde. int yada integer tüm tam sayıları kapsar
#bir bölme işlemi yapalım mesela 125/5 olsun işlemimiz
print(125/5) 
#işlem sonucu çıktımız 25.0 ifadesi oluyor ondalıklı olan ifadelerimiz float veri tipinde
#diğer sayısal tipimiz olan complex de iki kısımdan oluşan ifadeleri karşılıyor örneğin 5ö


#kalan tipler için sadece örnekler yazacağım aralarında tam kavrayamadıklarım var :D

kitapTürleri=[ "polisiye","psikoloji","dünyaKlasikleri","bilimKurgu"]
# bu şekilde kapalı parantezle " ve virgülle ifade ettiğimiz veriler liste türünde algılanmış oluyo çıktısını almak istediğimizde:
print(kitapTürleri[1])
print(kitapTürleri[0])
# yazıp çıktı aldığımızda bize polisiye ve psikoloji yi çıktı olarak verecek 
print(kitapTürleri[4])
#bu şekilde yazdığımda out of range hatası verir
