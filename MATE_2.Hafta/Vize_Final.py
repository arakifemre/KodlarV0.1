vize= float(input("Vize notunuzu giriniz:"))
final= float(input("Final notunuzu giriniz:"))
devam: bool = input("Devamsızlık hakkınızı aştınız mı?(E/H):").lower() == "h"
def harf_notu():
    ort = vize*0.4 + final*0.6
    if devam:
        if ort >= 90:
            return f"Ortalamanız {ort}. Harf notunuz AA. Mükemmel bir başarı!"
        elif ort >= 80:
            return f"Ortalamanız {ort}. Harf notunuz BA. Pekiyi!"
        elif ort >= 70:
            return f"Ortalamanız {ort}. Harf notunuz BB. İyi bir başarı!"
        elif ort >= 60:
            return f"Ortalamanız {ort}. Harf notunuz CB. Ortalama bir başarı!"
        elif ort >= 50:
            return f"Ortalamanız {ort}. Harf notunuz CC. Yeterli..."
        elif ort >= 40:
            return f"Ortalamanız {ort}. Harf notunuz DC. Koşullu başarı. AGNO'nuzun 2.00 üzerinde olmasına dikkat edin!"
        elif ort >= 30:
            return f"Ortalamanız {ort}. Harf notunuz DD. Başarısız!"
        elif ort >= 20:
            return f"Ortalamanız {ort}. Harf notunuz FD. Başarısız!"
        else:
            return f"Ortalamanız {ort}. Harf notunuz FF. Başarısız!"
    else:
        return f"Ortalamanız {ort}. Harf notunuz F0. Devamsızlık hakkınızı aşmışsınız! Bu sebeple başarısız sayıldınız."
harf_notu = harf_notu()
print(harf_notu)