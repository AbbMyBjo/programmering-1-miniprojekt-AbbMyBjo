import random

felmeddelande = "Något gick fel. Stänger av programmet."
# print("Välkommen till gympass-skaparen. Nedan kan du skriva vilka du har för krav på passet/passen jag ska göra åt dig.")

# a = input("Vill du fokusera på någon/några speciella delar av kroppen? ")
# if a == "ja":
#     a = input("Ange helkropp/överkropp/underkropp eller en/flera specifika kroppsdelar. \n")
# elif a == "nej":
#     a = "helkropp"
# else:
#     print(felmeddelande+"rad12")
a = "underkropp"
# b = input("Hur många pass vill du att jag ska göra? ")
b = 5
# try:
#     b = int(b)
# except:
#     while 1:
#         print("Ange ett giltigt nummer.")
#         b = input("Hur många pass vill du att jag ska göra? ")
#         try:
#             b = int(b)
#             break
#         except:
#             continue

# if b == 1:
#     d = input("Hur hårt ska passet vara? Välj mellan väldigt lätt, lätt, medel och intensivt. ")
# elif b > 1:
#     d = input("Hur hårda ska passen vara? Välj mellan väldigt lätt, lätt, medel och intensivt. ")
#     #e = input("Ska jag göra ett veckoschema för passen? ")
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

flera_pass = [ ]

i = 0
counter = 1

while counter <= b:
    i = 0
    x = 0
    y = 0

    print("Efter while")
    print(a)

    ettpass = []
    gympass_siffror = []

    if a == "helkropp":
        print("61")
        for keys in Gymövningar:
            EnNyÖvning = random.randrange(0, len(Gymövningar[i]["övningar"]))
            gympass_siffror.append(EnNyÖvning)
            i+=1

        gympass_bokstäver = []
        
        print("73")

        for keys in gympass_siffror:
            print(gympass_siffror)
            plats = (gympass_siffror[x])
            övning = Gymövningar[y]["övningar"][plats]
            x+=1
            y+=1
            gympass_bokstäver.append(övning)
        print("80")

        if d == "lätt":
            for keys in gympass_bokstäver:
               ettpass.append(keys+" 2x10")
            flera_pass.append(ettpass)
            print("85")

        elif d == "medel":
            for keys in gympass_bokstäver:
                ettpass.append(keys+" 3x10")
            flera_pass.append(ettpass)
            print("90")

        elif d == "intensivt":
            nyövning = random.randrange(0, len(Intensivt))
            gympass_siffror.append(Intensivt[nyövning])
            gympass_bokstäver.append(gympass_siffror[-1]) 
            for keys in gympass_bokstäver:
                ettpass.append(keys+" 3x15")
            flera_pass.append(ettpass)
            print("98")

        elif d == "väldigt lätt":
            for keys in gympass_bokstäver:
                ettpass.append(keys+" x10")
            flera_pass.append(ettpass)
            print("103")

        else:
            print(felmeddelande)
            exit
        i+=1
        counter+=1

    elif a == "överkropp":
        print("116")
        while i <= 6:
            a = random.randrange(0, len(Gymövningar[i]["övningar"]))
            gympass_siffror.append(a)

        x = 0
        y = 0

        gympass_bokstäver = []

        for saker in gympass_siffror:
            plats = (gympass_siffror[x])
            övning = Gymövningar[y]["övningar"][plats]
            x+=1
            y+=1
            gympass_bokstäver.append(övning)
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
        i+=1
        counter+=1

    elif a == "underkropp":
        print("168")
        while i <= 6:
            a = random.randrange(0, len(Gymövningar[6]["övningar"]))
            b = random.randrange(0, len(Gymövningar[7]["övningar"]))
            gympass_siffror.append(a)
            i += 1
            gympass_siffror.append(b)
            i += 1
            print(gympass_siffror)

        x = 0
        i = 0
        gympass_bokstäver = []

        while i <= len(gympass_siffror):
            plats = (gympass_siffror[x])
            övning = Gymövningar[6]["övningar"][plats]
            övning2 = Gymövningar[7]["övningar"][plats]
            x+=1
            # övning = Gymövningar[7]["övningar"][plats]
            # x+=1
            gympass_bokstäver.append(övning)
            gympass_bokstäver.append(övning2)

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

    else:
        print(felmeddelande+"2")
        break
    i+=1
    counter+=1

#if b = 1:
#print("Här är ditt pass: ")#
#else:
#print("Här är dina pass:")

passnummer = 1
for träningspass in flera_pass:
    print("pass "+ str(passnummer) + str(träningspass))
    passnummer+=1
#redigera if-satserna så alla inputs blir inkluderade innan fortsättning
#samma sak som innan med underkropp och olika kroppsdelar
#variera kroppdel man tränar, inte alltid samma om typ 6 pass