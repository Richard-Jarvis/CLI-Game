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
    input("On aasta 2047. Tehisintellekti kiire areng on muutnud TI autonoomseks. (Enter jätkamiseks)")
    input("TI-robotid on võtnud üle maailma ja on hakanud jahtima inimesi. Peaaegu kõik inimkond on kas surnud või vangistatud.")
    input("Sina oled olnud vanglas juba paar kuud ning oled kuulnud kuulujutte superarvutist, mis hoiab roboteid töös.")
    input("Ühel päeval sa pääsed vanglast ja tundub, et sinu puudumist ei ole märgatud. Sinu missioon on leida superarvuti ja see hävitada.")
else:
    fail = input("Sisesta salvestusfaili nimi: ")
    with open(fail, "r", encoding="utf-8") as fail:
        elud = int(fail.readline().strip())
        kuldmündid = int(fail.readline().strip())
        relv = fail.readline().strip()
        armor = int(fail.readline().strip())


#asula 1
#def asula1():
    




while True:
    if uusmang == "1":
        asula1()
#test