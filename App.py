principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than zero")
    else:
        break

while True:
    rate = float(input("Enter the interest rate amount: "))
    if rate < 0:
        print("interest rate can't be less zero")
    else:
        break

while True:
    time = float(input("Enter =the time in years: "))
    if time < 0:
        print("time can't be less than zero")
    else:
        break

print(principle)
print(rate)
print(time)

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: £{total:.2f}")
