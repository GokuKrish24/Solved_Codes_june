from os import *
from sys import *
from collections import *
from math import *


def insert(stack,element):
    if(len(stack)==0 or element>=stack[-1]):
        stack.append(element)
        return
    t=stack.pop()
    insert(stack,element)
    stack.append(t)

def sortStack(stack):
    if(len(stack)==0):
        return
    t=stack.pop()
    sortStack(stack)
    insert(stack,t)
    
        
