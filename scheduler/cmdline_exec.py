# -*- coding: utf-8 -*-
"""
Created on Sun May 12 17:06:13 2019

@author: ArchuBharathi
"""

# this is new to python 3.5

import os
import sys
#cmd = subprocess.run(["C:/path_to_python/python.exe", "C:/path_to_script/script.py"], stdout=subprocess.PIPE)
#os.system('exit()')
os.system('zkserver')
os.system('exit()')
sys.exit()
exit()
exit(1)




"""


import subprocess
cmdCommand = "zkserver"   #specify your cmd command
process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
print( output)

"""
"""

# this is new to python 3.5
import subprocess
import os
cmd = subprocess.run(["python"], stdout=subprocess.PIPE,shell = True)
return_string = cmd.stdout
"""