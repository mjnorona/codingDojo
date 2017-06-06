students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def outputValues(arr):
    for i in range(0, len(arr)):
        name = ""
        name += arr[i]["first_name"] + " "
        name += arr[i]["last_name"]
        print name

outputValues(students)

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
}

def outputValues2(objects):
    for key,data in objects.items():
        print key
        for i in range(0, len(data)):
           name = str(i + 1) + " - "
           name += data[i]["first_name"].upper() + " "
           name += data[i]["last_name"].upper() + " - " + str((len(data[i]["first_name"]) + len(data[i]["last_name"])))
           print name
    
    

outputValues2(users)