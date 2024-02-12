def is_prime(number):
    if number < 2:
        return False
    
    for i in range(2, number):
        # If number is divisible by any number in this range, it's not prime
        if number % i == 0:
            return False     
    # If no divisor found in the loop, number is prime
    return True 


def getPrimeNumbers(n):
    prime_numbers = []  # Initialize an empty list
    for num in range(2, n+1):
        # Check if the current number is prime using the is_prime function
        if is_prime(num):
            # If it's prime, add it to the prime_numbers list
            prime_numbers.append(num)
    return prime_numbers

# Set the value of n
n = 8
prime_numbers = getPrimeNumbers(n)
print("Prime numbers between 2 and", n, ":", prime_numbers)


