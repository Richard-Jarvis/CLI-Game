import random

#Salvestussüsteem
#elud, kuldmündid, relv, armor

uusmang = input("Kas soovid alustada uut mängu või laadida salvestus failist?\n 1 - Alusta uut mängu\n 2 - Lae salvestusfailist\n")

#Globaalsed muutujad
elud = 100
kuldmündid = 0
relv = "rusikad"
armor = 0


if uusmang == "1":
    input("lore1")
    input("lore2")
    input("lore3")
else:
    fail = input("Sisesta salvestusfaili nimi: ")
    with open(fail, "r", encoding="utf-8") as fail:
        elud = int(fail.readline().strip())
        kuldmündid = int(fail.readline().strip())
        relv = fail.readline().strip()
        armor = int(fail.readline().strip())


#asula 1
def asula1():
    




while True:
    if uusmang == "1":
        asula1()
#test