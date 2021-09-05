class Solution:
    def numDifferentIntegers(self, word):
        return len(set(x.lstrip('0') for x in re.findall(r'\d+', word)))