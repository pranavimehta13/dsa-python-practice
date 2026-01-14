class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []

        top = 0
        left = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1
        result = []

        while top <= bottom and left <= right:
            # top row
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # right column
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # bottom row
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            # left column
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
