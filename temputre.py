temp=int(input("Enter the temperature in fahrenheit:"))

def check_temperature(temp):
    if temp >= 85:
        print("Its hot outside")
    elif 60 <= temp <=85:
        print("its nice outside")
    else:
        print("It's cold outside")
result = check_temperature(temp)
print(result)
