def meterToFeet(Meters):
    return Meters * 1 / .3048

def gramToPound(Grams):
    return Grams * .002205

def celsiusToFarenheit(Celsius):
    return 32 + 1.8 * Celsius


conv = int(input())

for i in range(conv):
    enter = input().split(' ')
    mesure = float(enter[0])

    if enter[1] == "m":
        print(meterToFeet(mesure), "p")
    elif enter[1] == "g":
        print(gramToPound(mesure), "l")
    elif enter[1] == "c":
        print(celsiusToFarenheit(mesure), "f")
