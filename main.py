import requests
import random

def haal_woorden_op():
    url = 'https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english.txt'
    response = requests.get(url)
    woorden = response.text.splitlines()
    # Filter woorden: alleen letters, lengte tussen 4 en 10
    woorden = [w.lower() for w in woorden if w.isalpha() and 4 <= len(w) <= 10]
    return woorden

def galgje():
    woorden = haal_woorden_op()
    woord = random.choice(woorden)
    geraden_letters = set()
    pogingen = 6

    print("Welkom bij Galgje!")
    print(f"Het woord heeft {len(woord)} letters. Het is een Engels woord")

    while pogingen > 0:
        # Toon woord met streepjes of letters
        display_woord = ' '.join([letter if letter in geraden_letters else '_' for letter in woord])
        print("\nWoord:", display_woord)

        # Vraag om letter
        gok = input("Raad een letter: ").lower()
        if len(gok) != 1 or not gok.isalpha():
            print("Voer alsjeblieft één letter in.")
            continue

        if gok in geraden_letters:
            print("Die letter heb je al geraden.")
            continue

        geraden_letters.add(gok)

        if gok in woord:
            print("Goed geraden!")
        else:
            pogingen -= 1
            print(f"Fout! Pogingen over: {pogingen}")

        # Check of alles geraden is
        if all(letter in geraden_letters for letter in woord):
            print(f"Gefeliciteerd! Je hebt het woord '{woord}' geraden.")
            break
    else:
        print(f"Game over! Het woord was '{woord}'.")

if __name__ == "__main__":
    galgje()
