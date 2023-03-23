print("Hello World!")

baslik = "Tasit kredisi"
print(baslik)

# string => Metinsel ifade
baslik = "İhtiyac kredisi"
print(baslik)

# İnt, İnteger => Tam sayı
vade = 36
ekVade = 12
vade2 = "36" # String değer

#Float, decimal, double
aylikOdeme = 200.50

#bool, boolean => True, False
yukselisteMi = True

# Matematiksel operatorler

# Toplama operatoru (+)
print(5 + 5)
print(vade + 12)
print(vade + ekVade)
print(36 + 12)

# Cıkarma operatoru (-)

print(5 - 5)
print(vade - 12)
print(vade - ekVade)
print(36 - 12)

# carpma operatoru (*)

print(5 * 5)
print(vade * 12)
print(vade * ekVade)
print(36 * 12)

# bolum operatoru (/)

print(5 / 5)
print(vade / 12)
print(vade / ekVade)
print(36 / 12)

# Matematiksel operatorler ornek

yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

# mod operatoru (%)

print(10%2)
print(vade % 5)
print(vade % ekVade)
print(30 % 10)

# mantıksal operatorler 

#Esit(==) operatoru => boolean deger dondurur.
print(1 == 1)
print(1 == 2)

# Buyukluk(>) operatoru
print(1 > 2)
print(3 > 1)
print(1 > 1)
print(1 >= 1)#Hem buyuk hem esit ise buyuk esit operatoru kullanılır.

# Kucukluk(<) operatoru
print(1 < 2)
print(3 < 1)
print(1 < 1)
print(1 <= 1)# Hem kucuk hem esit ise kucuk esit operatoru kullanılır.

# Esit olmama(!) operatoru => boolean deger dondurur.

print(1 != 1) # False
print(1 != 2) # True

# or(veya), and(ve) => Boolean değer döndürür.

print(1 > 2 or 5 > 2) # Bir değer doğru ise True değeri döndürür.
print(1 > 2 and 5 > 2) # Her iki değer doğru ise True değeri döndürür.

print(1 > 2 or 5 > 2 and 3 > 2) # (1 > 2 or 5 > 2) => True ve (3 > 2) => True; True ve True, True değerini döndürür. 
print(1 > 2 and 5 > 2 and 3 > 2) # (1 > 2 and 5 > 2) => False ve (3 > 2) => True; False ve True, "and" olduğu için False değerini döndürür. 

print(1 > 2 or 5 > 2 and 3 > 2) # (1 > 2 or 5 > 2) => True ve (3 > 2) => True; False ve True, "or" olduğu için True değerini döndürür. 