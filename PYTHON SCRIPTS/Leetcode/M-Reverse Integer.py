class Solution:
    def reverse(self, x: int) -> int:
        if x>0: x = int(''.join(reversed([i for i in str(x)])))
        else: x = -int(''.join(reversed([i for i in str(abs(x))]))) 
        return x if x<=2**31 - 1 and x>= -2**31 else 0
'''
Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
'''