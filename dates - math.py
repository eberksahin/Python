import datetime

#Dates => Tarih

x = datetime.datetime.now()

# Tarih yıl, ay, gün, saat, dakika, saniye ve mikrosaniyeyi içerir.
print(x)

# Bir tarih oluşturmak için;

x = datetime.datetime(2023, 4, 1)

print(x)

#strftime() => Nesne datetime, tarih nesnelerini okunabilir dizeler halinde biçimlendirmek için bir yönteme sahiptir.

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))