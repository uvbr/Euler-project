

import fractions
 
def problem5(n):
    ans = 1   
    for i in range(1, n + 1):
        ans = (ans * i)/fractions.gcd(ans, i)        
    return ans
 
# main
n = 20
print problem5(n)