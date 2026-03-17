class Solution:
    def areIsomorphic(self, s1, s2):
        # code here
        if len(s1) != len(s2):
            return False
        s1_map = {}
        s2_map = {}
        for char1, char2 in zip(s1,s2):
            if char1 in s1_map:
                if s1_map[char1] != char2:
                    return False
            else:
                s1_map[char1] = char2
            if char2 in s2_map:
                if s2_map[char2] != char1:
                    return False
            else:
                s2_map[char2] = char1
        return True
            