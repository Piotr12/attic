"""
just a dummy sample on how to do xlsx reformating
"""
import reformat_xlsx
import sys
print(reformat_xlsx.reformat(sys.argv[1], ';',(None,"")))
