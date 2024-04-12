if __name__=="__main__":
   from arithmeticOps import *
   from BEGCD import begcd
else:
    from HelperFunctions.arithmeticOps import *
    from HelperFunctions.BEGCD import *

from gmpy2 import mpz

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
if __name__ == "__main__":
    # x=CRT([10159, 21929, 26683, 43801, 45389, 47093, 52313, 52387, 68473, 74587, 81031, 83873, 96199, 109661, 122651, 140069, 159349, 174431, 211333, 219547, 233417, 242309, 250057, 252823, 255209, 257993, 258329, 267913, 272381, 273253, 277421, 278671, 284161, 285539, 293087, 297079, 304259, 306041, 317609, 323473, 339071, 408427, 429211, 457403, 462491, 462499, 469411, 473327, 473743, 482093, 497869, 536491, 558497, 571783, 581137, 582677, 596147, 604931, 614377, 628973, 660917, 661121, 669913, 683699, 685319, 695059, 736097, 752809, 756023, 761897, 779609, 792377, 801989, 807077, 824231, 845657, 858101, 858463, 862727, 868033, 871303, 893383, 894749, 902413, 903541, 910621, 912853, 916177, 918347, 928307, 933209, 935581, 959143, 965533, 967999, 975643, 977057, 980401, 987509, 999389],[7362, 2189, 20302, 14635, 12562, 43509, 12908, 18577, 49323, 53284, 62742, 44368, 91773, 79572, 33440, 119963, 127915, 49347, 108867, 186344, 121474, 127395, 98031, 74148, 85085, 81739, 15750, 205347, 240154, 141760, 175102, 78071, 9419, 129086, 77609, 27236, 135847, 237547, 317419, 76270, 58610, 161941, 319331, 277455, 65251, 461241, 232860, 161859, 340568, 413619, 43619, 228513, 403910, 127666, 262097, 15513, 232973, 231383, 261640, 214036, 465258, 501171, 307333, 345397, 222225, 371699, 728016, 82685, 484128, 486393, 633473, 247950, 521602, 416515, 257549, 80245, 130763, 722143, 826700, 273527, 186629, 166347, 358700, 610294, 654876, 306202, 177946, 389458, 399781, 311556, 474966, 86194, 288140, 808885, 541045, 422086, 521884, 431013, 37990, 561972])
    # print(x)
   test_CRT()