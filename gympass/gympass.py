import random

felmeddelande = "Något gick fel. Stänger av programmet." 
print("Välkommen till gympass-skaparen. Nedan kan du skriva vilka du har för krav på passet/passen jag ska göra åt dig.")

a = input("Vill du fokusera på någon/några speciella delar av kroppen? \n") #låter användaren välja om hen vill fokusera på nån speciell del av kroppen
if a == "ja":
    a = input("Ange helkropp/överkropp/underkropp eller bål. \n") #skapar en variabel för den del av kroppen användaren skriver in att hen vill träna
elif a == "nej":
    a = "helkropp" #antar att användaren vill träna helkropp eftersom hen inte skrivit någon speciell del av kroppen
else:
    print(felmeddelande) #skrivs ut om programmet inte uppfattar det som skrivs i input och avslutar
    exit

b = input("Hur många pass vill du att jag ska göra? \n") #skapar en variabel för antal pass programmet ska göra

try: #kollar om input för antal pass är en giltig siffra genom att se om det går att göra om den till int
    b = int(b)
except: #ber användaren mata in ett giltigt nummer om try-satsen inte fungerar
    while 1:
        print("Ange ett giltigt nummer.")
        b = input("Hur många pass vill du att jag ska göra? \n")
        try: #testar om det är ett giltigt nummer igen och går ut ur loopen om det är det
            b = int(b) 
            break
        except: #fortsätter loopen om numret inte är giltigt 
            continue

if b == 1: #om b är 1 skapas en variabel (d) för svårighetsgrad som är i singular
    d = input("Hur hårt ska passet vara? Välj mellan väldigt lätt, lätt, medel och intensivt. \n")
elif b > 1: #om b är större än 1 skapas en variabel (d) för svårighetsgrad som är i plural
    d = input("Hur hårda ska passen vara? Välj mellan väldigt lätt, lätt, medel och intensivt. \n")

Gymövningar = [ #skapar en lista för gymövningar med ett dictionary för varje kroppsdel som har en lista med övningar för de musklerna
        {"namn": "biceps", "övningar":["skivstångscurl", "hantelcurl", "hammercurl", "chins", "preacher curls", "sittande bicepscurls", "koncentrationscurl"]},
        {"namn": "bröst", "övningar":["bänkpress", "hantelpress", "lutande bänkpress/hantelpress", "breda armävningar", "smal bänkpress", "kryssdrag", "pec deck", "bröstpress"]},
        {"namn": "mage", "övningar":["kabelcrunch", "hängande benlyft/benlyft", "kabelrotationer", "alternerande hälnuddningar", "cykelcrunch", "plankan", "fällkniven", "crunches"]},
        {"namn": "triceps", "övningar":["dips", "sittande dips", "triceps press med hantel", "skullcrushers", "french press", "triceps pushdown", "smal bänkpress", "smala armhävningar"]},
        {"namn": "rygg", "övningar":["marklyft", "hyperextension", "pullups", "sittande kabelrodd", "latsdrag", "hantelrodd", "rygglyft", "stångrodd"]},
        {"namn": "axlar", "övningar":["axelpress skivstång", "axelpress hantlar", "arnoldpress", "sidolyft", "face pull", "pullups", "dumbbell shrug", "kabelrotationer"]},
        {"namn": "lår", "övningar":["backsquats", "nordic hamstring curl", "frontsquats", "jumping squats", "utfallssteg", "höftlyft", "benpress", "bensträck", "bencurls", "höftabduktion"]},
        {"namn": "rumpa", "övningar":["jumping squats", "squats", "höftlyft", "utfallssteg", "rumplyft", "flutter kicks", "sumo marklyft", "backsquats", "frontsquats"]}]

#skapar en lista med lite intensivare övningar som används endast när svårighetsgraden intensivt matas in
Intensivt =["burpees", "armhävningar", "plankan", "thrusters", "man-makers", "kettlebell swingar", "box jumps", "jägarvila", "toe to bar"]

flera_pass = [] #skapar en lista där de slutgiltiga passen ska läggas in

counter = 0 #skapar variabeln counter och ger den värdet 0

while counter < b: 
#gör en loop som gäller när variabeln counter är mindre än variabeln b (antal pass)
#hela loopen används för att skapa pass som läggs i listan flera_pass 
    i = 0 #skapar variablerna i, x, y och i2 och ger alla de värdena 0
    x = 0 #variablerna nollställs igen när loopen börjar om
    y = 0
    i2 = 0

    ettpass = [] #skapar en lista som ska innehålla ett pass
    gympass_siffror = [] #skapar en lista där index ska ligga för varje övning i passet som ska skapas
    gympass_bokstäver = [] #skapar en lista där övningarna läggs in i bokstavsform
#alla 3 listor nollställs när loopen börjar om

    if a == "helkropp": #om input a är helkropp körs den här if-satsen
        for keys in Gymövningar: #för varje värde i Gymövningar ska loopen köras en gång
            övn_siff = random.randrange(0, len(Gymövningar[i]["övningar"])) #randomiserar ett index från en lista i gymövningar beroende på variabeln i som defineras som övn_siff
            gympass_siffror.append(övn_siff) #lägger till värdet ovan i listan
            i+=1 #lägger till 1 i värde på variabeln i

        for keys in gympass_siffror: #för varje värde i listan körs loopen en gång
            plats = (gympass_siffror[x]) #definerar plats som värdet på variabeln x i listan
            övning = Gymövningar[y]["övningar"][plats] #kollar vad index i listan heter som en string
            x+=1 #plussar på 1 på variabeln x
            y+=1 #plussar på 1 på variabeln y
            gympass_bokstäver.append(övning) #lägger till stringen i den nya listan

    elif a == "överkropp": #om input a är helkropp körs den här delen av if-satsen
        while i2 <= 5: #när variabeln i har ett värde som är lika med eller mindre än 5 körs loopen
            övn_siff = random.randrange(0, len(Gymövningar[i]["övningar"])) #samma som första for-loopen
            gympass_siffror.append(övn_siff)
            i2+=1
            i+=1

        for keys in gympass_siffror: #exakt likadan som for-loopen innan
            plats = (gympass_siffror[x])
            övning = Gymövningar[y]["övningar"][plats]
            x+=1
            y+=1
            gympass_bokstäver.append(övning)

    elif a == "underkropp": #om input a är underkropp körs den här delen av if-satsen
        while i <= 6: #när variabeln i har ett värde som är mindre eller lika med 6 körs loopen
            ÖvningEtt = random.randrange(0, len(Gymövningar[6]["övningar"])-1) #randomiserar en siffra mellan 0 och längden på listan för lårövningar
            ÖvningTvå = random.randrange(0, len(Gymövningar[7]["övningar"])-1) #randomiserar en siffra mellan 0 och längden på listan för rumpövningar
            gympass_siffror.append(ÖvningEtt) #lägger till index för övningen i listan
            gympass_siffror.append(ÖvningTvå) #lägger till index för övningen i listan
            i += 2

        ii = 0 #definerar ii som en variabel med värde 0
        while ii <= len(gympass_siffror): #när variabeln ii är mindre eller lika med längden på listan körs loopen
            while 1: #så länge man inte säger att den är false ska loopen köras
                if len(gympass_bokstäver)==8: #om längden på listan är 8, gå ut ur loopen
                    break
                else: #om den inte är 8
                    plats = (gympass_siffror[x]) #definerar plats som index x i listan
                    övning = Gymövningar[6]["övningar"][plats] #kollar vilken övning som har indexet plats och gör om det till en string
                    gympass_bokstäver.append(övning) #lägger till stringen i listan
                    övning2 = Gymövningar[7]["övningar"][plats]
                    gympass_bokstäver.append(övning2)
                    y+=1
                    x+=1
            ii+=1
    
    elif a == "bål": #om input a är bål körs den här delen av if-satsen
        while i < 6:
            ÖvningEtt = random.randrange(0, len(Gymövningar[2]["övningar"]))
            ÖvningTvå = random.randrange(0, len(Gymövningar[4]["övningar"]))
            gympass_siffror.append(ÖvningEtt)
            gympass_siffror.append(ÖvningTvå)
            i += 2

        sant = True #skapar variabeln sant och ger den värdet true

        while sant == True: #när sant har värdet true körs loopen
            if int(len(gympass_bokstäver)) == 8: #om längden på listan är 8, ge sant värdet false
                sant = False
            else: #om den inte är 8
                plats = (gympass_siffror[x])
                övning = Gymövningar[2]["övningar"][plats]
                gympass_bokstäver.append(övning)
                övning2 = Gymövningar[4]["övningar"][plats]
                gympass_bokstäver.append(övning2)
                y+=1
                x+=1

    counter += 1
    if d == "lätt": #om variabeln d är lätt körs den här
        for keys in gympass_bokstäver: #för varje värde i listan körs loopen
            ettpass.append(keys+" 2x10") #lägger till varje värde + " 2x10" i listan
        flera_pass.append(ettpass) #lägger till listan ettpass i listan flera_pass

    elif d == "medel":
        for keys in gympass_bokstäver:
            ettpass.append(keys+" 3x10") #samma som förra delen men skriver 3x10 istället för 2x10
        flera_pass.append(ettpass)

    elif d == "intensivt":
        nyövning = random.randrange(0, len(Intensivt)) #randomiserar ett tal mellan 0 och längden på listan för intensiva övningar
        gympass_siffror.append(Intensivt[nyövning]) #lägger till indexet i listan
        gympass_bokstäver.append(gympass_siffror[-1]) #lägger till den sista övningen i gympass_siffror i gympass_bokstäver
        for keys in gympass_bokstäver: 
            ettpass.append(keys+" 3x15")
        flera_pass.append(ettpass)

    elif d == "väldigt lätt":
        for keys in gympass_bokstäver:
            ettpass.append(keys+" x10")
        flera_pass.append(ettpass)

    else:
        print(felmeddelande)

i3 = 0
for listor in flera_pass: #kollar om det finns flera av samma värde i en lista och tar då bort alla utom 1
    i4 = 0
    for övning in flera_pass[i3]:
        poppat_värde = flera_pass[i3].pop(i4)
        sant2 = True
        i5 = 0
        i6 = 0
        while sant2 == True:
            if poppat_värde in flera_pass[i3]:
                tabortindex = flera_pass[i3].index(poppat_värde)
                flera_pass[i3].pop(tabortindex)
                i5 += 1
            elif i5 == len(flera_pass[i3]):
                break
            else:
                sant2 == False
                i5 += 1
        flera_pass[i3].insert(i6, poppat_värde)
        i6 += 1 
        i4 += 1
    i3 += 1

for lista in flera_pass: #lägger till nya övningar i listor som blivit kortare pga den förra loopen
    if len(lista) < 8:
        ny_gympass_siffror = []
        ny_gympass_bokstäver = []
        i7 = 0
        
        if a == "bål": #varje del av kroppen för sig så det blir rätt övningar
            while len(lista) < 8:
                ny_övn_siff = random.randrange(0, len(Gymövningar[2]["övningar"]))
                ny_gympass_siffror.append(ny_övn_siff)
                ny_övn_siff2 = random.randrange(0, len(Gymövningar[4]["övningar"]))
                ny_gympass_siffror.append(ny_övn_siff2)
                ny_plats = (ny_gympass_siffror[i7])
                ny_övning = Gymövningar[2]["övningar"][ny_plats]
                ny_övning2 = Gymövningar[4]["övningar"][ny_plats]
                if ny_övning in lista:
                    continue
                elif ny_övning not in lista:
                    if d == "väldigt lätt":
                        lista.append(ny_övning+ " x10")
                    elif d == "lätt":
                        lista.append(ny_övning+ " 2x10")
                    elif d == "medel":
                        lista.append(ny_övning+ " 3x10")
                    elif d == "intensivt":
                        lista.append(ny_övning+ " 3x15")
                if ny_övning2 in lista:
                    continue
                elif ny_övning2 not in lista:
                    if d == "väldigt lätt":
                        lista.append(ny_övning2+ " x10")
                    elif d == "lätt":
                        lista.append(ny_övning2+ " 2x10")
                    elif d == "medel":
                        lista.append(ny_övning2+ " 3x10")
                    elif d == "intensivt":
                        lista.append(ny_övning2+ " 3x15")
                i7 += 1

        elif a == "överkropp":
            while len(lista) < 8:
                övningslista = random.randrange(0, 5)
                ny_övn_siff = random.randrange(0, len(Gymövningar[övningslista]["övningar"]))
                ny_gympass_siffror.append(ny_övn_siff)
                ny_plats = (ny_gympass_siffror[i7])
                ny_övning = Gymövningar[övningslista]["övningar"][ny_plats]
                if ny_övning in lista:
                    continue
                elif ny_övning not in lista:
                    if d == "väldigt lätt":
                        lista.append(ny_övning+ " x10")
                    elif d == "lätt":
                        lista.append(ny_övning+ " 2x10")
                    elif d == "medel":
                        lista.append(ny_övning+ " 3x10")
                    elif d == "intensivt":
                        lista.append(ny_övning+ " 3x15")
                i7 += 1

        elif a == "underkropp":
            while len(lista) < 8:
                ny_övn_siff = random.randrange(0, len(Gymövningar[6]["övningar"]))
                ny_gympass_siffror.append(ny_övn_siff)
                ny_övn_siff2 = random.randrange(0, len(Gymövningar[7]["övningar"]))
                ny_gympass_siffror.append(ny_övn_siff2)
                ny_plats = (ny_gympass_siffror[i7])
                ny_övning = Gymövningar[6]["övningar"][ny_plats]
                ny_övning2 = Gymövningar[7]["övningar"][ny_plats]
                if ny_övning in lista:
                    continue
                elif ny_övning not in lista:
                    if d == "väldigt lätt":
                        lista.append(ny_övning+ " x10")
                    elif d == "lätt":
                        lista.append(ny_övning+ " 2x10")
                    elif d == "medel":
                        lista.append(ny_övning+ " 3x10")
                    elif d == "intensivt":
                        lista.append(ny_övning+ " 3x15")
                if ny_övning2 in lista:
                    continue
                elif ny_övning2 not in lista:
                    if d == "väldigt lätt":
                        lista.append(ny_övning2+ " x10")
                    elif d == "lätt":
                        lista.append(ny_övning2+ " 2x10")
                    elif d == "medel":
                        lista.append(ny_övning2+ " 3x10")
                    elif d == "intensivt":
                        lista.append(ny_övning2+ " 3x15")
                i7 += 1

        else: #om inget av ovanstående skrivs in finns bara helkropp kvar så de skulle kunnat stå elif a == "helkropp" lika gärna
            while len(lista) < 8:
                övningslista = random.randrange(0, len(Gymövningar))
                ny_övn_siff = random.randrange(0, len(Gymövningar[övningslista]["övningar"]))
                ny_gympass_siffror.append(ny_övn_siff)
                ny_plats = (ny_gympass_siffror[i7])
                ny_övning = Gymövningar[övningslista]["övningar"][ny_plats]
                if ny_övning in lista:
                    continue
                elif ny_övning not in lista:
                    if d == "väldigt lätt":
                        lista.append(ny_övning+ " x10")
                    elif d == "lätt":
                        lista.append(ny_övning+ " 2x10")
                    elif d == "medel":
                        lista.append(ny_övning+ " 3x10")
                    elif d == "intensivt":
                        lista.append(ny_övning+ " 3x15")
                i7 += 1

print(" ") #skriver "här är ditt/dina pass" beroende på antal pass man angett tidigare
if int(b) >= 2:
    print("Här är dina pass: \n")
elif b == 1:
    print("Här är ditt pass: \n")
else:
    print("Här är passen: \n")

passnummer = 1
for träningspass in flera_pass: #skriver ut passen som "Pass 1: " osv 
    print("Pass "+str(passnummer)+": ")
    print(', '.join(träningspass)+"\n")
    passnummer+=1