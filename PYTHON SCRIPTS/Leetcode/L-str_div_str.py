class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        dic = {}
        list1 = []
        if str1 in str2:
            for n in str1:
                dic[n] = dic.get(n, 0) + 1
            for n in str2:
                dic[n] = dic.get(n, 0) + 1
            print(dic)
            for k,v in dic.items():
                if v == 1:
                    return('')
                list1.append(k)              
            return(''.join(list1))
        else:
            print('error')
            return('')

m = Solution()
m.gcdOfStrings(
"TAUXXTAUXXTAUXXTAUXXTAUXX", 
"TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
)