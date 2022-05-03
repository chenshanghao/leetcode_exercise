class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        last_row = [1]
        for i in range(numRows):
            res.append(last_row)
            new_row = [last_row[0]]
            for i in range(1, len(last_row)):
                new_row.append(last_row[i - 1] + last_row[i])
            new_row.append(last_row[-1])
            last_row = new_row
        return res