""" Merge Intervals - https://leetcode.com/problems/merge-intervals

    Given a collection of intervals, merge all overlapping intervals.

    For example,
    Given [1,3],[2,6],[8,10],[15,18],
    return [1,6],[8,10],[15,18].
"""


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals: return []
        
        intervals.sort(key=lambda x:x.start)
        new_intervals = []
        start = intervals[0].start
        end = intervals[0].end

        for i in range(1, len(intervals)):
            if intervals[i].start <= end:
                end = max(end, intervals[i].end)
            else:
                new_intervals.append(Interval(start, end))
                start, end = intervals[i].start, intervals[i].end

        new_intervals.append(Interval(start, end))
        return new_intervals


# a = Solution()
# a1 = Interval(1,4)
# a2 = Interval(1,5)