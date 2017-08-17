class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # convert pattern into a list of chars
        # convert s into a list of words separated by space
        pattern = list(pattern)
        s = str.split()
        
        # base case
        if len(s) != len(pattern): return False
        
        # mapped will contain characters of pattern
        # mappings will contain all the mappings of char to words
        mapped = set()
        mappings = {}
        for i in range(len(s)):
            # if current word in s is already present in mappings
            # check its value
            if s[i] in mappings:
                if mappings[s[i]] != pattern[i]:
                    return False
            # if current word not in mappings, check whether current pattern
            # already exists
            else:
                if pattern[i] in mapped:
                    return False
                mappings[s[i]] = pattern[i]
                mapped.add(pattern[i])
        return True


# a = Solution()
# print(a.wordPattern("abba", "dog cat cat dog"))