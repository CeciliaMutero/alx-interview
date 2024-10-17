#!/usr/bin/python3
"""
This module defines a function that simulates a prime
number game between Maria and Ben.
"""

def isWinner(x, nums):
    """
    Determines the winner
    of the prime number game.
    """
    if x <= 0 or not nums:
        return None

    def sieve_of_eratosthenes(n):
        """Find all prime numbers up to n using the
        Sieve of Eratosthenes."""
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        return [i for i in range(2, n + 1) if sieve[i]]

    max_num = max(nums)
    primes_up_to_max = sieve_of_eratosthenes(max_num)

    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if i in primes_up_to_max else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
