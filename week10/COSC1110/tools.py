
#------------------------------------
#Title: My Tools Library for Python Console
# Author: Alyssa Cipriani
# Created: July 17, 2025
# Description: A set opf tools to be reused in our console apps.
#--------------------------------------
#
#
'''Note that this file does not use print statement in the functions
meaning it is locked 
to the console. If '''

#region IMPORTS
import random
#endregion IMPORTS

#region USER INPUT FUNCTIONS
def getString(prompt: str):
    '''Obtains a string from the user'''
    return input(prompt).strip()
    

def getStringLength(prompt: str, minLen: int, maxLen: int):
    '''Obtains a string from the user with length inside the given range'''
    isValid = False
    while not isValid:
        userString = input(prompt).strip()
        if minLen <= len(userString) <= maxLen: return userString

def getInt(prompt: str):
    pass

def getIntRange(prompt: str, min: int, max: int):
    pass

def getFloat(prompt: str):
    pass

def getFloatRange(prompt: str, min: float, max: float):
    pass
#endregion USER INPUT FUNCTIONS

#region RANDOM NUMBER GENERATIONS
def getRandIntRange(min: int, max: int):
    pass 

def getRandFloatRange(min: float, max: float):
    pass 
#endregion RANDOM NUMBER GENERATIONS