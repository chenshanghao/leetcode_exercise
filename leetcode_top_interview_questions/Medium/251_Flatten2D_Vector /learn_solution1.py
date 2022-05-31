class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.nums = []
        for inner_list in vec:
            print(inner_list)
            for num in inner_list:
                self.nums.append(num)
        self.position = -1
        

    def next(self) -> int:
        self.position += 1
        return self.nums[self.position]
        

    def hasNext(self) -> bool:
        return self.position + 1 < len(self.nums)
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()