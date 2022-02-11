#Update Values in Dictionaries and Lists
'''
1. Change the value 10 in x to 15. Once you're done, x should now be [[5,2,3], [15,8,9]]. Done:|x|
2. Change the last_name of the first student from 'Jordan' to 'Bryant' Done:|x|
3. In the sports_directory, change 'Messi' to 'Andres' Done:|x|
4. Change the value 20 in z to 30 Done:|x|
'''
#      |index0| |index1|
x = [ [5,2,3], [10,8,9] ] 
x[1][0]=15
print(x) # print x
"""
1. x @index1 will go to the second iteration "[10,8,9]" in the x "list"
2.then it will go to the 1st index in the list of numbers and access the #10.
3.finally you will use "=" the set x to it's new value "15" 
"""

students = [
      {'first_name':  'Michael', 'last_name' : 'Jordan'},
      {'first_name' : 'John', 'last_name' : 'Bryant'}
 ]
print(students[0]['first_name'] + ' ' + students[1]['last_name'])
'''
1. I wanted to print studen@index0@'first_name' in order to access that key
2.I glued it to students@index1@'last_name' to replace index0's 'last_name' to 'Bryant'
'''
sports_directory = {
       'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
       'soccer' : ['Messi', 'Ronaldo', 'Rooney']
   }
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)
'''
1. I decided to call the dictionary name and target the second string in the index. 
2. I @'soccer' to access the string within the index and went more deeper into the string by @index0 in the list ['Messi', 'Ronaldo', 'Rooney'].
3. From there, I used the "=" to set the value 'Messi' into its new value 'Andres'.
4. Finally, print(sports_directory) => This will print the whole dictionary index and the new value 'Andres' stored in the new list.
'''
z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30 # z@string'y' set new value integer to 30
print(z) # print z

students = [
            {'first_name':  'Michael', 'last_name' : 'Jordan'},
            {'first_name' : 'John', 'last_name' : 'Rosales'},
            {'first_name' : 'Mark', 'last_name' : 'Guillen'},
            {'first_name' : 'KB', 'last_name' : 'Tonel'}
       ]


def iterateDictionary(students): # created a function 
      for value in students:
        if type(value) is dict:
            iterateDictionary(value)
iterateDictionary(students)
print(students)


from multiprocessing.sharedctypes import Value
from turtle import st



def iterateDictionary2(students):
    for items in students:
        print(items['first_name'])
    for items in students:
        print(items['last_name'])
iterateDictionary2(students)


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
 }

def printInfo(dojo):
    locationsNum = len(dojo['locations'])
    print( f"{locationsNum} LOCATIONS")
    for x in dojo['locations']:
         print(x)
    instructorsNum = len(dojo['instructors'])

    print(f"{instructorsNum} INSTRUCTIONS")
    for c in dojo['instructors']:
         print(c)
printInfo(dojo)

# output:

# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

