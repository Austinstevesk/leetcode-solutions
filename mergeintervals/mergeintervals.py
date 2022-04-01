class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda i: i[0])
        output = [intervals[0]]
        
    
        for start, end in intervals[1:]:
            # output = [[1,6], [8,10], [15,18]]
            # start, end = [2,6]
            last_end_val = output[-1][1]
            if last_end_val >= start:
                output[-1][1] = max(last_end_val, end)
            else:    
                output.append([start, end])
        return output