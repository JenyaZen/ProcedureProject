# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 16:48:09 2022

@author: zakha
"""

from enum import Enum
import ProgrammingLanguage

class Inheritance(Enum):
    single = 1
    multiple = 2
    interface = 3

def printLanguageOOP(language):
    print("_____________________________\n" +
          "I'm Procedure language\n" +
          "My characteristics is:\n")
    ProgrammingLanguage.printProgrammingLanguage(language)
    print("Do I have abstract types?: " + language['inheritance'] + '\n'
          '_____________________________\n')
    
def createLanguageOOP(name, year, inheritance):
    language = ProgrammingLanguage.createProgrammingLanguage(name, year)
    language['inheritance'] = inheritance.name
    return language

        