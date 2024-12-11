#!/usr/bin/python3


def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes_up_to(n):
    """Get list of primes up to n."""
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def isWinner(x, nums):
    """
    Determine who wins the prime game more rounds.
    
    Args:
        x (int): number of rounds
        nums (list): array of n for each round
    
    Returns:
        str: 'Maria' or 'Ben' or None
    """
    if not nums or x < 1:
        return None
    
    maria_wins = 0
    ben_wins = 0
    
    # For each round
    for n in nums[:x]:
        if n < 2:
            ben_wins += 1
            continue
            
        # Get primes up to n
        primes = get_primes_up_to(n)
        
        # If number of primes is even, Ben wins
        # If number of primes is odd, Maria wins
        if len(primes) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
