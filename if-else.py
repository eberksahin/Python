# Karar yapilari

#if else
sayi1 = 10
sayi2 = 15

#sayi1 sayi2'den büyükse ekrana 1 daha buyuk yazdır.

#indent
if sayi1 > sayi2:
    print("sayi1 sayi2'den buyuktur.")
    print("İf blogunun icerisi")
elif sayi1 == sayi2:
    print("İki sayi esittir.")
# eger if ve else if bloklarına girmez ise
else:
    print("sayi1 sayi2'den kucuktur.")

print("İf bloğunun disi")

# 2. kullanım modeli
a = 36
b = 36
print("A") if a > b else print("=") if a == b else print("B")

# And

a = 200
b = 35
c = 500
if a > b and c > a:
  print("Her iki koşul da Doğru.")

# Or

a = 200
b = 35
c = 500
if a > b or a > c:
  print("Koşullardan en az biri Doğru")

# Not

a = 35
b = 200
if not a > b:
  print("a, b'den büyük DEĞİLDİR")

# pass(Geçiş Bildirimi)

#ififadeler boş olamaz, ancak herhangi bir nedenle içeriği olmayan bir ifadeniz varsa , hata almamak için ifadeyi if girin .
a = 35
b = 200

if b > a:
  pass