# for

#0 dan başlayarak 9 a kadar olan sayıları konsolda döndürür.
# i=0 i<10
for i in range(10):
    print("---------")
    print(i)
print("---------------------")

#5 den başlayarak 10 a kadar olan sayıları konsolda döndürür.
for i in range(5,10):
    print("---------")
    print(i)
print("---------------------")

# 0 dan başlayarak 50 ye kadar 10'ar, 10'ar olacak şekilde artırılan sayıları konsolda döndürür.
for i in range(0,50,10):
    print(i)
print("---------------------")

# Döngülerde Listelerin kullanımı

lists = ["Csharp", "JavaScript", "Pyhton"]
for loop in lists:
    print(loop)

# While 

## Sonsuz Döngü

# while True:
#     print("x")
print("---------------------")
# Sonlu Döngü

i = 0
while i < 10:
    print("x")
    i += 1
print("y")

print("---------------------")

# break
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# continue

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# else 

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
