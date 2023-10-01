"""List of prime numbers generator."""

def primes(number_of_primes):
    if number_of_primes <=0:
        raise ValueError("Number of primes must be greater than zero.")

    list = []
    candidate = 2
    while len(list) < number_of_primes:
        is_prime = True
        for divisor in range(2,int(candidate**0.5) + 1):
            if candidate % divisor == 0:
                is_prime = False
                break
        if is_prime:
            list.append(candidate)
        candidate += 1
    return list