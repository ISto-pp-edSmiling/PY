class Solution:
    def buddyStrings(self, s: str, g: str) -> bool:
        if len(g)!=len(s): return False
        a=0
        for i in range(len(s)):
            if s[i] == g[a]: a+=1
            else:
                b=a+1
                if i == len(s)-1: return False
                for l in range(i+1, len(s)):
                    if s[l] != g[b]:
                        s=[c for c in s]
                        s[l],s[i]=s[i],s[l]
                        return ''.join(s)==g
                    b+=1
        a=0
        while a!=len(s):
            for b in range(a+1, len(s)):
                if s[b]==s[a] and g[b]==g[a]: return True
            a+=1
        return False
    
# Input: s = "ab", goal = "ba"
# Output: true
# Explanation: You can swap s[0] = 'a' and s[1] = 'b'
# to get "ba", which is equal to goal.