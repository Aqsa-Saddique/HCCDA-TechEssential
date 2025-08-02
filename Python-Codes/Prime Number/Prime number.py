# Prime number checker

# Input from user
num = int(input("Enter a number: "))

# Check if number is greater than 1
if num > 1:
    # Check for factors
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
