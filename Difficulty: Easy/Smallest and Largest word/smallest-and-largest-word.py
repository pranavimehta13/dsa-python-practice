class Solution:
    def smallerAndLarge(self, s):
        words = s.split()
        if not words:
            return ["", ""]
            
        # Initialize both with the first word
        smallest = words[0]
        largest = words[0]
        
        for w in words:
            # Check for the absolute smallest
            if len(w) < len(smallest):
                smallest = w
            # Check for the absolute largest
            # Using >= if you want the *last* longest word found
            if len(w) >= len(largest):
                largest = w
                
        return [smallest, largest]