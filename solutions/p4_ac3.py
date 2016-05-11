# -*- coding: utf-8 -*-

from collections import deque


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

