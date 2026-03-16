class Solution:
    def removeSpecialCharacter(self, S):
        result = []
        for char in S:
            # Check if it falls within the lowercase or uppercase range
            if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
                result.append(char)
        if result == []:
            return -1
        return "".join(result)