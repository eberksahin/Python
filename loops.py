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