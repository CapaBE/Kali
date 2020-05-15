#! /usr/bin/python3

"""
    ************************
    This is an example of a
    multiline comment
    ************************
"""

strVar = "Dit is een string"
flpVar = 3.7 #floating point
lstVar = [1,2,3,4,5] #list
dctFruitColor = {'apple' : 'red', 'grape' : 'green', 'orange' : 'orange'} #dictionary

print("string:  "+ strVar)
print("floating point "+ str(flpVar))
print("List "+str(lstVar))
print("Dictionary "+ dctFruitColor['apple'])
dctFruitColor['apple'] = 'green'
print("Dictionary "+ dctFruitColor['apple'])
print(lstVar[2])
