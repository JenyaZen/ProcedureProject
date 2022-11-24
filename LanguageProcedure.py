# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 16:48:10 2022

@author: zakha
"""

import ProgrammingLanguage

def printLanguageProcedure(language):
    print("_____________________________\n" +
          "I'm Procedure language\n" +
          "My characteristics is:\n")
    ProgrammingLanguage.printProgrammingLanguage(language)
    print("Do I have abstract types?: " + str(language['hasAbstractTypes']) + '\n'
          '_____________________________\n')
    
def createLanguageProcedure(name, year, hasAbstractTypes):
    language = ProgrammingLanguage.createProgrammingLanguage(name, year)
    language['hasAbstractTypes'] = hasAbstractTypes
    return language

        