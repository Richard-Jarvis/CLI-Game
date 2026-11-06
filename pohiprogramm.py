import random
import time
#Salvestussüsteem
#elud, kuldmündid, relv, armor

uusmang = input("Kas soovid alustada uut mängu või laadida salvestus failist?\n 1 - Alusta uut mängu\n 2 - Lae salvestusfailist\n")

#Globaalsed muutujad
elud = 100
kuldmündid = 0
relv = "rusikad"
armor = 0
bag = []

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
        bag = fail.readline().strip()

#asula 1
def asula1():
    




while True:
    if uusmang == "1":
        asula1()

def kasiino():
    global kuldmündid
    
    mang = input("Mängud:\n 1 - Coinflip\n")
    if mang == "1":
        # Mäng käib kuni kasutaja ei sisesta panust
        while True:
            # Küsib panust kuni panus sobib
            try:
                while True:
                    panus = int(input("Kui palju soovid panustada?\n"))
                    if panus > kuldmündid:
                        print("Sul pole nii palju raha")
                        time.sleep(3)
                    elif panus <= 0:
                        print("Panus peab olema suurem kui 0")
                        time.sleep(3)
                    else:
                        break
            except:
                break
                    
           
            pool = input("Kas kull või kiri?\n")
                
            if random.choice(["kull", "kiri"]) == pool:
                kuldmündid += panus
                voit = [f"Võitsid!, sul on nüüd {kuldmündid} kuldmünti", f"Vedas, nüüd on sul taskus {kuldmündid} kuldmünti"]
                print(f"{random.choice(voit)}")
                time.sleep(3)
            else:
                kuldmündid -= panus
                kaotus = [f"Ei vedanud seekord, sul on järel {kuldmündid} kuldmünti", f"Kaotasid... sul on nüüd {kuldmündid} kuldmünti"]
                print(f"{random.choice(kaotus)}")
                time.sleep(2)
                if kuldmündid == 0:
                    print("Sul said kuldmündid otsa")
                    break
                time.sleep(3)



# loot funktsioon toimib erinevalt sõltuvalt, mida lootida
def loot(asukoht):
    if asukoht == "prügikast":
        valus = random.choice(
    elif asukoht == "maja":
    elif asukoht == "
    