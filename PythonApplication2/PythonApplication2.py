
print("Aastaaeg") # Eelmises oli tekst ülakomade/jutumärkidega poolik (puudus lõpumärk)
kuu = int(input("Sisesta kuu number (1-12) => "))

if kuu < 1 or kuu > 12: # Eelmises oli 'and', aga arv ei saa olla korraga alla 1 JA üle 12, peab olema 'or' (või)
    print("Vigane kuu")
elif kuu == 12 or kuu <= 2: # Eelmises oli üks '=', võrdlemiseks on vaja kahte '=='
    print("Talv")
elif 3 <= kuu <= 5: # Eelmises oli 'else if' (peab olema 'elif') ja valepidi märk '>=' (peab olema '<=')
    print("Kevad")
elif 6 <= kuu <= 8: # Eelmises oli märk valepidi ('>=') ja rea lõpust puudus koolon ':'
    print("Suvi")
else:
    print("Sügis")

print()
print("Kiiruse kontroll")
lubatud = int(input("Sisesta lubatud kiirus (km/h) => ")) # Eelmises puudus lõpust üks sulg ')'
kiirus = int(input("Sisesta tegelik kiirus (km/h) => ")) # Eelmises puudus 'int(' ja lõpust teine sulg ')'
yletus = kiirus - lubatud # Eelmises oli suure tähega 'Ületus', aga allpool väikese tähega 'ületus' (Python teeb neil vahet)

if yletus <= 0: # Eelmises oli märk valepidi '=<', õige on '<='
    print("Kiirust ei ületatud")
elif yletus > 40: # Tõstsin selle ettepoole, sest muidu jääbprogramm '> 0' juurde pidama ega jõua kunagi trahvi ega lubadeni
    print("Juhiluba võetakse ära")
elif yletus > 20: # Tõstsin selle ettepoole samal põhjusel (suuremad arvud kontrollitakse enne)
    print("Trahv")
elif yletus > 0: # Tõstsin selle viimaseks, muidu püüab see kõik ületused kinni ja annab alati ainult hoiatuse
    print("Hoiatus")

print()
print("Taksosõit")
km = float(input("Sisesta sõidu pikkus (km) => "))
oo = input("Kas sõit on öösel (jah/ei)? => ")
hind = 3 + km * 0.8 # Eelmises oli 'km + 0.8', aga kilomeetrid tuleb hinnaga korrutada 'km * 0.8'

if oo == "jah" or oo == "JAH": # Eelmises oli 'and' (sõna ei saa olla korraga väike ja suur) ning puudus koolon ':'
    hind = hind * 1.2

print("Sõidu hind:", round(hind, 2), "€") # Eelmises oli '"€"' jäänud print-käsu s
     
     
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

print("Vali programm:")
print("1 - Aastaaeg")
print("2 - Kiiruse kontroll")
print("3 - Taksosõit")

try:
    valik = int(input("Sisesta valik (1-3) => "))

    if valik == 1:
        print("\nAastaaeg")
        kuu = int(input("Sisesta kuu number (1-12) => "))
        if kuu < 1 or kuu > 12:
            print("Vigane kuu")
        elif kuu == 12 or kuu <= 2:
            print("Talv")
        elif 3 <= kuu <= 5:
            print("Kevad")
        elif 6 <= kuu <= 8:
            print("Suvi")
        else:
            print("Sügis")

    elif valik == 2:
        print("\nKiiruse kontroll")
        lubatud = int(input("Sisesta lubatud kiirus (km/h) => "))
        kiirus = int(input("Sisesta tegelik kiirus (km/h) => "))

        if lubatud < 0 or kiirus < 0:
            print("Kiirus ei saa olla negatiivne!")
        else:
            uletus = kiirus - lubatud
            if uletus <= 0:
                print("Kiirust ei ületatud")
            elif uletus <= 20:
                print("Hoiatus")
            elif uletus <= 40:
                print("Trahv")
            else:
                print("Juhiluba võetakse ära")

    elif valik == 3:
        print("\nTaksosõit")
        km = float(input("Sisesta sõidu pikkus (km) => "))
        oo = input("Kas sõit on öösel (jah/ei)? => ")

        # Alustustasu 3 € + 0.8 € iga kilomeetri kohta
        hind = 3 + km * 0.8

        if oo.lower() == "jah":
            hind = hind * 1.2

        if km > 50:
            print("Pika sõidu allahindlus 10%")
            hind = hind * 0.9

        print("Sõidu hind:", round(hind, 2), "€")

    else:
        print("Vigane valik")

except ValueError:
    print("Vigane valik")
     
