
print("Tere, maailm!")
nimi=input("Sisesta oma nimi: ")
print(f"Tere, maailm! Tervitan sind{nimi}!")
vanus=input("Sisesta oma vanus: ")
print(f"Tere, maailm! Tervitan sind {nimi}! Sa oled {vanus} aastat vana.")
 


vanus=16 #int
eesnimi="Jaak" #str
pikkus=16.5 #float
kas_käib_koolis=True #bool
print(f"Muutuja:{vanus}, tüüp: {type(vanus)}")
print(f"Muutuja:{eesnimi}, tüüp:{type(eesnimi)}")
print(f"Muutuja: {pikkus}, tüüp: {type (pikkus)}")
print(f"Muutuja: {kas_käib_koolis}, tüüp: {type(kas_käib_koolis)}")




from random import * #randint
kommide_arv=randint(1,100) #kommide arv on juhuslikult arv vahemikus1-100)
print(f"Laual on {kommide_arv} kommi.")
kommid=int(input("Mitu kommi soovid laualt ära võtta?"))
kommide_arv-= kommid #kommide_arv väheneb kommid võrra
print(f"Laual on nüüd {kommide_arv} kommi.")




from math import * #pi,sqrt()
try:

ümbermõõt=float(input("Sisesta puu ümbermõõt: ")) #teisendab strimgi ujukomaarvuks
läbimõõt=ümbermõõt/pi
print(f"Puu läbimõõt on {läbimõõt}.")
except:
    print("Sisesta mingi arv")



N=float(input("Sisesta ristküliku 1. külje pikkus: "))
N=float(input("Sisesta ristküliku 2. külje pikkus: "))
d=sqrt(N**2+M**2)
print(f"Ristküliku diagonaal on {d}.")



print("Sinu kiirus oli " + "km/h" + str(kiirus))



arv1=int(input("Sisesta 1. täisarv: "))
arv2=int(input("Sisesta 2. täisarv: "))
arv3=int(input("Sisesta 3. täisarv: "))
arv4=int(input("Sisesta 4. täisarv: "))
arv5=int(input("Sisesta 5. täisarv: "))
keskmne=(arv1+arv2+arv3+arv4+arv5)/5
summa=arv1+arv2+arv3+arv4+arv5
print(f"Arvude summa on {summa}.")
print(f"Arvude keskmine on {keskmine}.")
täisosa=summa//5
jääk=summa%5
print(f"Täisosa on{täisosa}.")
print(f"Jääk on {jääk}.")



print(" @..@ ")
print("(----)")
print("( \\__/ )")
print("^^  \"\"  ^^")



a=int(input("Sisesta 1. täisarv: "))
b=int(input("Sisesta 2. täisarv: "))
c=int(input("Sisesta 3. täisarv: "))
P=a+b+c 
print("Ristküliku ümbermõõt on:", P)

hind = 12.90
jootraha = 0.1
kokku_kulub = hind*(1+jootraha)
inimeste_arv = a
a = int(input("Mitu inimest pitsat sõi?, (a)"))
kulu_inimeste_kohta = kokku_kulu / inimeste_arv
print("iga sõber maksab" , kulu_inimese_kohta)



from import math
from datetime import *
tana=date.today()
print(f"Tere! Täna on{tana}")

# 27/12/2022
tana = tana.strftime("%d/%m/%Y")
print(tana1)
# December 27, 2022
tana = tana.strftime("%B %d, %Y")
print(tana2)
# 12/27/22
tana = tana.strftime("%m/%d/%y")
print(tana3)
# Dec-27-2022
tana = tana.strftime("%b-%d-%Y")
print(tana4)

aasta=tana.year
kuu=tana.month
paev=tana.day
print(f"Tänane aasta:{aasta}, kuu: {kuu}, päev:{paev}")
kuulõpuni=date(aasta,kuu+1, 1) - tana
aastalõpuni=date(aasta+1, 1, 1) - tana
print(f"Jäänud päevi kuu lõppuni: {kuulõpuni.days}")
print(f"Jäänud päevi aasta lõpuni: {aastalõpuni.days}")


print("Tehe  3 + 8 / (4 - 2) * 4", 3 + 8 / (4 - 2) * 4)
print["Tehe  3 + 8 / (4 - 2) * 4", 3 + 8 / (4 - 2) * 4]
print{"Tehe  3 + 8 / (4 - 2) * 4", 3 + 8 / (4 - 2) * 4}


try:
     R=float(input("Sisesta ringi raadius R: "))
     ruudu_pindala=(2*R)**2
     ruudu_ymbermoot=4*(2*R)
     ringi_pindala=pi*R**2
     ringi-ymbermoot=2*pi*R
     print(f"Ruudu pindala: {ruudu-pindala}, \nruudu ümbermõõt: {ruudu-ymbermoot}, \nringi pindala: {ringi-pindala}, \ringi ümbermõõt: {ringi-ymbermoot}")
except ValueError:
    print("Palun sisetsa kehtiv arv.")



Maa_raadius=6378 # km
Mundi_dia= # cm
Mundi_raadius=Mundi_dia/2 # cm
Maa_ymbermoot=2*pi*Maa_raadius*1000 # cm
Mundi_arv=Maa_ymbermoot/Mundi_diaprint(f"2-euroseid münte on vaja: {Mundi_arv:.0f}")


try:
    x=int(input("Sisestada arv: "))
    if x == 1:
        print("Õige")
    else:
        print("Vale")
except ValueError:
    print("Palun sisesta kehtiv täisarv.")


    vastus = input("Kas soovid jätkata? (jah/ei) ")
if vastus.lower() == "jah":
    print("Jätkame!")
else:
    print("Head aega!")



try: 
    x = int(input("Sisesta arv -5 kuni 5: "))
    if x < -5:
        print("Vähe")
    elif -5 <= x <= 5:
        print("OK")
    else:
        print("Palju")
except ValueError:
    print("Palun sisesta täisarv.")

#summa kontroll
try:
    summa = float(input("Sisesta summa: "))
    if summa>2000:
        hind=summa*0.8
    elif summa>1000:
        hind=summa*0,9
    else:
       hind=summa
       print("Hind:", hind)
except ValueError:
    print("Palun sisesta täisarv.")

