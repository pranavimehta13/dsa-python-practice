#User function Template for python3

class Solution:
    def removeChars (ob, str1, str2):
        # code here fo
        result = []
        for char in str1:
            if char not in str2:
                result.append(char)
        return "".join(result)