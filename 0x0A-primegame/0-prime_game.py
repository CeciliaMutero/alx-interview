#!/usr/bin/python3
def isWinner(x, nums):
    if x == 0 or not nums:
        return None
    
    max_n = max(nums)
    
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i]:
            for multiple in range(i * i, max_n + 1, i):
                sieve[multiple] = False
    
    prime_moves = [0] * (max_n + 1)
    
    for i in range(2, max_n + 1):
        prime_moves[i] = prime_moves[i - 1]
        if sieve[i]:
            prime_moves[i] += 1
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if prime_moves[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
