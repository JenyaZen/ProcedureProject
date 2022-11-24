# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 16:47:43 2022

@author: zakha
"""

def printProgrammingLanguage(language):
    print("Name: " + language['name'] + '\n' +
    "Year: " + language['year'] +'\n')
    
def createProgrammingLanguage(name, year):
    return({'name': name, 'year':year})
         