import warnings

def add_one(x):
    if not isinstance(x, (float, int, complex)):
        raise TypeError(f"`{x}` should be numeric")
    if isinstance(x, complex):
        warnings.warn(f"`{x}` is complex", UserWarning)
    return x+1
