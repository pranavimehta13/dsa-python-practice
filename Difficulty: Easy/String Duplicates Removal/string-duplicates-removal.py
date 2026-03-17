#User function Template for python3
class Solution:
	def removeDuplicates(self, s):
	    freq_map = {}
	    for char in s:
	        freq_map[char] = char
	    result = freq_map.keys()
	    return "".join(result)
	   
	   