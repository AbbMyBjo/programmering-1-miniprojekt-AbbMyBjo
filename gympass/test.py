import random

felmeddelande = "Något gick fel. Stänger av programmet."
print("Välkommen till gympass-skaparen. Nedan kan du skriva vilka du har för krav på passet/passen jag ska göra åt dig.")

a = "underkropp"
b = 5
d = "lätt"

Gymövningar = [
        {"namn": "biceps", "övningar":["skivstångscurl", "hantelcurl", "hammercurl", "pullups", "preacher curls", "sittande bicepscurls"]},
        {"namn": "bröst", "övningar":["bänkpress", "hantelpress", "lutande bänkpress/hantelpress", "breda armävningar", "smal bänkpress", "kryssdrag", "dips"]},
        {"namn": "mage", "övningar":["kabelcrunch", "hängande benlyft/benlyft", "kabelrotationer", "alternerande hälnuddningar", "cykelcrunch", "plankan", "fällkniven", "crunches"]},
        {"namn": "triceps", "övningar":["dips", "sittande dips", "skullcrushers", "triceps pushdown", "smal bänkpress"]},
        {"namn": "rygg", "övningar":["marklyft", "hyperextension", "pullups", "latsdrag", "hantelrodd", "rygglyft", "stångrodd"]},
        {"namn": "axlar", "övningar":["axelpress skivstång", "axelpress hantlar", "arnoldpress", "sidolyft", "face pull", "pullups"]},
        {"namn": "lår", "övningar":["backsquats", "nordic hamstring curl", "frontsquats", "jumping squats", "utfallssteg", "höftlyft", "benpress", "bensträck", "bencurls", "höftabduktion"]},
        {"namn": "rumpa", "övningar":["jumping squats", "squats", "höftlyft", "utfallssteg", "rumplyft", "flutter kicks", "sumo marklyft", "backsquats", "frontsquats"]}]

Uppvärmning = ["burpees", "kettlebell swingar", "hopprep", "löpband", "trappmaskin", "crosstrainer", "cykel", "SkiErg", "rodd"]
Kondition = ["kettlebell swingar", "hopprep", "löpband", "trappmaskin", "crosstrainer", "cykel", "SkiErg", "rodd"]
Intensivt =["burpees", "armhävningar", "plankan", "thrusters", "man-makers", "kettlebell swingar", "box jumps", "jägarvila", "toe to bar"]

i = 0
counter = 1
flera_pass = []

while counter <= b:
    i = 0
    x = 0
    y = 0
    i2=0
    ettpass = []
    gympass_siffror = []
    gympass_bokstäver = []
    if a == "överkropp":
        print("116")
        while i <= 5:
            övn_siff = random.randrange(0, len(Gymövningar[i2]["övningar"]))
            gympass_siffror.append(övn_siff)
            i2+=1
            i+=1

        x = 0
        y = 0
        i = 0

        for saker in gympass_siffror:
            plats = (gympass_siffror[x])
            övning = Gymövningar[y]["övningar"][plats]
            x+=1
            y+=1
            gympass_bokstäver.append(övning)
            print("i loop 132")
        print("132")

        if d == "lätt":
            for keys in gympass_bokstäver:
                ettpass.append(keys+" 2x10")
            flera_pass.append(ettpass)
            print("138")

        elif d == "medel":
            for keys in gympass_bokstäver:
                ettpass.append(keys+" 3x10")
            flera_pass.append(ettpass)
            print("144")

        elif d == "intensivt":
            nyövning = random.randrange(0, len(Intensivt))
            gympass_siffror.append(Intensivt[nyövning])
            gympass_bokstäver.append(gympass_siffror[-1]) 
            for keys in gympass_bokstäver:
                ettpass.append(keys+" 3x15")
            flera_pass.append(ettpass)
            print("153")

        elif d == "väldigt lätt":
            for keys in gympass_bokstäver:
                ettpass.append(keys+" x10")
            flera_pass.append(ettpass)
            print("159")

        else:
            print(felmeddelande)
        print("168")
    elif a == "underkropp":
        print("168")
        while i <= 6:
            ÖvningEtt = random.randrange(0, len(Gymövningar[6]["övningar"]))
            ÖvningTvå = random.randrange(0, len(Gymövningar[7]["övningar"]))
            gympass_siffror.append(ÖvningEtt)
            i += 1
            gympass_siffror.append(ÖvningTvå)
            i += 1
            print(gympass_siffror)

        x = 0
        i = 1
        y = 0

        while i <= len(gympass_siffror):
            plats = (gympass_siffror[x])
            try:
                övning = Gymövningar[6]["övningar"][plats]
                gympass_bokstäver.append(övning)
                x+=1
                i+=1

            except:
                x+=1
                i+=1
                if Gymövningar[6]["övningar"].index(övning) == len(Gymövningar[6]["övningar"]):
                    nyplats = len(Gymövningar[6]["övningar"])-Gymövningar[6]["övningar"][plats]
                    övning = Gymövningar[6]["övningar"][nyplats]
                    gympass_bokstäver.append(övning)
                else:
                    break

            plats = (gympass_siffror[y])
            try:
                övning2 = Gymövningar[7]["övningar"][plats]
                gympass_bokstäver.append(övning2)
                y+=1
                i+=1

            except:
                y+=1
                i+=1
                if Gymövningar[7]["övningar"].index(övning2) == len(Gymövningar[7]["övningar"]):
                    nyplats = len(Gymövningar[7]["övningar"])-Gymövningar[7]["övningar"][plats]
                    övning2 = Gymövningar[7]["övningar"][nyplats]
                    gympass_bokstäver.append(övning2)
                else:
                    break

        print("176")

        if d == "lätt":
            for keys in gympass_bokstäver:
               ettpass.append(keys+" 2x10")
            flera_pass.append(ettpass)
            print("182")

        elif d == "medel":
            for keys in gympass_bokstäver:
                ettpass.append(keys+" 3x10")
            flera_pass.append(ettpass)
            print("188")

        elif d == "intensivt":
            nyövning = random.randrange(0, len(Intensivt))
            gympass_siffror.append(Intensivt[nyövning])
            gympass_bokstäver.append(gympass_siffror[-1]) 
            for keys in gympass_bokstäver:
                ettpass.append(keys+" 3x15")
            flera_pass.append(ettpass)
            print("197")

        elif d == "väldigt lätt":
            for keys in gympass_bokstäver:
                ettpass.append(keys+" x10")
            flera_pass.append(ettpass)
            print("203")

        else:
            print(felmeddelande)
            exit
    elif a == "bål":
        print("90")
        while i <= 6:
            ÖvningEtt = random.randrange(0, len(Gymövningar[2]["övningar"]))
            ÖvningTvå = random.randrange(0, len(Gymövningar[4]["övningar"]))
            gympass_siffror.append(ÖvningEtt)
            i += 1
            gympass_siffror.append(ÖvningTvå)
            i += 1
            print(gympass_siffror)

        x = 0
        i = 1

        while i <= len(gympass_siffror):
            plats = (gympass_siffror[x])
            try:
                övning = Gymövningar[2]["övningar"][plats]
                gympass_bokstäver.append(övning)
                x+=1
                i+=1

            except:
                x+=1
                i+=1
                if Gymövningar[2]["övningar"].index(övning) > len(Gymövningar[2]["övningar"]):
                    nyplats = len(Gymövningar[2]["övningar"])-Gymövningar[2]["övningar"][plats]
                    övning = Gymövningar[2]["övningar"][nyplats]
                    gympass_bokstäver.append(övning)
                    x+=1
                    i+=1

            try:
                övning2 = Gymövningar[4]["övningar"][plats]
                gympass_bokstäver.append(övning2)
                x+=1
                i+=1

            except:
                x+=1
                i+=1
                if Gymövningar[4]["övningar"].index(övning2) > len(Gymövningar[4]["övningar"]):
                    nyplats = len(Gymövningar[4]["övningar"])-Gymövningar[4]["övningar"][plats]
                    övning2 = Gymövningar[4]["övningar"][nyplats]
                    gympass_bokstäver.append(övning2)
                    x+=1
                    i+=1

        print("176")

        if d == "lätt":
            for keys in gympass_bokstäver:
               ettpass.append(keys+" 2x10")
            flera_pass.append(ettpass)
            print("182")

        elif d == "medel":
            for keys in gympass_bokstäver:
                ettpass.append(keys+" 3x10")
            flera_pass.append(ettpass)
            print("188")

        elif d == "intensivt":
            nyövning = random.randrange(0, len(Intensivt))
            gympass_siffror.append(Intensivt[nyövning])
            gympass_bokstäver.append(gympass_siffror[-1]) 
            for keys in gympass_bokstäver:
                ettpass.append(keys+" 3x15")
            flera_pass.append(ettpass)
            print("197")

        elif d == "väldigt lätt":
            for keys in gympass_bokstäver:
                ettpass.append(keys+" x10")
            flera_pass.append(ettpass)
            print("203")

        else:
            print(felmeddelande)
            exit

    counter+=1

if b <= 2:
    print("Här är dina pass: ")
elif b == 1:
    print("Här är ditt pass: ")
else:
    print("Här är passen.")

# passnummer = 1
# for träningspass in flera_pass:
#     print("pass "+ str(passnummer) + str(träningspass))
#     passnummer+=1

# print(len(flera_pass))

i3 = 0
print(flera_pass)
for listor in flera_pass:
    i = 0
    i2 = 1
    print(flera_pass[i3])
    i3 += 1
    for övning in flera_pass[i3][i]:
        poppat_värde = flera_pass[i3].pop(i)
        print("279")
        if poppat_värde in flera_pass[i3]:
            print("280")
            tabortindex = flera_pass[i3].index(poppat_värde)
            print("280")
            flera_pass[i3].pop(tabortindex)
            i += 1
            i2 += 1
            print(i)
            print(flera_pass[i3])
        elif i2 == len(flera_pass[i3]):
            break
        elif i == len(flera_pass[i3]):
            break
        else:
            i2 += 1
        flera_pass[i3].append(poppat_värde)

passnummer = 1
for träningspass in flera_pass:
    print("pass "+ str(passnummer) + str(träningspass))
    passnummer+=1

# if a.__contains__("km"):
#     km_to_miles(a)
# elif a.__contains__("miles"):
#     miles_to_km(a)