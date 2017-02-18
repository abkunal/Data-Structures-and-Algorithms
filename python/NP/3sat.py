""" 3 SAT problem """

def formula(v):
    return (v[0] or v[1] or not v[2]) and (v[3] or not v[4] or not v[5]) and (v[6] or v[7] or v[8])


class ThreeSat:
    """ Solves the 3-SAT problem by trying all possible combinations. """

    def __init__(self, formula, variables):
        """ 
            Formula: the function which has to be computed. It is of the form:
            (x1 or x2 or (not x3)) and (x4 or (not x5) or (not x6)) and ...
            variables: The number of variables required in the given function
        """
        self._formula = formula
        self._var = variables

    def three_sat(self):
        return self.three_sat_worker([], self._var)

    def three_sat_worker(self, sofar, rest):
        """ 
            Returns True if the given formula has a solution for some input,
            False otherwise.
        """
        if rest == 0:
            return self._formula(sofar)
        else:
            if self.three_sat_worker(sofar + [True], rest - 1) == True:
                return True
            elif self.three_sat_worker(sofar + [False], rest - 1) == True:
                return True
            return False

def formula1(v):
    return (v[0] or v[1]) and (v[0] or not v[1]) and (not v[0])

s1 = ThreeSat(formula, 9)
s2 = ThreeSat(formula1, 2)

#s1.three_sat() == True
#s2.three_sat() == False
