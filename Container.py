# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 16:53:14 2022

@author: zakha
"""
import pickle
from LanguageProcedure import printLanguageProcedure, createLanguageProcedure
from LanguageOOP import printLanguageOOP, createLanguageOOP, Inheritance

def createNode(data):
      data
      next = None
      prev = None
      return {'prev': prev, 'next': next, 'data': data}
      

head = {'prev': None, 'next': None, 'data': None}
    

def pushToContainer(head, newVal):
    NewNode = createNode(newVal)
    NewNode['next'] = head
    head['prev'] = NewNode
    head = NewNode
    return head

def showInfo(head):
    node = head
    while (node['data'] is not None):
        if 'inheritance' in node['data'].keys():
            printLanguageOOP(node['data'])
        else: 
            printLanguageProcedure(node['data'])
        node = node['next']
    print("There's no more objects in this container")
    
def clearContainer(head):
    head = {'prev': None, 'next': None, 'data': None}
    return head

def openFromFile(file):
    with open(file, 'rb') as f:
        head = pickle.load(f)
        
        
    return head
        
def saveToFile(head, file):   
    with open(file, 'wb') as f:
        pickle.dump(head, f)
    
                