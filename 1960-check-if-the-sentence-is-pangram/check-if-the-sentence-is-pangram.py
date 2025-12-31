class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        alphabet = set('abcdefghijklmnopqrstuvwxyz')
        sent = set(sentence)
        if alphabet == sent:
            return True
        else:
            return False
        