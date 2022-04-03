class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # build the hashmap for first list
        dict_num_count = {}
        for num in nums1:
            if num in dict_num_count:
                dict_num_count[num] += 1
            else:
                dict_num_count[num] = 1
        ans = []
        
        # for-loop the second list
        for num in nums2:
            count = dict_num_count.get(num, 0)
            if count > 0:
                ans.append(num)
                dict_num_count[num] = count - 1

        return ans