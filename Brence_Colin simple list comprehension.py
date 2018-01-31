#list comprehension for finding cubes of prime numbers in range 2 to 100 (1 is not a prime number)
#x**3 cubes numbers in range; if all statement specifies to find only primes in range
cube_prime_numbers = [x**3 for x in range(2,100)
           if all (x % num !=0 for num in range(2,x))]

#display output
print (cube_prime_numbers)
