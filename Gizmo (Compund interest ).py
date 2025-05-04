import math

principle=0
rate=0
time=0

while True:
    principle=float(input("Enter the principle amount:"))
    if principle <0:
        print("The principle can't be less than zero")
    else:
        break


while True:
    rate =float(input("Enter the interest rate :"))
    if rate <0:
        print("The interest can't be less than zero")
    else:
        break

while True:
    time =int(input("Enter the time :"))
    if time <0:
        print("The time can't be less than or equal to zero")
    else:
        break

A=principle*pow((1+rate/100), 3)

print(f"Balance after {time} year/: R{A:.2f}")








