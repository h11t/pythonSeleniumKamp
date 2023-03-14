ÖDEV TANIMI:

Python'da Veri Tiplerini araştırınız, her bir veri tipi için kendi cümlelerinizle açıklamalar yazınız.

Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.

Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz.

Veri Tipleri:
int: tam sayıları ifade eder. 1845,  26  ...
float: ondalıklı sayıları ifade eder. 3.14 gibi
str: metinsel verileri ifade eder. "Merhaba" , "Hoşgeldin" , "142536" gibi
bool: matıksal verileri ifade eder. true ya da false olabilir.
list: aynı veri tipine sahip değerleri birarada bulundurur. [12,45,36] gibi
tuple: aynı veri tipine sahip değerleri birarada bulundurur (12,45,36) gibi
set: aynı veri tipine sahip değerleri birarada bulundurur {12,45,36} gibi
dict: farklı veri tipine sahip değerleri birarada bulundurur. {"ad":"hilal", "yas" : 30}


email="abc@abcmail.com"
sifre="142536"

mail=input("Mail: ")
password=input("Şifre: ")

if mail==email and password==sifre:
    print("Giriş Yapıldı")
else:
    print("Kullanıcı adı veya şifre hatalı")


