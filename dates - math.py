import datetime

## Dates => Tarih

x = datetime.datetime.now()

# Tarih yıl, ay, gün, saat, dakika, saniye ve mikrosaniyeyi içerir.
print(x)

# Bir tarih oluşturmak için;

x = datetime.datetime(2023, 4, 1)

print(x)

#strftime() => Nesne datetime, tarih nesnelerini okunabilir dizeler halinde biçimlendirmek için bir yönteme sahiptir.

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))


## Math

# min() - max() => En yüksek değer ve ya en düşük değeri bulmak için;

x = min(10, 15, 30)
y = max(10, 15, 30)

print(x)
print(y)

#abs() => Belirtilen sayının mutlak(pozitif) değerini döndürür.

x = abs(-4.30)

print(x)

#pow()

# x'in değerini y'nin (x üssü y) gücüne döndürür.

x = pow(4, 3)

print(x)

# Math Module => Matematik modülü

import math

# math.sqrt() => Bir sayının karekökünü döndürür.

x = math.sqrt(81)

print(x)

# math.ceil() => Bir sayıyı en yakın tam sayıya yukarı yuvarlar.
# math.floor() => Bir sayıyı en yakın tam sayıya aşağı yuvarlar.

x = math.ceil(1.8)
y = math.floor(1.8)

print(x) 
print(y) 

# math.pi => pi değerini (3.14...) döndürür.

x = math.pi

print(x)