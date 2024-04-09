from BEGCD import *

def CRT(coprime_factors: list, a_i: list) -> mpz:
    """
    Implements the Chinese Remainder Theorem (CRT) for big integers.

    Args:
        coprime_factors: List of coprime factors (gmpy2.mpz).
        a_i: List of remainders (gmpy2.mpz).

    Returns:
        The solution (x) as a gmpy2.mpz integer.
    """

    n = mpz(1)
    N_i = []
    for factor in coprime_factors:
        a=mpz(1)
        for  factor1 in coprime_factors:
           if(factor1!=factor):
              a=mpz(a*factor1)
        N_i.append(a)
        n = mpz(n * factor)

    N_i_inverse = []

    for i in range(len(coprime_factors)):
        gcd, s, t = begcd(N_i[i], coprime_factors[i])  
        N_i_inverse.append(mpz(s))

    a = mpz(0)  # Initialization with gmpy2

    for i in range(len(coprime_factors)):
        a = Modn(mpz(a + a_i[i] * N_i[i] * N_i_inverse[i]),n)  
    return a  

# from EGCD import *

def test_CRT():
  """
  Tests the CRT function for various inputs.
  """
  # Test cases with different coprime factors and remainders
  test_cases = [
      ([3, 5], [2, 3], 8),  # x = 2 (mod 3), x = 3 (mod 5)
      ([7, 11], [1, 5], 71),  # x = 1 (mod 7), x = 5 (mod 11)
      ([2, 3, 5], [1, 0, 4], 9),  # x = 1 (mod 2), x = 0 (mod 3), x = 4 (mod 5)
  ]

  for coprime_factors, a_i, expected_result in test_cases:
    x = CRT(coprime_factors, a_i)
    print(f"Testing CRT({coprime_factors}, {a_i}):")
    print(f"  - Solution (x): {x} (expected: {expected_result})")
    
    # Verify solution using modulo operation (optional)
    # for i in range(len(coprime_factors)):
    #   assert (x % coprime_factors[i]) == a_i[i]

# Run the test function
test_CRT()