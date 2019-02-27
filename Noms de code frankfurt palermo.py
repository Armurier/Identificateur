from time import sleep
frapal = {"thierry": "Néphron", "georges": "Sasuke", "may": "Decembre", "hala": "Etagere", "marilou": "Anaconda", "miali": "Freedom", "carlo": "Gringe", "bridi": "Salvitex", "cathia": "Amsterdam", "albert": "hurlu", "basma": "Riz", "marianasr": "Determination", "klink": "Benalla", "traboulsi": "mate20pro", "tripitch": "Freeze", "chalfoun": "Kechek", "sarah": "colle"}
listripitch = ('tripitch', 'tripiciano', 'frau tripiciano')
listhierry = ('jackje', 'thierry', 'thierry sokhn','thierry jack', 'thierry jack jean-marie', 'tjjmps')
def decodeur(code):
        if code in frapal:
            sleep(1)
            code2 = code.title()
            print(f"{code2} a pour nom de code {frapal[code]}")
            sleep(1)
        elif code in listhierry:
            sleep(1)
            code2 = code.title()
            print(f"{code2} a pour nom de code {frapal['thierry']}")
            sleep(1)
        elif code in listripitch:
            sleep(1)
            code2 = code.title()
            print(f"{code2} a pour nom de code {frapal['tripitch']}")
            sleep(1)
        else:
            sleep(1)
            code2 = code.title()
            print(f"{code2} n'a ou n'a toujours pas de nom de code")
            sleep(1.5)
while True:
    print("Quelle personne voulez-vous savoir parmi les gens du voyage")
    code = input()
    code = code.lower()
    decodeur(code)