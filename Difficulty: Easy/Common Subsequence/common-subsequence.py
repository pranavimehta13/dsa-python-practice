#User function Template for python3
class Solution:
	def commonSubseq(self, a, b):
		# your code here
		common = ""
		for char1 in a:
		    if char1 in b:
		        common += char1
		if common != "":
		    return 1
		return 0