
def CelToFah(x):
    return (x * 1.8) + 32
def FahToCel(x):
    return (x - 32) * 0.5556
def MeterToMile(x):
    return x / 1.8
def MileToMeter(x):
    return x * 1.8


print("Select your method")
print("1.Celsius to Fahrenheid")
print("2.Fahrenheid to Celsius")
print("3.Kilometers to Miles")
print("4.Miles to Kilometers")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        number = float(input("Enter your number to convert: "))

        if choice == '1':
            print(f"{number} °C = ", CelToFah(number), "°F")
        elif choice == '2':
            print(f"{number} °F = ", FahToCel(number), "°C")
        elif choice == '3':
            print(f"{number} KM = ", MeterToMile(number), "Miles")
        elif choice == '4':
            print(f"{number} Miles = ", MileToMeter(number), "KM")

        again = input("Do you want to keep going?: ")
        if again == 'no':
            break

    else:
        print("Invalid input")