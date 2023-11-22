class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        k = len(word1)
        d = len(word2)
        list = []
        if k <= d:
            for i in range(0, k):
                list.append(word1[i])
                list.append(word2[i])
            if k < d:
                list.append(word2[k:])
            return(''.join(list))
        if d <= k:
            for i in range(0, d):
                list.append(word1[i])
                list.append(word2[i])
            if d < k:
                list.append(word1[d:])
            return(''.join(list))

#merges two words together