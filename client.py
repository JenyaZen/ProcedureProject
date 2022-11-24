# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 16:42:52 2022

@author: zakha
"""

import sys
import Container


print('Hello\n')
if (len(sys.argv) != 3):
    print('You need to give me input and output files!!\n')
    sys.exit()
    
print('Adding objects from ' + sys.argv[1] + ' to Container\n')
container = Container.openFromFile(sys.argv[1])
print('Container filled!\n')
print('Hey, container, what you got?\n')
Container.showInfo(container)
print('Emptying container\n')
Container.clearContainer(container)
print('Container is now empty...\n')
print('Saving container to ' + sys.argv[2] + '\n')
Container.saveToFile(container, sys.argv[2])
print('Container saved!\n')
print('Bye Bye!\n')

    
