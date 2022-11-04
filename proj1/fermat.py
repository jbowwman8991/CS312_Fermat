import random

def prime_test(N, k):
	# This is main function, that is connected to the Test button. You don't need to touch it.
	return fermat(N,k), miller_rabin(N,k)   # O(kn^3 + kn^4)
    # Space Complexity is O(k + kn).

def mod_exp(x, y, N):
    # This is the modular exponentiation funciton that calculates modular exponentiation.
    # Everything below is O(n)
    if y == 0:                              # O(n)
        return 1                            # c
    z = mod_exp(x, y//2, N)                 # O(n^2)
    if y % 2 == 0:                          # c
        return ((z**2) % N)                 # O(n^2)
    else:                                   
        return (x * (z**2) % N)             # O(n^2)
    # Entire function is O(nn^2 + c) = O(n^3).
    # Space Complexity is O(1), no additional space is created. 

def fprobability(k):
    # This is the function that calculates the probability that k Fermat trials give you the correct answer.
    return (1 - 0.5**k)                     # O(k)
    # Space Complexity is O(1), no additional space is created. 

def mprobability(k):
    # This is the function that calculates the probability that k Miller-Rabin trials give you the correct answer.
    return (1 - 0.25**k)                    # O(k)
    # Space Complexity is O(1), no additional space is created. 

def fermat(N,k):
    # This is the fermat function that runs a primality test k times to test if N is prime or composite. 
    for i in range(1, k):                   # O(k)
        a = random.randint(1, N - 1)        # O(n)
        if mod_exp(a, N-1, N) == 1:         # O(n^3)
            continue                        # c
        else:
            return 'composite'              # c
    return 'prime'                          # c
    # Entire function is O(kn^3 + c) = O(kn^3).
    # Space Complexity is O(k).

def miller_rabin(N,k):
    # This is the miller rabin function that runs a primality test k times to test if N is prime or composite. 
    # It also takes into account carmichael numbers and knows that they exist and are composite. 
    if N == 2:                              
        return 'prime'                      # c
    if N % 2 == 0:                          # O(n^2)
        return 'composite'                  # c
    r, s = 0, N - 1                         # c
    while s % 2 == 0:                       # log(n)
        r += 1                              # O(n)
        s //= 2                             # O(n^2)
    for i in range(1, k):                   # O(k)
        a = random.randint(2, N - 1)        # O(n)
        x = mod_exp(a, s, N)                # O(n^3)
        if x == 1 or x == N - 1:            # c
            continue                        # c
        for j in range(r - 1):              # O(n)
            x = mod_exp(x, 2, N)            # O(n^3)
            if x == N - 1:                  # c
                break                       # c
        else:
            return 'composite'              # c
    return 'prime'                          # c
    # Entire function is O(n^2 + log(n)nn^2 + knn^3 + nn^3) = O(kn^4)
    # Space Complexity is O(kn).