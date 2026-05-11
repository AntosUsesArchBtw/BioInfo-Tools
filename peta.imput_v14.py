import time

def menu():
    print("\n" + "🧬" * 15)
    print("  ANALIZATOR DNA v4.0  ")
    print("🧬" * 15)
    print("1. Raport stabilności")
    print("2. Wczytaj nową sekwencję")
    print("3. Wyjście")

dna = "ATGGAAACCAACAACCCGTACGCTCGTGGTCCT"

while True:
    menu()
    wybor = input("\n[1,2 ALBO 3]> ")  # ← usunięto "2"

    if wybor == "1":
        print("Analizuję sekwencję...", end="")
        for _ in range(10):
            time.sleep(0.1)
            print(".", end="", flush=True)

        gc = (dna.count('G') + dna.count('C')) / len(dna) * 100
        print(f"\n[!] Wynik: {round(gc, 2)}% GC")
        print(f"[!] Status: {'STABILNY' if gc > 50 else 'ELASTYCZNY'}")

    elif wybor == "2":
        raw = input("Wklej DNA: ")
        dna = "".join(filter(lambda x: x in "ATGCatgc", raw)).upper()
        print(f"[OK] Baza zaktualizowana ({len(dna)} bp)")

    elif wybor == "3":
        print("\n[INFO] Zamykanie systemów Antoś-Tech...")
        break


