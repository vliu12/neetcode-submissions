class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = dict()
        for i in range(26):
            letter = order[i]
            rank[letter] = i

        def isOrdered(word1, word2): #return true iff word1 comes lexicographically before word2
            if word1.startswith(word2):
                return False
            if word2.startswith(word1):
                return True

            length = min(len(word1), len(word2))

            for i in range(length):
                l1 = word1[i]
                l2 = word2[i]
                counter = 0

                if (l1 == l2): 
                    continue

                return rank[l1] < rank[l2]

        
        for i in range(len(words) - 1):
            if not isOrdered(words[i], words[i+1]):
                print(words[i], words[i+1])
                return False

        return True
