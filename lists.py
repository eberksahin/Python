# Bir dizi(array) içerisinde farklı türden değerler kullanılabilir.

dizi = ["Pyhton", 29, 10.5]
print(dizi)

# Listeler

lists = ["Csharp", "JavaScript", "Pyhton"]
print(lists)

print(lists[0]) # konsolda 0.(Csharp) indeksini döndürür.

# len => Liste Uzunluğu
Listslen = ["Csharp", "JavaScript", "Pyhton"]
print(len(Listslen))

# type() => Veri tipini konsolda döndürür.

typelist = ["Csharp", "JavaScript", "Pyhton"]
print(type(typelist))

# append => Listenin sonuna eleman eklememizi sağlar.

lists.append("Java")
print(lists)

# pop => Verdiğin indeksdeki değerini silmeni sağlar.

lists.pop(3)
print(lists)

# remove => Belirttiğin değeri  silmeni sağlar. 

lists.remove("JavaScript")
print(lists)

# extend => İlgili dizideki elemanları belirtilen diziye ekler.

lists.extend(["React", "NodeJs"])
print(lists)