""" Course Schedule - https://leetcode.com/problems/course-schedule

    There are a total of n courses you have to take, labeled from 0 to n - 1.

    Some courses may have prerequisites, for example to take course 0 you have to 
    first take course 1, which is expressed as a pair: [0,1]

    Given the total number of courses and a list of prerequisite pairs, is it 
    possible for you to finish all courses?

    For example:

    2, [[1,0]]
    There are a total of 2 courses to take. To take course 1 you should have 
    finished course 0. So it is possible.

    2, [[1,0],[0,1]]
    There are a total of 2 courses to take. To take course 1 you should have 
    finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj_list = {i:[] for i in range(numCourses)}
        for edge in prerequisites:
            adj_list[edge[1]].append(edge[0])
            
        status = {i:0 for i in range(numCourses)}
        def dfs(vertex, adj_list, status):
            for u in adj_list[vertex]:
                if status[u] == 1:
                    return True
                elif status[u] == 0:
                    status[u] = 1
                    if dfs(u, adj_list, status) is True:
                        return True
            status[vertex] = 2
            return False

        visited = set()
        for vertex in adj_list:
            if status[vertex] == 1:
                return False
            elif status[vertex] == 0:
                status[vertex] = 1
                if dfs(vertex, adj_list, status) is True:
                    return False
        return True


# a = Solution()
# print(a.canFinish(10, [[0,1],[2,0],[2,1]]))
# print(a.canFinish(4,[[0,1],[1,2],[2,3],[3,2]]))
# print(a.canFinish(3,[[0,1],[0,2],[1,2]]))
# print(a.canFinish(4,[[1,0],[2,0],[3,1],[3,2]]))