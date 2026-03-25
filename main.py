name = input("Enter driver name: ")
destination = input("Enter destination: ")
distance = float(input("Enter distance (km): "))
consumption = float(input("Enter fuel consumption: "))
price = float(input("Enter fuel price: "))

fuel_cost = (distance / 100) * consumption * price

if distance < 100:
    category = "Short trip"
elif distance < 500:
    category = "Medium trip"
else:
    category = "Long trip"

print("Driver :", name)
print("Destination :", destination.upper())
print("Distance :", distance, "km")
print("Fuel cost :", fuel_cost,"KZT")
print("Category :", category)


print("Cost breakdown:")
for i in range(100, int(distance)+1, 100):
    cost = (i / 100) * consumption * price
    print(i, "km →", cost)


print("Destination Uppercase:", destination.upper())
print("Destination lowercase:", destination.lower())
print("Length:", len(destination))
print("Letter a:", destination.lower().count("a"))

