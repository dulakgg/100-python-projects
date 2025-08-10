
def km_to_miles():
    distance = input("Whats the distance (km)?\n>>> ")
    miles = float(distance) * 0.62137
    print(f"{distance} km is {miles} miles")

def celsius_to_fahrenheit():
    temperature = input("What's the temperature in celsius?\n>>> ")
    fahrenheit = (float(temperature) * 1.8) + 32
    print(f"{temperature} in fahrenheit is {fahrenheit}")

choice = input("What do you want to convert? \n1. km to miles \n2. celsius to fahrenheit\n>>> ")
if choice == 1:
    km_to_miles()
else:
    celsius_to_fahrenheit()