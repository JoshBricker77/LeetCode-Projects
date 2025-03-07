#Prime Number Generator
#get number
#divide number from 1 to current number and count divisors
#if total divisors = 2 is prime if it does not = 2 it is not prime
#print is prime or is not prime
number = input("Enter your number to check if prime")
number = int(number)
divisors = 0
if number != 2 or number % 2 == 0:
    for i in range(1, number + 1):
        if number % i == 0:
            divisors += 1
    if divisors == 2:
        print("number is prime")
    else:
        print("number is not prime")
elif number == 2:
    print("number is prime")
else:
    print("number is not prime")
