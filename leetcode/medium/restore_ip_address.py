""" Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses


    Given a string containing only digits, restore it by returning all 
    possible valid IP address combinations.

    For example:
    Given "25525511135",

    return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ## Helpers
        def canTakeOne(length, level):
            if level == 1:
                return 4 <= length <= 10
            elif level == 2:
                return 3 <= length <= 7
            elif level == 3:
                return 2 <= length <= 4
            elif level == 4:
                return 1 == length

        def canTakeTwo(length, level):
            if level == 1:
                return 5 <= length <= 11
            elif level == 2:
                return 4 <= length <= 8
            elif level == 3:
                return 3 <= length <= 5
            elif level == 4:
                return 2 == length

        def canTakeThree(length, level):
            if level == 1:
                return 6 <= length <= 12
            elif level == 2:
                return 5 <= length <= 9
            elif level == 3:
                return 4 <= length <= 6
            elif level == 4:
                return 3 == length

        self.ips = []
        def ip(sofar, rest, level):
            if rest == "":
                self.ips.append(".".join(sofar))
            else:
                if canTakeOne(len(rest), level):
                    ip(sofar + [rest[0]], rest[1:], level + 1)
                if canTakeTwo(len(rest), level):
                    if rest[0] != "0":
                        ip(sofar + [rest[:2]], rest[2:], level + 1)
                if canTakeThree(len(rest), level):
                    num = int(rest[:3])
                    if num < 256 and rest[0] != "0":
                        ip(sofar + [rest[:3]], rest[3:], level + 1)

        ip([], s, 1)
        return(self.ips)


# a = Solution()
# print(a.restoreIpAddresses("25525511135"))
# "010010"
#["0.1.0.010","0.1.00.10","0.1.001.0","0.10.0.10","0.10.01.0","0.100.1.0",
#"01.0.0.10","01.0.01.0","01.00.1.0","010.0.1.0"]
# ["0.10.0.10","0.100.1.0"]