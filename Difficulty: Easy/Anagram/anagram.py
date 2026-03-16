class Solution:
    def areAnagrams(self, s1, s2):
        n = len(s1)
        m = len(s2)
        if n != m:
            return False
        count_map = {}
        for char in s1:
            count_map[char] = count_map.get(char,0) + 1
        for char in s2:
            if char not in count_map:
                return False
            else:
                count_map[char] -= 1
            if count_map[char] < 0:
                return False
        return True
                