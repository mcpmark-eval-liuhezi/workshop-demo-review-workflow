def add(a, b):
    # Smart addition helper: sums two values.
    return a + b


def smart_add(a, b, verbose=False):
    """Add a and b.

    Args:
        a: First operand (numeric).
        b: Second operand (numeric).
        verbose: If True, return a formatted string instead of raw sum.

    Returns:
        The sum, or a verbose message string when verbose=True.
    """
    if a is None or b is None:
        return "add: one operand was None (unable to sum)"
    if verbose:
        return f"{a} + {b} = {a + b}"
    return a + b
