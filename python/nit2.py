""" https://www.hackerearth.com/codathon-nitbhopal/algorithm/new-government-new-name/ """

import string

def type1(query, strg, str_dict):
    pos = int(query[1]) - 1
    char = query[2]
    
    # Replacing in strg and updating values in dictionary
    str_dict[strg[pos]] -= 1
    strg[pos] = char
    str_dict[char] += 1


def type2(query, strg, str_dict):
    pos = int(query[1])
    count = 1

    for char in string.ascii_uppercase:
        if count + str_dict[char] > pos:
            print(char)
            return
        else:
            count += str_dict[char]


def main():
    string_size, num_queries = input().split()
    string_size = int(string_size)
    num_queries = int(num_queries)
    
    strg = list(input())
    
    # initializing dictionary
    str_dict = {}
    for c in string.ascii_uppercase:
        str_dict[c] = 0
    # updating the number of occurrences of characters
    for char in strg:
        str_dict[char] += 1
    
    # getting queries 
    queries = []
    for i in range(num_queries):
        queries.append(input().split())
    
    for query in queries:
        if query[0] == '1':
            type1(query, strg, str_dict)
        else:
            type2(query, strg, str_dict)


