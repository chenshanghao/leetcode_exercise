class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # ["A","A","A","A","B","B","B","B","C","C","C","D","D","D", "E","E"]
        # n=1
        # ["ABABABABCDECD"]
        # n=2
        # n=3
        # n=4
        
        tasks_count = list(collections.Counter(tasks).values())
        max_count = max(tasks_count)
        max_count_tasks = tasks_count.count(max_count)
        return max(len(tasks), (max_count-1)*(n+1)+max_count_tasks)
        