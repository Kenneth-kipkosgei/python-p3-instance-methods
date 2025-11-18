#!/usr/bin/env python3

def pytest_itemcollected(item):
    """Format collected test node ids using parent/class and test docstrings.

    This is defensive: some pytest Item objects may not have the expected
    attributes in all contexts, so use getattr and guard against None.
    """
    parent_obj = getattr(item.parent, "obj", None)
    node_obj = getattr(item, "obj", None)

    pref = parent_obj.__doc__.strip() if parent_obj and parent_obj.__doc__ else ""
    suf = node_obj.__doc__.strip() if node_obj and node_obj.__doc__ else ""

    if pref or suf:
        item._nodeid = " ".join(filter(None, (pref, suf)))