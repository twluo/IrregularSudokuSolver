# -*- coding: utf-8 -*-

from collections import deque
from p1_is_complete import is_complete
from p2_is_consistent import is_consistent
from p5_ordering import select_unassigned_variable
from p5_ordering import order_domain_values

def inference(csp, variable):
    """Performs an inference procedure for the variable assignment.

    For P6, *you do not need to modify this method.*
    """
    return ac3(csp, csp.constraints[variable].arcs())


def backtracking_search(csp):
    """Entry method for the CSP solver.  This method calls the backtrack method to solve the given CSP.

    If there is a solution, this method returns the successful assignment (a dictionary of variable to value);
    otherwise, it returns None.

    For P6, *you do not need to modify this method.*
    """
    if backtrack(csp):
        return csp.assignment
    else:
        return None


def backtrack(csp):
    """Performs the backtracking search for the given csp.

    If there is a solution, this method returns True; otherwise, it returns False.
    """

    # TODO copy from p3
    if is_complete(csp):
        return True
    else:
        variable = select_unassigned_variable(csp)
        #print variable
        for value in order_domain_values(csp, variable):
            #print value
            if is_consistent(csp, variable, value):
                #print "Found Valid"
                csp.variables.begin_transaction()
                variable.assign(value)
                if (inference(csp, variable)):
                    if backtrack(csp):
                        return True
                csp.variables.rollback()
        return False


def ac3(csp, arcs=None):
    """Executes the AC3 or the MAC (p.218 of the textbook) algorithms.
    If the parameter 'arcs' is None, then this method executes AC3 - that is, it will check the arc consistency
    for all arcs in the CSP.  Otherwise, this method starts with only the arcs present in the 'arcs' parameter
    in the queue.
    Note that the current domain of each variable can be retrieved by 'variable.domains'.
    This method returns True if the arc consistency check succeeds, and False otherwise."""

    queue_arcs = deque(arcs if arcs is not None else csp.constraints.arcs())
    while queue_arcs:
        xi, xj = queue_arcs.pop()
        if revise(csp, xi, xj):
            if not xi.domain:
                return False
            else:
                for xk in csp.constraints[xi]:
                    queue_arcs.append((xi, xk.var2))
    return True
    # TODO implement this

def revise(csp, xi, xj):
    # You may additionally want to implement the 'revise' method.
    change = False
    for vali in xi.domain:
        for contraint in csp.constraints[xi, xj]:
            for valj in xj.domain:
                if contraint.is_satisfied(vali, valj):
                    break
            else:
                xi.domain.remove(vali)
                change = True
    return change
