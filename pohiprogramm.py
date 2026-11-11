import random
import time

#Globaalsed muutujad
elud = 100
kuldmündid = 0
relv = "rusikad"
armor = 0
bag = []

###STARTUP###

uusmang = input("Kas soovid alustada uut mängu või laadida salvestus failist?\n 1 - Alusta uut mängu\n 2 - Lae salvestusfailist\n")

if uusmang == "1":
    input("On aasta 2047. Tehisintellekti kiire areng on muutnud TI autonoomseks. (Enter jätkamiseks)")
    input("TI-robotid on võtnud üle maailma ja on hakanud jahtima inimesi. Peaaegu kõik inimkond on kas surnud või vangistatud. (Enter jätkamiseks)")
    input("Sina oled olnud vanglas juba paar kuud ning oled kuulnud kuulujutte superarvutist, mis hoiab roboteid töös. (Enter jätkamiseks)")
    input("Ühel päeval sa pääsed vanglast ja tundub, et sinu puudumist ei ole märgatud. Sinu missioon on leida superarvuti ja see hävitada. (Enter jätkamiseks)")
    time.sleep(1)
    print("\n")
    print("-------")
    print("\n")
else:
    fail = input("Sisesta salvestusfaili nimi: ")
    with open(fail, "r", encoding="utf-8") as fail:
        elud = int(fail.readline().strip())
        kuldmündid = int(fail.readline().strip())
        relv = fail.readline().strip()
        armor = int(fail.readline().strip())
        bag = fail.readline().strip()


###FUNKTSIOONID###

##ASUKOHAD##

def esimene_asula():
    input("Pärast mitut tundi liikumist jõuad ühte väiksesse asulasse. (Enter jätkamiseks)")
    input("Seda küla on hiljuti rüüstatud, puidupõlemislõhn on ikka veel õhus. Rüüstamisest on alles jäänud vaid paar maja. (Enter jätkamiseks)")
    input("Tõenäoliselt on enamus asju ära röövitud, kuid võib-olla leidub siin veel midagi. (Enter jätkamiseks)")
    
    while True:
        sisend = input("\nMida soovid teha?\n 1 - Astu kirikusse\n 2 - Astu poolenisti mahapõlenud majja\n 3 - Jaluta mööda asulat ringi\n 4 - Liigu edasi järgmisesse")
        if sisend == "1":
            input("Astud kivist kirikusse. Kirik on pime ja niiske, sinu sammud kajavad kiriku seintelt. Näed enda ees altarit, millel ei ole enam midagi alles. (Enter jätkamiseks)")
            input("Ringi vaadates ei näe sa midagi, mis võiks olla sulle kasulik. Astud kirikust välja.")
        elif sisend == "2":
            print("")
        elif sisend == "3":
            print("")
        elif sisend == "4":
            break


##LISAFUNKTSIOONID##
        
def pickup(asi):
    global bag
    
    kas_võtsid = input(f"Leidsid {asi}.\n 1 - Võta {asi} kaasa\n 2 - Ära võta kaasa")
    if kas_võtsid == 1:
        bag.append(asi)
    else:
        return 0

def bagcheck(bag):
    if len(bag) == 0:
        print("Sinu seljakotis ei ole midagi!")
    else:
        print("Sinu seljakotis on: ", end="")
        for asi in bag:
            print(f"{asi},", end=" ")
        print("")

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


'''
# loot funktsioon toimib erinevalt sõltuvalt, mida lootida
def loot(asukoht):
    if asukoht == "prügikast":
        valus = random.choice(
    elif asukoht == "maja":
    elif asukoht == ""
    
'''

###MÄNGU LOOP
    
while True:
    if uusmang == "1":
        esimene_asula()
    





