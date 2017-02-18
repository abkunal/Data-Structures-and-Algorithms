""" Set Cover problem """

# Given a set X and subsets {S1, S2,...,Sn} such that S1 U S2 U ... U Sn = X
# Find the minimum number of subsets that contains all the elements of X.

def approx_set_cover(X, subsets):
    """
        Returns the approximate set cover for X given subsets
    """
    assert type(X) == set

    sorted_subsets = sorted(subsets, key=lambda x: len(x))
    
    return set_cover_solver(set(X), sorted_subsets, 0)


def set_cover_solver(X, subsets, count):
    if len(X) == 0:
        return count
    else:
        s = subsets.pop()
        count += 1
        
        for key in s:
            if key in X:
                X.remove(key)

        return set_cover_solver(X, subsets, count)


a = set(range(12))

s1 = set(range(6))
s3 = set([0,3,6,9])
s5 = set([2,5,8,11])
s6 = set([9,10])
s2 = set([4,5,7,8])
s4 = set([1,4,6,7,10])
subsets = list(map(list, [s1,s2,s3,s4,s5,s6]))

print(approx_set_cover(a, subsets))

# ==============================================================================
# Optimal Set Cover
def covers_set(subsets, X):
    """ Returns True if the given subsets covers set X. """
    X = set(X)
    for subset in subsets:
        for elem in subset:
            if elem in X:
                X.remove(elem)

    return len(X) == 0

min_cover = subsets
def bruteforce_set_cover(X, sofar, rest):
    """ Returns the minimum set cover """
    global min_cover

    if rest == []:
        if covers_set(sofar, X) is True:
            if len(sofar) < len(min_cover):
                min_cover = sofar
    else:
        take = list(sofar)
        take.append(rest[0])
        bf_set_cover(X, take, rest[1:])
        bf_set_cover(X, sofar, rest[1:])
# ==============================================================================

bruteforce_set_cover(a, [], subsets)
print("Optimal Set Cover: ", min_cover)
