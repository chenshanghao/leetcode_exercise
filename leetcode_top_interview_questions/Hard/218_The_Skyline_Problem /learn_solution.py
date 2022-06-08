class Solution:
    import heapq
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
      
        res = []
        events = [] 
        q = [0]
        heapq.heapify(q)
        left = []
        right = []
        
        for b in buildings:
            left.append([b[0], -b[-1], "start"])
    
        #1. Sort start edges by height from high -> low
        left.sort(key = lambda x: x[1])
    
        for b in buildings:
            right.append([b[1], -b[-1], "end"])
        
        #1. Sort end edges by height from low -> high
        right.sort(key = lambda x: x[1], reverse=True)
        
        #1. Sort points by left edge
        events = left + right
        events.sort(key = lambda x: x[0])
         
        for e in events:
            #2.  Get the start edges
            if e[-1] == "start":
                # If the current edge is higher than the current highest edges,
                # add it to the queue 
                if -e[1] > -heapq.nsmallest(1, q)[0]:
                    res.append([e[0], -e[1]])
                heapq.heappush(q, e[1])
                
            #3.  Get the end edges
            if e[-1] == "end":
                # Remove the height of this edge from the queue
                q.remove(e[1])
                
                # If the height of this edge was the highest edges,
                # add the position of this edge with the remain highest edges to the answer
                if -e[1] > -heapq.nsmallest(1, q)[0]:
                    res.append([e[0],-heapq.nsmallest(1, q)[0]])
            
        return res