#By default, A module will only be loaded once even if it was imported into a program multiple times
# To make your imported module load more than once, you have to use the reload() function.
# The reload() function is present in the { importlib } module!!

import time
from importlib import reload
import pip
import pip
import pip
import pip
import pip
#notice that ['Hello'] is printed to the termina only once even though we imported it 5 times.

reload(pip)
reload(pip)

# After using the reload() function, notice that ['Hello'] is printed three times in the terminal. One for the initial importation of the pip module [pip.py file in this directory] the other two is for the reload(pip) function.