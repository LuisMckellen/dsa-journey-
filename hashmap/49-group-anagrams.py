class Solution:
    def groupAnagrams(self, strs):
        from collections import defaultdict
        groups = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - 97] += 1
            groups[tuple(count)].append(word)
        return list(groups.values())
