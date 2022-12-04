x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


#1. Update values in dictionaries and lists

#Change the value 10 in x to 15
x[1][0] = 15
print(x[1][0])

#Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students[0]['last_name'])

#In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])

#Change the value 20 in z to 30
z[0]['y'] = 30
print(z)


#2. Iterate through a list of dictionaries 

"""
Create a function iterateDictionary(some_list) that, given a list of dictionaries,
the function loops through each dictionary
in the list and prints each key and the associated value. 
"""
travel_done = {
    'west': ['Canada', 'Mexico', 'USA'],
    'east': ['Spain', 'Germany']
}

def iterateDictionary(travel_done):
    for key, val in travel_done.items():
        for i in val:
            print(key,i)

iterateDictionary(travel_done)


#3. Get Values From a List of Dictionaries
"""
Create a function iterateDictionary2(key_name, some_list) that, given a list of 
dictionaries and a key name, the function prints the value stored in that key for each 
dictionary.
"""

Staff = {
     'Manager': {'name': 'Stacey'},
     'Developer': {'name': 'Gloria'},
     'Analyst': {'name': 'Orlando'}}

def iterateDictionary2(Staff):
    print(Staff['Manager']['name'])
    print(Staff['Developer']['name'])
    print(Staff['Analyst']['name'])

iterateDictionary2(Staff)


#4. Iterate Through a Dictionary with List Values
"""
Create a function printInfo(some_dict) that given a dictionary whose values are all 
lists, prints the name of each key along with the size of its list, and then prints the 
associated values within each key's list
"""

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Devon']
}

def printInfo(dojo):
    print(len(dojo['locations']))
    print(str.upper('locations'))
    for element in dojo['locations']:
        print(element)

printInfo(dojo)
