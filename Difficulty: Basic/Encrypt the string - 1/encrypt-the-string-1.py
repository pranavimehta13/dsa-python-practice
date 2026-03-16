class Solution:
    def encryptString(self, s):
        if not s:
            return ""
            
        result = []
        count = 1
        n = len(s)
        
        for i in range(n - 1):
            if s[i] == s[i+1]:
                count += 1
            else:
                # Store as "count then character"
                result.append(s[i] + str(count))
                count = 1
        
        # Add the last group
        result.append(s[-1] + str(count))
        
        # Join into a string and reverse the whole thing
        full_string = "".join(result)
        return full_string[::-1]