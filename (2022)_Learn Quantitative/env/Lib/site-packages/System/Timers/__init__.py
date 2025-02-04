import os
import sys

# If quantconnect-stubs is installed via pip and Lean is ran locally,
# importing anything from the current namespace makes the Python
# interpreter look in the quantconnect-stubs package for the implementation.
#
# The desired behavior is for the interpreter to use the implementation
# provided by the AddReference() call from Python.NET.
#
# To fix this, we temporarily remove the directory containing the
# quantconnect-stubs package from sys.path and re-import the current namespace
# so the relevant C# namespace is used when running Lean locally.

# Find the directory containing quantconnect-stubs (usually site-packages)
current_path = os.path.dirname(__file__)
while os.path.basename(current_path) != "System":
    current_path = os.path.dirname(current_path)
current_path = os.path.dirname(current_path)

# Temporarily remove the directory containing quantconnect-stubs from sys.path
original_path = sys.path[:]
sys.path.remove(current_path)

# Import the C# version of the current namespace
del sys.modules["System.Timers"]
from clr import AddReference
AddReference("System.Timers")
from System.Timers import *

# Restore sys.path
sys.path = original_path
