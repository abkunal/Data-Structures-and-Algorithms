""" Binary Watch - https://leetcode.com/problems/binary-watch/

    A binary watch has 4 LEDs on the top which represent the hours (0-11), 
    and the 6 LEDs on the bottom represent the minutes (0-59).

    Each LED represents a zero or one, with the least significant bit on the right.

    Given a non-negative integer n which represents the number of LEDs that are 
    currently on, return all possible times the watch could represent.

    Example:

    Input: n = 1
    Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
    Note:
    The order of output does not matter.
    
    The hour must not contain a leading zero, for example "01:00" is not valid, 
    it should be "1:00".
    
    The minute must be consist of two digits and may contain a leading zero, 
    for example "10:2" is not valid, it should be "10:02".
"""

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        from itertools import permutations
        four = "0123"
        six = "012345"
        
        small = max(num-6, 0)
        large = min(6, num)
        times = set()

        def get_hour(four):
            hour = 0
            for i in four:
                hour += 2**int(i)
            if hour > 11:
                return False
            return str(hour)

        def get_minute(six):
            minute = 0
            for i in six:
                minute += 2**int(i)
            if minute < 10:
                return "0" + str(minute)
            elif minute > 59:
                return False
            return str(minute)

        while small < 5 and large >= 0:
            pfour = list(permutations(four, small))
            psix = list(permutations(six, large))
            small += 1
            large -= 1

            for i in range(len(pfour)):
                for j in range(len(psix)):
                    h = get_hour(pfour[i])
                    m = get_minute(psix[j])
                    if h is False or m is False:
                        continue
                    times.add(h + ":" + m)

        return list(times)