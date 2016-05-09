# -*- coding: utf-8 -*-



def is_consistent(csp, variable, value):
    """Returns True when the variable assignment to value is consistent, i.e. it does not violate any of the constraints
    associated with the given variable for the variables that have values assigned.

    For example, if the current variable is X and its neighbors are Y and Z (there are constraints (X,Y) and (X,Z)
    in csp.constraints), and the current assignment as Y=y, we want to check if the value x we want to assign to X
    violates the constraint c(x,y).  This method does not check c(x,Z), because Z is not yet assigned."""

    for constraint in csp.constraints[variable]:
        v1 = constraint.var1
        v2 = constraint.var2
        if v2.is_assigned():
            if not constraint.is_satisfied(value, v2.value):
                return False
    return True
