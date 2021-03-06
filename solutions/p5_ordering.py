# -*- coding: utf-8 -*-

def select_unassigned_variable(csp):
    """Selects the next unassigned variable, or None if there is no more unassigned variables
    (i.e. the assignment is complete).

    This method implements the minimum-remaining-values (MRV) and degree heuristic. That is,
    the variable with the smallest number of values left in its available domain.  If MRV ties,
    then it picks the variable that is involved in the largest number of constraints on other
    unassigned variables.
    """

    # TODO implement this
    sortedVar = sorted(csp.variables, key = lambda variable: len(variable.domain))
    sortedVar = [var for var in sortedVar if not var.is_assigned()]
    smallest = sortedVar[0]
    lenSmallest = len([arc for arc in csp.constraints[smallest] if not arc.var2.is_assigned()])
    for variable in sortedVar[1:]:
        if len(variable.domain) > len(smallest.domain):
            return smallest
        lenVar = len([arc for arc in csp.constraints[variable] if not arc.var2.is_assigned()])
        if lenVar > lenSmallest:
            smallest = variable
            lenSmallest = lenVar
    return smallest




def order_domain_values(csp, variable):
    """Returns a list of (ordered) domain values for the given variable.

    This method implements the least-constraining-value (LCV) heuristic; that is, the value
    that rules out the fewest choices for the neighboring variables in the constraint graph
    are placed before others.
    """

    # TODO implement this
    domain = dict([(v, 0) for v in variable.domain])

    for constraint in csp.constraints[variable]:
        for v1 in constraint.var1.domain:
            for v2 in constraint.var2.domain:
                if v1 == v2:
                    domain[v1] += 1

    tosort = domain.items()
    tosort = sorted(tosort, key = lambda variable: variable[1])
    return [v[0] for v in tosort]
