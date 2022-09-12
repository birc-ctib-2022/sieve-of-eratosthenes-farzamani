"""Computing primes."""


def sieve(n: int) -> list[int]:
    """
    Compute all the primes up to (and possibly including) `n`.

    `n` must be positive.

    >>> sieve(15)
    [2, 3, 5, 7, 11, 13]

    """
    assert n > 0
    candidates = list(range(2, n + 1))
    primes = []

    # FIXME: fill out this bit

    # first candidate is prime
    prime = candidates.pop(0)
    primes.append(prime)

    # invariant
    n = len(candidates)

    while n > 0:
        p = candidates.pop(0)
        prime_check = [p % prime for prime in primes]
        if 0 not in prime_check:
            primes.append(p)
        else:
            pass

        # loop breaks if n = 0
        n = len(candidates)

    return primes
