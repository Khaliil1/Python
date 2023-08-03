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


x[1][0] = 15
print(x)

# **************

students['last_name'] = 'Bryant'
print(students)

# **************

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)


# **************

z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)

# *************************************************
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for s in students:
        print('first name -',s['first_name'],',',' last name -',s['last_name'])

print(iterateDictionary(students))

# **************************************************

def iterateDictionary2(key_name, some_list):
    for s in students:
        print(s[key_name])

print(iterateDictionary2('first_name', students))
print(iterateDictionary2('last_name', students))

# **************************************************

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']}

def printInfo(dojo):
    
    print(len(dojo['locations']), "LOCATIONS")
    for location in dojo['locations']:
          
          print(location)
    
    print(len(dojo['instructors']), "INSTRUCTORS")
    
    for instructor in dojo['instructors']:
       
       print(instructor)
       
printInfo(dojo)