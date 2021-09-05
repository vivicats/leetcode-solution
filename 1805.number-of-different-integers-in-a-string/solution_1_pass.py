    def numDifferentIntegers(self, word: str) -> int:
        res, startIndex = set(), 0
        for i, c in enumerate(word):
            if c.isdigit():
                if startIndex < i and word[startIndex] == '0':
                    startIndex += 1
            else:
                if startIndex < i:
                    res.add(word[startIndex:i])
                startIndex = i + 1

        if startIndex < len(word):
            res.add(word[startIndex:])
        return len(res)