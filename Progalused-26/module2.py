# Küsime kasutajalt eesnime
nimi = input("Sisesta eesnimi: ")

# Kontrollime, kas nimi on Juku (sõltumata tähesuurusest)
if nimi.lower() == "juku":
    print("Lähme Jukuga kinno!")
    
    # Kui nimi oli ainult suurtähtedega, lisame märkuse
    if nimi.isupper():
        print("Ära karju, Juku!")
        
    # Küsime vanust ja kontrollime, kas see on täisarv
    vanus_tekst = input("Sisesta Juku vanus: ")
    if vanus_tekst.isdigit():
        vanus = int(vanus_tekst)
        
        # Määrame pileti tüübi vastavalt vanusele
        if vanus < 0 or vanus > 100:
            print("Viga andmetes! Vanus peab olema vahemikus 0–100.")
        elif vanus < 6:
            print("Pilet on tasuta.")
        elif vanus <= 14:
            print("Vaja on osta lastepilet.")
        elif vanus <= 65:
            print("Vaja on osta täispilet.")
        else:
            print("Vaja on osta sooduspilet.")
    else:
        print("Viga! Vanus peab olema mittenegatiivne täisarv.")
else:
    print("Täna kinno ei minda.")




    import random

# Küsime kahe inimese nimed
nimi1 = input("Sisesta esimese inimese nimi: ")
nimi2 = input("Sisesta teise inimese nimi: ")

# Kontrollime, kas mõlemad nimed koosnevad ainult tähtedest
if nimi1.isalpha() and nimi2.isalpha():
    # Korrastame nimed suure algustähega
    nimi1_ilus = nimi1.capitalize()
    nimi2_ilus = nimi2.capitalize()
    
    # Otsustame juhuslikult, kas nad on pinginaabrid
    on_naabrid = random.choice([True, False])
    
    if on_naabrid:
        print(f"{nimi1_ilus} ja {nimi2_ilus} on täna pinginaabrid!")
    else:
        print(f"{nimi1_ilus} ja {nimi2_ilus} ei ole täna pinginaabrid.")
else:
    print("Viga! Mõlemad nimed peavad koosnema ainult tähtedest.")


try:
    # Küsime toa mõõtmed kümnendarvudena
    pikkus = float(input("Sisesta ristkülikukujulise toa pikkus meetrites: "))
    laius = float(input("Sisesta toa laius meetrites: "))
    
    if pikkus <= 0 or laius <= 0:
        print("Viga! Toa mõõtmed peavad olema positiivsed arvud.")
    else:
        pindala = round(pikkus * laius, 2)
        print(f"Toa põranda pindala on {pindala} ruutmeetrit.")
        
        soov = input("Kas soovid remonti teha? (jah/ei): ").lower()
        if soov == "jah":
            m2_hind = float(input("Sisesta põrandamaterjali ruutmeetri hind eurodes: "))
            materjali_kulu = round(pindala * m2_hind, 2)
            print(f"Põrandamaterjali maksumus on {materjali_kulu} eurot.")
            
            tegija = input("Kas teed remondi ise või kasutad professionaali? (ise/proff): ").lower()
            if tegija == "proff" or tegija == "professionaal":
                too_hind = float(input("Sisesta töö hind ruutmeetri kohta eurodes: "))
                koguhind = round(materjali_kulu + (pindala * too_hind), 2)
                print(f"Remondi koguhind koos tööga on {koguhind} eurot.")
            elif tegija == "ise":
                print(f"Ise tehes on remondi koguhind {materjali_kulu} eurot.")
            else:
                print("Tundmatu valik tegija kohta.")
        else:
            print("Selge, remonti praegu ei tehta.")
except ValueError:
    print("Viga! Palun sisesta mõõtmed ja hinnad korrektsete arvudena.")



    try:
    alghind = float(input("Sisesta toote alghind eurodes: "))
    
    if alghind < 0:
        print("Viga! Hind ei saa olla negatiivne.")
    else:
        # Kui hind on üle 700 euro, rakendub 30% soodustus (alles jääb 70%)
        if alghind > 700:
            lopphind = alghind * 0.70
            print(f"Sulle rakendus 30% soodustus! Lõplik hind on {lopphind:.2f} eurot.")
        else:
            print(f"Soodustus ei rakendu. Lõplik hind on {alghind:.2f} eurot.")
except ValueError:
    print("Viga! Palun sisesta hind arvuna.")



    try:
    temp = float(input("Sisesta toatemperatuur Celsiuse kraadides: "))
    
    # Võrdleme temperatuuri soovitusliku 18 kraadiga
    if temp > 18:
        print("Toatemperatuur on üle 18 kraadi (soovitatav talvine toasoojus).")
    elif temp == 18:
        print("Toatemperatuur on täpselt 18 kraadi.")
    else:
        print("Toatemperatuur on alla 18 kraadi. Tuba on jahe.")
except ValueError:
    print("Viga! Palun sisesta temperatuur numbrilisel kujul (nt 21.5 või -2).")



    try: 
        pikkus = float(input("Sisesta inimese pikkus sentimeetrites: "))
        if 30<=pikkus < 160:
            print("Inimene on lühike.")
        elif 160 <= pikkus <= 180:
            print("Inimene on keskmise pikkusega.")
        elif 180<pikkus<=220:
            print("Inimene on pikk")
        else:
            print("Arv ei sobi")
        except ValueError:
            print("Viga: Palun sisesta pikkus numbrina.")


try:
    sugu =input("Sugu: ")
    if sugu.isalpha():
        if sugu.lower()=="m" or sugu.upper()=="MEES":
            print("Mehe pikkuse analüüs")
             
            pikkus = float(input("Sisesta inimese pikkus sentimeetrites: "))
        if 30<=pikkus < 170:
            print("Inimene on lühike.")
        elif 170 <= pikkus <= 180:
            print("Inimene on keskmise pikkusega.")
        elif 180<pikkus<=220:
            print("Inimene on pikk")
        else:
            print("Arv ei sobi")
        except ValueError:
            print("Viga: Palun sisesta pikkus numbrina.")
        else:
            
            print("Naise pikkuse analüüs")
             
            pikkus = float(input("Sisesta inimese pikkus sentimeetrites: "))
        if 30<=pikkus < 160:
            print("Inimene on lühike.")
        elif 160 <= pikkus <= 180:
            print("Inimene on keskmise pikkusega.")
        elif 180<pikkus<=220:
            print("Inimene on pikk")
        else:
            print("Arv ei sobi")
        except ValueError:
            print("Viga: Palun sisesta pikkus numbrina.")

    else:
        print("Viga: kirjuta tähtedega")


from random import *
summa=0
arve="Toode     Kogus    Hind  Kokku\n"
valik=input("Kas soovid osta piima? (Jah/ei)")
if valik.lower()=="Jah": 
    kogus=input(Mitu piima soovid osta (int): "
    if kogus.isdigit():
        kogus=int(kogus)
        p_hind=round(unifrom(0.5,3.6),2)
        print(f"piima hind on {p_hind}€")
        summa+=round(kogus*p_hind,2)
        print(f"piima kogusumma on {summa}€")
        arve+=f"piim    {kogus}  {p_hind}€  {round(kogus*p_hind,2)}
    else:
    print("Viga:..") 
else:
    print("Selge: Piima ei taha")

print("Arve Nr. 123456789")
print(arve)



summa=0
arve="Toode     Kogus    Hind  Kokku\n"
valik=input("Kas soovid osta muna? (Jah/ei)")
if valik.lower()=="Jah": 
    kogus=input(Mitu muna soovid osta (int): "
    if kogus.isdigit():
        kogus=int(kogus)
        p_hind=round(unifrom(0.5,3.6),2)
        print(f"muna hind on {p_hind}€")
        summa+=round(kogus*p_hind,2)
        print(f"muna  kogusumma on {summa}€")
        arve+=f"muna  {kogus}  {p_hind}€  {round(kogus*p_hind,2)}
    else:
    print("Viga:..") 
else:
    print("Selge: Muna ei taha")

print("Arve Nr. 123456789")
print(arve)


from random import *
summa=0
arve="Toode     Kogus    Hind  Kokku\n"
valik=input("Kas soovid osta juustu? (Jah/ei)")
if valik.lower()=="Jah": 
    kogus=input(Mitu juustu soovid osta (int): "
    if kogus.isdigit():
        kogus=int(kogus)
        p_hind=round(unifrom(0.5,3.6),2)
        print(f"juustu hind on {p_hind}€")
        summa+=round(kogus*p_hind,2)
        print(f"juustu kogusumma on {summa}€")
        arve+=f"juustu  {kogus}  {p_hind}€  {round(kogus*p_hind,2)}
    else:
    print("Viga:..") 
else:
    print("Selge: Juustu ei taha")

print("Arve Nr. 123456789")
print(arve)


try:
   print("Nelinurga kontroll")
   k1=float(input("1. külje pikkus: "))
   k2=float(input("2. külje pikkus: "))
   k3=float(input("3. külje pikkus: "))
   k4=float(input("4. külje pikkus: "))
   if k1>0 and k2> and k3> and k4>0: 
        if k1==k2==k3==k4: 
            print ("Ruudu küljed")
        else:
            print("Nelinurga küljed")
   else:
        print("Viga: küljed peavad olema > 0")
except ValueError:
    print("Viga: On vaja ujukomaarv")



tehed=["+","-","*","/"]
try:
    arv1=float(input("Sisesta 1. arv: "))
    arv2=float(input("Sisesta 2. arv: "))
    tehe= input("Sisesta tehe: ")
    if tehe intehed:
        if tehe="+":
            print(f"{arv1}{tehe}{arv2}={arv1+arv2}")
        elif tehe=="-"
            print(f"{arv1}{tehe}{arv2}={arv1-arv2}")
        elif tehe=="/"
            print(f"{arv1}{tehe}{arv2}={arv1/arv2}")
        elif tehe=="*"
            print==(f"{arv1}{tehe}{arv2}={arv1*arv2}")
          if arv2==0:
              print("DIV/0")
           else:
              print(f"{arv1}{tehe}{arv2}={arv1/arv2}")
    else:
            print("Viga: tundmatu tehtemärk")
except ValueError:
    print("Viga: sisesta arvud")

