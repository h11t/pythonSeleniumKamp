ogrenciler=[] ##liste tanımlandı

print("***************")

def Ekle(isim,soyisim):
    ogrenciler.append(isim+" "+soyisim)
    print(isim+" "+soyisim+" eklendi")

def Sil(isim,soyisim):
    ogrenciler.remove(isim+" "+soyisim)
    print(isim+" "+soyisim+" silindi")

def CokluKayit(ogrenciDizisi):
    ogrenciler.extend(ogrenciDizisi)
    Listele(ogrenciDizisi)
    print("Yukarıdaki isimler eklendi")

def OgrenciNoBul(isim,soyisim):
    return ogrenciler.index(f"{isim} {soyisim}")
    
def CokluSil(*silinecekOgrenciDizisi):
    i=0
    while i<len(silinecekOgrenciDizisi):
        ogrenciler.remove(silinecekOgrenciDizisi[i])
        print(silinecekOgrenciDizisi[i]+" silindi")
        i=i+1
def Listele(ogrDizisi):
    for ogr in ogrDizisi:
        print(ogr)
    
print("**********")
Ekle("Zeynep","Tek")

print("**********")
ogrncDizi=['Hilal Tek','Mesut Tek','Asiye Tek']
CokluKayit(ogrncDizi)

print("**********")
Sil('Asiye','Tek')

print("**********")
print("Hilal Tek in nosu:",OgrenciNoBul("Hilal","Tek"))

print("**********")
CokluSil('Mesut Tek',"Zeynep Tek")

print("**********")
Listele(ogrenciler)



