import random

felmeddelande = "Något gick fel. Stänger av programmet."
print("Välkommen till gympass-skaparen. Nedan kan du skriva vilka du har för krav på passet/passen jag ska göra åt dig.")

a = "bål"
b = 5
d = "lätt"

Gymövningar = [
        {"namn": "biceps", "övningar":["skivstångscurl", "hantelcurl", "hammercurl", "chins", "preacher curls", "sittande bicepscurls", "koncentrationscurl"]},
        {"namn": "bröst", "övningar":["bänkpress", "hantelpress", "lutande bänkpress/hantelpress", "breda armävningar", "smal bänkpress", "kryssdrag", "pec deck", "bröstpress"]},
        {"namn": "mage", "övningar":["kabelcrunch", "hängande benlyft/benlyft", "kabelrotationer", "alternerande hälnuddningar", "cykelcrunch", "plankan", "fällkniven", "crunches"]},
        {"namn": "triceps", "övningar":["dips", "sittande dips", "triceps press med hantel", "skullcrushers", "french press", "triceps pushdown", "smal bänkpress", "smala armhävningar"]},
        {"namn": "rygg", "övningar":["marklyft", "hyperextension", "pullups", "sittande kabelrodd", "latsdrag", "hantelrodd", "rygglyft", "stångrodd"]},
        {"namn": "axlar", "övningar":["axelpress skivstång", "axelpress hantlar", "arnoldpress", "sidolyft", "face pull", "pullups", "dumbbell shrug", "kabelrotationer"]},
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

    elif a == "underkropp":
        print("88")
        while i <= 6:
            ÖvningEtt = random.randrange(0, len(Gymövningar[6]["övningar"])-1)
            ÖvningTvå = random.randrange(0, len(Gymövningar[7]["övningar"])-1)
            gympass_siffror.append(ÖvningEtt)
            i += 1
            gympass_siffror.append(ÖvningTvå)
            i += 1
            print(gympass_siffror)

        x = 0
        i = 1
        y = 0

        while i <= len(gympass_siffror):
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
        print("90")
        inte = 0
        while inte < 6:
            ÖvningEtt = random.randrange(0, len(Gymövningar[2]["övningar"]))
            ÖvningTvå = random.randrange(0, len(Gymövningar[4]["övningar"]))
            gympass_siffror.append(ÖvningEtt)
            gympass_siffror.append(ÖvningTvå)
            inte += 2
            print(gympass_siffror)

        x = 0
        i = 1
        y = 0
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
    print("88")


if int(b) <= 2:
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
# for listor in flera_pass:
#     i4 = 0
#     print(flera_pass[i3])
#     i3 += 1
#     for övning in flera_pass[i3][i4]:
#         poppat_värde = flera_pass[i3].pop(i4)
#         print("279")
#         if poppat_värde in flera_pass[i3]:
#             print("280")
#             tabortindex = flera_pass[i3].index(poppat_värde) #GÖR OM LOOPEN!!!!!!!!!!!!!!
#             print("280")
#             flera_pass[i3].pop(tabortindex)
#             i4 += 1
#             print(i4)
#             print(flera_pass[i3])
#         elif i4 == len(flera_pass[i3]):
#             break
#         elif i4 == len(flera_pass[i3]):
#             break
#         else:
#             i4+=1
#         flera_pass[i3].append(poppat_värde) 

passnummer = 1
for träningspass in flera_pass:
    print("pass "+ str(passnummer) + str(träningspass))
    passnummer+=1

# if a.__contains__("km"):
#     km_to_miles(a)
# elif a.__contains__("miles"):
#     miles_to_km(a)
# kör debug programmet