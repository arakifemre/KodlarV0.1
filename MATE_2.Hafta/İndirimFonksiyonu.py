gfiyat = float(input("İndirimsiz fiyatı giriniz: "))
indirim = float(input("İndirim yüzdesini giriniz: "))

def indirim_hesapla(fiyat, oran):
    indirimtutari = fiyat * oran / 100
    sonfiyat = fiyat - indirimtutari

    return indirimtutari, sonfiyat

indirimtutari, sonfiyat = indirim_hesapla(gfiyat, indirim)

print(f"Yapılan indirim: {indirimtutari} \n Son fiyat:{sonfiyat}")