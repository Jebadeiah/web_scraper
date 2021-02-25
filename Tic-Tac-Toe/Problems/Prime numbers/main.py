prime_numbers = [num for num in range(2, 1001) if all(num % div != 0 for div in range(2, num - 1))]
