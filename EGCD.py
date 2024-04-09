from math import floor
from gmpy2 import mpz

class EGCD:
    opt_s = []
    opt_t = []
    opt_r = []
    def egcd(self, a: int, b: int) -> list:
        # Ensure a is always greater than or equal to b
        # a, b = max(a, b), min(a, b)
        self.opt_s.append(mpz(1))  # Use gmpy2.mpz for big integers
        self.opt_s.append(mpz(0))

        self.opt_t.append(mpz(0))
        self.opt_t.append(mpz(1))

        self.opt_r.append(mpz(a))  # Use gmpy2.mpz for big integers
        self.opt_r.append(mpz(b))

        while(self.opt_r[-1] != 0):
            # Use integer division with // to avoid floating-point issues
            q = mpz(self.opt_r[-2] // self.opt_r[-1])
            r = mpz(self.opt_r[-2] - q * self.opt_r[-1])
            s = mpz(self.opt_s[-2] - q * self.opt_s[-1])
            t = mpz(self.opt_t[-2] - q * self.opt_t[-1])

            self.opt_r.append(r)
            self.opt_s.append(s)
            self.opt_t.append(t)

        return [self.opt_r[-2], self.opt_s[-2], self.opt_t[-2]]

def test_egcd():
  """
  Tests the egcd function for various inputs, including very large numbers.
  """
  gcd1, s, t = EGCD().egcd(9999999999999999999999999999999999999999988888878, 1234567890098765432112345123456789009876543211234416)
  # Corrected validation:
  gcd2 = s * 9999999999999999999999999999999999999999988888878 + t * 1234567890098765432112345123456789009876543211234416
  print(gcd1, s, t)
  print(gcd2)

# Run the test function
# test_egcd()
