print ("Hello world!"
print ("Ma õpin“ ,1, ". kursusel") #print väljastab info ekraanile



kursus=1 #int
aasta=2026 #int

print ("Ma õpin", kursus,". kursusel") #print väljastab info ekraanile
print ("Aasta on", aasta)

print ("Aastal", aasta+1, "olen juba", kursus+1," kursusel")

print ("2026", "10", "01", sep="/") #sep=" " määrab, mis eraldab väljastavaid väärtusi
print ("Sama", end="") #end="\n" määrab, mis pannakse lõppu. vaikimisi on see reavahetus 
print("rida") 

#Sisendamine
nimi=input("Sisesta oma nimi: ") #funktsioon, mis võimaldab kasutajal sisestada väärtust
print ("Tere",nimi, "!") #print väljastab info ekraanile

#Teised andmetüübid
a= input("Esimene arv: ") #str 17-> "17"
b=input("Teine arv: ") #str
print (a+b)

a= input("Esimene arv: ") #int 17-> 17, float
b= int(input("Teine arv: "))

#Põhioperatsionid
print("Liitmine: ")
a= input("Esimene arv: ") #int 17-> 17, float
b= int(input("Teine arv: ")) 
print (a,"+",b,b"=",a + b)

print("Lahutamine: ")
a=float(input("Esimene arv: "))
b=float(input("Teine arv: "))
print(a,"-",b,"=",a-b) 

#Tõeväärtused
p = True #5 > 3
q = False #2 > 4
print(not p, p and q, p or q)
print(5 > 3 and 2 > 4) #->False
print (5 > 3 or 2 > 4) #->True

#Formatimine
nimi = "Mari"
punktid = 87
print(f"{nimi} sai {punktid} punkti.")

hind = 19.9
kogus = 3
print(f"Kokku: {hind * kogus:.2f} eurot") #ümardab kahe komakohani

#Matemaatilised funktsioonid
print("Pii väärtus:", math.pi) # Pii väärtus
print("√16 =", math.sqrt(16)) #Rutudelement
print("sin(π/2) =", math.sin(math.pi / 2)) #Sinus
print("sin(30°) =", round(math.sin(math.radians(30)), 2)) # Sinus
print("5! =", math.factorial(5)) #Faktoriaal 1*2*3*4*5=120 
