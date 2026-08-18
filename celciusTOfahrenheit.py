def celcius():
    fah=((9/5)*cel)+32
    return fah

cel=float(input("Enter celcius : "))

print(f"{cel} into fahrenheit is {celcius():.2f}")