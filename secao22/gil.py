"""
GIL - Python Global Interpreter Lock
"""

import sys

a = []
b = a
print(sys.getrefcount(a))
