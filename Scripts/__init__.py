from . import debug, parsejson, latex
from .SYSTEM_PROMPTS import *

import sys
args = sys.argv
print("All arguments:", args)

if "--debug" in args:
    debug.DebugMode = True
    