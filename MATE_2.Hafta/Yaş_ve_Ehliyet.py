dogumyili= int(input("Doğum yılınızı yazın:"))
mevcutYil= int(input("Hangi Yıldayız:"))

def ehliyet():
    yas= mevcutYil-dogumyili
    ehliyet:bool = yas>=18
    return yas, ehliyet
yas, ehliyet= ehliyet()

if ehliyet:
    print(f"Yaşınız {yas} ve  ehliyet almaya uygun")

else:
    print(f"Yaşınız {yas} ve ehliyet almaya uygun değil")