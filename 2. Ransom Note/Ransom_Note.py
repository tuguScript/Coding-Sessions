from collections import defaultdict


class Solution():
    def canSpell(self, mag, note):
        print(mag)
        mag = list(mag)
        print(mag)
        letters = defaultdict(int)
        for c in mag:
            letters[c] += 1
        for c in note:
            if(letters[c] <= 0):
                return False
            letters[c] -= 1
        return True


print(Solution().canSpell('abcdef', 'bed'))
# True
# print(Solution().canSpell('abcdef', 'cat'))
# False
