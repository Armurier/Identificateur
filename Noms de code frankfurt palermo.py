from time import sleep
from playsound import playsound
frapal = {
    "thierry": "Néphron",
    "georges": "Sasuke",
    "may": "Decembre",
    "hala": "Etagere",
    "marilou": "Anaconda",
    "miali": "Freedom",
    "carlo": "Gringe",
    "bridi": "Salvitex",
    "cathia": "Amsterdam",
    "albert": "hurlu",
    "basma": "Riz",
    "nasr": "Determination",
    "klink": "Benalla",
    "traboulsi": "mate20pro",
    "tripitch": "Freeze",
    "chalfoun": "Kechek",
    "sarah": "colle"
}
while True:
    print("Quelle personne voulez-vous savoir parmi les personnes du voyage")
    code = input()
    code = code.lower()
    def decodeur(code):
        if code in frapal:
            sleep(1)
            code2 = code.title()
            print(f"{code2} a pour nom de code {frapal[code]}")
            sleep(1)
    decodeur(code)