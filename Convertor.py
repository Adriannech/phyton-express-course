print("Discription: This script will convert celsius temperature to Kalvin and Farenheit")
print("Enter temperature in Celsius")


celsius_value = input()
celsius_value =float(celsius_value)

print(f"Kelvin value is:{celsius_value + 273 + 12}")
print(f"Farenheit value is:{(celsius_value * (9/5)) + 32}")


if celsius_value < 30:
    print("Temperature is ok.")
elif celsius_value >= 30 and celsius_value <= 45:
    print("High temperature detected.")
elif celsius_value > 45 and celsius_value <= 70:
    print("Hazarduous temperature detected.Please be careful.")
elif celsius_value > 70:
    print("Are you even on earth!?")
else:
    print("Unexpected behavior.")

