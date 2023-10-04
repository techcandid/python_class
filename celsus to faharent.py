def celsius_to_fahreheit(celsius):
   fahreheit = (celsius * 9/5) + 32
   return fahreheit
#test to function with three different temperature

temperature1 = 76.00
temperature2 = 23.54
temperature3 = 12.87

converted_tem1 = celsius_to_fahreheit(temperature1)
converted_tem2 = celsius_to_fahreheit(temperature2)
converted_tem3 = celsius_to_fahreheit(temperature3)

print(f"{temperature1} degree celsius is equal to {converted_tem1}")
print(f"{temperature1} degree celsius is equal to {converted_tem2}")
print(f"{temperature1} degree celsius is equal to {converted_tem3}")
