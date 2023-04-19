import numpy as np
import mpmath
from mpmath import mp

# Set mpmath precision
mp.dps = 50

def zeta(s, n_terms=1000):
    """
    Compute the Riemann zeta function using the Euler-Maclaurin formula.
    :param s: Complex number input.
    :param n_terms: Number of terms to use for the Euler-Maclaurin formula.
    :return: Value of the Riemann zeta function at point s.
    """
    def bernoulli(n):
        """Compute the n-th Bernoulli number."""
        return mpmath.bernoulli(n)

    def euler_maclaurin_term(k, s):
        """Compute the k-th term of the Euler-Maclaurin formula."""
        B = bernoulli(2 * k) / (2 * k * mpmath.fac(2 * k))
        return mpmath.power(-1, k) * B * mpmath.power(s, -2 * k + 1) / (2 * k - 1)

    main_sum = sum([mpmath.power(n, -s) for n in range(1, n_terms + 1)])

    euler_maclaurin_sum = sum([euler_maclaurin_term(k, s) for k in range(1, n_terms + 1)])

    return main_sum + euler_maclaurin_sum

# Search for zeros of the Riemann zeta function with real part close to 1/2
for i in range(1, 100):
    s = mpmath.mpc(0.5, i)
    zeta_val = zeta(s)
    if abs(zeta_val) < 1e-10:
        print(f"Possible zero found near s = {s} with zeta(s) = {zeta_val}")

