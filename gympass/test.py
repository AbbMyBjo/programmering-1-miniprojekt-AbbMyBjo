import random

felmeddelande = "Något gick fel. Stänger av programmet."
print("Välkommen till gympass-skaparen. Nedan kan du skriva vilka du har för krav på passet/passen jag ska göra åt dig.")

a = "överkropp"
b = 6
d = "medel"

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
        while i <= 6:
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
            exit
    counter+=1

if b < 1:
    print("Här är dina pass: ")
elif b == 1:
    print("Här är ditt pass: ")

passnummer = 1
for träningspass in flera_pass:
    print("pass "+ str(passnummer) + str(träningspass))
    passnummer+=1

# i = 0
# i2 = 0

# for listor in träningspass:
#     for övningar in träningspass[i]:
#         if träningspass[i].__contains__(träningspass[i2])


# if a.__contains__("km"):
#     km_to_miles(a)
# elif a.__contains__("miles"):
#     miles_to_km(a)