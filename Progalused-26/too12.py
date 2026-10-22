
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
ümbermõõt=float(input("Sisesta puu ümbermõõt: ")) #teisendab strimgi ujukomaarvuks
läbimõõt=ümbermõõt/pi
print(f"Puu läbimõõt on {läbimõõt}.")



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


print("   @..@ ")
print("  (----) ")
print(" ( \__/ ) ")
print(" ^^ "" ^^ ")


a=int(input("Sisesta 1. täisarv: "))
b=int(input("Sisesta 2. täisarv: "))
c=int(input("Sisesta 3. täisarv: "))
P=a+b+c 



