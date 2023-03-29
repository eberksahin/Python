# Fonksiyonlar

fiyat = 100
indirim = 30

yeniFiyat = fiyat - indirim

print(yeniFiyat)

print("-----------------------")
# Definition => Tanım, tanımlama

def calculate():
    print(100-30)

calculate()
#Parametre kullanımı
def calculateWithParams(fiyat,indirim):
    print(fiyat - indirim)

calculateWithParams(120,80)
calculateWithParams(80,30)

def sayHello(name):
    print(f"Merhaba {name}")


sayHello("Berk")

# Fonksiyonu geri döndürme

def calculateAndReturn(fiyat, indirim):
    return fiyat - indirim

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat)
