# -*- coding: utf-8 -*-
from p1_is_complete import is_complete
from p2_is_consistent import is_consistent


def select_unassigned_variable(csp):
    """Selects the next unassigned variable, or None if there is no more unassigned variables
    (i.e. the assignment is complete).

    For P3, *you do not need to modify this method.*
    """
    return next((variable for variable in csp.variables if not variable.is_assigned()))


def order_domain_values(csp, variable):
    """Returns a list of (ordered) domain values for the given variable.

    For P3, *you do not need to modify this method.*
    """
    return [value for value in variable.domain]


def inference(csp, variable):
    """Performs an inference procedure for the variable assignment.

    For P3, *you do not need to modify this method.*
    """
    return True


def backtracking_search(csp):
    """Entry method for the CSP solver.  This method calls the backtrack method to solve the given CSP.

    If there is a solution, this method returns the successful assignment (a dictionary of variable to value);
    otherwise, it returns None.

    For P3, *you do not need to modify this method.*
    """
    if backtrack(csp):
        return csp.assignment
    else:
        return None


def backtrack(csp):
    """Performs the backtracking search for the given csp.

    If there is a solution, this method returns True; otherwise, it returns False.
    """
    #print "Finding Match"
    # TODO implement this
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
                if backtrack(csp):
                    return True
                csp.variables.rollback()
        return False
