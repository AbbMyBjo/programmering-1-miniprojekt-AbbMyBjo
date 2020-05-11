import random

felmeddelande = "Något gick fel. Stänger av programmet." 
print("Välkommen till gympass-skaparen. Nedan kan du skriva vilka du har för krav på passet/passen jag ska göra åt dig.")

a = input("Vill du fokusera på någon/några speciella delar av kroppen? \n")
if a == "ja":
    a = input("Ange helkropp/överkropp/underkropp eller bål. \n")
    a = "helkropp"
else:
    print(felmeddelande)
    exit

b = input("Hur många pass vill du att jag ska göra? \n")

try:
    b = int(b)
except:
    while 1:
        print("Ange ett giltigt nummer.")
        b = input("Hur många pass vill du att jag ska göra? \n")
        try:
            b = int(b) 
            break
        except:
            continue

if b == 1:
    d = input("Hur hårt ska passet vara? Välj mellan väldigt lätt, lätt, medel och intensivt. \n")
elif b > 1:
    d = input("Hur hårda ska passen vara? Välj mellan väldigt lätt, lätt, medel och intensivt. \n")

Gymövningar = [
        {"namn": "biceps", "övningar":["skivstångscurl", "hantelcurl", "hammercurl", "chins", "preacher curls", "sittande bicepscurls", "koncentrationscurl"]},
        {"namn": "bröst", "övningar":["bänkpress", "hantelpress", "lutande bänkpress/hantelpress", "breda armävningar", "smal bänkpress", "kryssdrag", "pec deck", "bröstpress"]},
        {"namn": "mage", "övningar":["kabelcrunch", "hängande benlyft/benlyft", "kabelrotationer", "alternerande hälnuddningar", "cykelcrunch", "plankan", "fällkniven", "crunches"]},
        {"namn": "triceps", "övningar":["dips", "sittande dips", "triceps press med hantel", "skullcrushers", "french press", "triceps pushdown", "smal bänkpress", "smala armhävningar"]},
        {"namn": "rygg", "övningar":["marklyft", "hyperextension", "pullups", "sittande kabelrodd", "latsdrag", "hantelrodd", "rygglyft", "stångrodd"]},
        {"namn": "axlar", "övningar":["axelpress skivstång", "axelpress hantlar", "arnoldpress", "sidolyft", "face pull", "pullups", "dumbbell shrug", "kabelrotationer"]},
        {"namn": "lår", "övningar":["backsquats", "nordic hamstring curl", "frontsquats", "jumping squats", "utfallssteg", "höftlyft", "benpress", "bensträck", "bencurls", "höftabduktion"]},
        {"namn": "rumpa", "övningar":["jumping squats", "squats", "höftlyft", "utfallssteg", "rumplyft", "flutter kicks", "sumo marklyft", "backsquats", "frontsquats"]}]

Intensivt =["burpees", "armhävningar", "plankan", "thrusters", "man-makers", "kettlebell swingar", "box jumps", "jägarvila", "toe to bar"]

flera_pass = []

counter = 0
while counter < b: 
    i = 0
    x = 0
    y = 0
    i2=0

    ettpass = []
    gympass_siffror = []
    gympass_bokstäver = []


    if a == "helkropp":
        for keys in Gymövningar:
            övn_siff = random.randrange(0, len(Gymövningar[i]["övningar"]))
            gympass_siffror.append(övn_siff)
            i+=1

        for keys in gympass_siffror:
            plats = (gympass_siffror[x])
            övning = Gymövningar[y]["övningar"][plats]
            x+=1
            y+=1
            gympass_bokstäver.append(övning)

    elif a == "överkropp":
        while i <= 5:
            övn_siff = random.randrange(0, len(Gymövningar[i2]["övningar"]))
            gympass_siffror.append(övn_siff)
            i2+=1
            i+=1

        for saker in gympass_siffror:
            plats = (gympass_siffror[x])
            övning = Gymövningar[y]["övningar"][plats]
            x+=1
            y+=1
            gympass_bokstäver.append(övning)

    elif a == "underkropp":
        while i <= 6:
            ÖvningEtt = random.randrange(0, len(Gymövningar[6]["övningar"])-1)
            ÖvningTvå = random.randrange(0, len(Gymövningar[7]["övningar"])-1)
            gympass_siffror.append(ÖvningEtt)
            i += 1
            gympass_siffror.append(ÖvningTvå)
            i += 1

        ii = 0
        while ii <= len(gympass_siffror):
            while 1:
                if len(gympass_bokstäver)==8:
                    break
                else:
                    plats = (gympass_siffror[x])
                    övning = Gymövningar[6]["övningar"][plats]
                    gympass_bokstäver.append(övning)
                    övning2 = Gymövningar[7]["övningar"][plats]
                    gympass_bokstäver.append(övning2)
                    y+=1
                    x+=1
            i+=1
    
    elif a == "bål":
        while i < 6:
            ÖvningEtt = random.randrange(0, len(Gymövningar[2]["övningar"]))
            ÖvningTvå = random.randrange(0, len(Gymövningar[4]["övningar"]))
            gympass_siffror.append(ÖvningEtt)
            gympass_siffror.append(ÖvningTvå)
            i += 2

        sant = True

        while sant == True:
            if int(len(gympass_bokstäver)) == 8:
                sant = False
            else:
                sant = True
                plats = (gympass_siffror[x])
                övning = Gymövningar[2]["övningar"][plats]
                gympass_bokstäver.append(övning)
                övning2 = Gymövningar[4]["övningar"][plats]
                gympass_bokstäver.append(övning2)
                y+=1
                x+=1

    counter += 1
    if d == "lätt":
        for keys in gympass_bokstäver:
            ettpass.append(keys+" 2x10")
        flera_pass.append(ettpass)

    elif d == "medel":
        for keys in gympass_bokstäver:
            ettpass.append(keys+" 3x10")
        flera_pass.append(ettpass)

    elif d == "intensivt":
        nyövning = random.randrange(0, len(Intensivt))
        gympass_siffror.append(Intensivt[nyövning])
        gympass_bokstäver.append(gympass_siffror[-1]) 
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
for listor in flera_pass:
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

for lista in flera_pass:
    if len(lista) < 8:
        ny_gympass_siffror = []
        ny_gympass_bokstäver = []
        i7 = 0
        if a == "bål":
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

        else:
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

print(" ")
if int(b) <= 2:
    print("Här är dina pass: \n")
elif b == 1:
    print("Här är ditt pass: \n")
else:
    print("Här är passen: \n")

passnummer = 1
for träningspass in flera_pass:
    print("Pass "+str(passnummer)+": ")
    print(', '.join(träningspass)+"\n")
    passnummer+=1