def V(orig, k, **kw):
    """An AI-written variant of an original question; type/topics/chapter are copied from the original at build time."""
    return dict(id=f"{orig}-v{k}", source=f"AI variant of {orig}", variant_of=orig, near_duplicate_of=orig,
                drafted_by_claude="all (AI variant)", **kw)
def r(x, d=2):
    s = f"{round(x, d):.{d}f}"
    return s.rstrip('0').rstrip('.') if '.' in s else s
