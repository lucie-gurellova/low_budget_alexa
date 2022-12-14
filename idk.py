import os
import time
import playsound
# a = input("Co chceš říct?")
#time.sleep(5)
#os.system("say" + a)
def zacni_nadavat_polsky():
    playsound.playsound("/Users/luciegurellova/Downloads/o-kua.mp3")

def ahoj():
    os.system("say nazdar swagre")

def obsah_obdelnik(a,b):
    return a*b

def manual():
    print("ahoj - znova pozdravi")
    print("zacni_nadavat_polsky")
    print("obsah_obdelnik")
    print("konec")
manual()
ahoj()
time.sleep(3)
while True:
    os.system("say Co chceš")
    prikaz = input("Co chceš?").strip()
    if prikaz == "ahoj":
        ahoj()
    if prikaz == "zacni_nadavat_polsky":
        zacni_nadavat_polsky()
    if prikaz == "obsah_obdelnik":
        a = input("napiš jednotku pro rozměr jedné strany:").strip()
        b = input("napiš jednotku pro rozměr druhé strany:").strip()
        c = obsah_obdelnik(int(a),int(b))
        print(c)
    if prikaz == "konec":
        break
    if prikaz == "manual":
        manual()



def nej_cislo(cisla):
    nejmensi_cislo = cisla[0]
    for cislo in cisla :
        if nejmensi_cislo > cislo :
            nejmensi_cislo = cislo
    return nejmensi_cislo

def soucet_cisel(cisla):
    soucet = 0
    for cislo in cisla:
        soucet = soucet + cislo
    return soucet

#for cislo in pole_cisel:
   # print(cislo * cislo)

#for i in range(0,len(pole_cisel)):
   # print(pole_cisel[i] * pole_cisel[i])

pole_cisel = [2,9,6,1,8,4]
pole_cisel2 = [5,9,6,8,4]
i = 2

#print(pole_cisel[i])
#print(pole_cisel[2])

for i in range(1,11):
    print(i)

z = len(pole_cisel)
x = print(z)
y = nej_cislo(pole_cisel)

