import random
import os


class Person():
    FirstName = ""
    LastName = ""
    Phone = ""
    Mail = ""

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"

    def Find(self, param):
        if param in self.FirstName or \
            param in self.LastName or \
            param in self.Mail or \
            param in self.Phone:

            return True
        else:
            return False


# kişileri tutacağımız  bir dizi (geçici database)

first_names = [
    "Kelly", "Harry", "Lloyd", "Don", "Marilyn", "Henry", "Marcia", "Kim",
    "Lena", "Delores"
]
last_names = [
    "Fleming", "Jimenez", "Pierce", "Howard", "Sanchez", "Sims", "Thomas",
    "Roberts", "Nguyen", "Torres"
]
domain = [
    "hotmail", "bilgeadam", "aof.edu", "sabanci", "gmail", "yahoo", "live",
    "garanti", "teknosa", "nike"
]
people = []
for i in range(10):
    person = Person()
    person.FirstName = first_names[random.randint(0, len(first_names) - 1)]
    person.LastName = last_names[random.randint(0, len(last_names) - 1)]
    person.Mail = f"{person.FirstName}.{person.LastName}@{domain[random.randint(0, len(domain) - 1)]}.com".lower(
    )

    person.Phone = f"+90 (5{random.randint(10,99)}) {random.randint(100,999)} {random.randint(10,99)} {random.randint(10,99)}"

    people.append(person)


def Liste(param=""):
    os.system("clear")
    index = 0
    if param == "":
        for person in people:
            print("-" * 50)
            print(f"{'Id':<15}: {index}")
            for key, value in person.__dict__.items():
                print(f"{key:<15}: {value}")
            print("-" * 50)
            print()
            index += 1
    else:
        for person in people:
            if (person.Find(param)):
                print("-" * 50)
                print(f"{'Id':<15}: {index}")
                for key, value in person.__dict__.items():
                    print(f"{key:<15}: {value}")
                print("-" * 50)
                print()
            index += 1


def Main():
    ekle = "a"
    sil = "d"
    guncelle = "u"
    liste = "l"
    bul = "f"
    islem = ""
    result = True

    while result:
        print("Lütfen yapmak istediğiniz işlemi seçinz")
        print("_" * 40)
        print("Kişi ekleme işlemi için     : a")
        print("Kişi silme işlemi için      : d")
        print("Kişi güncelleme işlemi için : u")
        print("Kişi bulmak için            : f")
        print("Kişileri listelemek için    : l ")
        print("İşleme devam etmek istemiyorsanız herhangi bir tuşa basınız")
        islem = input("Lütfen bir anahtar kelime giriniz : ").lower()

        if islem == "a":
            os.system("clear")
            person = Person()
            person.FirstName = input("Lütfen kişinin adını giriniz : ")
            person.LastName = input("Lütfen kişinin soyadını giriniz : ")
            person.Phone = input(
                "Lütfen kişinin telefon numarasını giriniz : ")
            person.Mail = input("Lütfen kişinin mail adresini giriniz : ")

            people.append(person)
            print("Kişi Rehbere Eklendi!")
        elif islem == "d":
            os.system("clear")
            Liste()
            id = int(
                input(
                    "Lütfen silmek istediğiniz kişinin ID değerini giriniz : ")
            )
            people.remove(people[id])
            print("Kişi başarıyla rehberden silindi")
        elif islem == "u":
            os.system("clear")
            Liste()
            id = int(
                
                input(
                        "Lütfen güncellemek istediğiniz kaydın ID değerini giriniz : "
                
                ))
            updated_person = people[id]

            for key, value in vars(updated_person).items():
                vl = input(f"Lütfen {key} giriniz : ")
                vars(updated_person).__setitem__(key, vl)

            # updated_person.FirstName = input("Lütfen FirstName girini : ")
            # updated_person.LastName = input("Lütfen LastName girini : ")
            # updated_person.Mail = input("Lütfen Mail girini : ")
            # updated_person.Phone = input("Lütfen Phone girini : ")

        elif islem == "l":
            os.system("clear")
            Liste()
        elif islem == "f":
            os.system("clear")
            Liste(input("Lütfen anahtar kelime giriniz : "))
        else:
            os.system("clear")
            result = False
            print("Rehber uygulamasından çıkış yaptınız!")


Main()