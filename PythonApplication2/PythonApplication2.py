



print("Aastaaeg") # ma ei tea kas see loeab aga seal juttumärkides oli ainult 1 juttumärgi kriips
kuu=int(input("Sisesta kuu number (1-12) => "))
if kuu<1 and kuu>12:
    print("Vigane kuu")
elif kuu=12 or kuu<=2:
    print("Talv")
else if 3>=kuu<=5:  #ennem oli < aga see on väiksem kui, siis saaks panna 1,2 mis on talve kuud mitte kevad.
    print("Kevad")
elif 6>=kuu<=8    #siin sama asi mis eelmises paranduses
print("Suvi")
else:
    print("Sügis")
print()
print("Kiiruse kontroll")
lubatud=int(input("Sisesta lubatud kiirus (km/h) => "))  #siin oli ainult üks sulg, aga pidi olema 2
kiirus=int(input("Sisesta tegelik kiirus (km/h) => "))   #seal ka peaks olema ju int, sest vasutus ilmselt tuleb täisarv ja ka on vaja kahte sukgu ja oli ainult 1
Ületus=kiirus-lubatud  #ma ei tea kui suur viga on panna Ü asemel y
if Ületus=<0:          #sama siin
    print("Kiirust ei ületatud")
elif ületus>0:         # siin ka
    print("Hoiatus")
elif ületus>20:        #siin ka
    print("Trahv")
elif ületus>40:        #siin samuti
    print("Juhiluba võetakse ära")
print()
print("Taksosõit")
km=float(input("Sisesta sõidu pikkus (km) => "))
oo=input("Kas sõit on öösel (jah/ei)? => ")
hind=3+km+0.8
if oo=="jah" and oo=="JAH":  #peaks olema koolon, aga puudus
    hind=hind*1.2
print("Sõidu hind:", round(hind,2)), "€"  #siin ka vaja kahte sulgu, aga oli ainult 1
     
     
      #Programmi tulemus:

 
#Aastaaeg
#Sisesta kuu number (1-12) => 4
#Kevad

#Kiiruse kontroll
#Sisesta lubatud kiirus (km/h) => 50
#Sisesta tegelik kiirus (km/h) => 75
#Trahv

#Taksosõit
#Sisesta sõidu pikkus (km) => 10
#Kas sõit on öösel (jah/ei)? => jah
#Sõidu hind: 13.2 €






#Muuda programmi nii, et alguses kuvatakse menüü ja kasutaja valib, millist osa käivitada:
 
#Vali programm:
#1 - Aastaaeg
#2 - Kiiruse kontroll
#3 - Taksosõit
#Sisesta valik (1-3) =>
#Käivitub ainult valitud osa. Kui kasutaja sisestab midagi muud kui 1, 2 või 3, kuvatakse teade Vigane valik.

#Lisa taksosõidu osasse allahindlus: kui sõit on pikem kui 50 km, väheneb hind 10%.
#Kiiruse kontrolli osa ei tohi lubada sisestada negatiivset kiirust.
#Lisaülesande tulemus (näide):

 
#Vali programm:
#1 - Aastaaeg
#2 - Kiiruse kontroll
#3 - Taksosõit
#Sisesta valik (1-3) => 3
#Taksosõit
#Sisesta sõidu pikkus (km) => 60
#Kas sõit on öösel (jah/ei)? => ei
#Pika sõidu allahindlus 10%
#Sõidu hind: 45.9 €

from math import *
try: 
    programmivalikud =print("1 - Aastaaeg","2 - Kiiruse kontroll","3 - Taksosõit")
    valikud=int(input("Sisesta number 1 kuni 3: "))
    if valik <1 and >3:   # ei olnud koolonit, aga peaks olema ju
        print("Ei ole sobiv arv.")
    else:
        print("Sobiv arv sisestatud.")
except ValueError:
    print("vigane valik.")
    
    print("Valisite taksosõit!")
    
    print("Taksosõit")
km=float(input("Sisesta sõidu pikkus (km) => "))
oo=input("Kas sõit on öösel (jah/ei)? => ")
hind=3+km+0.8
if oo=="jah" and oo=="JAH":    #peaks olema koolon ju, aga polnud
    hind=hind*1.2
  10%/hinnast
print("Sõidu hind:", round(hind,2)), "€"  #puudub koolon, enne oli ainult 1
     