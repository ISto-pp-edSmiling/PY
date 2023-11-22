class Solution:
    def reverseVowels(self, s: str) -> str:
        v = 'aeiouAEIOU'
        s = list(s)
        start, end = 0, len(s) - 1

        while start < end:
            if s[start] in v and s[end] in v:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            elif s[start] in v: 
                end -= 1
            else:
                start += 1
        
        return ''.join(s)
    
    # reverses the vowels
    
    # when you input 'leetcode' it works because the first 'e' gets replacwed by the second 'e'