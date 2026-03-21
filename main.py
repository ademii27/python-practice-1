# Step a) Input & Variables
driver_name = input("Enter driver name: ")
distance = float(input("Enter distance (km): "))
consumption = float(input("Enter fuel consumption (L/100km): "))
fuel_price = float(input("Enter fuel price (KZT/L): "))

# Step b) Calculations
litres_needed = distance * consumption / 100
fuel_cost = litres_needed * fuel_price
cost_per_km = fuel_cost / distance

# Step c) Formatted Output
print("=" * 30)
print("ROAD TRIP SUMMARY")
print("=" * 30)
print(f"Driver : {driver_name}")
print(f"Distance : {distance:.1f} km")
print(f"Consumption : {consumption:.1f} L/100km")
print(f"Fuel price : {fuel_price:.1f} KZT/L")
print("-" * 30)
print(f"Litres needed: {litres_needed:.1f} L")
print(f"Fuel cost : {fuel_cost:.1f} KZT")
print(f"Cost per km : {cost_per_km:.1f} KZT")
print("=" * 30)

# Step d) Comparison
print("Trip longer than 300 km:", distance > 300)
print("Fuel cost above 5000 KZT:", fuel_cost > 5000)
