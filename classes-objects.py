# Sınıflar => Classlar
# Objects => Objeler

class Human:
    # built-in - constructor - initialize
    def __init__(self,name):
        self.name = name
        print("Bir Human instance'i üretildi.")
    def __str__(self):
        return f"STR Fonksiyonundan dönen değer : {self.name}"
    def talk(self,sentence):
        name = "Sahin"
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} is Walking...")

# İnstance => Örnek

# Human Classından bir örnek atıyoruz.
human1 = Human("Berk")
human1.talk("Merhaba") 
human1.walk()
print(human1)

human2 = Human("Sahin")
human2.talk("Hello") 
human2.walk()
print(human2)
