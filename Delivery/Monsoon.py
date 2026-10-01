import sys
import weatherdesk 

city = input()
base_price = float(input())
orders = int(input())
riders = int(input())

temp, rain = weatherdesk.weather_now(city)

if temp == -1.0 or rain == -1.0:
    print("could not reach sky.... either service is down or city name is not supported")
    sys.exit() 

pressure = int(orders / riders)

if rain > 0 and pressure > 3:
    surge = 1.5
    reason = "raining AND every rider is buried in orders"
elif rain > 0:
    surge = 1.3
    reason = "raining fewer riders want to go out"
elif temp >= 33 and pressure > 3:
    surge = 1.4
    reason = "heat wave AND riders are stretched thin"
elif temp >= 33:
    surge = 1.2
    reason = "heat wave nobody wants to step outside"
elif pressure > 4:
    surge = 1.25
    reason = "dry and pleasant, but demand is running ahead of riders"
else:
    surge = 1.0
    reason = "calm hour charge the normal price"

# Step 4: Work out the final price
final_price = base_price * surge

# Output: Exact format with pressure and price rounded to 2 decimal places
print(f"Temperature: {temp} C")
print(f"Rain: {rain} mm")
print(f"Orders per rider: {pressure:.2f}")
print(f"Surge: {surge}")
print(f"Reason: {reason}")
print(f"Price: {final_price:.2f}")
