Weather = {"Karachi":"Cloudy","Islamabad":"Rainy","Lahore":"Sunny"}
for i in Weather: #  will print key
    print(i)
print()
for city in Weather.keys():
    print(city)
print()
for weather in Weather.values():
   print(weather)
print()   
for city,weather in Weather.items():
  print(f"It is {weather} in {city}")
print()
