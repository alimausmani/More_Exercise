
# Iss program ko attempt karne ke liye pehle ek users.json 
# naam ki file mein neeche diye hue text ko save karein.

A={
    "users": [{
            "firstName": "vidur",
            "lastName": "singla",
            "details": {
                "age": 21,
                "mobileNo": 1234567890,
                "City": "Delhi"
            }
        },
        {
            "firstName": "rishabh",
            "lastName": "verma",
            "details": {
                "age": 22,
                "mobileNo": 12345678320,
                "City": "Chandigarh"
            }
        },
        {
            "firstName": "abhishek",
            "lastName": "gupta",
            "details": {
                "age": 25,
                "mobileNo": 12332567890,
                "City": "Gurgaon"
            }
        }
    ]
}

# Visualize

# Uske baad aapne jiss directory mein users.json save kiya hai, 
# usse directory mein yeh python ka code save kariye ek dusri file mein.

import json
# with open('user.json',"w") as write_file:    
#      data = json.dump(A,write_file,indent=4)
# with open('user.json',"r") as read_file:
#     c=read_file.read()     
users = ['users']
for A in "user":
  counter = 0
  print ("users full name is " + A['firstName'] + ' ' + A['lastName'])
  while counter < len(A['details']):
    print ("users mobile number is " + A['details'][counter]['mobileNo'])
    print ("users age  is " + A['details'][counter]['age'])
    print ("users city is " + A['details'][counter]['city'])
with open('user.json',"w") as write_file:    
     data = json.dump(A,write_file,indent=4)
with open('user.json',"r") as read_file:
    c=read_file.read()     

# users.json file mein users ka data padha hai.
# Yeh program users.json file ko read kar kar usmein 
# se users ka data print karega. Iss file ko debug kar kar run karo.

# Topics covered:

# Key error

# loop iterates over the wrong list.


