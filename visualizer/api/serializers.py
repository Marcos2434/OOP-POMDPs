from z3 import *
from fractions import Fraction as frac

def z3_rational_to_float(rational):
    return float(rational.numerator_as_long()) / float(rational.denominator_as_long())

def Z3Serializer(m : Model) -> dict:
    """
    Convert a Z3 model to a JSON serializable format. Support for int, rational, and string values.

    Args:
        m (Model): a Z3 model
        
    Returns:
        dict: a dictionary representation of the model
    """
    values = {}
    for decl in m.decls():
        if m[decl].sort().kind() == Z3_INT_SORT:
            values[str(decl)] = m[decl].as_long()
        elif m[decl].sort().kind() == Z3_REAL_SORT:
            values[str(decl)] = z3_rational_to_float(m[decl])
        else:
            values[str(decl)] = str(m[decl])
    
    return values