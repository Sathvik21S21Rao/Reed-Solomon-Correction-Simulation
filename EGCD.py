from math import floor
class EGCD:
    opt_s = []
    opt_t = []
    opt_r = []
    def egcd(self,a,b) ->list:
        # a , b = max(a,b) , min(a,b)
        self.opt_s.append(1)
        self.opt_s.append(0)
        
        self.opt_t.append(0)
        self.opt_t.append(1)
        
        self.opt_r.append(a)
        self.opt_r.append(b)
        while(self.opt_r[-1] != 0):
            q = floor(self.opt_r[-2]/self.opt_r[-1])
            r = self.opt_r[-2] - q * self.opt_r[-1]
            s = self.opt_s[-2] - q * self.opt_s[-1]
            t = self.opt_t[-2] - q * self.opt_t[-1]
            
            self.opt_r.append(r)
            self.opt_s.append(s)
            self.opt_t.append(t)
            
        return [self.opt_r[-2],self.opt_s[-2],self.opt_t[-2]]
            
def test_egcd():
  """
  Tests the egcd function for various inputs.
  """
  gcd1 , s , t= EGCD().egcd(355 , 213)
  gcd2 = s*355 + t*213
  print(gcd1,s,t)
  print(gcd2)

# Run the test function
# test_egcd()
