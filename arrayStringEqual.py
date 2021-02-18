class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        wrd1 = ""
        wrd2 = ""
        for i in range(len(word1)):
            wrd1 += str(word1[i])
        for i in range(len(word2)):
            wrd2 += str(word2[i])

        if wrd1 == wrd2:
            return True
        else:
            return False
        
