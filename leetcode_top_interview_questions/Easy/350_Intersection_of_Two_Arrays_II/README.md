### Follow up

1. What if the given array is already sorted? How would you optimize your algorithm?

We can use either [Approach 2](https://leetcode.com/problems/intersection-of-two-arrays-ii/solution/#approach-2-sort) or [Approach 3](https://leetcode.com/problems/intersection-of-two-arrays-ii/solution/#approach-3-built-in-intersection), dropping the sort of course. It will give us linear time and constant memory complexity.



2. What if `nums1`'s size is small compared to `nums2`'s size? Which algorithm is better?

[Approach 1](https://leetcode.com/problems/intersection-of-two-arrays-ii/solution/#approach-1-hash-map) is a good choice here as we use a hash map for the smaller array.



3. What if elements of `nums2` are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

If `nums1` fits into the memory, we can use [Approach 1](https://leetcode.com/problems/intersection-of-two-arrays-ii/solution/#approach-1-hash-map) to collect counts for `nums1` into a hash map. Then, we can sequentially load and process `nums2`.

If neither of the arrays fit into the memory, we can apply some partial processing strategies:

- Split the numeric range into subranges that fits into the memory. Modify [Approach 1](https://leetcode.com/problems/intersection-of-two-arrays-ii/solution/#approach-1-hash-map) to collect counts only within a given subrange, and call the method multiple times (for each subrange).

- Use an external sort for both arrays. Modify [Approach 2](https://leetcode.com/problems/intersection-of-two-arrays-ii/solution/#approach-2-sort) to load and process arrays sequentially.