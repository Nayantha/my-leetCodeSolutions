def solution(n):
    str_len = n
    max_int = int(str_len * (5000 / 2465) + 475)
    primes = [True] * max_int
    primes[0] = primes[1] = False

    for number, is_prime in enumerate(primes):
        if is_prime and number < max_int ** .5:
            multiple_list = list(range(number, max_int, number))
            multiple_list.remove(number)
            for multiple in multiple_list:
                primes[multiple] = False
    prime_str = "".join([str(x) for x, y in enumerate(primes) if y])
    return prime_str[n:n+5]
    
def prime():
    max = 3
    primes = [True] * max
    primes[0] = primes[1] = False
    
    for number, is_prime in enumerate(primes):
        if is_prime and number < max ** .5:
            multiple_list = list(range(number, max, number))
            multiple_list.remove(number)
            for multiple in multiple_list:
                primes[multiple] = False
            
            # for multiple in range(number ** 2, max, number):
            #     primes[multiple] = False
    
    for number, is_prime in enumerate(primes):
        if is_prime:
            print("{:>3}".format(number), end=" ")
        else:
            print("{:>3}".format(" "), end="")
        if number % 10 == 0 and number != 0:
            print("")
    
    prime_str = "".join([str(x) for x, y in enumerate(primes) if y])
    print(prime_str)

print(solution(3))
