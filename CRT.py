from EGCD import *

def CRT(coprime_factors : list , a_i : list) -> int:
    
    n=1
    for factor in coprime_factors:
        n = n*factor
    
    N_i = [n/factor for factor in coprime_factors]
    N_i_inverse = []
    
    for i in range(len(coprime_factors)):
        gcd  , s , t = EGCD().egcd(N_i[i],coprime_factors[i])
        N_i_inverse.append(s)
    
    a = 0
    
    for i in range(len(coprime_factors)):
        a = a+a_i[i]*N_i[i]*N_i_inverse[i]
    
    return int(a)

# from EGCD import *

def test_CRT():
  """
  Tests the CRT function for various inputs.
  """
  # Test cases with different coprime factors and remainders
  test_cases = [
      ([3, 5], [2, 3], 8),  # x = 2 (mod 3), x = 3 (mod 5)
      ([7, 11], [1, 5], -83),  # x = 1 (mod 7), x = 5 (mod 11)
      ([2, 3, 5], [1, 0, 4], 39),  # x = 1 (mod 2), x = 0 (mod 3), x = 4 (mod 5)
  ]

  for coprime_factors, a_i, expected_result in test_cases:
    x = CRT(coprime_factors, a_i)
    print(f"Testing CRT({coprime_factors}, {a_i}):")
    print(f"  - Solution (x): {x} (expected: {expected_result})")
    
    # Verify solution using modulo operation (optional)
    for i in range(len(coprime_factors)):
      assert (x % coprime_factors[i]) == a_i[i]

# Run the test function
# test_CRT()
