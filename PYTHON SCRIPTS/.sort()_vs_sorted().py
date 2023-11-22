#this is a code that calc if something is an anagram, using sorted() and .sort():

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        gam = sorted(t)
        mag = sorted(s)
        print(gam)
        print(mag)
        if gam == mag:
            print(True)
        else:
            print(False)

m = Solution()
m.isAnagram('anagram', 'naagram')

print('===Next===')
#.sort() use when something is already a list (it also destroys the original list, returning None)

class Gun:
    def isAnagram(self, s: str, t: str) -> bool:
        gam = s.split().sort()
        mag = t.split().sort()
        print(gam)
        print(mag)
        if gam == mag:
            print(True)
        else:
            print(False)

m = Gun()
m.isAnagram('anagram', 'naagram')