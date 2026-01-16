def klasyfikacja_bmi(bmi):

    if bmi < 16.0:
        return "wygłodzenie", "minimalne, ale zwiększony poziom innych problemów"
    elif 16.0 <= bmi <= 16.99:
        return "wychudzenie", "minimalne, ale zwiększony poziom innych problemów"
    elif 17.0 <= bmi <= 18.49:
        return "niedowaga", "minimalne, ale zwiększony poziom innych problemów"
    elif 18.5 <= bmi <= 24.99:
        return "pożądana masa ciała", "minimalne"
    elif 25.0 <= bmi <= 29.99:
        return "nadwaga", "średnie"
    elif 30.0 <= bmi <= 34.99:
        return "otyłosc I stopnia", "wysokie"
    elif 35.0 <= bmi <= 39.99:
        return "otyłosc II stopnia (duża)", "bardzo wysokie"
    else:  # >= 40.0
        return "otyłosc III stopnia (chorobliwa)", "ekstremalny poziom ryzyka"


def oblicz_bmi(waga, wzrost, system):
    wynik = 0
    if system == 1:
        wynik = waga / (wzrost ** 2)
    elif system == 2:
        wynik = (waga / (wzrost ** 2)) * 703

    return wynik


def main():
    print("---KALKULATOR BMI---")
    print("Wybierz jednostki: 1 - Metryczne (kg, m), 2 - Imperialne (lb, in)")

    try:
        system = int(input("Twój wybór (1/2): "))
        if system not in [1, 2]:
            print("Niepoprawny wybór systemu.")
            return

        ile_osob = int(input("Ile osób chcesz wpisać?: "))
    except ValueError:
        print("To nie jest poprawna liczba.")

    wyniki = []

    for i in range(ile_osob):
        try:
            print(f"\n---OSOBA {i + 1}---")
            waga = float(input("Podaj wagę: "))
            wzrost = float(input("Podaj wzrost: "))

            if wzrost == 0:
                print("Wzrost nie może być zerem!")
                continue

            bmi = oblicz_bmi(waga, wzrost, system)
            kategoria, ryzyko = klasyfikacja_bmi(bmi)

            print(f"Twoje BMI: {bmi:.2f}")
            print(f"Status: {kategoria}, Ryzyko: {ryzyko}")

            wyniki.append([i + 1, round(bmi, 2), kategoria, ryzyko])

        except ValueError:
            print("Błąd wprowadzania danych.")

    with open("wyniki_bmi.txt", "w", encoding="utf-8") as plik:
        plik.write("ID, BMI, Kategoria, Ryzyko\n")
        for wiersz in wyniki:
            linia = f"{wiersz[0]}, {wiersz[1]}, {wiersz[2]}, {wiersz[3]}\n"
            plik.write(linia)

    print("\nZapisano wyniki do pliku wyniki_bmi.txt")

main()